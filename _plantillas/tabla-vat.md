# Plantilla de tabla VAT para probar un recurso

Copia este fichero junto a tu recurso como `VAT_<Nombre>.md` y rellena la
tabla. Sirve de guion para forzar y observar en PLCSIM sin improvisar.

Ejemplo relleno: [VAT del FB_AlarmLatch](../../bloques-de-funcion/fb-alarm-latch/arnes-ob1.md).

## Tabla

| Señal | Operando | Formato en VAT | Uso |
|---|---|---|---|
| `<entrada 1>` | `M0.0` | Binario | Forzar `0`/`1` por caso |
| `<entrada 2>` | `M0.1` | Binario | Pulsos de un ciclo |
| `<habilitación>` | `M0.2` | Binario | Estado inicial conocido antes del primer caso |
| `<tiempo/consigna>` | `MD4` | TIME/REAL | Un valor por caso |
| `<salida 1>` | `M2.0` | Binario | Solo lectura |
| `<salida 2>` | `M2.1` | Binario | Solo lectura |

## Reglas

1. Las entradas de prueba van en memorias `M` del proyecto desechable.
2. Las salidas observadas **no se fuerzan nunca**.
3. Cada caso del protocolo indica qué forzar y qué esperar; la tabla solo es el mapa.
4. Tras casos especiales (inhibición, retardos), devolver los operandos a su valor base antes de seguir.
