from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

FRONTMATTER_BOUNDARY = "---"
SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def load_frontmatter(path: Path) -> dict[str, Any]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ValueError(f"não foi possível ler {path}: {exc}") from exc

    lines = text.splitlines()
    if not lines or lines[0].strip() != FRONTMATTER_BOUNDARY:
        raise ValueError(f"frontmatter YAML ausente em {path}")

    try:
        closing = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == FRONTMATTER_BOUNDARY)
    except StopIteration as exc:
        raise ValueError(f"frontmatter YAML sem delimitador final em {path}") from exc

    yaml_text = "\n".join(lines[1:closing])
    try:
        data = yaml.safe_load(yaml_text)
    except yaml.YAMLError as exc:
        raise ValueError(f"frontmatter YAML inválido em {path}: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError(f"frontmatter YAML deve ser mapping em {path}")
    return data


def extract_catalog_versions(markdown: str) -> dict[str, str]:
    versions: dict[str, str] = {}
    for raw_line in markdown.splitlines():
        line = raw_line.strip()
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if not cells:
            continue
        name_match = re.search(r"`([a-z0-9]+(?:-[a-z0-9]+)*)`", cells[0])
        if not name_match:
            continue
        name = name_match.group(1)
        version = None
        for cell in cells[1:]:
            candidate = cell.replace("**", "").replace("`", "").strip()
            if SEMVER_RE.fullmatch(candidate):
                version = candidate
                break
        if version is None:
            continue
        if name in versions and versions[name] != version:
            raise ValueError(f"entrada de catálogo duplicada para {name}")
        versions[name] = version
    return versions


def validate_skill_record(
    root: Path,
    skill: dict[str, Any],
    readme_versions: dict[str, str],
    status_versions: dict[str, str],
) -> list[str]:
    errors: list[str] = []
    name = skill.get("name")
    version = skill.get("version")
    path = skill.get("path")

    if not isinstance(name, str) or not SKILL_NAME_RE.fullmatch(name):
        errors.append(f"nome de skill inválido: {name!r}")
        return errors
    if not isinstance(version, str) or not SEMVER_RE.fullmatch(version):
        errors.append(f"SemVer inválido em {name}: {version!r}")
    expected_path = f"skills/{name}/SKILL.md"
    if path != expected_path:
        errors.append(f"path canônico de {name} deve ser {expected_path}, encontrado {path!r}")
        return errors

    skill_file = root / expected_path
    if not skill_file.is_file():
        errors.append(f"arquivo canônico ausente: {expected_path}")
        return errors
    try:
        frontmatter = load_frontmatter(skill_file)
    except ValueError as exc:
        errors.append(str(exc))
        return errors
    if frontmatter.get("name") != name:
        errors.append(f"frontmatter name divergente em {expected_path}: {frontmatter.get('name')!r} != {name!r}")
    description = frontmatter.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"frontmatter description ausente em {expected_path}")

    readme_version = readme_versions.get(name)
    if readme_version != version:
        errors.append(f"README.md deve registrar {name} como {version}, encontrado {readme_version!r}")
    status_version = status_versions.get(name)
    if status_version != version:
        errors.append(f"general-skills-status.md deve registrar {name} como {version}, encontrado {status_version!r}")
    return errors
