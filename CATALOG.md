# 📚 Catálogo de recursos

Índice unificado de todo el contenido del repositorio. Para encontrar rápido lo que necesitas sin tener que abrir cada carpeta.

> **¿Buscas el flujo de cómo aportar un recurso?** Está en [`CONTRIBUTING.md`](./CONTRIBUTING.md). Este fichero es solo el índice.

---

## Leyenda de estados

| Símbolo | Significado |
|:---:|---|
| ✅ | **Disponible** — README + `.xml` exportados, listo para importar |
| 📝 | **Solo documentado** — el diseño/README está, falta el `.xml` |
| ⏳ | **Planificado** — recurso identificado como necesario, sin empezar |

---

## 🏷️ Tipos de datos (UDT)

> Carpeta: [`tipos-de-datos/`](./tipos-de-datos/)

| Estado | Recurso | Descripción | TIA Portal | Familia PLC |
|:---:|---|---|:---:|:---:|
| 📝 | [`udt-motor`](./tipos-de-datos/udt-motor/) | Estructura estándar para control y diagnóstico de motor digital (Comando / Estado / Fallos / Diagnóstico / Config) | V20 | 1200 / 1500 |
| ⏳ | `udt-analog-input` | Entrada analógica con raw, escalado, alarmas HH/H/L/LL, calidad y unidades | — | — |
| ⏳ | `udt-valve` | Válvula digital (abrir/cerrar) con feedback y timeout | — | — |
| ⏳ | `udt-drive` | Variador de frecuencia (consigna, realimentación, fallos típicos) | — | — |
| ⏳ | `udt-alarm` | Alarma con activación, ack, timestamp y prioridad | — | — |

---

## 🧩 Bloques de función (FB / FC)

> Carpeta: [`bloques-de-funcion/`](./bloques-de-funcion/)

| Estado | Recurso | Descripción | TIA Portal | Familia PLC |
|:---:|---|---|:---:|:---:|
| ⏳ | `fc-escalado` | Escalado lineal genérico INT (0-27648) → REAL (min-max ingeniería) | — | — |
| ⏳ | `fb-motor` | Control digital de motor — consume `UDT_Motor`, gestiona manual/auto, timeouts, contador horas | — | — |
| ⏳ | `fb-analog-input` | Procesado de entrada analógica — consume `UDT_AnalogInput`, escalado + alarmas + filtrado + simulación | — | — |
| ⏳ | `fb-valve` | Control de válvula con feedback y timeout | — | — |
| ⏳ | `fb-hourmeter` | Contador de horas con persistencia | — | — |
| ⏳ | `fb-edge-counter` | Contador de flancos con reset | — | — |
| ⏳ | `fb-pulse-gen` | Generador de pulsos parametrizable (Hz o periodo) | — | — |

---

## 🏗️ Bloques de organización (OB)

> Carpeta: [`bloques-de-organizacion/`](./bloques-de-organizacion/)

| Estado | Recurso | Descripción | TIA Portal | Familia PLC |
|:---:|---|---|:---:|:---:|
| ⏳ | `ob1-plantilla` | OB1 con secciones comentadas (entradas, lógica, salidas, diagnóstico) | — | — |
| ⏳ | `ob100-startup` | OB de arranque con inicialización típica | — | — |
| ⏳ | `ob82-85-86-errores` | Gestión básica de errores de hardware (diagnóstico, fallo módulo, fallo rack) | — | — |

---

## 🖥️ HMI

> Carpeta: [`hmi/`](./hmi/)

| Estado | Recurso | Descripción | TIA Portal | Panel |
|:---:|---|---|:---:|:---:|
| ⏳ | `faceplate-motor` | Faceplate vinculado a `UDT_Motor` | — | Comfort / Unified |
| ⏳ | `faceplate-valve` | Faceplate de válvula | — | Comfort / Unified |
| ⏳ | `faceplate-analog` | Faceplate de variable analógica con alarmas | — | Comfort / Unified |
| ⏳ | `pantalla-alarmas` | Pantalla base de alarmas con filtros | — | Comfort / Unified |
| ⏳ | `plantilla-navegacion` | Header + footer + área de contenido reutilizable | — | Comfort / Unified |

---

## 📋 Plantillas de proyecto

> Carpeta: [`plantillas-de-proyecto/`](./plantillas-de-proyecto/)

| Estado | Recurso | Descripción | TIA Portal | Familia PLC |
|:---:|---|---|:---:|:---:|
| ⏳ | `plantilla-maquina-simple` | 1 PLC + 1 HMI Basic, estructura mínima | — | 1200 |
| ⏳ | `plantilla-linea-modular` | Varios PLCs comunicados, librerías compartidas | — | 1500 |

---

## 🛣️ Roadmap por orden recomendado

El orden sugerido para ir rellenando el repo (cada pieza apoya a la siguiente):

1. **UDTs base** — `udt-motor`, `udt-analog-input`, `udt-valve`, `udt-drive`, `udt-alarm`
2. **FC de escalado** — `fc-escalado` (validación end-to-end del flujo)
3. **FBs que consumen los UDTs** — `fb-motor`, `fb-analog-input`, `fb-valve`, `fb-hourmeter`...
4. **OBs base** — `ob1-plantilla`, `ob100-startup`, `ob82-85-86-errores`
5. **HMI** — faceplates vinculados a los UDTs
6. **Plantillas de proyecto** — una vez hay piezas suficientes que referenciar

---

## ➕ ¿Cómo añadir tu recurso a este catálogo?

Cuando subas un recurso nuevo:

1. En la PR, edita este `CATALOG.md` y añade/actualiza la fila correspondiente.
2. Cambia el estado a ✅ si subes README + `.xml`, o a 📝 si solo subes README.
3. Rellena las columnas TIA Portal y PLC con las versiones que has probado.

Si tu recurso encaja en una nueva sub-categoría que no existe, abre un [Issue](../../issues/new/choose) antes para discutirlo.
