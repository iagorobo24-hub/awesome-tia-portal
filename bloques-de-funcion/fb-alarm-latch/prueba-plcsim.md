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

El 23/09/2026 se encendió y apagó una CPU 1513 virtual temporal en modo local Softbus. No se le descargó el proyecto, por lo que todavía no se pueden marcar como aprobados los casos anteriores. Una ruta TCP/IP ensayada antes intentó llamar funciones de mapeo de red en modo Softbus y obtuvo `SREC_NOT_SUPPORTED` (`-19`); además, `SetIPSuite` antes de arrancar la CPU obtuvo `SREC_INSTANCE_NOT_RUNNING` (`-14`). Son fallos de secuencia/modo de la prueba, no fallos demostrados del FB. [Siemens documenta Softbus y su descarga desde TIA](https://docs.tia.siemens.cloud/r/simatic_s7_1500_et_200mp_manual_collection_enus_20/comprehensive-information/cpu-function-manuals/s7-plcsim-advanced/simulating/simulating-a-cpu/control-panel-user-interface/s7-plcsim-advanced-control-panel).

Cuando se complete la prueba, publicar una captura del bloque y otra de la observación en PLCSIM, ambas tomadas del proyecto de demostración y sin rutas ni datos de cliente. Registrar los valores realmente observados junto a esta tabla.
