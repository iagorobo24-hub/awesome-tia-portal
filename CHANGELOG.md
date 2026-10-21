# Changelog

Formato compacto inspirado en Keep a Changelog. Cada versión enlaza su release en GitHub.

## [Sin publicar]

### Añadido

- `fc-escalado` deja de ser una ficha de diseño y pasa a **bloque verificado**: fuente SCL, XML exportado, arnés con OB1 en SCL y tabla de tags `Agent_Escalado`, y nueve casos de escalado observados sobre una CPU 1513 virtual (33/33 pasos, 0 errores y 0 avisos en compilación y descarga). Incluye la nota de las dos desviaciones respecto a la ficha original: la salida es un `VAR_OUTPUT` y no un valor de retorno, porque el generador de fuentes SCL de TIA V20 exige el tipo de retorno en la cabecera y no admite `VERSION`, `AUTHOR` ni `FAMILY` en un `FUNCTION`; y las variables de prueba son `Real` porque la API de PLCSIM no expone acceso simbólico a `Int`.
- `MATRIZ-TRAZABILIDAD.md`: qué hay **realmente** en cada una de las 24 carpetas (fuente, compilación, ejecución y evidencia), con los pasos que faltan para cerrar cada ficha. Hoy hay 2 recursos verificados en ejecución y 22 fichas de diseño sin código importable.
- Evidencias de PLCSIM con los valores observados de los dos bloques verificados, y capturas del Control Panel de PLCSIM Advanced con la instancia virtual en marcha y su dirección.

### Cambiado

- `fb-alarm-latch` pasa a estado **verificado**: descarga a CPU virtual (`Download Success`, 0 errores y 0 avisos) y nueve casos de comportamiento observados (65/65 pasos), con su evidencia y su captura. La matriz de compatibilidad ya no marca PLCSIM como bloqueado.
- Catálogo: nuevo estado `verified` con su leyenda, y `scripts/generate_catalog.py` lo reconoce y lo genera.
- `snippets/filtro-ton` pasa a verificado en ejecución: es el filtro `OnDelay` del `FB_AlarmLatch`, ejecutado en PLCSIM.
- `prueba-plcsim.md` y `protocolo-plcsim.md` recogen las cuatro condiciones que la API de PLCSIM Advanced impone a la vez, para que la repetición no choque con las mismas paredes.

## [v0.1.0] - 2026-10-16 - Base consolidada

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
