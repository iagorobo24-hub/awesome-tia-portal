---
name: FB_Hourmeter
type: fb
tia_version: V20
tia_compat: [V18, V19, V20]
plc_family: [s7-1200, s7-1500]
depends_on: []
used_by: []
tags: [horas, contador, persistencia, fb]
status: documented
---

# FB_Hourmeter

> Contador de horas de funcionamiento — acumula el tiempo en el que su entrada está activa, con persistencia entre cortes de tensión.

**Tipo:** `Bloque de función (FB)`
**Versión TIA Portal:** V20 *(compatible con V18 y V19)*
**Familia PLC:** S7-1200 / S7-1500

---

## ¿Qué problema resuelve?

Cualquier proyecto industrial necesita contar horas de funcionamiento de equipos para mantenimiento preventivo. Hacerlo "a mano" obliga a calcular ciclos, convertir milisegundos a horas, gestionar la retentividad… Y siempre se acaba colando un error.

`FB_Hourmeter` es un bloque pequeño y autónomo que cuenta horas mientras su entrada está a `TRUE`. Tantas instancias como equipos haya en la máquina.

---

## Variables / Interfaz

### Entradas (Input)

| Variable | Tipo | Descripción |
|---|---|---|
| `xRunning` | BOOL | `TRUE` mientras el equipo está en marcha y debe acumular horas |
| `xReset` | BOOL | Pulso para resetear el contador a 0 (típico tras mantenimiento) |
| `rUmbralAviso` | REAL | Horas a partir de las cuales se activa `qAvisoMantenimiento` (0.0 = deshabilitado) |

### Salidas (Output)

| Variable | Tipo | Descripción |
|---|---|---|
| `qAvisoMantenimiento` | BOOL | `TRUE` cuando `rHoras >= rUmbralAviso` |

### InOut

| Variable | Tipo | Descripción |
|---|---|---|
| `rHoras` | REAL | Acumulador de horas (debe ser **retentivo** en el DB de instancia) |

### Estáticas (Static) destacadas

| Variable | Tipo | Descripción |
|---|---|---|
| `tCiclo` | TIME | Tiempo del último ciclo (calculado por TIA Portal) |
| `rAcumuladorMs` | REAL | Acumulador interno en milisegundos hasta llegar a 1h |
| `rtrigReset` | R_TRIG | Flanco para reset |

---

## Cómo importarlo en TIA Portal

1. Descarga el archivo `fb-hourmeter.xml`.
2. En TIA Portal: clic derecho sobre **Bloques de programa** → **Importar** → confirma.

---

## Ejemplo de uso

```scl
// Conteo de horas de la bomba principal
"FB_Hourmeter".M01_Horas(
    xRunning      := "DB_Equipos".M01_BombaPrincipal.Estado.xEnMarcha,
    xReset        := "DB_HMI".xResetHorasBombaM01,
    rUmbralAviso  := 8000.0,                                         // aviso a las 8000h
    rHoras        := "DB_Equipos".M01_BombaPrincipal.Diagnostico.rHorasFuncionamiento,
    qAvisoMantenimiento => "DB_HMI".xMantBombaM01
);
```

---

## Lógica resumida

1. Mientras `xRunning = TRUE`, el FB acumula `tCiclo` en `rAcumuladorMs`.
2. Cada vez que `rAcumuladorMs >= 3_600_000` (1 hora en ms), incrementa `rHoras += 1.0` y resta los ms acumulados.
3. Si `rHoras >= rUmbralAviso` y `rUmbralAviso > 0.0` → `qAvisoMantenimiento := TRUE`.
4. Flanco de subida en `xReset` → `rHoras := 0.0`, `rAcumuladorMs := 0.0`.

---

## Notas / Limitaciones conocidas

- `rHoras` debe declararse en un DB con la flag **Retain** activa para sobrevivir a un corte de tensión.
- La precisión es de ~1 hora (no fracciones). Si necesitas medio o cuarto de hora, ajusta el divisor a 1_800_000 o 900_000.
- Si `tCiclo` del PLC es muy alto (>100ms) hay deriva acumulativa; para precisión más fina usa `RD_SYS_T` y resta timestamps en lugar de acumular `tCiclo`.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
