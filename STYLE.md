# 📏 Guía de estilo del repo

Convenciones que sigue este repo para que todos los recursos (UDTs, FBs, FCs, OBs, HMI, plantillas) se entiendan a la primera y encajen bien entre sí.

> **Criterio**: priorizamos coherencia interna y compatibilidad con TIA Portal. Si una práctica no está aquí, mira lo que ya hay en el repo y replícalo. Ante la duda, pregunta en un Issue antes de abrir la PR.

---

## 📑 Tabla de contenido

- [1. Estructura de carpetas](#1-estructura-de-carpetas)
- [2. Naming de carpetas, archivos y bloques](#2-naming-de-carpetas-archivos-y-bloques)
- [3. Naming de variables (prefijos húngaros)](#3-naming-de-variables-prefijos-húngaros)
- [4. Tipos de datos y formato](#4-tipos-de-datos-y-formato)
- [5. Codificación y formato de archivos](#5-codificación-y-formato-de-archivos)
- [6. README por recurso](#6-readme-por-recurso)
- [7. Idioma](#7-idioma)
- [8. Compatibilidad de versiones TIA](#8-compatibilidad-de-versiones-tia)
- [9. Comentarios en SCL](#9-comentarios-en-scl)
- [10. Antes de hacer commit](#10-antes-de-hacer-commit)

---

## 1. Estructura de carpetas

El repo se organiza por **categoría** en la raíz, y dentro de cada categoría hay una **subcarpeta por recurso**:

```
awesome-tia-portal/
├── tipos-de-datos/              # UDTs
│   ├── udt-motor/               # 1 carpeta = 1 recurso
│   │   ├── README.md            # obligatorio (siempre)
│   │   └── udt-motor.xml        # requerido cuando status: available · opcional con status: documented
│   └── udt-analog-input/
├── bloques-de-funcion/          # FBs y FCs
├── bloques-de-organizacion/     # OBs
├── hmi/                         # Pantallas, faceplates
├── plantillas-de-proyecto/      # Estructuras base
└── _plantillas/                 # Plantillas internas del repo (sort first)
```

**Reglas:**

- Cada recurso vive en **su propia subcarpeta**, nunca sueltos en la raíz de una categoría.
- **`README.md` es obligatorio en toda subcarpeta** (lo verifica el workflow `check-resources.yml` y falla si falta).
- **El `.xml`** se exige según el `status` declarado en el frontmatter del README:
  - `status: documented` — hay descripción pero el XML aún no se ha exportado desde TIA. CI emite aviso pero pasa.
  - `status: available` — recurso completo. CI exige el `.xml` (pendiente: validación estricta en #10 del análisis).
  - `status: wip` — trabajo en curso, no se considera estable.
- **No** crees carpetas nuevas en la raíz sin discutirlo en un Issue primero.
- Las carpetas que empiezan con `_` (como `_plantillas`) son **internas del repo**, no recursos publicables. El guion bajo las ordena al principio de la lista.

---

## 2. Naming de carpetas, archivos y bloques

### Carpetas y archivos del repo

- **kebab-case** en minúsculas, sin acentos, sin espacios.
- Una palabra descriptiva por concepto, separada por guiones.

| ✅ Bien | ❌ Mal |
|---|---|
| `udt-motor/` | `UDT_Motor/`, `udt_motor/`, `udtMotor/` |
| `fb-analog-input/` | `FB_AnalogInput/`, `fb-AnalogInput/` |
| `bloques-de-funcion/` | `bloques-de-función/`, `BloquesDeFuncion/` |
| `udt-motor.xml` | `UDT_Motor.xml`, `udt_motor.XML` |

> **¿Por qué sin acentos?** Las URLs con acentos pueden romperse en clientes de Git antiguos y son un dolor en CI. Mantenemos los acentos solo en el contenido (texto Markdown), nunca en nombres de archivos o carpetas.

### Nombres de bloques dentro de TIA Portal

Aquí seguimos la convención **PascalCase con guion bajo** que ya es estándar en el sector:

| Tipo | Prefijo | Ejemplo |
|---|---|---|
| UDT | `UDT_` | `UDT_Motor`, `UDT_AnalogInput` |
| Function Block | `FB_` | `FB_Motor`, `FB_AnalogInput` |
| Function | `FC_` | `FC_Escalado`, `FC_Convertir` |
| Organization Block | `OB_` o estándar | `OB1`, `OB100`, `OB82` |
| Faceplate HMI | `Faceplate_` | `Faceplate_Motor` |
| Pantalla HMI | `Pantalla_` | `Pantalla_Alarmas` |

### Mapeo entre carpeta y nombre TIA

La regla es directa:

| Carpeta del repo | Nombre del bloque en TIA |
|---|---|
| `udt-motor/` | `UDT_Motor` |
| `fb-analog-input/` | `FB_AnalogInput` |
| `fc-escalado/` | `FC_Escalado` |
| `faceplate-motor/` | `Faceplate_Motor` |

---

## 3. Naming de variables (prefijos húngaros)

Usamos **prefijo húngaro lowercase** seguido del nombre del concepto en **PascalCase**.

### Prefijos por tipo primitivo (obligatorios)

| Prefijo | Tipo | Ejemplo |
|---|---|---|
| `x` | `BOOL` | `xMarcha`, `xFallo`, `xModoAuto` |
| `i` | `INT` | `iValorRaw`, `iPrioridad` |
| `di` | `DINT` | `diArranques`, `diContador` |
| `ud` | `UDINT` | `udNumeroSerie` |
| `r` | `REAL` | `rValor`, `rConsignaVelocidad` |
| `lr` | `LREAL` | `lrPrecision` |
| `s` | `STRING` | `sEstado`, `sUnidad` |
| `t` | `TIME` | `tTimeoutArranque`, `tDelayAlarma` |
| `dt` | `DTL` / `DATE_AND_TIME` / `DATE` | `dtTimestamp` |
| `w` | `WORD` | `wEstado` |
| `dw` | `DWORD` | `dwBitmap` |
| `b` | `BYTE` | `bMascara` |
| `e` | `INT` o `DINT` usado como enum | `eUnidadVelocidad`, `eModo` |

> **Regla clave**: el prefijo refleja el **tipo de dato**, no la dirección (input/output). La dirección se entiende por la sección del README (Entradas / Salidas / Estáticas).

### Prefijos para instancias de Function Blocks estándar

Para variables locales que son instancias de FBs estándar, usamos el **nombre del FB en lowercase** como prefijo:

| Prefijo | FB | Ejemplo |
|---|---|---|
| `ton` | `TON` (timer on) | `tonTimeoutArranque`, `tonCiclo` |
| `tof` | `TOF` (timer off) | `tofRetardoParo` |
| `tp` | `TP` (timer pulse) | `tpPulsoUnico` |
| `rtrig` | `R_TRIG` (rising edge) | `rtrigEdgeArranque`, `rtrigSignal` |
| `ftrig` | `F_TRIG` (falling edge) | `ftrigEdgeParo` |
| `ctu` | `CTU` (count up) | `ctuPiezas` |
| `ctd` | `CTD` (count down) | `ctdRestantes` |
| `ctud` | `CTUD` (count up/down) | `ctudPosicion` |

### Excepción `q` para outputs BOOL

Por compatibilidad con la nomenclatura clásica de Siemens (área `%Q`), aceptamos el prefijo **`q`** *únicamente* en outputs de tipo `BOOL` que se conectan directamente a una salida física o a un indicador HMI:

```
qSalidaContactor       BOOL    Salida hacia bobina del KM
qLamparaMarcha         BOOL    Lámpara verde marcha
```

Esto es la única excepción permitida al "el prefijo refleja el tipo". Para outputs no-BOOL, vuelve al prefijo de tipo (`rValorCalculado`, `iCodigoError`).

### UDTs y estructuras complejas

Las variables que **son instancias de un UDT** o estructuras complejas usan **PascalCase sin prefijo**, igual que el tipo:

```
Motor                  UDT_Motor          Estructura del motor
Analog                 UDT_AnalogInput    Estructura de entrada analógica
Alarmas                ARRAY[1..50] OF UDT_Alarm    Lista de alarmas
```

### Nombres deseables vs no deseables

| ✅ Bien | ❌ Mal | Motivo |
|---|---|---|
| `xMarcha` | `Marcha`, `marcha`, `XMarcha` | Falta prefijo / case incorrecto |
| `iEntradaTermico` (si fuera INT) | `iEntradaTermico` (siendo BOOL) | Prefijo no coincide con tipo |
| `xEntradaTermico` (BOOL físico) | `iEntradaTermico` (BOOL físico) | Misma observación |
| `tonTimeoutArranque` | `TON_TimeoutArranque`, `TimerArranque` | Prefijo del FB en lowercase |
| `rtrigEdgeArranque` | `rEdgeArranque` (R_TRIG ≠ REAL) | Colisión `r` REAL vs `r` R_TRIG |

---

## 4. Tipos de datos y formato

### Mayúsculas / minúsculas

Los tipos de datos siempre se escriben en **MAYÚSCULAS** en los READMEs:

```
✅ BOOL, INT, DINT, REAL, STRING, TIME, DTL, WORD, DWORD, BYTE
❌ Bool, Int, Real, String, Time, Dtl
```

### STRING con tamaño

Usa siempre **corchetes**, que es la sintaxis nativa de TIA Portal:

```
✅ STRING[40], STRING[80], STRING[10]
❌ STRING(40), STRING(80)
```

### ARRAY

Siempre con la palabra `OF` y el tipo en mayúsculas:

```
✅ ARRAY[1..50] OF UDT_Alarm
✅ ARRAY[0..99] OF REAL
❌ Array[1..50] of UDT_Alarm
```

### Constantes y enums

Para valores tipo enum (motor: 0=manual, 1=auto, 2=remoto), usa el prefijo `e` y documenta los valores en una nota:

```
| `eModo` | INT | 0 = manual · 1 = auto · 2 = remoto |
```

---

## 5. Codificación y formato de archivos

### Markdown (`.md`)

- **UTF-8 sin BOM**.
- Saltos de línea **LF** (`\n`), nunca CRLF.
- Sin espacios en blanco al final de línea (excepto los dos espacios deliberados para `<br>`).
- Una línea en blanco al final del archivo.

### XML exportado de TIA Portal

- **UTF-8 sin BOM**. TIA a veces exporta con BOM — usa un editor (VS Code: "Save with Encoding → UTF-8") para limpiarlo antes de commitear.
- **Saltos de línea**: lo que TIA exporte. No reformatees el XML manualmente — algún parser puede romperse.
- **No commitear metadatos sensibles**: revisa que el XML no contiene IPs internas, nombres de usuario, rutas de proyecto, nombres de empresa. Si los lleva, edítalos antes del commit.

### Otros archivos

- `.gitignore` ya ignora todos los formatos de archivo de proyecto TIA (`*.ap20`, `*.zap20`, etc.). **No subas proyectos completos** al repo — solo recursos individuales exportados.

---

## 6. README por recurso

Cada recurso tiene un `README.md` que sigue la plantilla [`_plantillas/README-recurso.md`](./_plantillas/README-recurso.md).

**Secciones obligatorias** (en este orden):

1. **Frontmatter YAML** con metadatos (`name`, `type`, `tia_version`, `plc_family`, `depends_on`, `tags`, `status`...). **Debe ocupar las primeras líneas del archivo** (delimitadas por `---`) para que los parsers lo reconozcan; nada — ni comentarios HTML — puede ir antes.
2. **Título + descripción de 1 línea** (el "tagline"), inmediatamente después del cierre `---` del frontmatter.
3. **¿Qué problema resuelve?** — 2-4 frases sin tecnicismos innecesarios.
4. **Variables / Interfaz** — tablas separadas para Input / Output / InOut / Static.
5. **Cómo importarlo en TIA Portal** — pasos numerados.
6. **Ejemplo de uso** — código SCL real, no pseudocódigo.
7. **Cómo validarlo** — caso de prueba mínimo para verificar que funciona.
8. **Notas / Limitaciones conocidas** — qué NO hace, en qué versiones falla, etc.
9. **Dependencias** — qué otros recursos del repo necesita (si aplica).
10. **Compatibilidad** — matriz V18/V19/V20.
11. **Capturas / GIF** — opcional pero recomendado para HMI.
12. **Historial de cambios** — opcional al principio, útil cuando el recurso evolucione.
13. **Autor** — opcional.

**Reglas de redacción:**

- Frases cortas. Si una frase tiene más de 25 palabras, parte en dos.
- Sin disculpas (*"perdona pero..."*, *"si me he equivocado..."*) — al grano.
- Usa **`código en formato monoespaciado`** para todo lo que sea identificador (nombres de variables, tipos, valores literales, rutas).
- Listas con `-` (guion), no con `*` o `+`.

---

## 7. Idioma

- **Texto en prosa**: español.
- **Identificadores de variables**: español o inglés, **mantén consistencia dentro de un recurso**. Si un recurso usa `xMarcha`, no mezcles luego con `xRunning`.
- **Tipos de datos y palabras clave de TIA**: en inglés, MAYÚSCULAS (`BOOL`, `STRING`, `IF`, `THEN`).
- **Comentarios en SCL**: español preferentemente.

> El repo prioriza la comunidad hispanohablante. Si un colaborador internacional aporta en inglés, lo aceptamos pero idealmente con una traducción al español.

---

## 8. Compatibilidad de versiones TIA

El repo está optimizado para **TIA Portal V20**. Cada recurso debe declarar en su README la matriz de versiones donde se ha probado:

| Versión | Estado | Notas |
|---|:---:|---|
| V20 | ✅ | Versión de referencia |
| V19 | ✅ | Probado, funciona idéntico |
| V18 | ⚠️ | Funciona pero algunos campos opcionales no aparecen |
| V17 y anteriores | ❌ | No probado, no soportado |

**Convenciones de iconos:**
- ✅ probado y funciona OK
- ⚠️ funciona pero con limitaciones (documentar cuáles)
- ❌ no soportado / no probado
- ➖ no aplica (ej: faceplate Unified en V18 no existe)

Si tu recurso solo se ha probado en V20, sé honesto: pon ⚠️ o ➖ en V18/V19 y deja una nota.

---

## 9. Comentarios en SCL

- Comentarios de **bloque** al principio de cada sección lógica:
  ```scl
  // ===========================================================
  // Sección 2: Lógica de seguridad
  // ===========================================================
  ```
- Comentarios de **línea** (`//`) para aclarar una decisión, no para narrar el código.
- **Nunca** comentar el diff (*"// ahora también comprobamos X"*). El "qué cambió" va en el commit / PR description, no en el código.
- Si el código es trivial, no añadas comentario. Confía en buenos nombres de variables.

---

## 10. Antes de hacer commit

Mini-checklist antes de abrir la PR:

- [ ] El nombre de la subcarpeta es kebab-case y coincide con el nombre TIA (ej: `udt-motor` → `UDT_Motor`).
- [ ] El `README.md` sigue la plantilla y tiene todas las secciones obligatorias.
- [ ] El frontmatter YAML al inicio del README está completo, incluyendo el campo `status` correcto.
- [ ] Los nombres de variables usan los prefijos correctos (sección 3).
- [ ] Los tipos de datos están en MAYÚSCULAS y `STRING[N]` con corchetes.
- [ ] Si `status: available`: el `.xml` está presente, en UTF-8 sin BOM y no contiene IPs / usernames / rutas internas.
- [ ] Si `status: available`: he probado importar el `.xml` en TIA Portal V20 desde cero y compila.
- [ ] He regenerado [`CATALOG.md`](./CATALOG.md) con `python3 scripts/generate_catalog.py` y commiteado el resultado.
- [ ] CI pasa en verde.

---

## 📚 Recursos relacionados

- [`CONTRIBUTING.md`](./CONTRIBUTING.md) — guía para contribuidores no técnicos en GitHub.
- [`_plantillas/README-recurso.md`](./_plantillas/README-recurso.md) — plantilla de README por recurso.
- [`CATALOG.md`](./CATALOG.md) — índice de todos los recursos del repo (auto-generado).
- [`scripts/generate_catalog.py`](./scripts/generate_catalog.py) — script que produce el `CATALOG.md` a partir del frontmatter de cada recurso.

---

¿Encuentras una incoherencia entre esta guía y el repo? Abre un Issue. Esta guía evoluciona con el repo.
