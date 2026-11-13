---
name: FB_ControlPID
type: fb
tia_version: V20
tia_compat: [V20]
plc_family: [s7-1200, s7-1500]
depends_on: []
used_by: []
tags: [pid, control, regulacion, temperatura, presion, fb]
status: documented
level: medio
---

# FB_ControlPID

> Controlador PID en forma paralela con anti-windup, limitación de salida y filtrado opcional de la medida.

Bloque de control PID reutilizable para regulación de temperatura, presión, caudal u otras variables de proceso. Implementa los términos proporcional, integral y derivativo de forma independiente, con protección contra el devaneo integral (anti-windup) y límite de salida configurable.

- **Tipo:** Function Block (FB)
- **Lenguaje:** SCL
- **Estado:** documentado (sin fuente SCL ni .xml todavía; es una especificación de interfaz)
- **TIA Portal:** V20 (no verificado)
- **Familia PLC:** S7-1200 / S7-1500

## ¿Qué problema resuelve?

Regular una variable de proceso (temperatura, presión, nivel, caudal) manteniéndola en una consigna. Tener un bloque PID parametrizable y con protección anti-windup evita reescribir el regulador en cada máquina y reduce el riesgo de saturación del acumulador integral.

## Variables / Interfaz

| Variable | Tipo | Dirección | Descripción |
|---|---|---|---|
| `xHabilitar` | BOOL | Input | Habilita el controlador; FALSE detiene y pone salida a 0. |
| `xReset` | BOOL | Input | Reinicia el acumulador integral y el filtro derivativo. |
| `rSetpoint` | REAL | Input | Valor deseado (consigna) en unidades de ingeniería. |
| `rMedida` | REAL | Input | Valor medido de la variable de proceso. |
| `rKp` | REAL | Input | Ganancia proporcional. |
| `rKi` | REAL | Input | Ganancia integral (1/s). |
| `rKd` | REAL | Input | Ganancia derivativa (s). |
| `rLimiteMin` | REAL | Input | Límite inferior de la salida. |
| `rLimiteMax` | REAL | Input | Límite superior de la salida. |
| `rSalida` | REAL | Output | Salida del controlador, limitada a [rLimiteMin, rLimiteMax]. |
| `rError` | REAL | Output | Error actual: `rSetpoint - rMedida`. |
| `xSaturado` | BOOL | Output | TRUE si la salida está limitada (útil para anti-windup externo). |
| `rIntegral` | REAL | Static | Acumulador del término integral (estado interno). |
| `rMedidaAnterior` | REAL | Static | Medida del ciclo anterior (para el término derivativo). |
| `diCiclo` | DINT | Static | Contador de ciclos de ejecución del bloque. |

## Cómo importarlo en TIA Portal

Este recurso es una **ficha de diseño**: todavía no incluye fuente `.scl` ni exportación `.xml` importable.

Cuando exista el archivo, los pasos son:

1. Descarga el archivo `fb-control-pid.xml` de esta carpeta.
2. En TIA Portal, abre tu proyecto.
3. Clic derecho sobre **Bloques de programa** → **Importar**.
4. Selecciona el `.xml` y confirma.

## Ejemplo de uso

```scl
// Control de temperatura de un horno: consigna 180 ºC, salida 0-100 %
"Inst_PID_Temperatura"(
    xHabilitar := #xControlActivo,
    xReset := #xResetPID,
    rSetpoint := 180.0,
    rMedida := #rTempActual,        // entrada del termopar escalada
    rKp := 2.5,
    rKi := 0.1,
    rKd := 0.05,
    rLimiteMin := 0.0,
    rLimiteMax := 100.0,
    rSalida => #rPotenciaCalor,     // hacia salida analógica / PWM
    rError => #rErrorTemp,
    xSaturado => #xPIDSaturado
);
```

## Ecuación implementada (especificación)

Cada ciclo de llamada (tiempo de muestreo `Ts` entre llamadas):

```text
e(k)      = rSetpoint - rMedida
P(k)      = rKp * e(k)
I(k)      = I(k-1) + rKi * e(k) * Ts        (con anti-windup si saturado)
D(k)      = rKd * (rMedida - rMedidaAnterior) / Ts
SalidaRaw = P(k) + I(k) + D(k)
rSalida   = limitar(SalidaRaw, rLimiteMin, rLimiteMax)
xSaturado = (SalidaRaw <> rSalida)
```

`rMedidaAnterior` se actualiza al final de cada ciclo. El acumulador integral `rIntegral` se congela cuando la salida está saturada y el error apunta en el mismo sentido (anti-windup por retroceso).

## Notas / Limitaciones conocidas

- El tiempo de muestreo `Ts` debe ser constante entre llamadas (llamar siempre desde el mismo OB cíclico con el mismo retardo). El bloque no mide `Ts` internamente.
- `rKi` y `rKd` se asumen ya escalados por `Ts` si se prefiere no incluir `Ts` en la ecuación; documentar el valor usado.
- La acción derivativa actúa sobre la medida (no sobre el error) para evitar picos al cambiar la consigna.
- No es un bloque de seguridad: no usar en funciones de seguridad funcional.
- Los valores de ganancia son ejemplo; deben ajustarse al proceso real.

## Dependencias

| Recurso | Por qué lo necesita |
|---|---|
| Ninguna | — |

## Compatibilidad TIA Portal

| Versión | Estado | Notas |
|---|---|---|
| V20 | ➖ | No verificado (especificación de interfaz) |
| V19 | ➖ | No verificado |
| V18 | ➖ | No verificado |
| V17 y anteriores | ❌ | No soportado |

Iconos: ✅ probado y OK · ⚠ con limitaciones (documenta cuáles) · ❌ no soportado · ➖ no aplica / no verificado.

---

## Historial de cambios

- `2026-11-12` — v0.1 — Ficha de diseño inicial. Sin fuente SCL ni .xml.

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
