# Arnés de prueba — FC_Escalado

Arnés mínimo para ejercitar `FC_Escalado` en TIA Portal, sobre un proyecto **desechable**.
No es un proyecto de cliente ni de planta.

## Qué monta

1. Un proyecto de demostración V20 con una CPU S7-1500 estándar.
2. La fuente [`FC_Escalado.scl`](FC_Escalado.scl) importada como fuente externa y sus bloques
   generados.
3. La tabla de tags `Agent_Escalado` con seis variables `Real` (ver abajo).
4. Un `Main` (OB1) en SCL que llama al bloque cada ciclo.
5. Compilación exigida: **0 errores y 0 advertencias**.

## Mapa de tags (tabla `Agent_Escalado`)

| Tag | Tipo | Dirección | Papel |
|---|---|---|---|
| `RawValue` | Real | `%MD20` | Valor crudo de la entrada (de prueba) |
| `RawMin` | Real | `%MD24` | Raw del mínimo de escala |
| `RawMax` | Real | `%MD28` | Raw del máximo de escala |
| `ScaleMin` | Real | `%MD32` | Valor de ingeniería del raw mínimo |
| `ScaleMax` | Real | `%MD36` | Valor de ingeniería del raw máximo |
| `ScaledValue` | Real | `%MD40` | Salida escalada (la escribe el bloque) |

**Por qué son `Real` y no `Int`:** la API de PLCSIM Advanced resuelve y escribe símbolos `Real`
de forma nativa, pero no expone acceso simbólico a `Int`. El OB1 convierte con `REAL_TO_INT`
(que trunca hacia cero) al llamar al bloque, que **conserva su interfaz `Int`**. Los valores de
prueba se mantienen dentro del rango `Int`.

## El OB1

El SCL exacto que se ejecutó está en [`OB1_Arnes-ejecutado.scl`](OB1_Arnes-ejecutado.scl):

```scl
"FC_Escalado"(iValorCrudo := REAL_TO_INT("RawValue"),
              iRawMin     := REAL_TO_INT("RawMin"),
              iRawMax     := REAL_TO_INT("RawMax"),
              rEscalaMin  := "ScaleMin",
              rEscalaMax  := "ScaleMax",
              rEscalado   => "ScaledValue");
```

## Plan de comportamiento

El plan tiene 33 pasos y se ejecuta contra la instancia virtual ya descargada. Cada caso escribe
los cinco parámetros, deja correr el ciclo y lee `ScaledValue`.

```json
{ "command": "write-float-tag RawValue 13824.0", "delayMs": 300 },
{ "command": "read-float-tag ScaledValue",
  "expect": { "status": "ok", "op": "read-float-tag", "value": 50.0, "tolerance": 0.0001 } }
```

Dos cosas que el plan necesita y no son evidentes:

- **La lista de etiquetas hay que refrescarla** con `IInstance::UpdateTagList()` antes de la
  primera lectura simbólica. Sin eso la lectura devuelve `-47` (`SREC_NOT_UP_TO_DATE`) aunque la
  CPU ejecute el programa descargado.
- **La comparación de `Real` va con tolerancia**, no con igualdad textual: el adaptador serializa
  con 6 dígitos significativos.

## Casos

| Caso | Forzado | Esperado |
|---|---|---|
| escala-mínimo | `0..27648 → 0..100`, raw 0 | 0 |
| escala-máximo | raw 27648 | 100 |
| escala-mitad | raw 13824 | 50 |
| escala-cuarto | raw 6912 | 25 |
| 4-20 mA mínimo | `5530..27648 → 0..10`, raw 5530 | 0 |
| 4-20 mA media | raw 16589 | 5 |
| fuera de rango | raw 30000 | 108.5069 |
| raw negativo | raw -1000 | -3.6169 |
| rango degenerado | `RawMin = RawMax = 1000` | 7.5 |

## Ejecutado

El 21/10/2026 sobre CPU 1513 virtual (PLCSIM Advanced V7.0, modo TCP/IP sobre
`Siemens PLCSIM Virtual Ethernet Adapter`): descarga `Success` con 0 errores y 0 avisos,
`GoOnline` → `Online`, plan **33/33**. Valores observados y desviaciones en
[`evidencia-plcsim-2026-10-21.json`](evidencia-plcsim-2026-10-21.json).
