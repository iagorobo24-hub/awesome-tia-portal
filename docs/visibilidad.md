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
| Enlace mutuo con Vyenkor | Alto | Tener el primer ✅ y releases | Bloqueado hasta `FB_AlarmLatch` available |

## Checklist de candidatura (para cuando toque)

- [x] Madurez: repo creado en abril 2026 (pide 30 días mínimo)
- [x] Licencia clara (MIT), contributing, código de conducta equivalente en tono
- [x] CI propio en verde y web pública
- [ ] Primer recurso ✅ `available` (en curso, otra sesión)
- [ ] Release con el ✅ dentro (será v0.2.0)
- [ ] Descripción en inglés del repo (una línea, para listas angloparlantes)

## Plan

1. Al caer el primer ✅: abrir issue/PR de enlace mutuo con Vyenkor (ES↔EN, V20↔V21 se complementan).
2. Reevaluar listas de nicho cada release; no forzar la entrada en la gran lista oficial a costa del formato propio.
