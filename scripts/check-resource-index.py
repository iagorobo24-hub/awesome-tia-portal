#!/usr/bin/env python3
"""Comprueba que el README y la matriz cubren todas las carpetas de recursos.

No modifica archivos y no considera que un XML exportado sea reimportable.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
CATEGORIES = (
    "tipos-de-datos",
    "bloques-de-funcion",
    "bloques-de-organizacion",
    "hmi",
    "plantillas-de-proyecto",
)
RESOURCE_LINK = re.compile(
    r"\]\(\./(" + "|".join(CATEGORIES) + r")/([a-z0-9-]+)/\)"
)
STATUS = re.compile(r"(?m)^status:\s*['\"]?([a-z-]+)")

def resource_links(text: str) -> set[str]:
    return {f"{category}/{name}" for category, name in RESOURCE_LINK.findall(text)}

def main() -> int:
    expected: set[str] = set()
    statuses: Counter[str] = Counter()
    errors: list[str] = []
    for category in CATEGORIES:
        directory = ROOT / category
        if not directory.is_dir():
            errors.append(f"Falta categoría: {category}")
            continue
        for resource in sorted(path for path in directory.iterdir() if path.is_dir()):
            relative = f"{category}/{resource.name}"
            expected.add(relative)
            readme = resource / "README.md"
            if not readme.is_file():
                errors.append(f"Falta README: {relative}")
                continue
            match = STATUS.search(readme.read_text(encoding="utf-8-sig"))
            if not match:
                errors.append(f"Falta status: {relative}")
            else:
                statuses[match.group(1)] += 1

    for filename in ("README.md", "MATRIZ-TRAZABILIDAD.md"):
        file = ROOT / filename
        if not file.is_file():
            errors.append(f"Falta índice: {filename}")
            continue
        linked = resource_links(file.read_text(encoding="utf-8-sig"))
        errors += [f"{filename}: falta recurso {path}" for path in sorted(expected - linked)]
        errors += [f"{filename}: enlace huérfano {path}" for path in sorted(linked - expected)]

    summary = ", ".join(f"{key}={value}" for key, value in sorted(statuses.items()))
    print(f"Índice: {len(expected)} recursos; {summary}; {len(errors)} errores")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
