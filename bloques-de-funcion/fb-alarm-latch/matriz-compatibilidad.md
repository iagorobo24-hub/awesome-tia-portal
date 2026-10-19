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

## Hallazgo H-19 — resumen

Con TIA V20 y el clásico V19 instalados a la vez, la interfaz PG/PC que TIA enumera como
`PLCSIM` es la del simulador clásico, cuyo runtime no enlaza por Softbus con un proyecto
V20. Resultado observado en 6 intentos: `DownloadToPlc` y `GoOnline` fallan ambos con
`NotReachable` / `Connect to module PLC_1 failed`, pese a que la instancia virtual está
sana por API.

> Detalle completo y evidencia por intento en
> [`RUN.md`](https://github.com/iagorobo24-hub/T-IA-Portal-RocaRoibas/blob/main/70-runs/e2e/20261016-fb-alarm-latch/RUN.md)
> (run `20261016-fb-alarm-latch` del workspace TIA-Claude).

## Cómo completar esta matriz

1. Instalar S7-PLCSIM clásico **V20** (pareja correcta de TIA V20), o
2. usar la ruta TCP/IP con la NIC virtual Siemens en consola elevada, o
3. retirar el clásico V19 para que TIA V20 use la interfaz Softbus de Advanced.

Repetir entonces: `DownloadToPlc` → `Online` → plan de 9 casos y anotar `PLCSIM = Sí`
por fila. Hasta entonces, **la columna PLCSIM permanece vacía a propósito**.
