# Cómo contribuir

Gracias por querer aportar algo. Este documento explica el proceso paso a paso, incluyendo la parte de GitHub — pensado para gente que igual no lo ha usado antes.

---

## Antes de empezar — ¿qué tipo de aportación quieres hacer?

- **Añadir un recurso nuevo** (un bloque, un UDT, una pantalla HMI...) → sigue la guía completa de abajo
- **Corregir un error en algo que ya existe** → puedes abrir un [Issue](../../issues) explicando el problema, o proponer el cambio directamente
- **Mejorar documentación** → mismo proceso que añadir un recurso, pero solo tocas el README

---

## Guía completa para añadir un recurso nuevo

### Paso 1 — Crea tu cuenta en GitHub (si no tienes)

Ve a [github.com](https://github.com) y regístrate. Es gratis.

---

### Paso 2 — Haz un Fork del repositorio

Un Fork es una copia del repositorio en tu cuenta personal, donde puedes trabajar sin afectar al original.

1. Arriba a la derecha de esta página, pulsa el botón **Fork**
2. GitHub crea una copia en tu cuenta — algo como `tu-usuario/tia-portal-library`

---

### Paso 3 — Clona tu Fork en tu ordenador

```bash
git clone https://github.com/TU-USUARIO/tia-portal-library.git
cd tia-portal-library
```

Si no tienes Git instalado: [descárgalo aquí](https://git-scm.com/downloads). En Windows el instalador configura todo solo.

---

### Paso 4 — Crea una rama para tu aportación

Nunca trabajes directamente en `main`. Crea una rama con un nombre descriptivo:

```bash
git checkout -b feat/nombre-de-tu-recurso
```

Ejemplos de nombres de rama:
- `feat/fb-escalado-analogico`
- `feat/udt-motor-asincrono`
- `docs/correccion-readme-temporizador`

---

### Paso 5 — Añade tu recurso en la carpeta correcta

```
bloques-de-funcion/     → FBs, FCs
tipos-de-datos/         → UDTs
bloques-de-organizacion/→ OBs
hmi/                    → Pantallas y recursos HMI
plantillas-de-proyecto/ → Estructuras base
```

Dentro de la carpeta que corresponda, crea una subcarpeta con el nombre de tu recurso:

```
bloques-de-funcion/
└── escalado-analogico/
    ├── README.md          ← obligatorio
    └── escalado-analogico.xml
```

---

### Paso 6 — Rellena el README de tu recurso

Usa la plantilla que está en [`/_plantillas/README-recurso.md`](./_plantillas/README-recurso.md).

**Esto es lo más importante.** Un recurso sin documentación clara no se va a usar.

---

### Paso 7 — Commit y push

```bash
git add .
git commit -m "feat: añadir bloque de escalado de señal analógica"
git push origin feat/nombre-de-tu-recurso
```

---

### Paso 8 — Abre una Pull Request

1. Ve a tu Fork en GitHub
2. Verás un botón **"Compare & pull request"** — púlsalo
3. Rellena el título y la descripción usando la plantilla que aparece automáticamente
4. Pulsa **"Create pull request"**

A partir de ahí alguien del proyecto revisa tu aportación. Si hay algo que ajustar, se comenta en la propia PR. Si todo está bien, se hace merge y ya forma parte del repo.

---

## Criterios para que una PR sea aceptada

- ✅ Tiene README completo con la plantilla
- ✅ El archivo exportado es `.xml` (exportado desde TIA Portal)
- ✅ El nombre de la carpeta y del archivo es descriptivo y en minúsculas con guiones
- ✅ No incluye proyectos completos, solo el bloque o recurso concreto
- ✅ Compatible con TIA Portal V20 (si funciona en versiones anteriores, se indica)

---

## ¿Tienes dudas?

Abre un [Issue](../../issues/new) con la etiqueta `pregunta` y te respondemos.
