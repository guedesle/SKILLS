#!/usr/bin/env python3
"""Sincroniza, em um repositório consumidor, todos os mirrors pull registrados.

Este script é executado pelo workflow reutilizável do catálogo central. Ele lê
`registry.json`, seleciona somente os mirrors `mode: pull` do repositório/branch
correntes e copia exclusivamente os diretórios explicitamente gerenciados.

O script não faz commit, push nem remove conteúdo fora dos paths registrados.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path


def load_registry(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def safe_relative_path(raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute() or not raw.strip() or ".." in path.parts:
        raise ValueError(f"Path de mirror inseguro: {raw!r}")
    return path


def ensure_inside(root: Path, child: Path) -> Path:
    root_resolved = root.resolve()
    child_resolved = child.resolve()
    try:
        child_resolved.relative_to(root_resolved)
    except ValueError as exc:
        raise ValueError(f"Destino fora do repositório consumidor: {child}") from exc
    return child_resolved


def select_pull_mirrors(data: dict, repository: str, branch: str | None) -> list[dict]:
    matches: list[dict] = []
    repo_pull_branches: set[str] = set()

    for skill in data.get("skills", []):
        for mirror in skill.get("mirrors", []):
            if mirror.get("mode", "push") != "pull":
                continue
            if mirror.get("repository") != repository:
                continue

            mirror_branch = mirror.get("branch", "main")
            repo_pull_branches.add(mirror_branch)
            if branch and mirror_branch != branch:
                continue

            matches.append(
                {
                    "name": skill["name"],
                    "version": skill["version"],
                    "source": skill["path"],
                    "target": mirror["path"],
                    "branch": mirror_branch,
                }
            )

    if not matches:
        if repo_pull_branches and branch:
            known = ", ".join(sorted(repo_pull_branches))
            raise RuntimeError(
                f"Há mirrors pull para {repository}, mas não para a branch {branch!r}. "
                f"Branches registradas: {known}."
            )
        raise RuntimeError(f"Nenhum mirror pull registrado para {repository}.")

    return matches


def copy_registered_mirrors(central_root: Path, target_root: Path, mirrors: list[dict]) -> list[str]:
    managed_paths: list[str] = []
    seen_targets: set[str] = set()

    for mirror in mirrors:
        source_file = central_root / safe_relative_path(mirror["source"])
        if not source_file.is_file() or source_file.name != "SKILL.md":
            raise RuntimeError(f"Skill canônica ausente ou inválida: {mirror['source']}")

        source_dir = source_file.parent
        target_rel = safe_relative_path(mirror["target"])
        target_key = target_rel.as_posix()
        if target_key in seen_targets:
            raise RuntimeError(f"Path de mirror duplicado para o consumidor: {target_key}")
        seen_targets.add(target_key)

        destination = ensure_inside(target_root, target_root / target_rel)
        if destination.exists():
            shutil.rmtree(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source_dir, destination)

        managed_paths.append(target_key)
        print(
            f"SYNC: {mirror['name']} v{mirror['version']} -> "
            f"{target_key} ({mirror['branch']})"
        )

    return managed_paths


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--central-root", required=True, help="Checkout do catálogo guedesle/SKILLS.")
    parser.add_argument("--repository", required=True, help="Repositório consumidor em owner/name.")
    parser.add_argument("--branch", help="Branch corrente do consumidor.")
    parser.add_argument("--target-root", required=True, help="Checkout do repositório consumidor.")
    parser.add_argument("--paths-output", required=True, help="Arquivo que receberá um path gerenciado por linha.")
    args = parser.parse_args()

    central_root = Path(args.central_root).resolve()
    target_root = Path(args.target_root).resolve()
    registry_path = central_root / "registry.json"

    if not registry_path.is_file():
        print(f"ERRO: registry.json ausente em {central_root}", file=sys.stderr)
        return 2
    if not target_root.is_dir():
        print(f"ERRO: checkout consumidor ausente em {target_root}", file=sys.stderr)
        return 2

    try:
        data = load_registry(registry_path)
        mirrors = select_pull_mirrors(data, args.repository, args.branch)
        managed_paths = copy_registered_mirrors(central_root, target_root, mirrors)
    except (RuntimeError, ValueError, KeyError) as exc:
        print(f"ERRO: {exc}", file=sys.stderr)
        return 2

    output = Path(args.paths_output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(managed_paths) + "\n", encoding="utf-8")

    print(f"Mirrors pull sincronizados: {len(managed_paths)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
