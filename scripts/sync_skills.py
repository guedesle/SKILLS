#!/usr/bin/env python3
"""Valida o catálogo e sincroniza mirrors push quando explicitamente habilitados.

Uso:
  python scripts/sync_skills.py --check
  python scripts/sync_skills.py --apply

O mesmo validador é usado localmente e no CI. Além do registry/mirrors, o
check garante que skills canônicas, frontmatter e documentação não derivem.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry.json"
README = ROOT / "README.md"
STATUS = ROOT / "general-skills-status.md"
VALID_MIRROR_MODES = {"pull", "push"}
SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def run(cmd: list[str], cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess:
    proc = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, encoding="utf-8", errors="replace")
    if check and proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"Falha: {' '.join(cmd)}")
    return proc


def load_registry() -> dict:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if data.get("repository") != "guedesle/SKILLS":
        raise RuntimeError("registry.json não aponta para guedesle/SKILLS como repositório canônico.")
    return data


def is_safe_relative_path(raw: str | None) -> bool:
    if not raw or not raw.strip():
        return False
    path = Path(raw)
    return not path.is_absolute() and ".." not in path.parts


def parse_frontmatter_text(body: str) -> dict[str, str]:
    lines = body.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    result: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return result
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return {}


def parse_frontmatter(path: Path) -> dict[str, str]:
    try:
        return parse_frontmatter_text(path.read_text(encoding="utf-8"))
    except OSError:
        return {}


def canonical_skill_paths() -> set[str]:
    return {
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "skills").glob("*/SKILL.md")
        if path.is_file()
    }


def validate_catalog_docs(skill_name: str, path: str, version: str, readme: str, status: str) -> list[str]:
    errors: list[str] = []
    if f"({path})" not in readme:
        errors.append(f"README.md não referencia a skill canônica {skill_name}: {path}")
    if f"`{skill_name}`" not in readme:
        errors.append(f"README.md não documenta a skill: {skill_name}")
    if f"`{skill_name}`" not in status:
        errors.append(f"general-skills-status.md não documenta a skill: {skill_name}")
    if version not in readme:
        errors.append(f"README.md não contém a versão registrada {version} para {skill_name}")
    return errors


def validate_registry(data: dict) -> list[str]:
    errors: list[str] = []
    names: set[str] = set()
    paths: set[str] = set()
    mirror_targets: set[tuple[str, str, str]] = set()
    pull_mirror_count = 0

    if data.get("schema_version", 0) < 2:
        errors.append("schema_version deve ser >= 2 para mirrors pull genéricos.")

    readme = README.read_text(encoding="utf-8") if README.is_file() else ""
    status = STATUS.read_text(encoding="utf-8") if STATUS.is_file() else ""
    if not readme:
        errors.append("README.md ausente ou vazio.")
    if not status:
        errors.append("general-skills-status.md ausente ou vazio.")

    pull_runtime = data.get("pull_mirror", {})
    skills = data.get("skills", [])
    if not isinstance(skills, list) or not skills:
        return errors + ["registry.json deve conter uma lista não vazia de skills."]

    for skill in skills:
        name = skill.get("name")
        path = skill.get("path")
        version = skill.get("version")
        if not name or not path or not version:
            errors.append(f"Registro incompleto: {skill!r}")
            continue
        if not SKILL_NAME_RE.fullmatch(name):
            errors.append(f"Nome de skill inválido; use kebab-case: {name}")
        if not SEMVER_RE.fullmatch(version):
            errors.append(f"SemVer inválido em {name}: {version}")
        expected_path = f"skills/{name}/SKILL.md"
        if path != expected_path:
            errors.append(f"Path canônico de {name} deve ser {expected_path}, encontrado {path}")
        if name in names:
            errors.append(f"Skill duplicada: {name}")
        names.add(name)
        if path in paths:
            errors.append(f"Path canônico duplicado: {path}")
        paths.add(path)

        file_path = ROOT / path
        if not file_path.is_file():
            errors.append(f"Arquivo canônico ausente: {path}")
        else:
            fm = parse_frontmatter(file_path)
            if fm.get("name") != name:
                errors.append(f"Frontmatter name divergente em {path}: {fm.get('name')!r} != {name!r}")
            if not fm.get("description"):
                errors.append(f"Frontmatter description ausente em {path}")

        errors.extend(validate_catalog_docs(name, path, version, readme, status))

        for mirror in skill.get("mirrors", []):
            mode = mirror.get("mode", "push")
            repository = mirror.get("repository")
            branch = mirror.get("branch", "main")
            target_path = mirror.get("path")

            if mode not in VALID_MIRROR_MODES:
                errors.append(f"Modo de espelho inválido em {name}: {mode}")
            if not repository or not target_path:
                errors.append(f"Espelho inválido em {name}: {mirror!r}")
                continue
            if not is_safe_relative_path(target_path):
                errors.append(f"Path de mirror inseguro em {name}: {target_path!r}")

            target_key = (repository, branch, target_path)
            if target_key in mirror_targets:
                errors.append(f"Target de mirror duplicado: {repository}:{branch}:{target_path}")
            mirror_targets.add(target_key)

            if mode == "pull":
                pull_mirror_count += 1

    actual_paths = canonical_skill_paths()
    for unregistered in sorted(actual_paths - paths):
        errors.append(f"Skill canônica não registrada: {unregistered}")
    for missing in sorted(paths - actual_paths):
        errors.append(f"Registry aponta para skill inexistente: {missing}")

    if pull_mirror_count:
        reusable = pull_runtime.get("reusable_workflow")
        consumer = pull_runtime.get("consumer_workflow")
        if not reusable:
            errors.append("pull_mirror.reusable_workflow é obrigatório quando há mirrors pull.")
        if not consumer:
            errors.append("pull_mirror.consumer_workflow é obrigatório quando há mirrors pull.")

    return errors


def copy_skill(source_skill_file: Path, target_repo: Path, target_path: str) -> None:
    source_dir = source_skill_file.parent
    destination = target_repo / target_path
    if destination.exists():
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_dir, destination)


def sync_push_mirror(skill: dict, mirror: dict, apply: bool) -> dict:
    repository = mirror["repository"]
    branch = mirror.get("branch", "main")
    target_path = mirror["path"]
    source_file = ROOT / skill["path"]

    with tempfile.TemporaryDirectory(prefix="skills-sync-") as tmp:
        repo_dir = Path(tmp) / repository.split("/", 1)[1]
        run(["gh", "repo", "clone", repository, str(repo_dir), "--", "--branch", branch, "--single-branch"])
        copy_skill(source_file, repo_dir, target_path)

        status = run(["git", "status", "--porcelain", "--", target_path], cwd=repo_dir).stdout.strip()
        changed = bool(status)
        result = {
            "skill": skill["name"],
            "version": skill["version"],
            "repository": repository,
            "branch": branch,
            "path": target_path,
            "mode": "push",
            "changed": changed,
            "applied": False,
        }
        if not changed or not apply:
            return result

        run(["git", "add", "--", target_path], cwd=repo_dir)
        run(["git", "commit", "-m", f"chore(skills): sincronizar {skill['name']} v{skill['version']}"], cwd=repo_dir)
        run(["git", "push", "origin", branch], cwd=repo_dir)
        result["applied"] = True
        return result


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Valida catálogo, registry e configuração dos mirrors.")
    mode.add_argument("--apply", action="store_true", help="Aplica somente mirrors mode=push.")
    parser.add_argument("--skill", action="append", default=[], help="Limita a uma ou mais skills pelo nome.")
    args = parser.parse_args()

    data = load_registry()
    errors = validate_registry(data)
    if errors:
        for error in errors:
            print(f"ERRO: {error}", file=sys.stderr)
        return 2

    selected = set(args.skill)
    known = {s["name"] for s in data.get("skills", [])}
    unknown = selected - known
    if unknown:
        print(f"ERRO: skills não registradas: {', '.join(sorted(unknown))}", file=sys.stderr)
        return 2

    selected_mirrors: list[tuple[dict, dict]] = []
    for skill in data.get("skills", []):
        if selected and skill["name"] not in selected:
            continue
        for mirror in skill.get("mirrors", []):
            selected_mirrors.append((skill, mirror))

    push_mirrors = [(skill, mirror) for skill, mirror in selected_mirrors if mirror.get("mode", "push") == "push"]

    if args.apply and push_mirrors:
        if shutil.which("gh") is None or shutil.which("git") is None:
            print("ERRO: --apply para mirrors push requer gh e git no PATH.", file=sys.stderr)
            return 2
        if not os.environ.get("GH_TOKEN"):
            auth = run(["gh", "auth", "status"], check=False)
            if auth.returncode != 0:
                print("ERRO: GitHub CLI não autenticado e GH_TOKEN ausente.", file=sys.stderr)
                return 2

    results: list[dict] = []
    reusable = data.get("pull_mirror", {}).get("reusable_workflow", "")
    for skill, mirror in selected_mirrors:
        mirror_mode = mirror.get("mode", "push")
        if mirror_mode == "pull":
            results.append({
                "skill": skill["name"],
                "version": skill["version"],
                "repository": mirror["repository"],
                "branch": mirror.get("branch", "main"),
                "path": mirror["path"],
                "mode": "pull",
                "reusable_workflow": reusable,
                "changed": False,
                "applied": False,
            })
        else:
            results.append(sync_push_mirror(skill, mirror, apply=args.apply))

    print(f"Catálogo válido: {len(data.get('skills', []))} skills canônicas registradas e documentadas.")
    print(f"Espelhos selecionados: {len(selected_mirrors)}.")
    for result in results:
        if result["mode"] == "pull":
            print(f"PULL: {result['skill']} -> {result['repository']}:{result['path']} via {result['reusable_workflow']}")
            continue
        state = "ATUALIZADO" if result["applied"] else ("DRIFT" if result["changed"] else "OK")
        print(f"{state}: {result['skill']} -> {result['repository']}:{result['path']}")

    if args.check and any(r["mode"] == "push" and r["changed"] for r in results):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
