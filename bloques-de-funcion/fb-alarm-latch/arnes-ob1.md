# Arnés OB1 para FB_AlarmLatch

Llamada cíclica mínima para poder descargar el bloque a PLCSIM y observar
sus transiciones. Corresponde a [FB_AlarmLatch.scl](FB_AlarmLatch.scl)
y ejecuta los casos de [prueba-plcsim.md](prueba-plcsim.md).

## DB de instancia

- Crear un DB de instancia del tipo `FB_AlarmLatch` con nombre `AlarmPump`.
- No usar multiinstancia: una sola instancia facilita la tabla de observación.

## Mapa de señales (memorias M, CPU de demostración)

| Señal del FB | Operando | Comentario |
|---|---|---|
| `Condition` | `M0.0` | Forzar desde VAT |
| `CmdAck` | `M0.1` | Pulsos de un ciclo desde VAT |
| `Enable` | `M0.2` | Forzar `TRUE` al inicio; `FALSE` solo en el caso de inhibición |
| `OnDelay` | `MD4` | `TIME`; `T#0MS` salvo en el caso de retardo (`T#500MS`) |
| `Active` | `M2.0` | Observar |
| `Latched` | `M2.1` | Observar |
| `Unacked` | `M2.2` | Observar |
| `GoneUnacked` | `M2.3` | Observar |
| `Horn` | `M2.4` | Observar |

Las memorias `M0.x` arrancan a `FALSE` (reposo correcto). `M0.2` debe
forzarse a `TRUE` antes del primer caso. `MD4` ocupa los bytes 4 a 7:
no se solapa con `M0.x` ni `M2.x`.

## Network 1 de OB1 (LAD, llamada CALL)

Un solo network con la instrucción CALL al DB `AlarmPump`:

```text
Network 1: llamada ciclica al latch de alarma
+---------------------------------------------------------------+
|  CALL "AlarmPump" , "FB_AlarmLatch"                           |
|    ENO  o-------- (sin uso)                                   |
|    Condition := "M0.0"                                        |
|    CmdAck    := "M0.1"                                        |
|    Enable    := "M0.2"                                        |
|    OnDelay   := "MD4"                                         |
|    Active       => "M2.0"                                     |
|    Latched      => "M2.1"                                     |
|    Unacked      => "M2.2"                                     |
|    GoneUnacked  => "M2.3"                                     |
|    Horn         => "M2.4"                                     |
+---------------------------------------------------------------+
```

La entrada `EN` del CALL queda siempre a `TRUE` (sin contactos previos):
el FB debe ejecutarse en todos los ciclos durante la prueba.

## Tabla VAT (recomendada: `VAT_AlarmLatch`)

| Operando | Formato en VAT | Uso |
|---|---|---|
| `M0.0` | Binario | Forzar `0`/`1` por caso |
| `M0.1` | Binario | Pulso: `1` un ciclo y volver a `0` |
| `M0.2` | Binario | `1` siempre salvo inhibición |
| `MD4` | TIME | `T#0MS`, `T#500MS` en el caso de retardo |
| `M2.0` … `M2.4` | Binario | Solo lectura |

## Compilación

Compilar el software PLC completo tras añadir el network. Resultado
exigido antes de seguir: **0 errores y 0 advertencias**. Guardar el
proyecto y anotar el resultado en la evidencia (ver
[protocolo-plcsim.md](protocolo-plcsim.md)).
