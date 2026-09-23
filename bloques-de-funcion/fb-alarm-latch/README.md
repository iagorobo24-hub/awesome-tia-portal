# FB_AlarmLatch

Enclava una alarma de proceso, conserva una alarma que ya desapareció sin reconocimiento y genera una petición de sirena hasta que el operador la reconozca.

**Archivo:** [FB_AlarmLatch.scl](FB_AlarmLatch.scl) · **Lenguaje:** SCL · **Versión de bloque:** 0.1 · **Dependencias:** temporizador `TON_TIME` de TIA Portal.

## Estado comprobado

- **Fuente disponible:** el archivo SCL se incluye aquí. Procede de la librería propia MIT de [TIA-Claude](https://github.com/iagorobo24-hub/T-IA-Portal-RocaRoibas/tree/master/60-library/blocks).
- **Compilación:** el bloque de origen fue importado y compilado en TIA Portal V20 con **0 errores y 0 advertencias** el 14/09/2026, según el [registro de la librería](https://github.com/iagorobo24-hub/T-IA-Portal-RocaRoibas/blob/master/60-library/blocks/README.md). Esta copia conserva la lógica; solo se ha retirado una referencia a una ruta interna del comentario.
- **Pendiente:** no hay prueba de comportamiento en PLCSIM, exportación XML de esta copia, ni matriz de CPU/HSP. No se declara listo para producción.

## Interfaz

| Señal | Dirección | Significado |
|---|---|---|
| `Condition` | Entrada | Condición de alarma ya evaluada. |
| `CmdAck` | Entrada | Orden de reconocimiento. |
| `Enable` | Entrada | Permite la alarma; `FALSE` borra el enclavamiento. |
| `OnDelay` | Entrada | Tiempo de filtrado; `T#0S` deja paso inmediato. |
| `Active` | Salida | Condición filtrada presente. |
| `Latched` | Salida | Alarma aún visible. |
| `Unacked` | Salida | Pendiente de reconocer. |
| `GoneUnacked` | Salida | Condición desaparecida, sin reconocimiento. |
| `Horn` | Salida | Petición de sirena mientras no se reconozca. |

## Estados esperados

| Condición | Reconocida | Resultado |
|---|---|---|
| Presente | No | Activa, enclavada y sirena solicitada. |
| Presente | Sí | Sigue activa y visible; sirena apagada. |
| Desaparecida | No | Sigue visible como `GoneUnacked`; sirena solicitada. |
| Desaparecida | Sí | Se borra el enclavamiento. |

La tabla describe la intención del código. **Todavía necesita una prueba de transiciones en PLCSIM.**

## Uso en un proyecto de prueba

1. Trabaja sobre una copia de un proyecto V20 y conserva un backup antes de importar.
2. Crea una fuente externa SCL desde [FB_AlarmLatch.scl](FB_AlarmLatch.scl) y genera el bloque desde ella en TIA Portal. Comprueba nombre, lenguaje e interfaz en el proyecto resultante.
3. Compila el software PLC. Si hay errores, corrige o revierte; guarda solo después de compilar correctamente.
4. Prueba en una CPU virtual las cuatro transiciones de la tabla antes de utilizarlo en una máquina.

Ejemplo conceptual de llamada desde un bloque que ya declara una instancia `AlarmPump`:

```scl
#AlarmPump(
    Condition := #PumpFault,
    CmdAck := #Acknowledge,
    Enable := TRUE,
    OnDelay := T#500MS,
    Active => #AlarmActive,
    Latched => #AlarmVisible,
    Unacked => #AlarmUnacked,
    GoneUnacked => #AlarmGoneUnacked,
    Horn => #HornRequest
);
```

`Horn` es una **petición de proceso**. Este FB no implementa funciones F/Safety ni sustituye una cadena de seguridad certificada. `Enable := FALSE` borra la memoria; decide explícitamente si esa semántica es adecuada para tu instalación.
