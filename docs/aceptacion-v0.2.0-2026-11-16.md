# Awesome TIA Portal — acta de aceptación candidata v0.2.0

**Revisión local:** 2026-11-16. **Estado global:** CANDIDATA LOCAL, **no publicada ni aprobada como versión definitiva**.

## Identidad y alcance

- Rama de cierre: `feat/awesome-v0.2.0-closure`, basada en `origin/main` @ `d5cefeaf69d0b4e5fd923b4a0da8e1319576e960`.
- Los cambios de la rama original `feat/github-research-templates` se preservan; **no** se ha fusionado ni reintroducido el `docs/research/analisis.json` bruto (4,35 MB). El archivo distribuible mantiene 43.328 bytes.
- Objetivo de v0.2.0: una biblioteca técnicamente honesta, controles editoriales, dos recursos con evidencia y una publicación reproducible; no convertir los otros 24 diseños en bloques funcionales.

## Puertas D0–D5

| Puerta | Evidencia de esta revisión | Estado |
|---|---|---|
| D0 Inventario y contrato | 26 fichas: 5 UDT, 11 FB/FC, 3 OB, 5 HMI, 2 plantillas; 2 `verified`, 24 `documented`; script de cobertura con prueba negativa | PASS LOCAL |
| D1 Documentación / CI / seguridad | README, FAQ, matriz y rutas corregidos; seis Gitleaks falsos positivos históricos con huellas exactas; lint Markdown, links, formatos y estructura con validadores locales | PASS LOCAL, REMOTE CI NO EJECUTADA |
| D2 Importación y pruebas técnicas | XML originales importados desde cero con Openness/TIA V20 y dos fixtures independientes de ensayo (OB1 SCL, DB de instancia para alarma, 6/9 tags); ambas compiladas con 0 errores y 0 advertencias. Los casos PLCSIM del 21/10 constan en evidencia histórica | PASS IMPORTACIÓN Y PREPARACIÓN; REGRESIÓN PLCSIM NUEVA BLOQUEADA SIN DESCARGA |
| D3 Experiencia de uso | Diferenciación de 24 diseños y 2 recursos; guía de reproducción, sidebar y resumen inglés. GitHub Pages publicado actual: estado `built`, HTTP 200 y configuración Docsify/sidebar detectada | PASS ESTÁTICO Y SITIO PUBLICADO; CANDIDATA NO DESPLEGADA NI PROBADA VISUALMENTE |
| D4 Release candidata | Trabajo en rama aislada, manifiestos y evidencias, sin merge/tag/push/release | CANDIDATA LOCAL |
| D5 Auditoría de aceptación | Conclusiones, limitaciones y puertas verificables en esta acta | PARCIAL; aceptación final pendiente |

## Evidencias primarias

- [Batería final local, 16/11](evidencias/comprobaciones-offline-v0.2.0-2026-11-16.json): 12 controles ejecutados y aprobados; catálogo, enlaces, XML/SCL, cobertura, estructura, Markdownlint, Gitleaks historial y directorio de trabajo, diff, tamaño máximo, parse JSON y SVG.
- [Reimportación y compilación reales, 16/11](evidencias/validacion-importacion-tia-v20-2026-11-16.json): 2 XML, dos readbacks verificados, software compilation `Success` / 0 errores / 0 advertencias, backup completo 7/7 archivos, proyecto guardado y cerrado.
- [Preparación y bloqueo de regresión PLCSIM, 16/11](evidencias/preparacion-regresion-plcsim-2026-11-16.json): propiedades de simulación activadas, arneses independientes de FB y FC compilados 0/0, tablas de 9 y 6 señales verificadas, manifests/backup comprobados; sin descarga ni pruebas conductuales nuevas.
- [Preflight read-only y regresión de seguridad, 16/11](evidencias/preflight-regresion-simulada-2026-11-16.json): ruta Windows por adaptador virtual Siemens, pero inventario Openness con tres rutas sin preferida; corrección del DB de instancia validada únicamente en copia aislada (13 pruebas negativas y 11 controles mock). **No existe evidencia visual nativa del diálogo de descarga; no se descargó**.
- [Ensayo PLCSIM previo FB, 21/10](../bloques-de-funcion/fb-alarm-latch/evidencia-plcsim-2026-10-21.json): 65/65 pasos, nueve casos.
- [Ensayo PLCSIM previo FC, 21/10](../bloques-de-funcion/fc-escalado/evidencia-plcsim-2026-10-21.json): 33/33 pasos, nueve casos.
- [Revisión de referencias GitHub, 16/11](evidencias/referencias-externas-2026-11-16.json): 12 repositorios accesibles y no archivados, sin integración de código tercero.
- [Ejecución Git/Gitleaks previa, 16/11](validacion-local-2026-11-16.md): seis falsos positivos, reproducciones históricas con y sin exclusiones.
- [Guía de repetición](guia-reproduccion-v20.md).

## Límites que no se deben ocultar

- La ejecución de las dos baterías PLCSIM **no se ha repetido** sobre las nuevas fixtures. Se han preparado por separado los arneses y las tablas, compilados 0/0, con soporte de simulación leído como `true` en OB/FB/FC y copias completas. **La descarga está bloqueada por seguridad**: falta una observación visual reciente del diálogo de destino simulado exigida por R17 y, para la fixture FB, el DB de instancia no expone `PLCSimAdvancedSupport` que el runner solicita indiscriminadamente. No se han omitido controles ni conectado con hardware físico. La API V7 y el registro/limpieza de una instancia temporal sí pasaron con cero instancias residuales.
- Gitleaks 8.24.3 pasó **dos escaneos distintos** de la rama candidata: 88 commits históricos (0 hallazgos, exit 0) y archivos actuales con `--no-git` (0 hallazgos, exit 0). Se corrigieron dos alertas nuevas provocadas por citar literalmente un valor de simulación en documentación; no se añadieron exclusiones extra.
- La CI de GitHub Actions sobre esta candidata debe comprobarse en una rama publicada antes del merge. No equiparar pruebas locales con CI remota; los defectos reales que muestre CI deben corregirse. La publicación, si se efectúa, debe distinguir claramente la evidencia conductual histórica de las fixtures nuevas todavía sin descarga.
- El artefacto XML no incluye todos los atributos del bloque (por ejemplo `PriorityNumber`); la importación informó de coincidencia de atributos verificables, sin atribuirle el resto.
- Solo TIA V20 + CPU 1513, no hay pruebas de compatibilidad V18/V19, S7-1200, HMI o CPU física; nada está certificado para uso industrial ni Safety.
- La revisión de enlaces GitHub y licencias no sustituye una evaluación exhaustiva de seguridad de cada herramienta ajena. Siemens publica MIT para fuente y condiciones royalty-free para binarios en su `LICENSE.md`; por eso la API GitHub expone `NOASSERTION`.
- La web publicada responde HTTP 200 y GitHub Pages indica `built`, pero no se ha hecho un test visual/móvil ni desplegado la candidata.
- La autorización para el cierre y la publicación se concedió en la sesión del 16/11/2026; las operaciones Git/publicación quedan condicionadas a superar las comprobaciones y no falsear el estado de simulación.

## Criterio de cierre

Para declarar **v0.2.0 lista para publicar**: verificar que el árbol final pasa tests locales, diff y seguridad; confirmar el tratamiento de la regresión PLCSIM pendiente o justificar la aceptación de la evidencia histórica según alcance del release; comprobar render/navegación y resolver hallazgos críticos. La ejecución de la publicación (commit, push, tag y release) no forma parte de esta autorización.

No se asigna una puntuación global inventada de 100 puntos. Los criterios no evaluados quedan fuera de calificación y no se sustituyen por el recuento de Markdown o estrellas.
