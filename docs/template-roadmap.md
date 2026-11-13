# Plan de futuras plantillas (template-roadmap)

> Fase 3 y 5 del plan. Lista priorizada de plantillas propuestas para el Awesome TIA Portal, con utilidad, complejidad y referencia de origen.
> Estado: propuestas, sin validar en TIA Portal (no hay TIA Portal disponible en este entorno). Marcar cada una como "pendiente de validación" hasta que exista fuente SCL compilada y probada.

## Criterio de prioridad

1. **Resuelve un problema frecuente** en máquinas/reales (arranque, paro, recetas, regulación, diagnóstico).
2. **Sin dependencias de recursos no importables** del repo (autocontenido o depende solo de UDTs propios ya documentados).
3. **Formato textual** apto para control de versiones (SCL, XML, JSON/YAML, Markdown).
4. **Pequeña, legible y modular** — no arquitecturas complejas sobrediseñadas.

## Top 10 oportunidades de nuevas plantillas

| Pri. | Plantilla | Categoría | Problema que resuelve | Complejidad | Origen / referencia |
|:--:|---|---|---|---|---|
| 1 | `fb-interbloqueo-equipos` | Lógica PLC | Impide que dos equipos mutuamente excluyentes (ej. dos válvulas de la misma línea) estén activos a la vez. | Baja | Detectada en investigación; no existe en el catálogo actual. |
| 2 | `fb-gestor-recetas` | Lógica PLC | Carga/aplica un conjunto de consignas (receta) desde una DB o array a los controladores de la máquina. | Media | Oportunidad identificada en Fase 3 (gestión de recetas). No existe en el catálogo. |
| 3 | `fb-rampa-consigna` | Lógica PLC | Limita la velocidad de variación (slew rate) de una consigna analógica para evitar saltos bruscos en variadores/valvulas. | Baja | Oportunidad Fase 3 (tratamiento de señales analógicas). No existe. |
| 4 | `fb-diagnostico-equipo` | Diagnósticos | Agrupa fallos, advertencias y estados de un equipo en una palabra de estado y texto de diagnóstico para HMI. | Media | Oportunidad Fase 3 (diagnósticos). `udt-alarm` existe, pero no un FB de diagnóstico de equipo. |
| 5 | `fb-modo-manual-auto` | Lógica PLC | Cambia el control de un equipo entre mando del operador (HMI) y control automático (PLC), con traslado bumpless opcional. | Media | Oportunidad Fase 3 (gestión de modos Manual/Automático). Parcialmente cubierto por `fb-motor`/`fb-valve`, pero como bloque independiente reutilizable falta. |
| 6 | `fb-contador-piezas-produccion` | Lógica PLC | Cuenta piezas producidas con reset por turno/lote y retentivo. | Baja | Oportunidad Fase 3 (temporizadores/contadores reutilizables). `fb-edge-counter` existe, pero enfocado a flancos genéricos, no a producción. |
| 7 | `udt-alarma-sistema` | Tipos de datos | Estructura de alarma de sistema con texto, grupo, máscara de enrutamiento a HMI y bit de enclavamiento. Complementa `udt-alarm` (de proceso). | Baja | Detectada como complemento de `udt-alarm`. No existe. |
| 8 | `fb-secuenciador-receta-parametrizable` | Lógica PLC | Extensión de `fb-secuenciador-pasos` (ya creado como ficha) donde cada paso lleva parámetros (tiempos, consignas) leídos de una receta. | Media | Se deriva de `fb-secuenciador-pasos` creado en esta sesión. |
| 9 | `plantilla-proyecto-modular-s7-1200` | Plantillas de proyecto | Estructura mínima para máquina con S7-1200 + HMI Basic/Comfort, con carpetas, convenciones y bloques vacíos listos. | Media | Oportunidad Fase 3 (estructuras estándar de proyectos). Existe `plantilla-maquina-simple` como ficha; falta consolidar como plantilla de proyecto usable. |
| 10 | `script-openness-export-bloques` | Productividad | Script Python/C# de TIA Openness que exporta bloques seleccionados a XML/SCL para control de versiones. | Media | Oportunidad Fase 3 (scripts TIA Openness, generación automática de bloques). Referencia: `siemens/tia-portal-openness-code-snippets` (clase A). |

## Plantillas ya creadas en esta sesión (estado documentado, sin validar)

Estas ya existen como fichas de diseño (`status: documented`) en `bloques-de-funcion/`:

| Carpeta | Plantilla | Estado | Validación |
|:---|---|:---|:---|
| `fb-estado-maquina` | Máquina de estados finita (16 estados) | Documentado (README, sin SCL ni .xml) | Pendiente: fuente SCL, compilación, prueba |
| `fb-secuenciador-pasos` | Secuenciador de hasta 16 pasos | Documentado (README, sin SCL ni .xml) | Pendiente: fuente SCL, compilación, prueba |
| `fb-control-pid` | Controlador PID con anti-windup y límites | Documentado (README, sin SCL ni .xml) | Pendiente: fuente SCL, compilación, prueba |

## Siguientes pasos recomendados

1. Elegir una de las tres plantillas creadas (p. ej. `fb-estado-maquina`) y escribir la fuente SCL real.
2. Importar en un proyecto desechable de TIA Portal V20, compilar (0 errores, 0 avisos) y documentar evidencia.
3. Exportar a `.xml`, verificar importación desde cero y publicar la evidencia en la carpeta del recurso.
4. Cambiar `status` de `documented` a `compiled` o `available` en el frontmatter y regenerar `CATALOG.md`.
5. Repetir con `fb-secuenciador-pasos` y `fb-control-pid`.
6. A partir de ellas, abordar el Top 10 (interbloqueo, gestor de recetas, rampa, diagnóstico de equipo, manual/auto).

## Nota de validación

Ninguna de las plantillas de este roadmap ha sido compilada ni probada en TIA Portal ni en PLCSIM en este entorno. Todas se marcan como **pendiente de validación**.
