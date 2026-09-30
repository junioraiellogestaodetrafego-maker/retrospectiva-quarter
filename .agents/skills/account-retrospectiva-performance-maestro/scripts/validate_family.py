#!/usr/bin/env python3
"""Valida frontmatter, módulos esperados e duplo-write da família."""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path


EXPECTED = {
    "account-retrospectiva-performance-maestro",
    "account-retrospectiva-contexto-fontes",
    "account-retrospectiva-midia",
    "account-retrospectiva-criativos",
    "account-retrospectiva-funil-inside-sales",
    "account-retrospectiva-vendedores",
    "account-retrospectiva-atendimento",
    "account-retrospectiva-ecommerce",
    "account-retrospectiva-breakeven",
    "account-retrospectiva-reconciliacao",
    "account-retrospectiva-evidencias",
    "account-retrospectiva-achados-gaps",
    "account-retrospectiva-consolidacao",
    "account-retrospectiva-drive-handoff",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def files(root: Path) -> dict[str, Path]:
    return {
        str(path.relative_to(root)).replace("\\", "/"): path
        for path in root.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("workspace", type=Path, nargs="?", default=Path.cwd())
    args = parser.parse_args()
    workspace = args.workspace.resolve()
    agents = workspace / ".agents" / "skills"
    claude = workspace / ".claude" / "skills"
    errors: list[str] = []

    for name in sorted(EXPECTED):
        left = agents / name
        right = claude / name
        if not left.is_dir() or not right.is_dir():
            errors.append(f"diretório ausente: {name}")
            continue
        left_files = files(left)
        right_files = files(right)
        if set(left_files) != set(right_files):
            errors.append(f"estrutura divergente: {name}")
            continue
        for relative in left_files:
            if digest(left_files[relative]) != digest(right_files[relative]):
                errors.append(f"hash divergente: {name}/{relative}")

        skill = (left / "SKILL.md").read_text(encoding="utf-8")
        pattern = rf"(?ms)^---\s*\nname: {re.escape(name)}\n.*?\narea: account\nauthor: .+\nversion: \d+\.\d+\.\d+\n---"
        if not re.search(pattern, skill):
            errors.append(f"frontmatter inválido: {name}")

    if errors:
        print("FALHOU")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"OK: {len(EXPECTED)} skills com duplo-write e frontmatter válido")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
