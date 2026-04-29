# 📦 TIA Portal Library — El "Awesome" de la Automatización con Siemens

[![License: MIT](https://img.shields.io/github/license/iagorobo24-hub/awesome-tia-portal?color=blue)](./LICENSE)
[![TIA Portal](https://img.shields.io/badge/TIA%20Portal-V20-009999?logo=siemens&logoColor=white)](#-versión-de-tia-portal)
[![PLC](https://img.shields.io/badge/PLC-S7--1200%20%2F%20S7--1500-orange)](#-versión-de-tia-portal)
[![Last commit](https://img.shields.io/github/last-commit/iagorobo24-hub/awesome-tia-portal)](https://github.com/iagorobo24-hub/awesome-tia-portal/commits/main)
[![Issues](https://img.shields.io/github/issues/iagorobo24-hub/awesome-tia-portal)](https://github.com/iagorobo24-hub/awesome-tia-portal/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)
[![Awesome](https://awesome.re/badge.svg)](https://github.com/topics/awesome)

Colección organizada de bloques, tipos de datos, plantillas y recursos reutilizables para **Siemens TIA Portal V20**, mantenida por la comunidad.

> **Sin programas completos. Sin proyectos enteros.** Solo piezas útiles, bien documentadas y listas para usar (Plug & Play).

---

## 📑 Tabla de contenido

- [¿Por qué este repositorio?](#-por-qué-este-repositorio)
- [Recursos destacados](#-recursos-destacados-empieza-por-aquí)
- [Contenido del repositorio](#-contenido-del-repositorio)
- [Cómo usar un recurso](#-cómo-usar-un-recurso)
- [¿Quieres aportar?](#-quieres-aportar-es-más-fácil-de-lo-que-parece)
- [Versión de TIA Portal](#-versión-de-tia-portal)
- [Licencia](#-licencia)

---

## 🚀 ¿Por qué este repositorio?

En el mundo de la automatización, a menudo reinventamos la rueda. Cada programador tiene su propia librería de "bloques útiles" guardada en su disco duro.

**TIA Portal Library** nace para:
- **Centralizar el conocimiento**: Un lugar común para encontrar ese bloque de escalado o ese UDT de motor que todos necesitamos.
- **Estandarizar**: Facilitar que otros técnicos entiendan tu código usando piezas comunes y bien documentadas.
- **Aprender**: Ver cómo otros resuelven problemas comunes en SCL o Ladder.

---

## ⭐ Recursos destacados — empieza por aquí

Si vas a usar el repo por primera vez, estos son los recursos fundacionales sobre los que se construye todo lo demás. Empieza por los UDTs, sigue por el FC de escalado, y luego añade los FBs y faceplates que necesites:

| | Recurso | Qué hace |
|:---:|---|---|
| 🏷️ | [`UDT_Motor`](./tipos-de-datos/udt-motor/) | Estructura estándar para control y diagnóstico de motor digital |
| 🏷️ | [`UDT_AnalogInput`](./tipos-de-datos/udt-analog-input/) | Entrada analógica con escalado, alarmas HH/H/L/LL y simulación |
| 🧩 | [`FC_Escalado`](./bloques-de-funcion/fc-escalado/) | Escalado lineal genérico INT (0-27648) → REAL en unidades de ingeniería |
| 🧩 | [`FB_Motor`](./bloques-de-funcion/fb-motor/) | Control digital de motor — consume `UDT_Motor`, gestiona manual/auto, timeouts y horas |
| 🖥️ | [`Faceplate_Motor`](./hmi/faceplate-motor/) | Faceplate HMI vinculado a `UDT_Motor` con un único *binding* |
| 🏗️ | [`OB1_Plantilla`](./bloques-de-organizacion/ob1-plantilla/) | Esqueleto de OB1 con secciones estándar (lectura → seguridad → lógica → diagnóstico → escritura) |

> 👉 **Para ver todos los recursos disponibles, planificados y su estado, consulta el [📚 catálogo completo](./CATALOG.md).**

---

## 📂 Contenido del repositorio

| Carpeta | Recurso | Qué contiene |
|---|---|---|
| 🧩 | [`/bloques-de-funcion`](./bloques-de-funcion/) | FBs y FCs (Escalados, control de motores, alarmas...) |
| 🏷️ | [`/tipos-de-datos`](./tipos-de-datos/) | UDTs reutilizables para estructuras de datos limpias |
| 🏗️ | [`/bloques-de-organizacion`](./bloques-de-organizacion/) | OBs con arquitecturas base y gestión de ciclos |
| 🖥️ | [`/hmi`](./hmi/) | Pantallas, faceplates y recursos visuales |
| 📋 | [`/plantillas-de-proyecto`](./plantillas-de-proyecto/) | Estructuras base para empezar proyectos desde cero |

---

## 🛠️ Cómo usar un recurso

1. **Explora**: Entra en la carpeta que te interesa.
2. **Lee**: Revisa el `README.md` del recurso — ahí verás qué hace, sus entradas/salidas y cómo usarlo.
3. **Descarga**: Bájate el archivo `.xml`.
4. **Importa**: En TIA Portal: `Clic derecho en "Bloques de programa" → Importar`.

---

## 🤝 ¿Quieres aportar? (Es más fácil de lo que parece)

**¿Tienes un bloque que usas en todos tus proyectos?** ¡Compártelo!

No hace falta ser un experto en GitHub. Hemos preparado una [guía de contribución paso a paso](./CONTRIBUTING.md) pensada para gente que viene del mundo del PLC. Si prefieres no usar comandos, puedes abrir un [Issue](../../issues) y subir tu archivo ahí.

---

## ⚠️ Versión de TIA Portal

Este repo está optimizado para **TIA Portal V20**.
*Nota: Muchos recursos funcionan en V18/V19, revisa la descripción individual de cada bloque.*

---

## 📜 Licencia

MIT — Puedes usar, modificar y distribuir libremente en tus proyectos industriales. Ver [LICENSE](./LICENSE).
