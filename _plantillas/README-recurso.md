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

### Estáticas (Static) — solo para FBs

| Variable | Tipo | Descripción |
|---|---|---|
| *(vacío si no aplica)* | — | — |

---

## Cómo importarlo en TIA Portal

1. Descarga el archivo `nombre-del-recurso.xml`
2. En TIA Portal, abre tu proyecto
3. En el árbol del proyecto, clic derecho sobre **Bloques de programa**
4. Selecciona **Importar**
5. Busca el `.xml` descargado y confirma

El bloque aparecerá en tu árbol listo para usar.

---

## Ejemplo de uso

Describe brevemente cómo se instancia y conecta. Puedes poner una captura de pantalla si tienes.

```
Instancia del FB: "EscaladoSensor_PH"
  iValorCrudo  ← MW100  (valor raw del canal AI0)
  rMinEscala   ← 0.0    (pH mínimo)
  rMaxEscala   ← 14.0   (pH máximo)
  rValorEscalado → MD200 (valor en pH)
```

---

## Notas / Limitaciones conocidas

- El bloque asume que el rango del módulo analógico está configurado en 0-10V (0-27648)
- Para rangos 4-20mA (6912-27648) habría que ajustar el valor mínimo de entrada

---

## Autor

**GitHub:** [@tu-usuario](https://github.com/tu-usuario)  
*(El campo autor es opcional — puedes dejarlo en blanco si prefieres)*
