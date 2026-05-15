---
name: Plantilla_MaquinaSimple
type: plantilla
tia_version: V20
tia_compat: [V18, V19, V20]
plc_family: [s7-1200]
depends_on: []
used_by: []
tags: [plantilla, maquina, basic]
status: documented
---

# Plantilla — Máquina simple (1 PLC + 1 HMI)

> Estructura base de proyecto TIA Portal para una máquina sencilla: **un PLC S7-1200 + un HMI Basic/Comfort pequeño**. Carpetas, convenciones de nombres y bloques vacíos listos para rellenar.

**Tipo:** `Plantilla de proyecto`
**Versión TIA Portal:** V20
**Familia PLC:** S7-1200
**HMI:** KTP400/700/900 Basic o Comfort

---

## ¿Qué problema resuelve?

Empezar un proyecto desde cero implica perder 2-3 horas montando carpetas, definiendo convenciones de nombres, creando los DBs base, OBs de arranque, plantillas HMI… Esta plantilla parte de un proyecto vacío pero con esa estructura ya hecha — solo hay que rellenar la lógica concreta de la máquina.

Pensada para máquinas individuales: **monobloque mecánico, 1 PLC, 1 HMI, sin red distribuida**.

---

## Estructura del proyecto incluida

```
PLC_1 [CPU 1215C DC/DC/DC]
├── Bloques de programa
│   ├── OB1 [Main] ← incluye plantilla [`ob1-plantilla`](../../bloques-de-organizacion/ob1-plantilla/)
│   ├── OB100 [Startup] ← incluye plantilla [`ob100-startup`](../../bloques-de-organizacion/ob100-startup/)
│   ├── OB82 [Diagnostic] ← incluye [`ob82-85-86-errores`](../../bloques-de-organizacion/ob82-85-86-errores/)
│   ├── DB_Equipos    [Global DB]  ← motores, válvulas...
│   ├── DB_Analogicas [Global DB]  ← entradas analógicas
│   ├── DB_Alarmas    [Global DB]  ← array de UDT_Alarm
│   ├── DB_Proceso    [Global DB]  ← estado de máquina, secuencia
│   ├── DB_HMI        [Global DB]  ← variables específicas del HMI
│   ├── DB_Seguridad  [Global DB]  ← cadenas y enclavamientos
│   └── DB_Diagnostico[Global DB]  ← contadores OB de error
├── Tipos de datos PLC
│   ├── UDT_Motor
│   ├── UDT_Valve
│   ├── UDT_AnalogInput
│   └── UDT_Alarm
└── Variables PLC
    └── Tabla "Tags" con prefijos i/q estándar

HMI_1 [KTP700 Basic]
├── Pantallas
│   ├── 00_Inicio
│   ├── 10_Sinoptico
│   ├── 20_Alarmas       ← incluye [`pantalla-alarmas`](../../hmi/pantalla-alarmas/)
│   ├── 30_Ajustes
│   └── 40_Diagnostico
├── Plantillas globales
│   └── Plantilla_Navegacion ← incluye [`plantilla-navegacion`](../../hmi/plantilla-navegacion/)
└── Faceplates
    ├── Faceplate_Motor
    ├── Faceplate_Valve
    └── Faceplate_Analog
```

---

## Convenciones de nombres incluidas

- **Equipos**: `M01_NombreEquipo` (motores), `V01_NombreValvula` (válvulas), `AI01_NombreSensor`, `AO01_NombreActuador`.
- **DBs globales**: `DB_Categoria` (`DB_Equipos`, `DB_Proceso`, `DB_HMI`...).
- **Variables**: prefijo húngaro corto (`x` BOOL, `i` INT, `r` REAL, `s` STRING, `t` TIME, `dt` DTL).
- **Tags físicos**: `iSetaArmario`, `iFinalCarrera_V01_Abierta`, `qContactor_M01`...

---

## Cómo importarlo en TIA Portal

1. Descarga el archivo `plantilla-maquina-simple.zip` (proyecto archivado).
2. En TIA Portal: **Proyecto → Recuperar** → selecciona el `.zap20` extraído.
3. Renombra el proyecto y ya tienes la estructura lista.

> **Nota**: TIA Portal exporta proyectos en `.zap20` (V20) o `.ap20` (no archivado). Esta plantilla se distribuye archivada.

---

## Cómo usar la plantilla

1. Abre el proyecto recuperado.
2. Renombra la CPU/HMI según tu hardware real.
3. Ajusta el slot, IP y subred en la configuración HW.
4. Empieza a rellenar `DB_Equipos` declarando una variable `M01_BombaPrincipal : UDT_Motor` por cada equipo.
5. En `OB100`, rellena los textos de alarma y umbrales de tu proyecto.
6. En `OB1`, llama a un `FB_Motor` por cada motor declarado.

---

## Notas / Limitaciones conocidas

- **TIA Portal V20** es necesario para abrir el archivo `.zap20`. Para V19 hay que migrar manualmente (TIA Portal lo permite).
- La plantilla incluye los UDTs y FBs **de ejemplo vacíos** — los `.xml` reales hay que importarlos desde sus respectivas carpetas del repo.
- La CPU está configurada como genérica `1215C DC/DC/DC` — cámbiala antes de descargar al PLC real.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
