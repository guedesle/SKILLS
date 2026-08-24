from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
VALID_KINDS = {"trigger_positive", "trigger_negative", "behavior", "portability"}
FILE_KIND = {
    "trigger-positive.yaml": "trigger_positive",
    "trigger-negative.yaml": "trigger_negative",
    "behavior.yaml": "behavior",
    "portability.yaml": "portability",
}
REQUIRED_EVAL_FILES = ("trigger-positive.yaml", "trigger-negative.yaml", "behavior.yaml")
ALLOWED_TOP_LEVEL = {"schema_version", "skill", "kind", "cases"}
ALLOWED_CASE_KEYS = {"id", "input", "expect", "classification", "notes"}


def _load_yaml(path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        return None, [f"{path}: YAML inválido: {exc}"]
    if not isinstance(data, dict):
        return None, [f"{path}: documento deve ser mapping"]
    return data, []


def validate_eval_document(path: Path, expected_kind: str | None = None, expected_skill: str | None = None) -> list[str]:
    errors: list[str] = []
    data, load_errors = _load_yaml(path)
    if load_errors:
        return load_errors
    assert data is not None

    unknown_top = sorted(set(data) - ALLOWED_TOP_LEVEL)
    if unknown_top:
        errors.append(f"{path}: chaves top-level não suportadas: {', '.join(unknown_top)}")

    if data.get("schema_version") != 1:
        errors.append(f"{path}: schema_version deve ser 1")

    skill = data.get("skill")
    if not isinstance(skill, str) or not skill.strip():
        errors.append(f"{path}: skill deve ser string não vazia")
    elif expected_skill and skill != expected_skill:
        errors.append(f"{path}: skill {skill!r} diverge de {expected_skill!r}")

    kind = data.get("kind")
    if kind not in VALID_KINDS:
        errors.append(f"{path}: kind inválido: {kind!r}")
    if expected_kind and kind != expected_kind:
        errors.append(f"{path}: kind {kind!r} diverge do esperado {expected_kind!r}")

    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        errors.append(f"{path}: cases deve ser lista não vazia")
        return errors

    seen: set[str] = set()
    for index, case in enumerate(cases, start=1):
        prefix = f"{path}: case #{index}"
        if not isinstance(case, dict):
            errors.append(f"{prefix} deve ser mapping")
            continue
        unknown_case = sorted(set(case) - ALLOWED_CASE_KEYS)
        if unknown_case:
            errors.append(f"{prefix}: chaves não suportadas: {', '.join(unknown_case)}")
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(f"{prefix}: id deve ser string não vazia")
        elif case_id in seen:
            errors.append(f"{prefix}: id duplicado: {case_id}")
        else:
            seen.add(case_id)
        case_input = case.get("input")
        if not isinstance(case_input, str) or not case_input.strip():
            errors.append(f"{prefix}: input deve ser string não vazia")
        if kind == "behavior":
            expect = case.get("expect")
            if not isinstance(expect, str) or not expect.strip():
                errors.append(f"{prefix}: behavior exige expect não vazio")
        if kind == "portability":
            classification = case.get("classification")
            if classification not in {"PROJECT_ONLY", "GENERALIZABLE", "GENERAL_WITH_ADAPTER", "GLOBAL_READY"}:
                errors.append(f"{prefix}: portability exige classification válida")
    return errors


def iter_eval_files(root: Path, selected: set[str]) -> list[tuple[Path, str, str]]:
    items: list[tuple[Path, str, str]] = []
    skills_root = root / "skills"
    if not skills_root.is_dir():
        return items
    for skill_dir in sorted(p for p in skills_root.iterdir() if p.is_dir()):
        if selected and skill_dir.name not in selected:
            continue
        eval_dir = skill_dir / "evals"
        if not eval_dir.is_dir():
            continue
        for path in sorted(eval_dir.glob("*.yaml")):
            expected_kind = FILE_KIND.get(path.name)
            if expected_kind is None:
                items.append((path, "__unsupported__", skill_dir.name))
            else:
                items.append((path, expected_kind, skill_dir.name))
    return items


def validate_repository(root: Path = ROOT, selected: set[str] | None = None) -> list[str]:
    selected = selected or set()
    errors: list[str] = []
    skills_root = root / "skills"
    known = {p.name for p in skills_root.iterdir() if p.is_dir()} if skills_root.is_dir() else set()
    unknown = selected - known
    if unknown:
        errors.append(f"skills não encontradas: {', '.join(sorted(unknown))}")
        return errors

    skills_to_check = sorted(selected or known)
    for skill in skills_to_check:
        skill_dir = skills_root / skill
        eval_dir = skill_dir / "evals"
        if not eval_dir.is_dir():
            continue
        if not (skill_dir / "SKILL.md").is_file():
            errors.append(f"{skill}: SKILL.md ausente para pacote com evals")
        for required in REQUIRED_EVAL_FILES:
            if not (eval_dir / required).is_file():
                errors.append(f"{skill}: eval obrigatório ausente: {required}")

    for path, expected_kind, skill in iter_eval_files(root, selected):
        if expected_kind == "__unsupported__":
            errors.append(f"{path}: nome de arquivo de eval não suportado")
            continue
        errors.extend(validate_eval_document(path, expected_kind, skill))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", action="append", default=[])
    args = parser.parse_args()
    errors = validate_repository(ROOT, set(args.skill))
    if errors:
        for error in errors:
            print(f"ERRO: {error}", file=sys.stderr)
        return 2
    print("Skill eval validation PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
