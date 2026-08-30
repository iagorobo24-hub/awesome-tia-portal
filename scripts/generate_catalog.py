#!/usr/bin/env python3
"""Genera CATALOG.md a partir del frontmatter de cada README de recurso.

Uso:
    python3 scripts/generate_catalog.py            # escribe CATALOG.md
    python3 scripts/generate_catalog.py --check    # solo verifica sincronización (CI)

Reglas:
- Cada subcarpeta de primer nivel dentro de las 5 categorías reconocidas debe
  contener un README.md con frontmatter YAML válido.
- El frontmatter debe declarar al menos `name`, `type` y `status`.
- El "tagline" del recurso es la primera línea de blockquote (`> ...`) que
  aparezca después del título H1.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CATALOG_PATH = REPO / "CATALOG.md"

# Categorías y metadatos de presentación. Orden = orden en CATALOG.md.
CATEGORIES = [
    {
        "folder": "tipos-de-datos",
        "title": "🏷️ Tipos de datos (UDT)",
        "types": {"udt"},
        "columns": ["status", "resource", "description", "tia", "plc"],
    },
    {
        "folder": "bloques-de-funcion",
        "title": "🧩 Bloques de función (FB / FC)",
        "types": {"fb", "fc"},
        "columns": ["status", "resource", "description", "tia", "plc"],
    },
    {
        "folder": "bloques-de-organizacion",
        "title": "🏗️ Bloques de organización (OB)",
        "types": {"ob"},
        "columns": ["status", "resource", "description", "tia", "plc"],
    },
    {
        "folder": "hmi",
        "title": "🖥️ HMI",
        "types": {"hmi-faceplate", "hmi-pantalla"},
        "columns": ["status", "resource", "description", "tia", "panel"],
    },
    {
        "folder": "plantillas-de-proyecto",
        "title": "📋 Plantillas de proyecto",
        "types": {"plantilla"},
        "columns": ["status", "resource", "description", "tia", "plc"],
    },
]

STATUS_BADGE = {
    "available": "✅",
    "documented": "📝",
    "wip": "⚙️",
    "planned": "⏳",
}

PLC_LABEL = {
    "s7-1200": "1200",
    "s7-1500": "1500",
}

PANEL_LABEL = {
    "comfort": "Comfort",
    "unified": "Unified",
    "basic": "Basic",
}

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


# ---------------------------------------------------------------------------
# Parsing del frontmatter
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> dict | None:
    """Parsea el frontmatter YAML manualmente (sin dependencias externas).

    Soporta los tipos que usa el repo:
      - escalares simples (`name: UDT_Motor`)
      - listas inline (`tags: [motor, control]`)
      - listas vacías (`depends_on: []`)
    No soporta listas multi-línea ni anidación; suficiente para los frontmatters
    de este repo y ahorra una dependencia (PyYAML).
    """
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    data: dict = {}
    for raw in m.group(1).splitlines():
        line = raw.split("#", 1)[0].rstrip()  # quita comentarios inline
        if not line.strip():
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            if not inner:
                data[key] = []
            else:
                data[key] = [item.strip() for item in inner.split(",")]
        else:
            data[key] = value
    return data


def extract_tagline(text: str) -> str:
    """Devuelve la primera línea de blockquote (`> ...`) tras el primer H1."""
    after_fm = FRONTMATTER_RE.sub("", text, count=1)
    in_body = False
    for raw in after_fm.splitlines():
        line = raw.rstrip()
        if not in_body:
            if line.startswith("# "):
                in_body = True
            continue
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith(">"):
            return stripped.lstrip(">").strip()
        # Si nos topamos con texto que no es blockquote, salimos.
        break
    return ""


# ---------------------------------------------------------------------------
# Render
# ---------------------------------------------------------------------------

def fmt_plc(plc_family: list[str]) -> str:
    if not plc_family:
        return "—"
    return " / ".join(PLC_LABEL.get(p, p) for p in plc_family)


def fmt_panel(panels: list[str]) -> str:
    if not panels:
        return "—"
    return " / ".join(PANEL_LABEL.get(p, p) for p in panels)


def fmt_tia(version: str | None, compat: list[str]) -> str:
    if version:
        return version
    if compat:
        return compat[-1]
    return "—"


def collect_resources() -> dict[str, list[dict]]:
    """Devuelve {category_folder: [resource_dict, ...]}."""
    by_category: dict[str, list[dict]] = {c["folder"]: [] for c in CATEGORIES}
    issues: list[str] = []

    for cat in CATEGORIES:
        cat_path = REPO / cat["folder"]
        if not cat_path.is_dir():
            continue
        for sub in sorted(p for p in cat_path.iterdir() if p.is_dir()):
            readme = sub / "README.md"
            if not readme.exists():
                issues.append(f"{sub.relative_to(REPO)}: falta README.md")
                continue
            text = readme.read_text(encoding="utf-8")
            fm = parse_frontmatter(text)
            if fm is None:
                issues.append(
                    f"{readme.relative_to(REPO)}: falta frontmatter YAML al inicio"
                )
                continue
            for required in ("name", "type", "status"):
                if required not in fm:
                    issues.append(
                        f"{readme.relative_to(REPO)}: frontmatter sin '{required}'"
                    )
            if fm.get("type") not in cat["types"]:
                issues.append(
                    f"{readme.relative_to(REPO)}: type='{fm.get('type')}' no encaja "
                    f"con la categoría {cat['folder']} (esperado: {sorted(cat['types'])})"
                )
            tagline = extract_tagline(text)
            if not tagline:
                issues.append(f"{readme.relative_to(REPO)}: sin tagline (línea `> …`)")
            by_category[cat["folder"]].append({
                "folder": sub.name,
                "path": str(sub.relative_to(REPO)),
                "name": fm.get("name", ""),
                "type": fm.get("type", ""),
                "status": fm.get("status", "wip"),
                "tagline": tagline,
                "tia_version": fm.get("tia_version"),
                "tia_compat": fm.get("tia_compat", []) or [],
                "plc_family": fm.get("plc_family", []) or [],
                "hmi_panel": fm.get("hmi_panel", []) or [],
            })

    if issues:
        for i in issues:
            print(f"❌ {i}", file=sys.stderr)
        sys.exit(2)

    return by_category


def render_table(cat: dict, resources: list[dict]) -> str:
    cols = cat["columns"]
    headers = {
        "status": "Estado",
        "resource": "Recurso",
        "description": "Descripción",
        "tia": "TIA Portal",
        "plc": "Familia PLC",
        "panel": "Panel",
    }
    align = {
        "status": ":---:",
        "resource": "---",
        "description": "---",
        "tia": ":---:",
        "plc": ":---:",
        "panel": ":---:",
    }
    head_row = "| " + " | ".join(headers[c] for c in cols) + " |"
    sep_row = "|" + "|".join(align[c] for c in cols) + "|"
    rows = [head_row, sep_row]
    for r in resources:
        cells = []
        for c in cols:
            if c == "status":
                cells.append(STATUS_BADGE.get(r["status"], "❔"))
            elif c == "resource":
                cells.append(f"[`{r['folder']}`](./{r['path']}/)")
            elif c == "description":
                cells.append(r["tagline"] or "—")
            elif c == "tia":
                cells.append(fmt_tia(r["tia_version"], r["tia_compat"]))
            elif c == "plc":
                cells.append(fmt_plc(r["plc_family"]))
            elif c == "panel":
                cells.append(fmt_panel(r["hmi_panel"]))
        rows.append("| " + " | ".join(cells) + " |")
    return "\n".join(rows)


# ---------------------------------------------------------------------------
# Documento completo
# ---------------------------------------------------------------------------

HEADER = """\
# 📚 Catálogo de recursos

Índice unificado de todo el contenido del repositorio. Para encontrar rápido lo que necesitas sin tener que abrir cada carpeta.

> **Este archivo se genera automáticamente** a partir del frontmatter YAML de cada README de recurso.
> No lo edites a mano: ejecuta `python3 scripts/generate_catalog.py` después de añadir o modificar un recurso.
> El flujo de cómo aportar un recurso está en [`CONTRIBUTING.md`](./CONTRIBUTING.md).

---

## Leyenda de estados

| Símbolo | Significado |
|:---:|---|
| ✅ | **Disponible** — README + `.xml` exportados, listo para importar |
| 📝 | **Solo documentado** — el diseño/README está, falta el `.xml` |
| ⚙️ | **En curso** — recurso identificado y en desarrollo |
| ⏳ | **Planificado** — recurso identificado como necesario, sin empezar |

---
"""

FOOTER = """
## 🛣️ Roadmap por orden recomendado

El orden sugerido para ir rellenando el repo (cada pieza apoya a la siguiente):

1. **UDTs base** — `udt-motor`, `udt-analog-input`, `udt-valve`, `udt-drive`, `udt-alarm`
2. **FC de escalado** — `fc-escalado` (validación end-to-end del flujo)
3. **FBs que consumen los UDTs** — `fb-motor`, `fb-analog-input`, `fb-valve`, `fb-hourmeter`...
4. **OBs base** — `ob1-plantilla`, `ob100-startup`, `ob82-85-86-errores`
5. **HMI** — faceplates vinculados a los UDTs
6. **Plantillas de proyecto** — una vez hay piezas suficientes que referenciar

---

## ➕ ¿Cómo añadir tu recurso a este catálogo?

1. Crea tu carpeta de recurso copiando [`_plantillas/README-recurso.md`](./_plantillas/README-recurso.md) y rellena el frontmatter YAML.
2. Ejecuta `python3 scripts/generate_catalog.py` desde la raíz del repo. Esto regenera **este** archivo automáticamente.
3. Commitea los dos cambios (tu recurso + el `CATALOG.md` actualizado) en la misma PR.
4. CI verificará que `CATALOG.md` esté sincronizado: si no lo está, fallará con instrucciones.
"""


def render_catalog() -> str:
    by_category = collect_resources()
    parts = [HEADER]
    for cat in CATEGORIES:
        resources = by_category[cat["folder"]]
        parts.append("")
        parts.append(f"## {cat['title']}")
        parts.append("")
        parts.append(f"> Carpeta: [`{cat['folder']}/`](./{cat['folder']}/)")
        parts.append("")
        if resources:
            parts.append(render_table(cat, resources))
        else:
            parts.append("_Aún no hay recursos en esta categoría._")
        parts.append("")
        parts.append("---")
    parts.append(FOOTER)
    return "\n".join(parts).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="No escribe CATALOG.md, solo falla si está desincronizado.",
    )
    args = parser.parse_args()

    rendered = render_catalog()

    if args.check:
        if not CATALOG_PATH.exists():
            print("❌ CATALOG.md no existe", file=sys.stderr)
            return 1
        current = CATALOG_PATH.read_text(encoding="utf-8")
        if current != rendered:
            print(
                "❌ CATALOG.md está desincronizado con el frontmatter de los recursos.\n"
                "   Ejecuta: python3 scripts/generate_catalog.py\n"
                "   Y commitea el resultado.",
                file=sys.stderr,
            )
            return 1
        print("✅ CATALOG.md sincronizado")
        return 0

    CATALOG_PATH.write_text(rendered, encoding="utf-8")
    print(f"✅ Generado {CATALOG_PATH.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
