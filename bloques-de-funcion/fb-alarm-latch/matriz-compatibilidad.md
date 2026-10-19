# Matriz de compatibilidad — FB_AlarmLatch + arnés OB1

Tuplas verificadas por lectura live del proyecto (no inferidas). Cada fila indica si la
compilación y la ejecución en PLCSIM quedaron realmente probadas o siguen pendientes.

| Bloque | CPU (referencia exacta) | TIA | Compilación 0/0 | PLCSIM |
|---|---|---|---|---|
| `FB_AlarmLatch` (FB2, SCL) | 1513-1 PN · `6ES7 513-1AM03-0AB0` · FW **V3.0** | **V20** | **Sí** — 0 errores / 0 avisos | **No** — bloqueado (H-19) |
| `Main` (OB1, SCL) — arnés `CALL "AlarmPump"` | 1513-1 PN · `6ES7 513-1AM03-0AB0` · FW V3.0 | **V20** | **Sí** — 0 errores / 0 avisos | **No** — bloqueado (H-19) |
| `AlarmPump` (DB1, instancia de FB_AlarmLatch) | 1513-1 PN · FW V3.0 | **V20** | **Sí** — 0 errores / 0 avisos | **No** — bloqueado (H-19) |
| `FB_AgentDemo` (FB1, SCL) — baseline de la fixture | 1513-1 PN · FW V3.0 | **V20** | **Sí** — 0 errores / 0 avisos | **No** — bloqueado (H-19) |

## Entorno de la prueba

| Componente | Versión | Nota |
|---|---|---|
| TIA Portal | **V20** | build V20.0.0, sin update aplicado |
| PLCSIM Advanced | **V7.0.0.0** (API 7.0) | Runtime Manager operativo; `Online Access = PLCSIM (Softbus)` confirmado |
| S7-PLCSIM clásico | **V19** (1900.1.60.8554) | instalado en el mismo host — ver hallazgo H-19 |
| SOFTBUS | `SOFTBUS` · interfaz `PLCSIM` · `ip=null` · códigos API `0x0` | instancia registrada correctamente |
| SOFTBUS en TIA | ruta única `PG/IE / PLCSIM [no IP] → 1 X1` | `CheckDownloadReadiness`: `ready=true`, `isConsistent=true`, 0 NICs |

## Compatibilidad de versión (matriz Siemens)

TIA **V20** requiere S7-PLCSIM Advanced **V7.0** (cubre TIA V14–V20 y CPU FW V1.8–V4.0).
La CPU de esta prueba es FW **V3.0**, dentro del rango soportado → **la combinación de
versiones es válida**. El bloqueo H-19 no es de compatibilidad, sino de coexistencia del
PLCSIM clásico V19 en la interfaz PG/PC del host.

## Hallazgo H-19 — hipótesis original **refutada**

Se propuso que el bloqueo venía de que **S7-PLCSIM clásico V19** ocupaba la interfaz
PG/PC `PLCSIM`. **Se refutó empíricamente**: tras instalar **S7-PLCSIM clásico V20**
(`S7PLCSIMV20.exe`, v2000.0.200.9871) y repetir la descarga en tres variantes
—interfaz `PLCSIM`, sin forzar interfaz y `PLCSIM.TCPIP.1`— el resultado no cambió.
La versión del simulador clásico **no es la causa**.

Lo que sí está medido:

- TIA V20 en esta máquina **no alcanza ninguna CPU virtual por Softbus**, ni con la
  instancia de PLCSIM Advanced sana (`registerCode/powerOnCode = 0x0`), ni con `GoOnline`.
- La **única ruta** que TIA declara es `PN/IE / PLCSIM [no IP] -> 1 X1`. Pedir
  explícitamente `PLCSIM.TCPIP.1` es rechazado por el propio servidor **antes** de
  intentar la conexión, lo que confirma que no hay una segunda interfaz que probar.
- Siete intentos llegaron a la fase de conexión y fallaron de forma idéntica.

Determinar el ajuste concreto que rompe esa ruta exige **inspección visual del diálogo
de descarga** (lista de destinos y aviso de CPU simulada). El Ribbon de TIA V20 no
expone controles por UI Automation en este host, así que esa observación no puede
automatizarse.

> Detalle completo, intento a intento, en
> [`informe-ejecucion-2026-10-19.md`](informe-ejecucion-2026-10-19.md) (run
> `20261016-fb-alarm-latch` del workspace TIA-Claude).

## Cómo completar esta matriz

1. Inspeccionar el diálogo de descarga en la TIA GUI y registrar qué destinos aparecen.
   Dependiendo de lo observado: ajustar la PG/PC, retirar el clásico V19 para que TIA
   use la interfaz Softbus de Advanced, o probar la ruta TCP/IP con la NIC virtual.
2. Repetir `DownloadToPlc` → `Online` → plan de 9 casos y anotar `PLCSIM = Sí` por fila.

Hasta entonces, **la columna PLCSIM permanece vacía a propósito**.
