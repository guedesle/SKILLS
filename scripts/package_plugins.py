#!/usr/bin/env python3
"""Build skills-only OpenAI plugin marketplace artifacts from canonical skills."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import stat
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry.json"
PLUGIN_CATALOG = ROOT / "plugin-catalog.json"
DEFAULT_OUTPUT = ROOT / "dist" / "plugins"
SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EXCLUDED_PARTS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache"}
EXCLUDED_NAMES = {".DS_Store"}
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def load_json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise RuntimeError(f"{path} deve conter objeto JSON")
    return data


def canonical_skill_map(root: Path, registry: dict) -> dict[str, dict]:
    result: dict[str, dict] = {}
    for item in registry.get("skills", []):
        name = item.get("name")
        if name:
            result[name] = item
    return result


def packageable_files(skill_dir: Path) -> list[Path]:
    files: list[Path] = []
    for path in skill_dir.rglob("*"):
        rel = path.relative_to(skill_dir)
        if any(part in EXCLUDED_PARTS for part in rel.parts) or path.name in EXCLUDED_NAMES:
            continue
        if path.is_symlink():
            raise RuntimeError(f"symlink não permitido em plugin: {rel.as_posix()}")
        if path.is_file():
            files.append(path)
    return sorted(files, key=lambda p: p.relative_to(skill_dir).as_posix())


def validate_catalog(root: Path, registry: dict, catalog: dict) -> list[str]:
    errors: list[str] = []
    if catalog.get("schema_version") != 1:
        errors.append("plugin-catalog.json: schema_version deve ser 1")

    marketplace = catalog.get("marketplace")
    if not isinstance(marketplace, dict) or not marketplace.get("name") or not marketplace.get("display_name"):
        errors.append("plugin-catalog.json: marketplace exige name e display_name")

    plugins = catalog.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        return errors + ["plugin-catalog.json: plugins deve ser lista não vazia"]

    known = canonical_skill_map(root, registry)
    seen_plugins: set[str] = set()
    assigned: set[str] = set()

    for plugin in plugins:
        name = plugin.get("name", "")
        version = plugin.get("version", "")
        prefix = f"plugin {name or '<sem-nome>'}"
        if not NAME_RE.fullmatch(name):
            errors.append(f"{prefix}: name deve ser kebab-case")
        if name in seen_plugins:
            errors.append(f"{prefix}: plugin duplicado")
        seen_plugins.add(name)
        if not SEMVER_RE.fullmatch(version):
            errors.append(f"{prefix}: version deve ser SemVer")
        for key in ("description", "display_name", "short_description", "long_description", "category"):
            if not isinstance(plugin.get(key), str) or not plugin[key].strip():
                errors.append(f"{prefix}: {key} obrigatório")
        prompts = plugin.get("default_prompts", [])
        if prompts and (not isinstance(prompts, list) or not all(isinstance(x, str) and x.strip() for x in prompts)):
            errors.append(f"{prefix}: default_prompts deve ser lista de strings")
        skills = plugin.get("skills")
        if not isinstance(skills, list) or not skills:
            errors.append(f"{prefix}: skills deve ser lista não vazia")
            continue
        local_seen: set[str] = set()
        for skill_name in skills:
            if skill_name in local_seen:
                errors.append(f"{prefix}: skill duplicada no plugin: {skill_name}")
                continue
            local_seen.add(skill_name)
            if skill_name in assigned:
                errors.append(f"{prefix}: skill já atribuída a outro plugin: {skill_name}")
            assigned.add(skill_name)
            record = known.get(skill_name)
            if not record:
                errors.append(f"{prefix}: skill não registrada: {skill_name}")
                continue
            expected = root / record["path"]
            if not expected.is_file():
                errors.append(f"{prefix}: SKILL.md ausente: {record['path']}")
                continue
            try:
                files = packageable_files(expected.parent)
            except RuntimeError as exc:
                errors.append(f"{prefix}: {exc}")
                continue
            if expected not in files:
                errors.append(f"{prefix}: SKILL.md não seria empacotado: {skill_name}")
    return errors


def plugin_manifest(plugin: dict) -> dict:
    return {
        "name": plugin["name"],
        "version": plugin["version"],
        "description": plugin["description"],
        "repository": "https://github.com/guedesle/SKILLS",
        "skills": "./skills/",
        "interface": {
            "displayName": plugin["display_name"],
            "shortDescription": plugin["short_description"],
            "longDescription": plugin["long_description"],
            "developerName": "guedesle",
            "category": plugin["category"],
            "defaultPrompt": plugin.get("default_prompts", []),
        },
    }


def marketplace_manifest(catalog: dict) -> dict:
    return {
        "name": catalog["marketplace"]["name"],
        "interface": {"displayName": catalog["marketplace"]["display_name"]},
        "plugins": [
            {
                "name": plugin["name"],
                "source": {"source": "local", "path": f"./plugins/{plugin['name']}"},
                "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                "category": plugin["category"],
            }
            for plugin in catalog["plugins"]
        ],
    }


def _copy_skill(source_dir: Path, dest_dir: Path) -> None:
    for path in packageable_files(source_dir):
        rel = path.relative_to(source_dir)
        dest = dest_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)


def _zip_tree(source_dir: Path, zip_path: Path) -> None:
    with zipfile.ZipFile(zip_path, "w") as archive:
        for path in sorted(p for p in source_dir.rglob("*") if p.is_file()):
            rel = path.relative_to(source_dir).as_posix()
            info = zipfile.ZipInfo(rel, date_time=ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(info, path.read_bytes())


def build(root: Path, output: Path, registry: dict, catalog: dict) -> dict:
    if output.exists():
        shutil.rmtree(output)
    marketplace_root = output / "marketplace"
    plugin_root = marketplace_root / "plugins"
    known = canonical_skill_map(root, registry)
    built: list[dict] = []

    for plugin in catalog["plugins"]:
        target = plugin_root / plugin["name"]
        (target / ".codex-plugin").mkdir(parents=True, exist_ok=True)
        (target / ".codex-plugin" / "plugin.json").write_text(
            json.dumps(plugin_manifest(plugin), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        skill_versions: list[dict] = []
        for skill_name in plugin["skills"]:
            record = known[skill_name]
            source_dir = (root / record["path"]).parent
            _copy_skill(source_dir, target / "skills" / skill_name)
            skill_versions.append({"name": skill_name, "version": record["version"]})

        archive = output / f"{plugin['name']}-v{plugin['version']}.zip"
        archive.parent.mkdir(parents=True, exist_ok=True)
        _zip_tree(target, archive)
        built.append({
            "name": plugin["name"],
            "version": plugin["version"],
            "archive": archive.name,
            "skills": skill_versions,
        })

    market_file = marketplace_root / ".agents" / "plugins" / "marketplace.json"
    market_file.parent.mkdir(parents=True, exist_ok=True)
    market_file.write_text(
        json.dumps(marketplace_manifest(catalog), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    manifest = {
        "schema_version": 1,
        "source_repository": registry.get("repository"),
        "format": "openai-skills-only-plugin-marketplace",
        "marketplace_root": "marketplace",
        "plugins": built,
    }
    (output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Valida catálogo de plugins sem gerar artefatos.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    try:
        registry = load_json(REGISTRY)
        catalog = load_json(PLUGIN_CATALOG)
    except (OSError, json.JSONDecodeError, RuntimeError) as exc:
        print(f"ERRO: {exc}", file=sys.stderr)
        return 2

    errors = validate_catalog(ROOT, registry, catalog)
    if errors:
        for error in errors:
            print(f"ERRO: {error}", file=sys.stderr)
        return 2

    if args.check:
        print(f"Skills-only plugin check PASS: {len(catalog['plugins'])} plugin(s).")
        return 0

    output = args.output if args.output.is_absolute() else ROOT / args.output
    manifest = build(ROOT, output, registry, catalog)
    print(f"Skills-only plugin marketplace gerado: {len(manifest['plugins'])} plugin(s) em {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
