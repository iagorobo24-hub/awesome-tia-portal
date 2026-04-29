# FB_EdgeCounter

> Contador de flancos de subida con reset y configuración de límite — útil para contar ciclos de máquina, piezas producidas, paradas…

**Tipo:** `Bloque de función (FB)`
**Versión TIA Portal:** V20 *(compatible con V18 y V19)*
**Familia PLC:** S7-1200 / S7-1500

---

## ¿Qué problema resuelve?

Contar pulsos parece trivial, pero hay 3 errores típicos: olvidar el flanco (cuenta cada ciclo del PLC), no manejar el desbordamiento, y no permitir reset desde HMI. `FB_EdgeCounter` resuelve los tres con un FB pequeño y reutilizable.

---

## Variables / Interfaz

### Entradas (Input)

| Variable | Tipo | Descripción |
|---|---|---|
| `xSignal` | BOOL | Señal a contar (cuenta cada flanco de subida) |
| `xReset` | BOOL | Pulso para resetear el contador a 0 |
| `diLimite` | DINT | Valor al alcanzar el cual se activa `qLimiteAlcanzado` (0 = sin límite) |

### Salidas (Output)

| Variable | Tipo | Descripción |
|---|---|---|
| `qLimiteAlcanzado` | BOOL | `TRUE` cuando `diContador >= diLimite` (con `diLimite > 0`) |
| `qPulso` | BOOL | Espejo del flanco detectado (1 ciclo de PLC en `TRUE` por cada flanco) |

### InOut

| Variable | Tipo | Descripción |
|---|---|---|
| `diContador` | DINT | Valor del contador (debe ser retentivo) |

### Estáticas (Static)

| Variable | Tipo | Descripción |
|---|---|---|
| `rtrigSignal` | R_TRIG | Detector de flanco de subida |
| `rtrigReset` | R_TRIG | Detector de flanco para reset |

---

## Cómo importarlo en TIA Portal

1. Descarga el archivo `fb-edge-counter.xml`.
2. En TIA Portal: clic derecho sobre **Bloques de programa** → **Importar** → confirma.

---

## Ejemplo de uso

```scl
// Contar piezas producidas en una línea
"FB_EdgeCounter".PiezasOK(
    xSignal   := %I2.0,                          // sensor de paso
    xReset    := "DB_HMI".xResetContadorPiezas,
    diLimite  := 10000,
    diContador => "DB_Produccion".diPiezasOK,
    qLimiteAlcanzado => "DB_HMI".xLoteCompletado
);

// Contar arranques de un motor (sin límite)
"FB_EdgeCounter".M01_Arranques(
    xSignal  := "DB_Equipos".M01_BombaPrincipal.Estado.xEnMarcha,
    xReset   := FALSE,
    diLimite := 0,
    diContador => "DB_Equipos".M01_BombaPrincipal.Diagnostico.diArranques
);
```

---

## Lógica resumida

1. Flanco de subida en `xSignal` → `diContador += 1`, `qPulso := TRUE` durante 1 ciclo.
2. Flanco de subida en `xReset` → `diContador := 0`.
3. Si `diLimite > 0` y `diContador >= diLimite` → `qLimiteAlcanzado := TRUE`.

---

## Notas / Limitaciones conocidas

- `diContador` debe ser retentivo para que el contador sobreviva a cortes de tensión.
- DINT permite contar hasta 2.147.483.647 — más que suficiente para cualquier aplicación industrial.
- Si la frecuencia de pulsos es mayor a la mitad del ciclo de PLC (típicamente >50Hz), usa contadores HW (HSC) en lugar de este FB.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
