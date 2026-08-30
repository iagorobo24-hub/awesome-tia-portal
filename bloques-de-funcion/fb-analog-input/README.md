---
name: FB_AnalogInput
type: fb
tia_version: V20
tia_compat: [V18, V19, V20]
plc_family: [s7-1200, s7-1500]
depends_on: [tipos-de-datos/udt-analog-input]
used_by: []
tags: [analogica, escalado, alarmas, fb]
status: documented
---

# FB_AnalogInput

> Bloque de procesado de entrada analógica — escalado, filtrado pasa-baja, alarmas HH/H/L/LL con histéresis, y simulación.

**Tipo:** `Bloque de función (FB)`
**Versión TIA Portal:** V20 *(compatible con V18 y V19)*
**Familia PLC:** S7-1200 / S7-1500

**Depende de:** [`UDT_AnalogInput`](../../tipos-de-datos/udt-analog-input/)

---

## ¿Qué problema resuelve?

Cada entrada analógica necesita el mismo tratamiento: leer raw → escalar → filtrar → comprobar 4 niveles de alarma con histéresis y delay → vigilar cable cortado → permitir simulación. Si lo programas a mano cada vez, tarde o temprano hay un error de signos o histéresis.

`FB_AnalogInput` resuelve todo el ciclo en un único FB que consume `UDT_AnalogInput` como InOut. La señal entra cruda y la estructura sale lista para usar en lógica y para mostrar en HMI.

---

## Variables / Interfaz

### Entradas (Input)

| Variable | Tipo | Descripción |
|---|---|---|
| `iValorCrudo` | INT | Valor raw del módulo (típicamente `%IW...`) |
| `xModuloOK` | BOOL | Calidad reportada por el módulo (de `MODULE_DIAG` o equivalente) |

### InOut

| Variable | Tipo | Descripción |
|---|---|---|
| `Analog` | UDT_AnalogInput | Estructura completa de la entrada analógica |

### Salidas (Output)

| Variable | Tipo | Descripción |
|---|---|---|
| `qAlarmaActiva` | BOOL | OR de las 4 alarmas (HH, H, L, LL) — útil para enclavamientos rápidos |

### Estáticas (Static) destacadas

| Variable | Tipo | Descripción |
|---|---|---|
| `rValorAnterior` | REAL | Para el filtrado pasa-baja |
| `tonDelayHH/H/L/LL` | TON | Temporizadores de retardo de alarma |
| `rContadorMedia` | REAL | Suma para calcular `Procesado.rValorMedio` |

---

## Cómo importarlo en TIA Portal

1. Asegúrate de tener importado primero el [`UDT_AnalogInput`](../../tipos-de-datos/udt-analog-input/).
2. Descarga el archivo `fb-analog-input.xml`.
3. En TIA Portal: clic derecho sobre **Bloques de programa** → **Importar** → confirma.

---

## Ejemplo de uso

```scl
// En el OB de arranque (OB100), configura los parámetros una sola vez:
"DB_Analogicas".AI01_TempReactor.Escalado.rRangoMinIng := 0.0;
"DB_Analogicas".AI01_TempReactor.Escalado.rRangoMaxIng := 150.0;
"DB_Analogicas".AI01_TempReactor.Procesado.sUnidad    := 'ºC';
"DB_Analogicas".AI01_TempReactor.Alarmas.rLimiteHH    := 130.0;
"DB_Analogicas".AI01_TempReactor.Alarmas.rLimiteH     := 110.0;
"DB_Analogicas".AI01_TempReactor.Alarmas.rLimiteL     := 20.0;
"DB_Analogicas".AI01_TempReactor.Alarmas.rLimiteLL    := 5.0;
"DB_Analogicas".AI01_TempReactor.Alarmas.rHisteresis  := 1.0;
"DB_Analogicas".AI01_TempReactor.Config.rConstanteFiltro := 0.2;
"DB_Analogicas".AI01_TempReactor.Config.tDelayAlarma  := T#2s;
"DB_Analogicas".AI01_TempReactor.Config.xHabilitado   := TRUE;

// En el OB de programa (OB1):
"FB_AnalogInput"(
    iValorCrudo := %IW64,
    xModuloOK   := TRUE,
    Analog      := "DB_Analogicas".AI01_TempReactor
);
```

---

## Lógica resumida

1. Si `Diagnostico.xSimulacion = TRUE` → `rValor := rValorSimulado` y se saltan los pasos siguientes.
2. Escalado lineal de `iValorRaw` con los límites de `Escalado` → valor sin filtrar.
3. Filtrado pasa-baja: `rValor := alfa * rValorAnterior + (1-alfa) * rValorActual` con `alfa = Config.rConstanteFiltro`.
4. Comparación con los 4 umbrales con histéresis y delay → `Alarmas.xAlarmaHH/H/L/LL`.
5. Detección de cable cortado: `iValorRaw < iRangoMinRaw - margen` → `Diagnostico.xCableCortado := TRUE`.
6. Actualización de `rValorMin`, `rValorMax` y `rValorMedio` (media móvil).

---

## Notas / Limitaciones conocidas

- El filtrado se aplica **después** del escalado para que el valor filtrado mantenga las unidades de ingeniería.
- `rValorMin` y `rValorMax` se resetean por código (no se exponen como Input — pásalos a 0 desde el HMI escribiéndolos directamente al UDT).
- Para módulos 4-20mA configura `iRangoMinRaw := 5530`. Cable cortado se dispara si `iValorRaw < 4000`.
- El delay de alarma `tDelayAlarma` aplica al activar; al desactivar la alarma cae inmediatamente (con histéresis).

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
