# System Map — awesome-tia-portal

**Estado:** `draft` · **Perfil provisional:** `LITE` · **Fecha:** 2026-10-27  
**Referencia GitHub inspeccionada:** `main` @ `ec558a5d06466f7c8b8fb95f6eb78fd0aad793d5`  
**Alcance:** inventario inicial de rutas verificadas en GitHub; **no** validación de arquitectura ni funcionamiento.

## Routing mínimo

| Documento | Ruta | Evidencia / uso |
|---|---|---|
| `README.md` | [Abrir](../../README.md) | Documento existente en HEAD; contenido arquitectónico pendiente de reconciliar |
| `AGENTS.md` | [Abrir](../../AGENTS.md) | Documento existente en HEAD; contenido arquitectónico pendiente de reconciliar |
| `CLAUDE.md` | [Abrir](../../CLAUDE.md) | Documento existente en HEAD; contenido arquitectónico pendiente de reconciliar |
| `CHANGELOG.md` | [Abrir](../../CHANGELOG.md) | Documento existente en HEAD; contenido arquitectónico pendiente de reconciliar |
| `docs/system-map/manifest.yaml` | [Metadatos](./manifest.yaml) | Estado draft, cobertura desconocida y SHA de descubrimiento |

## Why this shape

Se crea un punto de entrada PSM sin duplicar documentación del anfitrión ni deducir dominios o APIs a partir de nombres de carpetas. `source.commit` fija el snapshot remoto de descubrimiento, **no** una línea base arquitectónica certificada. La selección `LITE` es provisional: si la fase de discovery identifica varios dominios materiales, migrar a `FULL` antes de activar el mapa.

## Contratos, impacto e invariantes

- **Dominios / flujos / límites externos:** `UNKNOWN` hasta inspeccionar implementación, configuración y tests.
- **Invariantes:** `UNKNOWN`; ninguna garantía runtime se deduce de la presencia de archivos.
- **Hits / Does not hit:** no determinados; antes de cualquier cambio material se debe realizar el contrato de impacto sobre código real.

## Criterio de avance

1. Completar discovery + reconciliación (incluyendo gobernanza del host), elegir perfil real y verificar rutas/símbolos en el commit relevante.
2. Construir dominios, flujos, fronteras e invariantes con evidencia de dos ejes y análisis de excepciones.
3. Ejecutar `MECHANICAL_GATE`, `SEMANTIC_AGENT_REVIEW` y Cold-Agent Walk; solo entonces promover `draft → active` y certificar `source.commit`.

**Validación actual:** `MECHANICAL_GATE: UNAVAILABLE`; `SEMANTIC_AGENT_REVIEW: PENDING`; pruebas de ejecución: `NOT RUN`. Solo se usó GitHub; no se revisó el trabajo local sin publicar.
