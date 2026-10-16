#!/usr/bin/env python3
"""Valida los artefactos exportados de TIA Portal (.xml) y busca datos sensibles.

Uso:
    python3 scripts/validate-xml.py

Reglas:
- Si no hay ningun .xml todavia, no falla: informa y sale con 0.
- Cada .xml debe estar bien formado (parse XML) y en UTF-8 sin BOM.
- Ni los .xml ni los .scl pueden contener IPs privadas ni rutas de
  usuario (restos tipicos de una exportacion desde un PC de ingenieria).
  Ver STYLE.md seccion 10.
"""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

PRIVATE_IP = re.compile(
    r"(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    r"|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}"
    r"|192\.168\.\d{1,3}\.\d{1,3})"
)
USER_PATH = re.compile(r"(?:C:\\Users\\|/home/|/Users/)[^\s\"'<>]+", re.IGNORECASE)

SENSITIVE = [
    ("IP privada", PRIVATE_IP),
    ("ruta de usuario", USER_PATH),
]


def check_xml(path: Path) -> list[str]:
    """Devuelve la lista de problemas del .xml (vacia = OK)."""
    issues: list[str] = []
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        issues.append("tiene BOM; debe ser UTF-8 sin BOM")
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        return issues + ["no es UTF-8 valido"]
    try:
        ET.fromstring(text)
    except ET.ParseError as exc:
        issues.append(f"XML mal formado: {exc}")
    for label, pattern in SENSITIVE:
        if pattern.search(text):
            issues.append(f"contiene posible {label} (revisar antes de publicar)")
    return issues


def check_text(path: Path) -> list[str]:
    """Busca datos sensibles en fuentes (.scl)."""
    issues: list[str] = []
    try:
        text = path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        return [f"no es UTF-8 valido"]
    for label, pattern in SENSITIVE:
        if pattern.search(text):
            issues.append(f"contiene posible {label} (revisar antes de publicar)")
    return issues


def main() -> int:
    xml_files = sorted(REPO.rglob("*.xml"))
    scl_files = sorted(REPO.rglob("*.scl"))
    # Ignorar lo que viva dentro de .git por si acaso.
    xml_files = [p for p in xml_files if ".git" not in p.parts]
    scl_files = [p for p in scl_files if ".git" not in p.parts]

    if not xml_files:
        print("ℹ️  Sin .xml todavia: solo se revisan datos sensibles en .scl.")

    errors = 0
    for path in xml_files:
        for issue in check_xml(path):
            print(f"❌ {path.relative_to(REPO)}: {issue}")
            errors += 1
    for path in scl_files:
        for issue in check_text(path):
            print(f"❌ {path.relative_to(REPO)}: {issue}")
            errors += 1

    if errors:
        return 1
    print(f"✅ Artefactos OK ({len(xml_files)} .xml, {len(scl_files)} .scl revisados)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
