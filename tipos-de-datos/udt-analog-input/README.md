# UDT_AnalogInput

> Estructura unificada para el procesamiento de una entrada analógica: valor raw, escalado a unidades de ingeniería, alarmas HH/H/L/LL y diagnóstico.

**Tipo:** `UDT`
**Versión TIA Portal:** V20 *(compatible con V18 y V19)*
**Familia PLC:** S7-1200 / S7-1500

---

## ¿Qué problema resuelve?

Cada entrada analógica se acaba tratando "a mano": leer el raw, escalarlo, comprobar 4 niveles de alarma, vigilar cable cortado, filtrar… y se hace distinto en cada proyecto. Este UDT define **una única interfaz estándar** que el `FB_AnalogInput` consume, el HMI enlaza directamente y permite reutilizar entre proyectos sin tener que reaprender variables.

Cubre todo el ciclo de vida del valor: desde el INT raw hasta el REAL escalado con alarmas, calidad y configuración.

---

## Variables / Interfaz

El UDT está organizado en 6 sub-estructuras para separar claramente raw, escalado, alarmas, diagnóstico y configuración.

### `Raw` — valor crudo de entrada

| Variable | Tipo | Descripción |
|---|---|---|
| `iValorRaw` | INT | Valor crudo del módulo analógico (típicamente 0-27648) |
| `xCalidadOK` | BOOL | `TRUE` si el módulo reporta calidad válida |

### `Procesado` — valor en unidades de ingeniería

| Variable | Tipo | Descripción |
|---|---|---|
| `rValor` | REAL | Valor escalado y filtrado en unidades de ingeniería |
| `rValorMin` | REAL | Mínimo histórico desde último reset |
| `rValorMax` | REAL | Máximo histórico desde último reset |
| `rValorMedio` | REAL | Media móvil del valor |
| `sUnidad` | STRING[10] | Unidad de ingeniería (ej: "ºC", "bar", "m³/h") |

### `Escalado` — parámetros de escalado lineal

| Variable | Tipo | Descripción |
|---|---|---|
| `rRangoMinIng` | REAL | Valor mínimo en unidades de ingeniería |
| `rRangoMaxIng` | REAL | Valor máximo en unidades de ingeniería |
| `iRangoMinRaw` | INT | Valor raw equivalente al mínimo (típico 0 para 0-10V, 5530 para 4-20mA) |
| `iRangoMaxRaw` | INT | Valor raw equivalente al máximo (típico 27648) |

### `Alarmas` — 4 niveles + estado

| Variable | Tipo | Descripción |
|---|---|---|
| `xAlarmaHH` | BOOL | Alarma muy alta activa |
| `xAlarmaH` | BOOL | Alarma alta activa |
| `xAlarmaL` | BOOL | Alarma baja activa |
| `xAlarmaLL` | BOOL | Alarma muy baja activa |
| `rLimiteHH` | REAL | Umbral muy alto |
| `rLimiteH` | REAL | Umbral alto |
| `rLimiteL` | REAL | Umbral bajo |
| `rLimiteLL` | REAL | Umbral muy bajo |
| `rHisteresis` | REAL | Histéresis aplicada al desactivar las alarmas |

### `Diagnostico` — estado del canal

| Variable | Tipo | Descripción |
|---|---|---|
| `xCableCortado` | BOOL | Detectado cable cortado (raw fuera de rango bajo en 4-20mA) |
| `xFueraRango` | BOOL | Valor fuera del rango configurado |
| `xSimulacion` | BOOL | Canal en modo simulación (no usa el raw) |
| `rValorSimulado` | REAL | Valor que se inyecta cuando `xSimulacion = TRUE` |

### `Config` — parámetros de comportamiento

| Variable | Tipo | Descripción |
|---|---|---|
| `rConstanteFiltro` | REAL | Constante del filtro pasa-baja (0.0 = sin filtrado, 1.0 = máximo) |
| `tDelayAlarma` | TIME | Retardo antes de activar una alarma (anti-ruido) |
| `xHabilitado` | BOOL | Habilita/deshabilita todo el procesamiento |

---

## Cómo importarlo en TIA Portal

1. Descarga el archivo `udt-analog-input.xml`
2. En TIA Portal, abre tu proyecto
3. En el árbol del proyecto, clic derecho sobre **Tipos de datos PLC**
4. Selecciona **Importar**
5. Busca el `.xml` descargado y confirma

---

## Ejemplo de uso

Declara una variable del tipo `UDT_AnalogInput` por cada canal de la instalación dentro de un DB de "Analógicas":

```
DB_Analogicas.AI01_TempReactor : UDT_AnalogInput
DB_Analogicas.AI02_PresionLinea : UDT_AnalogInput
```

Pásala al `FB_AnalogInput` (próximamente en el repo) que se encarga del escalado, filtrado y alarmas:

```
"FB_AnalogInput"(
    iValorCrudo := %IW64,
    Analog := "DB_Analogicas".AI01_TempReactor
);
```

Y enlaza la sub-estructura entera al faceplate analógico del HMI con un único *binding*.

---

## Notas / Limitaciones conocidas

- Los rangos `Raw` están pensados para módulos con resolución estándar de TIA Portal (0-27648). Para módulos de alta resolución (-32768 a 32767) hay que ajustar los límites en `Escalado.iRangoMinRaw` / `iRangoMaxRaw`.
- Los valores `rValorMin`, `rValorMax`, `rValorMedio` se calculan en el `FB_AnalogInput` — el UDT solo los aloja.
- Para entradas 4-20mA usar `iRangoMinRaw := 5530` (equivalente a 4mA) para que el cable cortado se detecte correctamente.
- `Procesado.rValorMin`, `rValorMax` y `Diagnostico.xSimulacion` deberían ser retentivos en el DB que aloje las instancias.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
