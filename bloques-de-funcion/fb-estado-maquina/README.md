---
name: FB_EstadoMaquina
type: fb
tia_version: V20
tia_compat: [V20]
plc_family: [s7-1200, s7-1500]
depends_on: []
used_by: []
tags: [maquina-de-estados, estado, secuenciador, fb]
status: documented
level: basico
---

# FB_EstadoMaquina

> Máquina de estados finita genérica con hasta 16 estados, transición condicionada por entradas y salida del estado activo.

Este bloque implementa una máquina de estados finita (FSM) sencilla y parametrizable. No depende de ningún otro recurso del repositorio, por lo que se puede importar y usar de forma independiente.

- **Tipo:** Function Block (FB)
- **Lenguaje:** SCL
- **Estado:** documentado (sin fuente SCL ni .xml todavía; es una especificación de interfaz)
- **TIA Portal:** V20 (no verificado)
- **Familia PLC:** S7-1200 / S7-1500

## ¿Qué problema resuelve?

En muchas máquinas y procesos se necesita pasar de un estado a otro según condiciones (sensores, temporizadores, comandos del operador). Tener una plantilla de máquina de estados reutilizable evita reescribir la misma lógica de salto de estados en cada proyecto.

## Variables / Interfaz

| Variable | Tipo | Dirección | Descripción |
|---|---|---|---|
| `xInicio` | BOOL | Input | Pone la máquina en el estado inicial (reset suave). |
| `xReset` | BOOL | Input | Fuerza retorno al estado 0 y detiene la máquina. |
| `iEstadoSiguiente` | INT | Input | Estado al que saltar si `xSaltar` es TRUE (0..15). |
| `xSaltar` | BOOL | Input | Ejecuta el salto forzado a `iEstadoSiguiente`. |
| `abCondicion` | ARRAY[0..15] OF BOOL | Input | Condición de transición de cada estado (una por estado). |
| `iEstadoActual` | INT | Output | Número del estado activo (0..15). |
| `xEstadoValido` | BOOL | Output | TRUE si `iEstadoActual` está en rango 0..15. |
| `xCambioEstado` | BOOL | Output | Pulso de un ciclo cuando cambia de estado. |
| `diCicloEstado` | DINT | Static | Contador de ciclos en el estado actual (se resetea al cambiar). |

## Cómo importarlo en TIA Portal

Este recurso es una **ficha de diseño**: todavía no incluye fuente `.scl` ni exportación `.xml` importable.

Cuando exista el archivo, los pasos son:

1. Descarga el archivo `fb-estado-maquina.xml` de esta carpeta.
2. En TIA Portal, abre tu proyecto.
3. Clic derecho sobre **Bloques de programa** → **Importar**.
4. Selecciona el `.xml` y confirma.

## Ejemplo de uso

```scl
// Instancia y llamada típica desde OB1
"Inst_EstadoMaquina"(
    xInicio := #xCicloAuto,
    xReset := #xParadaEmergencia,
    iEstadoSiguiente := 3,
    xSaltar := #xIrAEstado3,
    abCondicion[0] := #xSensorPiezaPresente,   // transición desde estado 0
    abCondicion[1] := #xTiempoEsperaTerminado, // transición desde estado 1
    abCondicion[2] := #xMotorAVelocidad,       // transición desde estado 2
    iEstadoActual => #iEstadoMaquina,
    xEstadoValido => #xEstadoOK,
    xCambioEstado => #xNuevoEstado
);
```

## Lógica de transición propuesta (especificación)

Cada ciclo, si `xReset` es FALSE:

1. Si `xInicio` y la máquina está en estado 0, se activa el estado 0.
2. Si `xSaltar` es TRUE, se pasa directamente a `iEstadoSiguiente`.
3. Si `abCondicion[iEstadoActual]` es TRUE, se avanza a `iEstadoActual + 1`.
4. Si se llega al estado 15, se permanece en 15 hasta un reset o salto.

`xCambioEstado` se pone TRUE durante un ciclo cuando el estado cambia.

## Notas / Limitaciones conocidas

- Máximo 16 estados (0..15). Para más estados, ampliar `abCondicion` y ajustar los límites.
- No incluye temporizadores internos: usa las condiciones de entrada para temporizar (por ejemplo, salida de un `TON` externo).
- No es un bloque de seguridad: no usar en funciones de parada de emergencia ni de seguridad funcional.
- El comportamiento de salida al entrar/salir de cada estado queda a cargo del bloque padre.

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
