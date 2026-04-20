# 📦 TIA Portal Library — El "Awesome" de la Automatización con Siemens

Colección organizada de bloques, tipos de datos, plantillas y recursos reutilizables para **Siemens TIA Portal V20**, mantenida por la comunidad.

> **Sin programas completos. Sin proyectos enteros.** Solo piezas útiles, bien documentadas y listas para usar (Plug & Play).

---

## 🚀 ¿Por qué este repositorio?

En el mundo de la automatización, a menudo reinventamos la rueda. Cada programador tiene su propia librería de "bloques útiles" guardada en su disco duro.

**TIA Portal Library** nace para:
- **Centralizar el conocimiento**: Un lugar común para encontrar ese bloque de escalado o ese UDT de motor que todos necesitamos.
- **Estandarizar**: Facilitar que otros técnicos entiendan tu código usando piezas comunes y bien documentadas.
- **Aprender**: Ver cómo otros resuelven problemas comunes en SCL o Ladder.

---

## 📂 Contenido del Recurso

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
