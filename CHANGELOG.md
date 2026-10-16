# Changelog

Formato compacto inspirado en Keep a Changelog. Cada versión enlaza su release en GitHub.

## [Sin publicar]

## [v0.1.0] — 2026-10-16 — Base consolidada

Primera base limpia: un solo `main`, CI completo en verde y web pública.

### Añadido

- `FB_AlarmLatch`: primera fuente SCL real con compilación V20 evidenciada (0/0), capturas del fixture y pack de cierre (arnés OB1, protocolo PLCSIM, plantilla de evidencia, procedimiento de exportación XML).
- Catálogo auto-generado desde frontmatter (`scripts/generate_catalog.py`) con estados ✅/🔧/📝/⏳ y niveles 🟢/🟡/🔴; CI falla si se desincroniza.
- Validaciones: estructura de recursos, artefactos XML (bien formado, sin BOM ni datos sensibles), 350+ enlaces locales, peso de binarios, markdownlint a cero avisos, gitleaks y lychee semanal de externos.
- Contenidos: rutas de aprendizaje, glosario ES-EN, FAQ, vídeos curados, plantilla VAT, CSV de textos de alarma, snippets SCL y prerrequisitos en tutoriales.
- Web pública con buscador (GitHub Pages + docsify) y tarjeta social.

### Cambiado

- README rediseñado con estado honesto (sin `.xml` todavía) y curación de fichas de IA no verificadas a fichas históricas.
- 8 ramas integradas o eliminadas; `main` como única rama.
