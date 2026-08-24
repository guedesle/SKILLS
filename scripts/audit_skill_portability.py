from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

WINDOWS_ABS = re.compile(r"\b[A-Za-z]:\\[^\s`]+")
POSIX_LOCAL = re.compile(r"(?<!https:)(?<!http:)\B/(?:home|Users|mnt|opt|srv|var|tmp)/[^\s`]+")
LOCALHOST = re.compile(r"\b(?:localhost|127\.0\.0\.1|0\.0\.0\.0)(?::\d+)?\b", re.I)
PRIVATE_HOST = re.compile(r"https?://[^\s/]*(?:\.local|\.internal|\.corp)(?:/[^\s]*)?", re.I)
PROJECT_ONLY_PHRASE = re.compile(r"\b(?:somente|apenas|only)\s+(?:neste|nesse|this)\s+(?:projeto|repository|reposit[oó]rio)\b", re.I)
ADAPTER_MARKER = re.compile(r"\b(?:adapter|adaptador|variante local|project adapter|local variant)\b", re.I)
PROJECT_PATH_MARKER = re.compile(r"\.(?:agents|claude|opencode)/skills/[a-z0-9-]+", re.I)


def audit_text(text: str) -> dict:
    blockers: list[str] = []
    signals: list[str] = []

    if WINDOWS_ABS.search(text):
        blockers.append("absolute-windows-path")
    if POSIX_LOCAL.search(text):
        blockers.append("absolute-local-posix-path")
    if LOCALHOST.search(text):
        blockers.append("localhost-endpoint")
    if PRIVATE_HOST.search(text):
        blockers.append("private-hostname")
    if PROJECT_ONLY_PHRASE.search(text):
        blockers.append("explicit-project-only-contract")

    has_project_path = bool(PROJECT_PATH_MARKER.search(text))
    has_adapter_marker = bool(ADAPTER_MARKER.search(text))
    if has_project_path:
        signals.append("project-skill-path")
    if has_project_path and has_adapter_marker:
        signals.append("adapter-marker")

    if blockers:
        classification = "PROJECT_ONLY"
    elif has_project_path and has_adapter_marker:
        classification = "GENERAL_WITH_ADAPTER"
    elif has_project_path:
        classification = "GENERALIZABLE"
    else:
        classification = "GLOBAL_READY"

    return {"classification": classification, "blockers": blockers, "signals": signals}


def read_target(path: Path) -> str:
    if path.is_file():
        return path.read_text(encoding="utf-8", errors="replace")
    if path.is_dir():
        chunks: list[str] = []
        for child in sorted(path.rglob("*")):
            if child.is_file() and child.suffix.lower() in {".md", ".yaml", ".yml", ".json", ".txt", ".py"}:
                chunks.append(child.read_text(encoding="utf-8", errors="replace"))
        return "\n".join(chunks)
    raise FileNotFoundError(path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        result = audit_text(read_target(args.path))
    except OSError as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["classification"] != "PROJECT_ONLY" else 3


if __name__ == "__main__":
    raise SystemExit(main())
