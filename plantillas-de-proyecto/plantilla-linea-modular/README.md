---
name: Plantilla_LineaModular
type: plantilla
tia_version: V20
tia_compat: [V18, V19, V20]
plc_family: [s7-1500]
depends_on: []
used_by: []
tags: [plantilla, linea, modular]
status: documented
---

# Plantilla — Línea modular (varios PLCs + HMI central)

> Estructura base para una línea industrial con **varios PLCs S7-1500 comunicados** entre sí y un HMI Unified central. Pensada para escalar y compartir librerías entre PLCs.

**Tipo:** `Plantilla de proyecto`
**Versión TIA Portal:** V20
**Familia PLC:** S7-1500
**HMI:** WinCC Unified Comfort / RT

---

## ¿Qué problema resuelve?

Las líneas industriales reales no son un PLC suelto — son varios CPU coordinados (1 por estación, 1 maestro de línea, etc.) con datos compartidos vía PROFINET o I-Device, alarmas centralizadas y un HMI unificado. Diseñar bien esa arquitectura desde cero lleva días.

Esta plantilla parte de **3 PLCs comunicados + 1 HMI central** con la estructura base ya resuelta: librerías compartidas, comunicación por DB de intercambio, alarmas centralizadas en el PLC maestro.

---

## Arquitectura incluida

```
                          ┌────────────────────┐
                          │  HMI_Central       │
                          │  (WinCC Unified)   │
                          └──────────┬─────────┘
                                     │ PROFINET
                  ┌──────────────────┼──────────────────┐
                  │                  │                  │
        ┌─────────▼────────┐ ┌───────▼─────────┐ ┌──────▼──────────┐
        │  PLC_Maestro     │ │  PLC_Estacion1  │ │  PLC_Estacion2  │
        │  (S7-1500)       │ │  (S7-1500)      │ │  (S7-1500)      │
        │  - Coordinación  │ │  - Lógica E1    │ │  - Lógica E2    │
        │  - Alarmas       │ │  - I/O E1       │ │  - I/O E2       │
        │  - Recetas       │ │                 │ │                 │
        └──────────────────┘ └─────────────────┘ └─────────────────┘
```

---

## Estructura del proyecto incluida

### Librerías de proyecto compartidas

- **Lib_Tipos** — todos los UDTs (`UDT_Motor`, `UDT_Valve`, `UDT_AnalogInput`, `UDT_Alarm`, `UDT_Drive`).
- **Lib_Bloques** — todos los FBs (`FB_Motor`, `FB_Valve`, `FB_AnalogInput`...).
- **Lib_HMI** — faceplates compartidos (`Faceplate_Motor`, `Faceplate_Valve`, `Faceplate_Analog`).

> Estas librerías se actualizan en un único punto y se propagan automáticamente a los 3 PLCs y al HMI.

### PLC_Maestro

```
├── OB1, OB100, OB82, OB85, OB86
├── DB_Linea            ← estado global de línea (modo, fase, receta activa)
├── DB_Alarmas_Linea    ← alarmas centralizadas (array UDT_Alarm)
├── DB_Recetas          ← parámetros de receta
├── DB_Intercambio_E1   ← datos hacia/desde Estación 1 (struct comm)
├── DB_Intercambio_E2   ← datos hacia/desde Estación 2
└── FB_CoordinacionLinea
```

### PLC_Estacion1 / PLC_Estacion2

```
├── OB1, OB100, OB82
├── DB_Equipos      ← motores y válvulas locales
├── DB_Analogicas
├── DB_Intercambio  ← imagen del DB del maestro
└── FB_LogicaEstacion
```

### HMI_Central

```
Plantilla_Navegacion (header con nombre línea, footer con alarmas globales)
├── 00_Inicio
├── 10_Sinoptico_Linea
├── 11_Sinoptico_E1
├── 12_Sinoptico_E2
├── 20_Alarmas (centralizadas del maestro)
├── 30_Recetas
└── 40_Diagnostico
```

---

## Convenciones de comunicación

- **PROFINET I-Device**: cada estación expone un DB_Intercambio como I/O hacia el maestro.
- **Alarmas centralizadas**: cada estación escribe en un sub-array de `DB_Alarmas_Linea` del maestro vía `PUT/GET` o I-Device.
- **Recetas**: el maestro distribuye los parámetros activos a las estaciones via `DB_Intercambio`.
- **Sincronización**: el maestro publica un *latido* en `DB_Linea.diHeartbeat` que las estaciones vigilan para detectar pérdida de comunicación.

---

## Cómo importarlo en TIA Portal

1. Descarga el archivo `plantilla-linea-modular.zip`.
2. En TIA Portal: **Proyecto → Recuperar** → selecciona el `.zap20` extraído.
3. Ajusta IPs, slots y subred PROFINET según tu instalación.
4. Para añadir más estaciones, duplica `PLC_Estacion1` y renombra.

---

## Notas / Limitaciones conocidas

- Pensado para **S7-1500** (las librerías de proyecto y la I-Device requieren 1500). Para mezclar 1200/1500 hay que ajustar.
- La comunicación está hecha con **I-Device** sobre PROFINET. Para otras opciones (S7-Connection clásica, OPC UA), hay que reemplazar la capa de comunicación.
- El HMI Unified requiere licencia adecuada y panel/PC compatible — si trabajas con Comfort clásico, hay una versión simplificada de la plantilla pensada para máquinas más pequeñas.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
