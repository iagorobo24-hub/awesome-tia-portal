#!/usr/bin/env python3
"""One-shot helper: añade el frontmatter YAML a los READMEs existentes.

NO se ejecuta en CI. Se usó una sola vez para sembrar el frontmatter
en los 22 recursos pre-existentes. Se deja aquí versionado por si
hay que repetirlo o como referencia.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# (folder_relpath, frontmatter dict). Orden = orden histórico en CATALOG.md.
RESOURCES: list[tuple[str, dict]] = [
    # ---------- tipos-de-datos ----------
    ("tipos-de-datos/udt-motor", {
        "name": "UDT_Motor", "type": "udt",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "depends_on": [], "used_by": ["bloques-de-funcion/fb-motor", "hmi/faceplate-motor"],
        "tags": ["motor", "control", "udt"], "status": "documented",
    }),
    ("tipos-de-datos/udt-analog-input", {
        "name": "UDT_AnalogInput", "type": "udt",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "depends_on": [],
        "used_by": ["bloques-de-funcion/fb-analog-input", "hmi/faceplate-analog"],
        "tags": ["analogica", "escalado", "alarmas", "udt"],
        "status": "documented",
    }),
    ("tipos-de-datos/udt-valve", {
        "name": "UDT_Valve", "type": "udt",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "depends_on": [], "used_by": ["bloques-de-funcion/fb-valve", "hmi/faceplate-valve"],
        "tags": ["valvula", "control", "udt"], "status": "documented",
    }),
    ("tipos-de-datos/udt-drive", {
        "name": "UDT_Drive", "type": "udt",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "depends_on": [], "used_by": [],
        "tags": ["variador", "drive", "udt"], "status": "documented",
    }),
    ("tipos-de-datos/udt-alarm", {
        "name": "UDT_Alarm", "type": "udt",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "depends_on": [], "used_by": ["hmi/pantalla-alarmas"],
        "tags": ["alarma", "ack", "udt"], "status": "documented",
    }),
    # ---------- bloques-de-funcion ----------
    ("bloques-de-funcion/fc-escalado", {
        "name": "FC_Escalado", "type": "fc",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "depends_on": [],
        "used_by": ["bloques-de-funcion/fb-analog-input"],
        "tags": ["escalado", "analogica", "fc"], "status": "documented",
    }),
    ("bloques-de-funcion/fb-motor", {
        "name": "FB_Motor", "type": "fb",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "depends_on": ["tipos-de-datos/udt-motor"],
        "used_by": [], "tags": ["motor", "control", "fb"],
        "status": "documented",
    }),
    ("bloques-de-funcion/fb-analog-input", {
        "name": "FB_AnalogInput", "type": "fb",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "depends_on": ["tipos-de-datos/udt-analog-input"],
        "used_by": [],
        "tags": ["analogica", "escalado", "alarmas", "fb"],
        "status": "documented",
    }),
    ("bloques-de-funcion/fb-valve", {
        "name": "FB_Valve", "type": "fb",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "depends_on": ["tipos-de-datos/udt-valve"],
        "used_by": [], "tags": ["valvula", "control", "fb"],
        "status": "documented",
    }),
    ("bloques-de-funcion/fb-hourmeter", {
        "name": "FB_Hourmeter", "type": "fb",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "depends_on": [], "used_by": [],
        "tags": ["horas", "contador", "persistencia", "fb"],
        "status": "documented",
    }),
    ("bloques-de-funcion/fb-edge-counter", {
        "name": "FB_EdgeCounter", "type": "fb",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "depends_on": [], "used_by": [],
        "tags": ["contador", "flancos", "fb"], "status": "documented",
    }),
    ("bloques-de-funcion/fb-pulse-gen", {
        "name": "FB_PulseGen", "type": "fb",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "depends_on": [], "used_by": [],
        "tags": ["pulsos", "generador", "fb"], "status": "documented",
    }),
    # ---------- bloques-de-organizacion ----------
    ("bloques-de-organizacion/ob1-plantilla", {
        "name": "OB1", "type": "ob",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "depends_on": [], "used_by": [],
        "tags": ["ob", "main", "plantilla"], "status": "documented",
    }),
    ("bloques-de-organizacion/ob100-startup", {
        "name": "OB100", "type": "ob",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "depends_on": [], "used_by": [],
        "tags": ["ob", "startup", "arranque"], "status": "documented",
    }),
    ("bloques-de-organizacion/ob82-85-86-errores", {
        "name": "OB82_OB85_OB86", "type": "ob",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1500"],
        "depends_on": [], "used_by": [],
        "tags": ["ob", "errores", "diagnostico"], "status": "documented",
    }),
    # ---------- hmi ----------
    ("hmi/faceplate-motor", {
        "name": "Faceplate_Motor", "type": "hmi-faceplate",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "hmi_panel": ["comfort", "unified"],
        "depends_on": ["tipos-de-datos/udt-motor", "bloques-de-funcion/fb-motor"],
        "used_by": [], "tags": ["motor", "faceplate", "hmi"],
        "status": "documented",
    }),
    ("hmi/faceplate-valve", {
        "name": "Faceplate_Valve", "type": "hmi-faceplate",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "hmi_panel": ["comfort", "unified"],
        "depends_on": ["tipos-de-datos/udt-valve", "bloques-de-funcion/fb-valve"],
        "used_by": [], "tags": ["valvula", "faceplate", "hmi"],
        "status": "documented",
    }),
    ("hmi/faceplate-analog", {
        "name": "Faceplate_Analog", "type": "hmi-faceplate",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "hmi_panel": ["comfort", "unified"],
        "depends_on": [
            "tipos-de-datos/udt-analog-input",
            "bloques-de-funcion/fb-analog-input",
        ],
        "used_by": [], "tags": ["analogica", "faceplate", "hmi"],
        "status": "documented",
    }),
    ("hmi/pantalla-alarmas", {
        "name": "Pantalla_Alarmas", "type": "hmi-pantalla",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "hmi_panel": ["comfort", "unified"],
        "depends_on": ["tipos-de-datos/udt-alarm"],
        "used_by": [], "tags": ["alarmas", "pantalla", "hmi"],
        "status": "documented",
    }),
    ("hmi/plantilla-navegacion", {
        "name": "Plantilla_Navegacion", "type": "hmi-pantalla",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200", "s7-1500"],
        "hmi_panel": ["comfort", "unified"],
        "depends_on": [], "used_by": [],
        "tags": ["navegacion", "header", "footer", "hmi"],
        "status": "documented",
    }),
    # ---------- plantillas-de-proyecto ----------
    ("plantillas-de-proyecto/plantilla-maquina-simple", {
        "name": "Plantilla_MaquinaSimple", "type": "plantilla",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1200"],
        "depends_on": [], "used_by": [],
        "tags": ["plantilla", "maquina", "basic"],
        "status": "documented",
    }),
    ("plantillas-de-proyecto/plantilla-linea-modular", {
        "name": "Plantilla_LineaModular", "type": "plantilla",
        "tia_version": "V20", "tia_compat": ["V18", "V19", "V20"],
        "plc_family": ["s7-1500"],
        "depends_on": [], "used_by": [],
        "tags": ["plantilla", "linea", "modular"],
        "status": "documented",
    }),
]


def render_frontmatter(meta: dict) -> str:
    """Renderiza el dict como bloque YAML conservando el orden de claves."""
    order = [
        "name", "type", "tia_version", "tia_compat",
        "plc_family", "hmi_panel",
        "depends_on", "used_by", "tags", "status",
    ]
    lines = ["---"]
    for k in order:
        if k not in meta:
            continue
        v = meta[k]
        if isinstance(v, list):
            inner = ", ".join(v)
            lines.append(f"{k}: [{inner}]")
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    for relpath, meta in RESOURCES:
        readme = REPO / relpath / "README.md"
        if not readme.exists():
            print(f"❌ No existe: {readme}")
            return 1
        original = readme.read_text(encoding="utf-8")
        if original.startswith("---\n"):
            print(f"⏭️  ya tiene frontmatter: {relpath}")
            continue
        new = render_frontmatter(meta) + "\n" + original
        readme.write_text(new, encoding="utf-8")
        print(f"✅ frontmatter añadido: {relpath}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
