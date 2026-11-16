# Visibilidad: dónde registrar este repo (investigación 2026-10-16)

## Panorama

No existe una lista awesome de referencia para TIA Portal. Lo que hay son
volcados de proyectos (`.ap16`/`.ap17` binarios, sin curación ni CI) y una
biblioteca seria en inglés:

- [Vyenkor/TIA-Portal-SiemensLibrary](https://github.com/Vyenkor/TIA-Portal-SiemensLibrary) — V21, exports XML, releases versionadas y changelog. Par natural: mismo nicho, otro idioma y versión. Candidata a enlace mutuo, no a competencia.

## Candidaturas posibles

| Lista | Encaje | Requisito clave | Estado |
|---|---|---|---|
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | Bajo | Formato clásico de lista de enlaces + badge awesome + 30 días de madurez | Descartada por formato: somos biblioteca con evidencia, no índice de enlaces |
| Listas awesome de PLC/automatización | Medio | Encontrar una activa con guía de contribución | No localizada una canónica; vigilar |
| Enlace mutuo con Vyenkor | Alto | Evidencias propias revisadas y release publicado | Pendiente de release v0.2.0 y comunicación con el mantenedor |

## Checklist de candidatura (para cuando toque)

- [x] Madurez: repo creado en abril 2026 (pide 30 días mínimo)
- [x] Licencia clara (MIT), contributing, código de conducta equivalente en tono
- [ ] CI estructural y seguridad del candidato validado localmente; aún sin comprobar la ejecución remota del commit de v0.2.0. La web pública ya existe.
- [x] Dos recursos con XML reimportado y compilado 0/0 en TIA V20 (16/11/2026), estado `verified` conservado.
- [ ] Release con el ✅ dentro (será v0.2.0)
- [x] Descripción en inglés del repositorio añadida a README (sin prometer compatibilidad no comprobada).

## Plan

1. Tras publicar una versión con evidencia y revisar las normas del proyecto ajeno, valorar una referencia contextual a Vyenkor (ES↔EN, V20↔V21). No solicitar enlaces recíprocos artificiales.
2. Reevaluar listas de nicho cada release; no forzar la entrada en la gran lista oficial a costa del formato propio.
