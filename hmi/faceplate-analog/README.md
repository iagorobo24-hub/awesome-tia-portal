---
name: Faceplate_Analog
type: hmi-faceplate
tia_version: V20
tia_compat: [V18, V19, V20]
plc_family: [s7-1200, s7-1500]
hmi_panel: [comfort, unified]
depends_on: [tipos-de-datos/udt-analog-input, bloques-de-funcion/fb-analog-input]
used_by: []
tags: [analogica, faceplate, hmi]
status: documented
---

# Faceplate_Analog

> Faceplate HMI vinculado a `UDT_AnalogInput` — muestra valor con unidad, alarmas HH/H/L/LL, mín/máx y permite forzado/simulación.

**Tipo:** `HMI Faceplate`
**Versión TIA Portal:** V20
**Panel objetivo:** Comfort Panels · Unified Comfort · WinCC Unified RT

**Depende de:** [`UDT_AnalogInput`](../../tipos-de-datos/udt-analog-input/)

---

## ¿Qué problema resuelve?

Cada variable analógica en HMI requiere lo mismo: valor numérico grande, unidad, indicadores HH/H/L/LL, mín/máx, gráfico de tendencia… Hacerlo a mano para cada uno de los 50 canales del proceso es trabajo repetitivo y susceptible a errores.

`Faceplate_Analog` resuelve la representación estándar y queda funcional con un único *binding* a la instancia de `UDT_AnalogInput`.

---

## Estructura visual

```
┌─────────────────────────────────────────┐
│ AI01_TempReactor                         │
├─────────────────────────────────────────┤
│                                          │
│         87.5  ºC                         │   ← valor procesado grande
│                                          │
├─────────────────────────────────────────┤
│   ●HH  ○H  ○L  ○LL                       │   ← 4 LEDs de alarma
├─────────────────────────────────────────┤
│ Mín: 22.1   Máx: 130.4   Med: 75.2       │
├─────────────────────────────────────────┤
│ Limite HH: 130.0    [editar]            │   ← edición protegida con permiso
│ Limite H:  110.0    [editar]            │
│ Limite L:   20.0    [editar]            │
│ Limite LL:   5.0    [editar]            │
├─────────────────────────────────────────┤
│ ☐ Simulación      Valor sim: 0.0  [edit]│
│ Calidad: OK                              │
└─────────────────────────────────────────┘
```

---

## Interfaz del faceplate

Una única propiedad `Analog` de tipo `UDT_AnalogInput`.

### Lecturas mostradas

- Valor grande → `{Analog}.Procesado.rValor` formateado con `{Analog}.Procesado.sUnidad`.
- LEDs HH/H/L/LL → `{Analog}.Alarmas.xAlarmaHH/H/L/LL` (rojo = activa).
- Mín/máx/medio → `{Analog}.Procesado.rValorMin/Max/Medio`.
- Calidad → indicador verde/rojo según `{Analog}.Raw.xCalidadOK` y `{Analog}.Diagnostico.xCableCortado`.

### Edición desde HMI (con permiso)

- Editar umbrales → escribe `{Analog}.Alarmas.rLimiteHH/H/L/LL`.
- Toggle simulación → escribe `{Analog}.Diagnostico.xSimulacion` y `rValorSimulado`.

---

## Cómo importarlo en TIA Portal

1. Asegúrate de tener importado primero el [`UDT_AnalogInput`](../../tipos-de-datos/udt-analog-input/).
2. Descarga el archivo `faceplate-analog.xml`.
3. En TIA Portal HMI: clic derecho sobre **Faceplates** → **Importar** → confirma.

---

## Ejemplo de uso

```
Variable enlazada: "DB_Analogicas".AI01_TempReactor
```

---

## Notas / Limitaciones conocidas

- La edición de umbrales y la simulación deben protegerse con un **grupo de usuarios** (`Editor` / `Mantenimiento`); el faceplate expone una propiedad `xPermisoEdicion` que se enlaza al permiso del usuario actual.
- Para añadir un **gráfico de tendencia** integrado al faceplate, considera la versión Unified — Comfort no soporta tendencias dentro de faceplates pequeños sin trucos.
- El número de decimales y el ancho del display están parametrizados en propiedades del faceplate (`iDecimales`, `iAnchoDisplay`).

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
