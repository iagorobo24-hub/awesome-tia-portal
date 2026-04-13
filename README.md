# 📦 TIA Portal Library — Recursos abiertos para la comunidad

Colección organizada de bloques, tipos de datos, plantillas y recursos reutilizables para **Siemens TIA Portal V20**, mantenida por la comunidad.

> Sin programas completos. Sin proyectos enteros. Solo piezas útiles, bien documentadas y listas para usar.

---

## ¿Para qué sirve esto?

Cuando llevas tiempo trabajando con TIA Portal acabas acumulando pequeños bloques que resuelven problemas concretos — un temporizador con reset, un escalado de señal analógica, un control de marcha/paro con enclavamiento... Cosas que cualquiera vuelve a necesitar. El problema es que suelen quedarse en el disco duro de cada uno.

Este repo existe para cambiar eso: un sitio común donde esas piezas estén organizadas, explicadas y disponibles para cualquiera.

---

## Contenido

| Carpeta | Qué contiene |
|---|---|
| [`/bloques-de-funcion`](./bloques-de-funcion/) | FBs y FCs listos para importar |
| [`/tipos-de-datos`](./tipos-de-datos/) | UDTs reutilizables |
| [`/bloques-de-organizacion`](./bloques-de-organizacion/) | OBs con estructuras base |
| [`/hmi`](./hmi/) | Pantallas y recursos para Siemens HMI |
| [`/plantillas-de-proyecto`](./plantillas-de-proyecto/) | Estructuras base de proyecto |

---

## ¿Cómo usar un recurso?

1. Entra en la carpeta que te interesa
2. Lee el `README.md` del recurso — ahí está todo: qué hace, qué necesita y cómo importarlo
3. Descarga el archivo `.xml` correspondiente
4. En TIA Portal: `clic derecho en el árbol del proyecto → Importar`

---

## ¿Cómo contribuir?

**¿Tienes algo útil que quieras aportar?** Perfecto — lee la [guía de contribución](./CONTRIBUTING.md). Está escrita pensando en gente que igual no tiene mucha experiencia con GitHub, así que no hace falta ser experto.

Lo que buscamos: **piezas que resuelvan un problema concreto**, bien explicadas, sin código innecesario.

---

## Versión de TIA Portal

Este repo está orientado a **TIA Portal V20**. Si un recurso funciona también en versiones anteriores, se indica en su README.

---

## Licencia

MIT — puedes usar, modificar y distribuir libremente. Ver [LICENSE](./LICENSE).
