#!/usr/bin/env python3
"""Sincroniza skills canônicas de guedesle/SKILLS para espelhos registrados.

Uso:
  python scripts/sync_skills.py --check
  python scripts/sync_skills.py --apply

O script só altera caminhos explicitamente declarados em registry.json e nunca remove
conteúdo fora desses caminhos.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry.json"


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


def validate_registry(data: dict) -> list[str]:
    errors: list[str] = []
    names: set[str] = set()
    paths: set[str] = set()

    for skill in data.get("skills", []):
        name = skill.get("name")
        path = skill.get("path")
        version = skill.get("version")
        if not name or not path or not version:
            errors.append(f"Registro incompleto: {skill!r}")
            continue
        if name in names:
            errors.append(f"Skill duplicada: {name}")
        names.add(name)
        if path in paths:
            errors.append(f"Path canônico duplicado: {path}")
        paths.add(path)
        file_path = ROOT / path
        if not file_path.is_file():
            errors.append(f"Arquivo canônico ausente: {path}")
        if file_path.name != "SKILL.md":
            errors.append(f"Path canônico deve terminar em SKILL.md: {path}")

        for mirror in skill.get("mirrors", []):
            if not mirror.get("repository") or not mirror.get("path"):
                errors.append(f"Espelho inválido em {name}: {mirror!r}")

    return errors


def copy_skill(source_skill_file: Path, target_repo: Path, target_path: str) -> None:
    source_dir = source_skill_file.parent
    destination = target_repo / target_path
    if destination.exists():
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_dir, destination)


def sync_mirror(skill: dict, mirror: dict, apply: bool) -> dict:
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
            "changed": changed,
            "applied": False,
        }
        if not changed or not apply:
            return result

        run(["git", "add", "--", target_path], cwd=repo_dir)
        run(
            [
                "git",
                "commit",
                "-m",
                f"chore(skills): sincronizar {skill['name']} v{skill['version']}",
            ],
            cwd=repo_dir,
        )
        run(["git", "push", "origin", branch], cwd=repo_dir)
        result["applied"] = True
        return result


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Valida registro e mostra drift sem push.")
    mode.add_argument("--apply", action="store_true", help="Sincroniza os espelhos registrados e faz push.")
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

    if args.apply:
        if shutil.which("gh") is None or shutil.which("git") is None:
            print("ERRO: --apply requer gh e git no PATH.", file=sys.stderr)
            return 2
        if not os.environ.get("GH_TOKEN"):
            auth = run(["gh", "auth", "status"], check=False)
            if auth.returncode != 0:
                print("ERRO: GitHub CLI não autenticado e GH_TOKEN ausente.", file=sys.stderr)
                return 2

    results: list[dict] = []
    mirror_count = 0
    for skill in data.get("skills", []):
        if selected and skill["name"] not in selected:
            continue
        for mirror in skill.get("mirrors", []):
            mirror_count += 1
            results.append(sync_mirror(skill, mirror, apply=args.apply))

    print(f"Registro válido: {len(data.get('skills', []))} skills canônicas.")
    print(f"Espelhos selecionados: {mirror_count}.")
    for result in results:
        state = "ATUALIZADO" if result["applied"] else ("DRIFT" if result["changed"] else "OK")
        print(f"{state}: {result['skill']} -> {result['repository']}:{result['path']}")

    if args.check and any(r["changed"] for r in results):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
