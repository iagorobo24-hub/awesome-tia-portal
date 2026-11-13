---
name: FB_SecuenciadorPasos
type: fb
tia_version: V20
tia_compat: [V20]
plc_family: [s7-1200, s7-1500]
depends_on: []
used_by: []
tags: [secuenciador, pasos, receta, secuencia, fb]
status: documented
level: medio
---

# FB_SecuenciadorPasos

> Secuenciador de hasta 16 pasos con condición de avance por paso, paso actual, paso total y reset.

Este bloque ejecuta una secuencia ordenada de pasos. Cada paso avanza al siguiente cuando su condición asociada es TRUE. Sirve para ciclos de máquina, recetas simples o secuencias de arranque/parada.

- **Tipo:** Function Block (FB)
- **Lenguaje:** SCL
- **Estado:** documentado (sin fuente SCL ni .xml todavía; es una especificación de interfaz)
- **TIA Portal:** V20 (no verificado)
- **Familia PLC:** S7-1200 / S7-1500

## ¿Qué problema resuelve?

Muchas máquinas deben ejecutar una serie ordenada de acciones (paso 1: llenar, paso 2: calentar, paso 3: mezclar, paso 4: vaciar…). Tener un secuenciador reutilizable evita programar el control de paso actual y las condiciones de salto desde cero en cada proyecto.

## Variables / Interfaz

| Variable | Tipo | Dirección | Descripción |
|---|---|---|---|
| `xInicio` | BOOL | Input | Arranca la secuencia desde el paso 1. |
| `xPausa` | BOOL | Input | Congela el avance de pasos (mantiene el paso actual). |
| `xReset` | BOOL | Input | Vuelve al paso 0 (inactivo) y detiene la secuencia. |
| `abCondicionPaso` | ARRAY[1..16] OF BOOL | Input | Condición de avance de cada paso (uno por paso). |
| `iPasoActual` | INT | Output | Número del paso en curso (0 = inactivo, 1..16 = activo). |
| `iPasoTotal` | INT | Output | Último paso alcanzado (máximo alcanzado). |
| `xSecuenciaActiva` | BOOL | Output | TRUE si hay un paso en curso (1..16). |
| `xSecuenciaCompleta` | BOOL | Output | Pulso de un ciclo cuando se completa el paso 16. |
| `diCicloPaso` | DINT | Static | Contador de ciclos en el paso actual (se resetea al cambiar). |

## Cómo importarlo en TIA Portal

Este recurso es una **ficha de diseño**: todavía no incluye fuente `.scl` ni exportación `.xml` importable.

Cuando exista el archivo, los pasos son:

1. Descarga el archivo `fb-secuenciador-pasos.xml` de esta carpeta.
2. En TIA Portal, abre tu proyecto.
3. Clic derecho sobre **Bloques de programa** → **Importar**.
4. Selecciona el `.xml` y confirma.

## Ejemplo de uso

```scl
// Instancia y llamada típica desde OB1
"Inst_Secuenciador"(
    xInicio := #xCicloAuto,
    xPausa := #xPausaOperador,
    xReset := #xResetSecuencia,
    abCondicionPaso[1] := #xTanqueLleno,          // fin paso 1
    abCondicionPaso[2] := #xTemperaturaAlcanzada, // fin paso 2
    abCondicionPaso[3] := #xMezcladoTerminado,    // fin paso 3
    abCondicionPaso[4] := #xValvulaAbierta,       // fin paso 4
    iPasoActual => #iPasoEnCurso,
    iPasoTotal => #iPasoMaxAlcanzado,
    xSecuenciaActiva => #xSecuenciaMarcha,
    xSecuenciaCompleta => #xCicloTerminado
);
```

## Lógica de avance propuesta (especificación)

Cada ciclo, si `xReset` es FALSE:

1. Si `xInicio` y la secuencia está inactiva (`iPasoActual = 0`), se activa el paso 1.
2. Si `xPausa` es TRUE, se mantiene el paso actual sin avanzar.
3. Si `abCondicionPaso[iPasoActual]` es TRUE, se avanza a `iPasoActual + 1`.
4. Al completar el paso 16, `xSecuenciaCompleta` se pone TRUE un ciclo y la secuencia se detiene (`iPasoActual = 16`, `xSecuenciaActiva = FALSE`).

`diCicloPaso` cuenta los ciclos en el paso actual y se resetea a 0 al cambiar de paso.

## Notas / Limitaciones conocidas

- Máximo 16 pasos (1..16). Para más pasos, ampliar `abCondicionPaso` y ajustar los límites.
- `xSecuenciaCompleta` es un pulso de un ciclo: capturarlo en una borda si se usa para disparar otra acción.
- No incluye temporizadores ni retenciones entre pasos: usar condiciones de entrada (por ejemplo, salida de un `TON`) para temporizar.
- No es un bloque de seguridad: no usar en funciones de seguridad funcional.

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
