# Protocolo de ejecución en PLCSIM (FB_AlarmLatch)

Lista ordenada para ejecutar en la sesión con TIA Portal V20. No improvisar
el orden: cada fase exige la anterior en verde. Si algo no cuadra, parar
y anotar antes de seguir.

## F0. Precondiciones (no saltar)

1. Trabajar sobre el **proyecto desechable** (copia, nunca un proyecto de cliente o de planta).
2. Anotar el hash SHA-256 del `.ap20` antes de empezar.
3. TIA Portal V20 con licencia válida y PLCSIM disponible.
4. Fuente [FB_AlarmLatch.scl](FB_AlarmLatch.scl) ya importada y compilada (0/0).

## F1. Arnés y compilación

1. Montar el arnés exacto de [arnes-ob1.md](arnes-ob1.md): DB `AlarmPump`, network CALL en OB1, mapa de memorias.
2. Compilar el software PLC completo. Exigido: **0 errores y 0 advertencias**.
3. Crear la tabla VAT `VAT_AlarmLatch` con los 10 operandos.
4. Forzar `M0.2 = TRUE` (Enable) y comprobar reposo: `M2.0…M2.4 = 0`.

## F2. Arranque de la CPU virtual (lecciones del 23/09)

1. **Una sola** CPU virtual S7-1500, modo local Softbus (el modo que ya funcionó aquí).
2. No llamar a funciones de mapeo TCP/IP en modo Softbus (da `SREC_NOT_SUPPORTED`).
3. No configurar IP antes de arrancar la CPU (`SREC_INSTANCE_NOT_RUNNING`).
4. Anotar tipo de CPU virtual, modo y hora de arranque.

## F3. Descarga con seguridad (leer dos veces)

1. Abrir el diálogo de descarga y comprobar que la interfaz PG/PC y el destino corresponden **inequívocamente a la CPU virtual**.
2. Si aparece cualquier interfaz física o destino ambiguo: **cancelar y parar**.
3. Descargar **únicamente** a la instancia virtual. Jamás a un PLC de planta.
4. Pasar la CPU a RUN.

## F4. Casos y observación

`OnDelay = T#0MS` y `Enable = TRUE` salvo indicación. `CmdAck` se pulsa
un ciclo y se libera antes del caso siguiente.

| Paso | `M0.0` | `M0.1` | Esperado (`M2.0`…`M2.4`) | Observado |
|---|---|---|---|---|
| Reposo | 0 | 0 | 0, 0, 0, 0, 0 | |
| Aparece la alarma | 1 | 0 | 1, 1, 1, 0, 1 | |
| Reconocer con causa presente | 1 | 1 | 1, 1, 0, 0, 0 | |
| Desaparece tras reconocer | 0 | 0 | 0, 0, 0, 0, 0 | |
| Nuevo disparo y desaparición sin reconocer | 1 → 0 | 0 | al final 0, 1, 1, 1, 1 | |
| Reconocer causa desaparecida | 0 | 1 | 0, 0, 0, 0, 0 | |
| Inhibición (`M0.2 = FALSE`, `M0.0 = 1`) | 1 | 0 | 0, 0, 0, 0, 0 | |
| Retardo (`MD4 = T#500MS`, `M0.0 = 1`) | 1 | 0 | 0… hasta el retardo, luego 1, 1, 1, 0, 1 | |
| Ack como nivel (`M0.1 = 1` fijo, nueva alarma) | 0 → 1 | 1 fijo | Anotar si queda reconocida en el mismo ciclo | |

Tras la inhibición, devolver `M0.2 = TRUE` antes de seguir. Tras el caso
de retardo, devolver `MD4 = T#0MS`.

## F5. Cierre y evidencias

1. Captura de la observación en PLCSIM (vat o tabla de observación) sin datos sensibles, con versión, fecha y contexto.
2. Rellenar [evidencia-plcsim-plantilla.json](evidencia-plcsim-plantilla.json) con los valores observados y guardar como `evidencia-plcsim-AAAA-MM-DD.json`.
3. Anotar el hash SHA-256 del `.ap20` al terminar.
4. Apagar y dar de baja la CPU virtual; dejar el modo Softbus como estaba.

## Criterios de DONE

- Los 8 primeros casos coinciden con lo esperado, o cada desviación queda anotada como hallazgo (no se maquilla).
- El caso de ack como nivel queda documentado como comportamiento decidido (nivel frente a flanco).
- Existe captura + JSON de evidencia + hashes inicial y final.
