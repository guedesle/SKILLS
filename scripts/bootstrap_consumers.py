#!/usr/bin/env python3
"""Instala/valida o workflow consumidor padrão nos repositórios pull registrados.

O bootstrap é necessário somente uma vez por repositório/branch. Depois disso,
novas skills e novos mappings para esse consumidor passam a ser controlados
exclusivamente por `registry.json`.

Uso:
  python scripts/bootstrap_consumers.py --check
  python scripts/bootstrap_consumers.py --apply
  python scripts/bootstrap_consumers.py --apply --repository owner/repo

`--apply` usa a autenticação do GitHub CLI. Para criar/alterar arquivos em
`.github/workflows`, a credencial precisa ter permissão de workflow/conteúdo
adequada no repositório consumidor.
"""

from __future__ import annotations

import argparse
import base64
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry.json"
TEMPLATE = ROOT / "templates" / "sync-central-skills.yml"


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    proc = subprocess.run(cmd, text=True, capture_output=True, encoding="utf-8", errors="replace")
    if check and proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"Falha: {' '.join(cmd)}")
    return proc


def load_registry() -> dict:
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def consumers(data: dict) -> list[tuple[str, str]]:
    found: set[tuple[str, str]] = set()
    for skill in data.get("skills", []):
        for mirror in skill.get("mirrors", []):
            if mirror.get("mode", "push") != "pull":
                continue
            repository = mirror.get("repository")
            branch = mirror.get("branch", "main")
            if repository:
                found.add((repository, branch))
    return sorted(found)


def fetch_remote(repository: str, branch: str, workflow_path: str) -> dict | None:
    endpoint = f"repos/{repository}/contents/{workflow_path}?ref={branch}"
    proc = run(["gh", "api", endpoint], check=False)
    if proc.returncode == 0:
        return json.loads(proc.stdout)
    if "404" in proc.stderr or "Not Found" in proc.stderr:
        return None
    raise RuntimeError(proc.stderr.strip() or proc.stdout.strip())


def decode_content(payload: dict) -> str:
    raw = payload.get("content", "").replace("\n", "")
    return base64.b64decode(raw).decode("utf-8")


def put_remote(repository: str, branch: str, workflow_path: str, content: str, sha: str | None) -> None:
    encoded = base64.b64encode(content.encode("utf-8")).decode("ascii")
    cmd = [
        "gh",
        "api",
        "--method",
        "PUT",
        f"repos/{repository}/contents/{workflow_path}",
        "-f",
        "message=chore(skills): bootstrap generic central mirror",
        "-f",
        f"content={encoded}",
        "-f",
        f"branch={branch}",
    ]
    if sha:
        cmd.extend(["-f", f"sha={sha}"])
    run(cmd)


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--apply", action="store_true")
    parser.add_argument("--repository", action="append", default=[], help="Filtra owner/repo; pode repetir.")
    args = parser.parse_args()

    if shutil.which("gh") is None:
        print("ERRO: GitHub CLI (gh) não encontrado no PATH.", file=sys.stderr)
        return 2
    auth = run(["gh", "auth", "status"], check=False)
    if auth.returncode != 0:
        print("ERRO: GitHub CLI não autenticado.", file=sys.stderr)
        return 2
    if not TEMPLATE.is_file():
        print(f"ERRO: template ausente: {TEMPLATE}", file=sys.stderr)
        return 2

    data = load_registry()
    workflow_path = data.get("pull_mirror", {}).get(
        "consumer_workflow", ".github/workflows/sync-central-skills.yml"
    )
    template = TEMPLATE.read_text(encoding="utf-8")
    selected = set(args.repository)

    targets = [item for item in consumers(data) if not selected or item[0] in selected]
    known_repositories = {repository for repository, _ in consumers(data)}
    unknown = selected - known_repositories
    if unknown:
        print(f"ERRO: consumidores não registrados: {', '.join(sorted(unknown))}", file=sys.stderr)
        return 2

    drift = False
    for repository, branch in targets:
        try:
            remote = fetch_remote(repository, branch, workflow_path)
            if remote is None:
                state = "MISSING"
                different = True
            else:
                current = decode_content(remote)
                different = current != template
                state = "DRIFT" if different else "OK"

            if args.apply and different:
                put_remote(
                    repository,
                    branch,
                    workflow_path,
                    template,
                    remote.get("sha") if remote else None,
                )
                state = "BOOTSTRAPPED"
                different = False

            drift = drift or different
            print(f"{state}: {repository}:{branch}:{workflow_path}")
        except RuntimeError as exc:
            print(f"ERRO: {repository}:{branch}: {exc}", file=sys.stderr)
            return 2

    print(f"Consumidores pull selecionados: {len(targets)}.")
    if args.check and drift:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
