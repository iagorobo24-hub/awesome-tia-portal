# UDT_Alarm

> Estructura unificada para una alarma — activación, reconocimiento, timestamp, prioridad y texto descriptivo.

**Tipo:** `UDT`
**Versión TIA Portal:** V20 *(compatible con V18 y V19)*
**Familia PLC:** S7-1200 / S7-1500

---

## ¿Qué problema resuelve?

Las alarmas en TIA Portal se gestionan típicamente con bits sueltos en una marca o DB. Eso funciona, pero deja sin resolver: ¿cuándo se activó?, ¿está reconocida?, ¿qué prioridad tiene?, ¿qué texto se muestra al operario?

`UDT_Alarm` reúne en una única estructura toda la información que el operador necesita ver y que el sistema necesita gestionar (filtros, históricos, ack). Un array de `UDT_Alarm` da una **lista de alarmas estandarizada**, fácil de filtrar en HMI y exportar a histórico.

---

## Variables / Interfaz

| Variable | Tipo | Descripción |
|---|---|---|
| `xActiva` | BOOL | Condición de alarma actualmente cumplida |
| `xReconocida` | BOOL | El operador la ha reconocido (ack) |
| `xNueva` | BOOL | Activa **y** sin reconocer — la que se muestra parpadeando en HMI |
| `xMemorizada` | BOOL | Fue activa pero ya no lo está (queda en histórico hasta que se reconozca) |
| `dtTimestamp` | DTL | Marca de tiempo del momento en que se activó |
| `dtTimestampAck` | DTL | Marca de tiempo del reconocimiento |
| `iPrioridad` | INT | 1 = baja · 2 = media · 3 = alta · 4 = crítica |
| `sTexto` | STRING[80] | Texto descriptivo mostrado al operador |
| `sFuente` | STRING[40] | Origen / equipo de la alarma (ej: "M01_Bomba", "AI01_TempReactor") |
| `iCodigo` | INT | Código numérico interno de la alarma (para filtros y trazabilidad) |

---

## Cómo importarlo en TIA Portal

1. Descarga el archivo `udt-alarm.xml`
2. En TIA Portal, abre tu proyecto
3. En el árbol del proyecto, clic derecho sobre **Tipos de datos PLC**
4. Selecciona **Importar**
5. Busca el `.xml` descargado y confirma

---

## Ejemplo de uso

Lo más habitual es declarar un **array de alarmas** dentro de un DB global:

```
DB_Alarmas.aLista : ARRAY[1..256] OF UDT_Alarm
```

Asigna cada alarma del proyecto a un índice fijo y rellena los textos en el OB de arranque (`OB100`):

```
"DB_Alarmas".aLista[1].sTexto    := 'Térmico bomba principal disparado';
"DB_Alarmas".aLista[1].sFuente   := 'M01_BombaPrincipal';
"DB_Alarmas".aLista[1].iPrioridad := 3;
```

Después en el OB de programa enlazas la condición:

```
"DB_Alarmas".aLista[1].xActiva := "DB_Equipos".M01_BombaPrincipal.Fallos.xTermico;
```

Un FB transversal (`FB_AlarmManager`, no incluido en este repo) se encarga de:
- Detectar flancos de subida → rellenar `dtTimestamp`, marcar `xNueva`
- Procesar el ack → rellenar `dtTimestampAck`, limpiar `xNueva`
- Mantener `xMemorizada` hasta el ack final

---

## Notas / Limitaciones conocidas

- El timestamp `DTL` se rellena con `RD_LOC_T` o `RD_SYS_T` desde el FB gestor (no se autorrellena).
- `iPrioridad` es un INT por simplicidad; si prefieres un ENUM dedicado tendrás que cambiarlo después de exportar.
- Para alarmas analógicas con histéresis y delay (HH/H/L/LL), úsalo combinado con `UDT_AnalogInput` que ya gestiona los flags — un solo `UDT_Alarm` por nivel.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
