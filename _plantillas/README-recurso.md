---
# Plantilla de README para un recurso del repo.
# Copia este archivo en tu carpeta nueva (ej: tipos-de-datos/udt-mi-recurso/README.md)
# y rellena cada sección. Borra estos comentarios y las explicaciones en cursiva cuando termines.
# Lee primero la guía de estilo: ../STYLE.md
#
# IMPORTANTE: este bloque YAML (entre las dos líneas de tres guiones) debe
# quedar SIEMPRE en la primera línea del archivo, para que GitHub y los
# scripts del repo lo parseen correctamente.
name: NombreDelBloqueEnTIA          # Ej: UDT_Motor, FB_Motor, FC_Escalado, Faceplate_Motor
type: udt                            # udt | fb | fc | ob | hmi-faceplate | hmi-pantalla | plantilla
tia_version: V20                     # Versión principal de desarrollo
tia_compat: [V18, V19, V20]          # Versiones donde se ha probado (ver sección Compatibilidad)
plc_family: [s7-1500]                # s7-1200 | s7-1500 | ambas
hmi_panel: []                        # Solo si type es hmi-*: comfort | unified | basic
depends_on: []                       # Otras carpetas del repo que necesita: ["tipos-de-datos/udt-motor"]
used_by: []                          # Otros recursos que lo consumen: ["bloques-de-funcion/fb-motor"]
tags: [motor, control]               # Etiquetas libres para búsqueda
status: documented                   # documented | available | wip
---

# [Nombre del recurso]

> Una línea que explique qué hace. Sin rodeos.

**Tipo:** `Bloque de función (FB)` / `Función (FC)` / `UDT` / `OB` / `HMI`  
**Versión TIA Portal:** V20 *(también probado en: V18, V19 — elimina si no aplica)*  
**Familia PLC:** S7-1200 / S7-1500 / ambas

---

## ¿Qué problema resuelve?

Explica en 2-4 frases el problema concreto que resuelve este recurso. Sin tecnicismos innecesarios.

Ejemplo:
> Cuando se trabaja con entradas analógicas en formato 0-27648, es necesario convertir ese valor crudo a la unidad de ingeniería real (ºC, bar, m³/h...). Este bloque hace esa conversión de forma parametrizable sin tener que recalcular cada vez.

---

## Variables / Interfaz

> **Naming**: usa los prefijos definidos en [`STYLE.md` § 3](../STYLE.md#3-naming-de-variables-prefijos-húngaros). En resumen: `x` BOOL, `i` INT, `di` DINT, `r` REAL, `s` STRING, `t` TIME, `dt` DTL, `q` (BOOL outputs), `ton`/`tof`/`rtrig`/`ftrig` para instancias de FB estándar.

### Entradas (Input)

| Variable | Tipo | Descripción |
|---|---|---|
| `iValorCrudo` | INT | Valor raw de la entrada analógica (0-27648) |
| `rMinEscala` | REAL | Valor mínimo de la escala de ingeniería |
| `rMaxEscala` | REAL | Valor máximo de la escala de ingeniería |

### Salidas (Output)

| Variable | Tipo | Descripción |
|---|---|---|
| `rValorEscalado` | REAL | Valor convertido a la unidad de ingeniería |

### InOut — solo si aplica

| Variable | Tipo | Descripción |
|---|---|---|
| *(vacío si no aplica)* | — | — |

### Estáticas (Static) — solo para FBs

| Variable | Tipo | Descripción |
|---|---|---|
| *(vacío si no aplica)* | — | — |

---

## Cómo importarlo en TIA Portal

1. Descarga el archivo `nombre-del-recurso.xml` de esta carpeta.
2. En TIA Portal, abre tu proyecto.
3. En el árbol del proyecto, clic derecho sobre **Bloques de programa** (o **Tipos de datos PLC** si es un UDT).
4. Selecciona **Importar**.
5. Busca el `.xml` descargado y confirma.

El bloque aparecerá en tu árbol listo para usar.

---

## Ejemplo de uso

Describe brevemente cómo se instancia y conecta. Si tienes una captura, añádela en la sección "Capturas".

```scl
// Llamada típica en OB1 / FB padre
"Instancia_Escalado_pH"(
    iValorCrudo := "TI01_Raw",       // %IW64
    rMinEscala  := 0.0,
    rMaxEscala  := 14.0,
    rValorEscalado => "TI01_pH"
);
```

---

## Cómo validarlo

Caso de prueba mínimo para comprobar que el recurso funciona tras importarlo:

1. **Setup**: crea una variable `iEntrada` (INT) en una DB temporal y otra `rSalida` (REAL).
2. **Estímulo**: pon `iEntrada = 13824` (mitad del rango 0-27648), `rMinEscala = 0.0`, `rMaxEscala = 14.0`.
3. **Resultado esperado**: `rSalida ≈ 7.0`.
4. **Casos de borde**:
   - `iEntrada = 0` → `rSalida = 0.0`
   - `iEntrada = 27648` → `rSalida = 14.0`
   - `iEntrada = -100` (fuera de rango) → comportamiento documentado (saturar a 0 o devolver valor extrapolado).

---

## Notas / Limitaciones conocidas

- El bloque asume que el rango del módulo analógico está configurado en 0-10V (0-27648).
- Para rangos 4-20mA (5530-27648) habría que ajustar `iRangoMinRaw` en la configuración.
- **No** valida la calidad del módulo (eso lo hace `FB_AnalogInput`).

---

## Dependencias

> Lista los recursos del propio repo que este bloque necesita para funcionar. Si no depende de nada, deja "Ninguna".

| Recurso | Por qué lo necesita |
|---|---|
| [`UDT_Motor`](../../tipos-de-datos/udt-motor/) | Estructura del motor que recibe como InOut |

---

## Compatibilidad TIA Portal

| Versión | Estado | Notas |
|---|:---:|---|
| V20 | ✅ | Versión de referencia |
| V19 | ✅ | Probado, idéntico |
| V18 | ⚠️ | Probado, pero el campo `xNuevoCampo` no aparece |
| V17 | ❌ | No soportado (UDTs anidados) |

> Iconos: ✅ probado y OK · ⚠️ con limitaciones (documenta cuáles) · ❌ no soportado · ➖ no aplica.

---

## Capturas / GIF

> Opcional pero **muy recomendado** para HMI y faceplates. Sube imágenes a esta misma carpeta y referéncialas con rutas relativas.

```markdown
![Faceplate del motor en runtime](./faceplate-motor.png)
```

---

## Historial de cambios

> Opcional al inicio. Útil a partir de la versión 1.1 cuando el recurso evolucione.

- `2026-04-29` — v1.0 — Versión inicial.

---

## Autor

**GitHub:** [@tu-usuario](https://github.com/tu-usuario)  
*(El campo autor es opcional — puedes dejarlo en blanco si prefieres)*
