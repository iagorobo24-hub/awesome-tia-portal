# Matriz de compatibilidad — FB_AlarmLatch + arnés OB1

Tuplas verificadas por lectura live del proyecto (no inferidas). Cada fila indica si la
compilación y la ejecución en PLCSIM quedaron realmente probadas o siguen pendientes.

| Bloque | CPU (referencia exacta) | TIA | Compilación 0/0 | PLCSIM |
|---|---|---|---|---|
| `FB_AlarmLatch` (FB2, SCL) | 1513-1 PN · `6ES7 513-1AM03-0AB0` · FW **V3.0** | **V20** | **Sí** — 0 errores / 0 avisos | **Sí** — descarga y 9 casos verificados (2026-10-21) |
| `Main` (OB1, SCL) — arnés `CALL "AlarmPump"` | 1513-1 PN · `6ES7 513-1AM03-0AB0` · FW V3.0 | **V20** | **Sí** — 0 errores / 0 avisos | **Sí** — el arnés es lo que se ejecutó |
| `AlarmPump` (DB1, instancia de FB_AlarmLatch) | 1513-1 PN · FW V3.0 | **V20** | **Sí** — 0 errores / 0 avisos | **Sí** — DB leída y escrita durante los casos |
| `FB_AgentDemo` (FB1, SCL) — baseline de la fixture | 1513-1 PN · FW V3.0 | **V20** | **Sí** — 0 errores / 0 avisos | **Sí** — descargado junto con el resto |

Evidencia de ejecución: [`evidencia-plcsim-2026-10-21.json`](evidencia-plcsim-2026-10-21.json)
(65/65 pasos del plan, 9 casos con los valores observados) y la
[captura del Control Panel](assets/plcsim-control-panel-2026-10-21.png) con la instancia
`PLC_1` en marcha.

## Entorno de la prueba

| Componente | Versión | Nota |
|---|---|---|
| TIA Portal | **V20** | build `2000.0.9501.1` |
| PLCSIM Advanced | **V7.0.0.0** (API 7.0, `0x00070000`) | Runtime Manager operativo; `Online Access = TCP/IP Single Adapter` |
| S7-PLCSIM clásico | **V19** y **V20** | instalados en el mismo host; ver H-19 (refutado) |
| Transporte | **TCP/IP** sobre `Siemens PLCSIM Virtual Ethernet Adapter` (`192.168.0.2/24`) | instancia `PLC_1` en `192.168.0.1`, CPU virtual en `RUN` |
| Ruta de descarga | `PN/IE / Siemens PLCSIM Virtual Ethernet Adapter → 1 X1` | `Download Success`, 0 errores, 0 avisos |

## Compatibilidad de versión (matriz Siemens)

TIA **V20** requiere S7-PLCSIM Advanced **V7.0** (cubre TIA V14–V20 y CPU FW V1.8–V4.0).
La CPU de esta prueba es FW **V3.0**, dentro del rango soportado → **la combinación de
versiones es válida** y queda verificada en ejecución, no solo por rango.

## Las cuatro condiciones que había que cumplir

Ninguna era evidente y las cuatro hacen falta a la vez. Sin una de ellas la descarga
vuelve a fallar con `Connect to module PLC_1 failed`:

1. **La sesión Openness tiene que ir adjunta al TIA abierto** (`AttachToOpenProject`), no
   aislada. En sesión headless (`ConnectIsolated`) el mismo proyecto falla aunque la CPU
   virtual esté viva y respondiendo por S7.
2. **El Control Panel de PLCSIM Advanced necesita margen**: la primera descarga tras
   arrancarlo falla y la segunda, unos 100 s después, funciona. La OAM no queda configurada
   al instante.
3. **La lista de etiquetas hay que refrescarla** con `IInstance::UpdateTagList()`. Sin esa
   llamada la lectura simbólica devuelve `-47` (`SREC_NOT_UP_TO_DATE`) aunque la CPU
   ejecute el programa descargado.
4. **Los tags se nombran sin el prefijo de tabla**: la API resuelve por `Active`, no por
   `Agent_Signals.Active`; con el nombre cualificado devuelve `-4`
   (`SREC_DOES_NOT_EXIST`).

## Hallazgo H-19 — hipótesis original **refutada**

Se propuso que el bloqueo venía de que **S7-PLCSIM clásico V19** ocupaba la interfaz
PG/PC `PLCSIM`. **Se refutó empíricamente**: tras instalar **S7-PLCSIM clásico V20**
(`S7PLCSIMV20.exe`, v2000.0.200.9871) y repetir la descarga en tres variantes
—interfaz `PLCSIM`, sin forzar interfaz y `PLCSIM.TCPIP.1`— el resultado no cambió.
La versión del simulador clásico **no es la causa**.

Lo que sí era la causa, y quedó medido:

- **La configuración de hardware no compilaba** (3 errores por la protección de datos de
  configuración), porque `CompileSoftware` solo compila software. Se corrigió sin tocar
  contraseñas y el hardware pasó a 0/0.
- **El adaptador de PLCSIM invertía los octetos de la IP** al construirla, de modo que la
  CPU virtual recibía `1.0.168.192` en vez de `192.168.0.1`: el `SetIPSuite` lo aceptaba
  con `0x0` y lo descartaba en silencio. Corregido, la CPU responde a ping, a ARP y a S7.
- **El puerto IE1 de la instancia no se enlazaba con ninguna NIC**: el camino de registro
  nunca llamaba a `SetNetInterfaceMapping` ni a `SetNetInterfaceBindings`.

> Detalle completo, intento a intento, en
> [`informe-ejecucion-2026-10-19.md`](informe-ejecucion-2026-10-19.md) (run
> `20261016-fb-alarm-latch` del workspace TIA-Claude).

## Desviaciones de esta ejecución

- **Transporte TCP/IP en vez de Softbus local**: el Control Panel está en *TCP/IP Single
  Adapter* y su `ComChannel` es precisamente la NIC virtual de Siemens; forzar Softbus desde
  la API era incompatible.
- **Cuatro de los nueve casos releen solo parte de las señales**. Los valores no releídos
  se anotan como `-` y se razonan a partir del estado previo; no se presentan como
  observados.

## Lo que queda fuera del alcance

Esta matriz acredita el comportamiento del bloque en un proyecto desechable con arnés
dedicado, sobre una CPU virtual 1513-1 PN. **No acredita** uso en instalación real, ni
compatibilidad con otras familias de CPU, ni variantes del bloque sin el arnés.
