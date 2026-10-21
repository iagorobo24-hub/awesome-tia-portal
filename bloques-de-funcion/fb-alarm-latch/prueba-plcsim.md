# Prueba funcional prevista en PLCSIM

Esta prueba corresponde a [FB_AlarmLatch.scl](FB_AlarmLatch.scl). La fuente se importó y compiló en TIA Portal V20 con 0 errores y 0 advertencias en un proyecto desechable; [la evidencia](evidencia-tia-v20-2026-09-23.json) **no incluye una descarga ni transiciones observadas**.

## Montaje

1. Crear un proyecto de demostración V20 con CPU S7-1500 estándar, importar la fuente y compilar.
2. Añadir una llamada cíclica en OB1 con un DB de instancia. Exponer `Condition`, `CmdAck`, `Enable` y `OnDelay` como entradas de prueba y las cinco salidas del FB como señales observables.
3. Compilar de nuevo, guardar y registrar el árbol de software y el resultado de compilación.
4. Iniciar **una sola** CPU virtual compatible. Antes de descargar, verificar en el diálogo de TIA que la interfaz PG/PC y el destino corresponden inequívocamente a PLCSIM, nunca a un PLC de planta.
5. Descargar únicamente a la instancia virtual, ponerla en RUN, accionar entradas y guardar valores observados con fecha, versión y tipo de CPU.

## Casos mínimos

En cada fila, `OnDelay = T#0S` y `Enable = TRUE`, salvo que se indique otro valor. Un `CmdAck` se pulsa durante un ciclo y se libera antes del siguiente caso.

| Paso | `Condition` | `CmdAck` | Salidas esperadas (`Active`, `Latched`, `Unacked`, `GoneUnacked`, `Horn`) |
|---|---:|---:|---|
| Reposo | 0 | 0 | `0, 0, 0, 0, 0` |
| Aparece la alarma | 1 | 0 | `1, 1, 1, 0, 1` |
| Reconocer con causa presente | 1 | 1 | `1, 1, 0, 0, 0` |
| Desaparece tras reconocer | 0 | 0 | `0, 0, 0, 0, 0` |
| Nuevo disparo y desaparición sin reconocer | 1 → 0 | 0 | al final `0, 1, 1, 1, 1` |
| Reconocer causa desaparecida | 0 | 1 | `0, 0, 0, 0, 0` |
| Inhibición | 1 | 0, `Enable = FALSE` | `0, 0, 0, 0, 0` |

Añadir después un caso con `OnDelay = T#500MS` para medir la transición antes y después del retardo. Comprobar también qué ocurre si `CmdAck` permanece activado antes de una alarma nueva: el código actual interpreta el reconocimiento como **nivel**, no como flanco. Ese comportamiento debe decidirse y documentarse antes de usar el bloque en una instalación.

## Estado del camino de simulación en esta máquina

**Resuelto el 21/10/2026.** La prueba funcional se ejecutó completa sobre una CPU 1513 virtual
(PLCSIM Advanced V7.0, modo TCP/IP sobre `Siemens PLCSIM Virtual Ethernet Adapter`): descarga
`Success` con 0 errores y 0 avisos, `GoOnline` → `Online`, y el plan de 65 pasos pasó **65/65**
con los nueve casos de esta tabla correctos. Valores observados y desviaciones en
[`evidencia-plcsim-2026-10-21.json`](evidencia-plcsim-2026-10-21.json).

Para repetirlo hacen falta cuatro cosas que no son evidentes:

1. La sesión Openness debe ir **adjunta al TIA abierto** (`AttachToOpenProject`). En sesión
   headless aislada la descarga falla con `Connect to module PLC_1 failed` aunque la CPU virtual
   esté viva y respondiendo por S7.
2. Tras arrancar el Control Panel de PLCSIM Advanced hay que **esperar unos 100 s**: la primera
   descarga falla y la segunda funciona.
3. Antes de leer tags hay que llamar a **`IInstance::UpdateTagList()`**; sin eso la lectura
   simbólica devuelve `-47` (`SREC_NOT_UP_TO_DATE`).
4. Los tags se nombran **sin el prefijo de tabla** (`Active`, no `Agent_Signals.Active`); con el
   nombre cualificado devuelven `-4` (`SREC_DOES_NOT_EXIST`).

El 23/09/2026 se encendió y apagó una CPU 1513 virtual temporal en modo local Softbus. No se le descargó el proyecto, por lo que todavía no se pueden marcar como aprobados los casos anteriores. Una ruta TCP/IP ensayada antes intentó llamar funciones de mapeo de red en modo Softbus y obtuvo `SREC_NOT_SUPPORTED` (`-19`); además, `SetIPSuite` antes de arrancar la CPU obtuvo `SREC_INSTANCE_NOT_RUNNING` (`-14`). Son fallos de secuencia/modo de la prueba, no fallos demostrados del FB. [Siemens documenta Softbus y su descarga desde TIA](https://docs.tia.siemens.cloud/r/simatic_s7_1500_et_200mp_manual_collection_enus_20/comprehensive-information/cpu-function-manuals/s7-plcsim-advanced/simulating/simulating-a-cpu/control-panel-user-interface/s7-plcsim-advanced-control-panel).

Ya se publicó una captura del bloque desde el proyecto de demostración. La captura de la
observación en PLCSIM se publicó el 21/10/2026: el Control Panel corre elevado y su contenido no
es legible por automatización desde una sesión normal, pero **sus píxeles sí se pueden copiar
desde un proceso elevado**, que es como se obtuvo.

![Control Panel de PLCSIM Advanced V7.0 con la instancia virtual PLC_1 en marcha y la IP 192.168.0.1](assets/plcsim-control-panel-2026-10-21.png)

*Captura directa del Control Panel de PLCSIM Advanced V7.0, 21/10/2026. Se ve `Online Access =
TCP/IP Single Adapter`, `TCP/IP communication with: <Local>`, y `1 Active PLC Instance(s): PLC_1`
con el indicador verde de marcha y la dirección `/ 192.168.0.1`. Es la prueba de que el destino
de la descarga era una CPU virtual y no un PLC de planta.*

## Comprobación adicional del 24/09/2026

Se abrió el fixture en la interfaz de TIA Portal V20. La [captura del OB1](assets/tia-v20-ob1-sin-llamada-2026-09-24.jpg) confirma que su único network está vacío: el FB compilado **no se ejecutaría** si se descargase ahora. El preflight MCP devolvió compilación 0/0 y enumeró `Siemens PLCSIM Virtual Ethernet Adapter` como posible ruta PG/PC, pero también una tarjeta física. No se seleccionó destino ni se descargó nada; PLCSIM terminó sin CPU activa y se restauró el modo Softbus. Los hashes SHA-256 del `.ap20` de trabajo y de su copia previa coinciden. [Evidencia resumida](evidencia-preflight-2026-09-24.json).

Para completar la prueba se necesita un arnés cíclico en un **fixture aislado** que llame al FB y exponga entradas y salidas. Antes de importar lógica nueva debe poder leerse `isFailsafe=false`, lenguaje SCL y ausencia de protección del bloque exacto; para un bloque nuevo hay que probar primero su creación vacía y la clasificación posterior. El flujo de escritura V20 del workspace todavía no aporta esa secuencia completa, así que no se ha improvisado una edición LAD ni se ha tratado `CheckDownloadReadiness` como descarga efectiva.
