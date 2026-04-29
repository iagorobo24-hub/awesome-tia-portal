# 📚 Catálogo de recursos

Índice unificado de todo el contenido del repositorio. Para encontrar rápido lo que necesitas sin tener que abrir cada carpeta.

> **Este archivo se genera automáticamente** a partir del frontmatter YAML de cada README de recurso.
> No lo edites a mano: ejecuta `python3 scripts/generate_catalog.py` después de añadir o modificar un recurso.
> El flujo de cómo aportar un recurso está en [`CONTRIBUTING.md`](./CONTRIBUTING.md).

---

## Leyenda de estados

| Símbolo | Significado |
|:---:|---|
| ✅ | **Disponible** — README + `.xml` exportados, listo para importar |
| 📝 | **Solo documentado** — el diseño/README está, falta el `.xml` |
| ⚙️ | **En curso** — recurso identificado y en desarrollo |
| ⏳ | **Planificado** — recurso identificado como necesario, sin empezar |

---


## 🏷️ Tipos de datos (UDT)

> Carpeta: [`tipos-de-datos/`](./tipos-de-datos/)

| Estado | Recurso | Descripción | TIA Portal | Familia PLC |
|:---:|---|---|:---:|:---:|
| 📝 | [`udt-alarm`](./tipos-de-datos/udt-alarm/) | Estructura unificada para una alarma — activación, reconocimiento, timestamp, prioridad y texto descriptivo. | V20 | 1200 / 1500 |
| 📝 | [`udt-analog-input`](./tipos-de-datos/udt-analog-input/) | Estructura unificada para el procesamiento de una entrada analógica: valor raw, escalado a unidades de ingeniería, alarmas HH/H/L/LL y diagnóstico. | V20 | 1200 / 1500 |
| 📝 | [`udt-drive`](./tipos-de-datos/udt-drive/) | Estructura unificada para variadores de frecuencia (VFD) — comando, lectura, fallos comunes y configuración base. | V20 | 1200 / 1500 |
| 📝 | [`udt-motor`](./tipos-de-datos/udt-motor/) | Estructura unificada para el control y diagnóstico de un motor digital (marcha/paro con confirmación física). | V20 | 1200 / 1500 |
| 📝 | [`udt-valve`](./tipos-de-datos/udt-valve/) | Estructura unificada para válvulas digitales (todo/nada) con feedback de posición y vigilancia de timeout. | V20 | 1200 / 1500 |

---

## 🧩 Bloques de función (FB / FC)

> Carpeta: [`bloques-de-funcion/`](./bloques-de-funcion/)

| Estado | Recurso | Descripción | TIA Portal | Familia PLC |
|:---:|---|---|:---:|:---:|
| 📝 | [`fb-analog-input`](./bloques-de-funcion/fb-analog-input/) | Bloque de procesado de entrada analógica — escalado, filtrado pasa-baja, alarmas HH/H/L/LL con histéresis, y simulación. | V20 | 1200 / 1500 |
| 📝 | [`fb-edge-counter`](./bloques-de-funcion/fb-edge-counter/) | Contador de flancos de subida con reset y configuración de límite — útil para contar ciclos de máquina, piezas producidas, paradas… | V20 | 1200 / 1500 |
| 📝 | [`fb-hourmeter`](./bloques-de-funcion/fb-hourmeter/) | Contador de horas de funcionamiento — acumula el tiempo en el que su entrada está activa, con persistencia entre cortes de tensión. | V20 | 1200 / 1500 |
| 📝 | [`fb-motor`](./bloques-de-funcion/fb-motor/) | Bloque de control digital de motor — gestiona marcha/paro, modo manual/auto, vigilancia de feedback con timeout, contador de horas y arranques. | V20 | 1200 / 1500 |
| 📝 | [`fb-pulse-gen`](./bloques-de-funcion/fb-pulse-gen/) | Generador de pulsos parametrizable — produce un tren de pulsos con periodo y duty cycle configurables. Útil para parpadeos, refresco, tests, etc. | V20 | 1200 / 1500 |
| 📝 | [`fb-valve`](./bloques-de-funcion/fb-valve/) | Bloque de control de válvula digital — gestiona apertura/cierre, modo manual/auto, vigilancia de feedback con timeout, detección de posición inválida. | V20 | 1200 / 1500 |
| 📝 | [`fc-escalado`](./bloques-de-funcion/fc-escalado/) | Escalado lineal genérico de un INT raw (0-27648) a un REAL en unidades de ingeniería. | V20 | 1200 / 1500 |

---

## 🏗️ Bloques de organización (OB)

> Carpeta: [`bloques-de-organizacion/`](./bloques-de-organizacion/)

| Estado | Recurso | Descripción | TIA Portal | Familia PLC |
|:---:|---|---|:---:|:---:|
| 📝 | [`ob1-plantilla`](./bloques-de-organizacion/ob1-plantilla/) | Esqueleto de OB1 (`Main`) con secciones comentadas y orden de ejecución estándar — para no empezar de cero en cada proyecto. | V20 | 1200 / 1500 |
| 📝 | [`ob100-startup`](./bloques-de-organizacion/ob100-startup/) | OB de arranque (`Startup`) con inicialización típica: textos de alarmas, configuración de equipos, valores por defecto. | V20 | 1200 / 1500 |
| 📝 | [`ob82-85-86-errores`](./bloques-de-organizacion/ob82-85-86-errores/) | Plantillas de los OBs de **diagnóstico, fallo de programa y fallo de rack** con gestión básica de eventos: registro, alarma y modo seguro. | V20 | 1500 |

---

## 🖥️ HMI

> Carpeta: [`hmi/`](./hmi/)

| Estado | Recurso | Descripción | TIA Portal | Panel |
|:---:|---|---|:---:|:---:|
| 📝 | [`faceplate-analog`](./hmi/faceplate-analog/) | Faceplate HMI vinculado a `UDT_AnalogInput` — muestra valor con unidad, alarmas HH/H/L/LL, mín/máx y permite forzado/simulación. | V20 | Comfort / Unified |
| 📝 | [`faceplate-motor`](./hmi/faceplate-motor/) | Faceplate HMI vinculado a `UDT_Motor` — pop-up con comandos manuales, indicadores de estado, lista de fallos y métricas. | V20 | Comfort / Unified |
| 📝 | [`faceplate-valve`](./hmi/faceplate-valve/) | Faceplate HMI vinculado a `UDT_Valve` — pop-up con comandos abrir/cerrar manual, indicadores de posición, lista de fallos y diagnóstico. | V20 | Comfort / Unified |
| 📝 | [`pantalla-alarmas`](./hmi/pantalla-alarmas/) | Pantalla HMI base de gestión de alarmas — listado activo, histórico, filtros por prioridad/fuente y reconocimiento individual o masivo. | V20 | Comfort / Unified |
| 📝 | [`plantilla-navegacion`](./hmi/plantilla-navegacion/) | Plantilla maestra (header + footer + área de contenido) reutilizable en todas las pantallas del proyecto — con barra de alarmas, login de usuario, navegación principal y indicadores de estado. | V20 | Comfort / Unified |

---

## 📋 Plantillas de proyecto

> Carpeta: [`plantillas-de-proyecto/`](./plantillas-de-proyecto/)

| Estado | Recurso | Descripción | TIA Portal | Familia PLC |
|:---:|---|---|:---:|:---:|
| 📝 | [`plantilla-linea-modular`](./plantillas-de-proyecto/plantilla-linea-modular/) | Estructura base para una línea industrial con **varios PLCs S7-1500 comunicados** entre sí y un HMI Unified central. Pensada para escalar y compartir librerías entre PLCs. | V20 | 1500 |
| 📝 | [`plantilla-maquina-simple`](./plantillas-de-proyecto/plantilla-maquina-simple/) | Estructura base de proyecto TIA Portal para una máquina sencilla: **un PLC S7-1200 + un HMI Basic/Comfort pequeño**. Carpetas, convenciones de nombres y bloques vacíos listos para rellenar. | V20 | 1200 |

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

1. Crea tu carpeta de recurso copiando [`_plantillas/README-recurso.md`](./_plantillas/README-recurso.md) y rellena el frontmatter YAML.
2. Ejecuta `python3 scripts/generate_catalog.py` desde la raíz del repo. Esto regenera **este** archivo automáticamente.
3. Commitea los dos cambios (tu recurso + el `CATALOG.md` actualizado) en la misma PR.
4. CI verificará que `CATALOG.md` esté sincronizado: si no lo está, fallará con instrucciones.
