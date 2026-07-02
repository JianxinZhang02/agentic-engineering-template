#!/usr/bin/env python3
"""Lightweight health check for the Agentic Engineering template.

The script is intentionally dependency-free so it can run in a freshly cloned
template on Windows, macOS, and Linux.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "context/INDEX.md",
    "context/team/INDEX.md",
    "context/team/ai-policy.md",
    "context/team/tooling-governance.md",
    "requirements/_template/requirement.md",
    "requirements/_template/design.md",
    "requirements/_template/test-plan.md",
    "skills/README.md",
    "commands/README.md",
    "prompts/README.md",
    "rules/README.md",
    "hooks/README.md",
    "mcp-configs/README.md",
    "eval/README.md",
    "core_skills.json",
]

JSON_FILES = [
    "core_skills.json",
    "mcp-configs/mcp-servers.example.json",
    "mcp-configs/extensions.catalog.json",
    "schemas/skill-metadata.schema.json",
    "schemas/knowledge-entry.schema.json",
    "schemas/requirement-metadata.schema.json",
]

SENSITIVE_PATTERNS = [
    re.compile(r"\b[A-Z]:\\", re.IGNORECASE),
    re.compile(r"对话\.md"),
    re.compile(r"Agentic Engineering 规范建设指南\.pdf"),
    re.compile("sk-" + r"proj-[A-Za-z0-9_-]+"),
]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_required_files(errors: list[str]) -> None:
    for item in REQUIRED_FILES:
        if not (ROOT / item).exists():
            errors.append(f"missing required file: {item}")


def check_json(errors: list[str]) -> None:
    for item in JSON_FILES:
        path = ROOT / item
        if not path.exists():
            errors.append(f"missing json file: {item}")
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid json: {item}: {exc}")


def check_prompt_templates(errors: list[str]) -> None:
    prompt_dir = ROOT / "prompts"
    for tmpl in prompt_dir.glob("*.tmpl.md"):
        generated = tmpl.with_name(tmpl.name.replace(".tmpl.md", ".md"))
        if not generated.exists():
            errors.append(f"missing generated prompt for template: {rel(tmpl)}")
            continue
        if tmpl.read_text(encoding="utf-8") != generated.read_text(encoding="utf-8"):
            errors.append(
                f"stale prompt: {rel(generated)} differs from {rel(tmpl)}"
            )


def check_core_skills(errors: list[str]) -> None:
    path = ROOT / "core_skills.json"
    if not path.exists():
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    for entry in data.get("entries", []):
        skill_path = ROOT / entry.get("path", "")
        if not (skill_path / "SKILL.md").exists():
            errors.append(f"core skill missing SKILL.md: {entry.get('path')}")


def check_sensitive_refs(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix.lower() not in {".md", ".json", ".py", ".txt"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in SENSITIVE_PATTERNS:
            if pattern.search(text):
                errors.append(f"suspicious local/private reference in {rel(path)}")
                break


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="emit JSON result")
    args = parser.parse_args(argv)

    errors: list[str] = []
    check_required_files(errors)
    check_json(errors)
    check_prompt_templates(errors)
    check_core_skills(errors)
    check_sensitive_refs(errors)

    result = {
        "ok": not errors,
        "root": str(ROOT),
        "errors": errors,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        if errors:
            print("Template doctor found issues:")
            for error in errors:
                print(f"- {error}")
        else:
            print("Template doctor passed.")

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
