#!/usr/bin/env python3
"""Empacota skills canônicas como bundles Agent Skills para upload no ChatGPT.

Cada ZIP contém uma única skill com SKILL.md na raiz do arquivo, preservando
references/, scripts/, assets/ e demais recursos da pasta canônica.

Uso:
  python scripts/package_chatgpt_skills.py --check
  python scripts/package_chatgpt_skills.py
  python scripts/package_chatgpt_skills.py --skill low-hitl-orchestration
  python scripts/package_chatgpt_skills.py --output dist/chatgpt
"""

from __future__ import annotations

import argparse
import json
import stat
import sys
import zipfile
from pathlib import Path

from skill_validation import SKILL_NAME_RE, load_frontmatter

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry.json"
DEFAULT_OUTPUT = ROOT / "dist" / "chatgpt"
EXCLUDED_PARTS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache"}
EXCLUDED_NAMES = {".DS_Store"}
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def load_registry() -> dict:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if data.get("repository") != "guedesle/SKILLS":
        raise RuntimeError("registry.json não aponta para guedesle/SKILLS.")
    skills = data.get("skills")
    if not isinstance(skills, list) or not skills:
        raise RuntimeError("registry.json não contém skills registradas.")
    return data


def packageable_files(skill_dir: Path) -> list[Path]:
    files: list[Path] = []
    for path in skill_dir.rglob("*"):
        rel = path.relative_to(skill_dir)
        if any(part in EXCLUDED_PARTS for part in rel.parts):
            continue
        if path.name in EXCLUDED_NAMES:
            continue
        if path.is_symlink():
            raise RuntimeError(f"Symlink não permitido em bundle de skill: {rel.as_posix()}")
        if path.is_file():
            files.append(path)
    return sorted(files, key=lambda p: p.relative_to(skill_dir).as_posix())


def validate_skill(skill: dict) -> list[str]:
    errors: list[str] = []
    name = skill.get("name", "")
    version = skill.get("version", "")
    path = skill.get("path", "")

    if not SKILL_NAME_RE.fullmatch(name):
        errors.append(f"nome inválido: {name!r}")
        return errors

    expected = f"skills/{name}/SKILL.md"
    if path != expected:
        errors.append(f"path de {name} deve ser {expected}, encontrado {path!r}")
        return errors

    skill_file = ROOT / path
    if not skill_file.is_file():
        errors.append(f"SKILL.md ausente: {path}")
        return errors

    try:
        frontmatter = load_frontmatter(skill_file)
    except ValueError as exc:
        errors.append(str(exc))
        return errors
    if frontmatter.get("name") != name:
        errors.append(f"frontmatter name divergente em {path}")
    description = frontmatter.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"frontmatter description ausente em {path}")
    if not version:
        errors.append(f"versão ausente em registry.json para {name}")

    try:
        files = packageable_files(skill_file.parent)
    except RuntimeError as exc:
        errors.append(str(exc))
        return errors

    if skill_file not in files:
        errors.append(f"SKILL.md não seria incluído no bundle de {name}")
    return errors


def zip_entry(path: Path, arcname: str) -> tuple[zipfile.ZipInfo, bytes]:
    info = zipfile.ZipInfo(arcname, date_time=ZIP_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = (stat.S_IFREG | 0o644) << 16
    return info, path.read_bytes()


def build_bundle(skill: dict, output_dir: Path) -> Path:
    name = skill["name"]
    version = skill["version"]
    skill_dir = (ROOT / skill["path"]).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    bundle = output_dir / f"{name}-v{version}.zip"

    with zipfile.ZipFile(bundle, "w") as archive:
        for path in packageable_files(skill_dir):
            arcname = path.relative_to(skill_dir).as_posix()
            info, payload = zip_entry(path, arcname)
            archive.writestr(info, payload)
    return bundle


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Valida empacotamento sem gerar ZIPs.")
    parser.add_argument("--skill", action="append", default=[], help="Limita a uma ou mais skills pelo nome.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Diretório de saída dos bundles.")
    args = parser.parse_args()

    data = load_registry()
    skills = data["skills"]
    selected = set(args.skill)
    known = {skill["name"] for skill in skills}
    unknown = selected - known
    if unknown:
        print(f"ERRO: skills não registradas: {', '.join(sorted(unknown))}", file=sys.stderr)
        return 2

    chosen = [skill for skill in skills if not selected or skill["name"] in selected]
    errors: list[str] = []
    for skill in chosen:
        errors.extend(f"{skill['name']}: {error}" for error in validate_skill(skill))

    if errors:
        for error in errors:
            print(f"ERRO: {error}", file=sys.stderr)
        return 2

    if args.check:
        print(f"ChatGPT package check PASS: {len(chosen)} skills registradas e empacotáveis.")
        return 0

    output = args.output if args.output.is_absolute() else ROOT / args.output
    bundles = [build_bundle(skill, output) for skill in chosen]
    manifest = {
        "schema_version": 1,
        "source_repository": data["repository"],
        "format": "agent-skills",
        "bundle_layout": "one-skill-per-zip-with-SKILL.md-at-root",
        "skills": [
            {
                "name": skill["name"],
                "version": skill["version"],
                "bundle": f"{skill['name']}-v{skill['version']}.zip",
            }
            for skill in chosen
        ],
    }
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Bundles ChatGPT gerados: {len(bundles)} em {display_path(output)}")
    for bundle in bundles:
        print(display_path(bundle))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
