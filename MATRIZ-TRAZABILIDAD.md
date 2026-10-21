# Matriz de trazabilidad — qué hay realmente en cada carpeta

> Esta matriz existe para que nadie tenga que abrir 24 README para saber qué se puede
> importar. Cada fila dice **qué hay realmente** en la carpeta y **qué falta** para
> poder usarla sin leer la ficha entera.
>
> Los estados del [catálogo](CATALOG.md) son una etiqueta; esta tabla es el detalle.
> Nada aquí es una estimación: cada celda con un ✅ tiene su fichero o su evidencia.

## Leyenda de columnas

| Columna | Significado |
|---|---|
| Fuente | Hay un `.scl` o un `.xml` importable en la carpeta |
| Compilado | La fuente se compiló en TIA Portal V20 con **0 errores y 0 avisos** |
| Ejecutado | Se descargó a una CPU **virtual** y se observaron casos de comportamiento |
| Evidencia | Fichero de evidencia con los valores observados |

---

## Bloques de función

| Recurso | Tipo | Fuente | Compilado | Ejecutado | Evidencia |
|---|---|:---:|:---:|:---:|---|
| [`fb-alarm-latch`](./bloques-de-funcion/fb-alarm-latch/) | FB | ✅ SCL + XML | ✅ 0/0 | ✅ 65/65 pasos, 9 casos | [`evidencia-plcsim-2026-10-21.json`](./bloques-de-funcion/fb-alarm-latch/evidencia-plcsim-2026-10-21.json) |
| [`fc-escalado`](./bloques-de-funcion/fc-escalado/) | FC | ✅ SCL + XML | ✅ 0/0 | ✅ 33/33 pasos, 9 casos | [`evidencia-plcsim-2026-10-21.json`](./bloques-de-funcion/fc-escalado/evidencia-plcsim-2026-10-21.json) |
| [`fb-analog-input`](./bloques-de-funcion/fb-analog-input/) | FB | ❌ | ❌ | ❌ | — |
| [`fb-edge-counter`](./bloques-de-funcion/fb-edge-counter/) | FB | ❌ | ❌ | ❌ | — |
| [`fb-hourmeter`](./bloques-de-funcion/fb-hourmeter/) | FB | ❌ | ❌ | ❌ | — |
| [`fb-motor`](./bloques-de-funcion/fb-motor/) | FB | ❌ | ❌ | ❌ | — |
| [`fb-pulse-gen`](./bloques-de-funcion/fb-pulse-gen/) | FB | ❌ | ❌ | ❌ | — |
| [`fb-valve`](./bloques-de-funcion/fb-valve/) | FB | ❌ | ❌ | ❌ | — |

## Bloques de organización

| Recurso | Tipo | Fuente | Compilado | Ejecutado | Evidencia |
|---|---|:---:|:---:|:---:|---|
| [`ob1-plantilla`](./bloques-de-organizacion/ob1-plantilla/) | OB1 | ❌ | ❌ | ❌ | — |
| [`ob100-startup`](./bloques-de-organizacion/ob100-startup/) | OB100 | ❌ | ❌ | ❌ | — |
| [`ob82-85-86-errores`](./bloques-de-organizacion/ob82-85-86-errores/) | OB82/85/86 | ❌ | ❌ | ❌ | — |

## Tipos de datos (UDT)

| Recurso | Tipo | Fuente | Compilado | Evidencia |
|---|---|:---:|:---:|---|
| [`udt-alarm`](./tipos-de-datos/udt-alarm/) | UDT | ❌ | ❌ | — |
| [`udt-analog-input`](./tipos-de-datos/udt-analog-input/) | UDT | ❌ | ❌ | — |
| [`udt-drive`](./tipos-de-datos/udt-drive/) | UDT | ❌ | ❌ | — |
| [`udt-motor`](./tipos-de-datos/udt-motor/) | UDT | ❌ | ❌ | — |
| [`udt-valve`](./tipos-de-datos/udt-valve/) | UDT | ❌ | ❌ | — |

## HMI

| Recurso | Tipo | Fuente | Compilado | Evidencia |
|---|---|:---:|:---:|---|
| [`faceplate-analog`](./hmi/faceplate-analog/) | Faceplate | ❌ | ❌ | — |
| [`faceplate-motor`](./hmi/faceplate-motor/) | Faceplate | ❌ | ❌ | — |
| [`faceplate-valve`](./hmi/faceplate-valve/) | Faceplate | ❌ | ❌ | — |
| [`pantalla-alarmas`](./hmi/pantalla-alarmas/) | Pantalla | ❌ | ❌ | — |
| [`plantilla-navegacion`](./hmi/plantilla-navegacion/) | Navegación | ❌ | ❌ | — |

## Plantillas de proyecto

| Recurso | Tipo | Fuente | Evidencia |
|---|---|:---:|---|
| [`plantilla-linea-modular`](./plantillas-de-proyecto/plantilla-linea-modular/) | Plantilla | ❌ | — |
| [`plantilla-maquina-simple`](./plantillas-de-proyecto/plantilla-maquina-simple/) | Plantilla | ❌ | — |

## Snippets

| Snippet | Estado |
|---|---|
| [`filtro-ton`](./snippets/filtro-ton.md) | ✅ **Verificado en ejecución**: es el filtro `OnDelay` de `FB_AlarmLatch`, ejecutado en PLCSIM con el caso `retardo-500ms` |
| [`flanco-r-trig`](./snippets/flanco-r-trig.md) | 📝 Patrón ilustrativo, sin compilación aislada |
| [`saturacion-min-max`](./snippets/saturacion-min-max.md) | 📝 Patrón ilustrativo, sin compilación aislada |

---

## Qué significa "ficha de diseño" y qué falta para cerrarla

Las 22 carpetas con ❌ **no incluyen código**: son fichas con la interfaz propuesta, la lógica
resumida y ejemplos de uso. Sus propios README lo dicen, y esta tabla lo confirma. **No son
importables.**

Para cerrar una ficha hacen falta estos pasos, en este orden. Es el camino que se ha seguido
con `fc-escalado` y con `fb-alarm-latch`, y está documentado con sus trampas:

1. **Escribir la fuente SCL** en la carpeta, con la cabecera y los comentarios al estilo del
   repo. En un `FUNCTION` (FC) el generador de fuentes de TIA V20 **no admite** `VERSION`,
   `AUTHOR` ni `FAMILY`, y exige el tipo de retorno en la cabecera
   (`FUNCTION "X" : Void`); la salida va por `VAR_OUTPUT`.
2. **Importar la fuente** en un proyecto desechable. Importante: la sesión de Openness tiene que
   estar **offline** (`GoOffline`) para poder escribir; con la UI en línea, TIA rechaza la
   escritura con *This function is not supported in online mode*.
3. **Generar los bloques** desde la fuente y **compilar**: 0 errores y 0 avisos. El readback
   debe dar `isFailsafe=false`, `isKnowHowProtected=false` y `isConsistent=true`.
4. **Montar el arnés** (un OB1 en SCL y una tabla de tags) y volver a compilar.
5. **Descargar a una CPU virtual** y ejecutar un plan de casos de comportamiento. Los pasos
   concretos, y las cuatro condiciones que la API impone, están en
   [`R28`](https://github.com/iagorobo24-hub/T-IA-Portal-RocaRoibas/blob/master/10-kb/20-recetas/R28-aceptacion-plcsim.md).
6. **Escribir la evidencia** con los valores observados y publicarla en la carpeta.

Las cuatro condiciones que hacen falta a la vez y que no son evidentes:

| # | Condición | Qué pasa si no se cumple |
|---|---|---|
| 1 | La sesión Openness va **adjunta** al TIA abierto (`AttachToOpenProject`) | La descarga falla con `Connect to module PLC_1 failed` |
| 2 | **~100 s** tras arrancar el Control Panel de PLCSIM Advanced | La primera descarga falla y la segunda funciona |
| 3 | `IInstance::UpdateTagList()` antes de leer tags | La lectura simbólica devuelve `-47` |
| 4 | Los tags se nombran **sin el prefijo de tabla** | La lectura devuelve `-4` |

---

## En resumen

- **2 de 24 recursos** tienen código importable, compilado y ejecutado con evidencia:
  `fb-alarm-latch` y `fc-escalado`.
- **22 de 24** son fichas de diseño sin código. Son utiles como especificación, y su README lo
  dice con claridad; no como pieza importable.
- El [`CATALOG.md`](./CATALOG.md) marca el estado de cada carpeta; esta tabla lo desglosa.
