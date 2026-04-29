---
name: FB_PulseGen
type: fb
tia_version: V20
tia_compat: [V18, V19, V20]
plc_family: [s7-1200, s7-1500]
depends_on: []
used_by: []
tags: [pulsos, generador, fb]
status: documented
---

# FB_PulseGen

> Generador de pulsos parametrizable — produce un tren de pulsos con periodo y duty cycle configurables. Útil para parpadeos, refresco, tests, etc.

**Tipo:** `Bloque de función (FB)`
**Versión TIA Portal:** V20 *(compatible con V18 y V19)*
**Familia PLC:** S7-1200 / S7-1500

---

## ¿Qué problema resuelve?

TIA Portal ofrece la marca de ciclo (ej: `%M0.5` a 1Hz), pero solo a frecuencias fijas y sin control fino del duty cycle. Para parpadeos del HMI, refrescos cíclicos o señales de test, `FB_PulseGen` da un tren de pulsos con periodo y ancho configurables, y se puede instanciar tantas veces como se necesite.

---

## Variables / Interfaz

### Entradas (Input)

| Variable | Tipo | Descripción |
|---|---|---|
| `xEnable` | BOOL | Habilita el generador. Si `FALSE`, salida queda en `FALSE` |
| `tPeriodo` | TIME | Periodo total del ciclo (ej: T#1s = 1Hz) |
| `tAnchoPulso` | TIME | Tiempo en `TRUE` dentro del periodo. Si > `tPeriodo`, se satura a `tPeriodo` |

### Salidas (Output)

| Variable | Tipo | Descripción |
|---|---|---|
| `qPulso` | BOOL | Salida del tren de pulsos |

### Estáticas (Static)

| Variable | Tipo | Descripción |
|---|---|---|
| `tonCiclo` | TON | Temporizador del periodo |
| `tonAncho` | TON | Temporizador del ancho de pulso |

---

## Cómo importarlo en TIA Portal

1. Descarga el archivo `fb-pulse-gen.xml`.
2. En TIA Portal: clic derecho sobre **Bloques de programa** → **Importar** → confirma.

---

## Ejemplo de uso

```scl
// Parpadeo de lámpara de fallo (medio segundo encendida cada segundo)
"FB_PulseGen".Blink_1Hz_50pct(
    xEnable     := "DB_Equipos".M01_BombaPrincipal.Estado.xFallo,
    tPeriodo    := T#1s,
    tAnchoPulso := T#500ms,
    qPulso      => "DB_HMI".xLamparaFalloM01_Parpadeo
);

// Pulso corto cada 5 segundos para refrescar pantalla HMI
"FB_PulseGen".Refresh_5s(
    xEnable     := TRUE,
    tPeriodo    := T#5s,
    tAnchoPulso := T#100ms,
    qPulso      => "DB_HMI".xRefreshTrigger
);
```

---

## Lógica resumida

1. Si `xEnable = FALSE` → `qPulso := FALSE` y los temporizadores se resetean.
2. Si `xEnable = TRUE`:
   - `tonCiclo` cuenta hasta `tPeriodo` y reinicia.
   - Mientras `tonCiclo.ET < tAnchoPulso` → `qPulso := TRUE`.
   - El resto del periodo `qPulso := FALSE`.

---

## Notas / Limitaciones conocidas

- La precisión depende del tiempo de ciclo del PLC. Para periodos < 100ms el jitter puede ser apreciable.
- Si `tAnchoPulso > tPeriodo`, internamente se satura a `tPeriodo` y la salida queda siempre en `TRUE`.
- Si necesitas un **único pulso** (no tren), usa el bloque `TP` estándar de TIA Portal.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
