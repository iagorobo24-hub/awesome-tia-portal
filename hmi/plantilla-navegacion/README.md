---
name: Plantilla_Navegacion
type: hmi-pantalla
tia_version: V20
tia_compat: [V18, V19, V20]
plc_family: [s7-1200, s7-1500]
hmi_panel: [comfort, unified]
depends_on: []
used_by: []
tags: [navegacion, header, footer, hmi]
status: documented
---

# Plantilla de Navegación HMI

> Plantilla maestra (header + footer + área de contenido) reutilizable en todas las pantallas del proyecto — con barra de alarmas, login de usuario, navegación principal y indicadores de estado.

**Tipo:** `HMI Template / Master Screen`
**Versión TIA Portal:** V20
**Panel objetivo:** Comfort Panels · Unified Comfort · WinCC Unified RT

---

## ¿Qué problema resuelve?

Sin plantilla maestra, cada pantalla del HMI duplica la cabecera, los botones de navegación, el reloj, los indicadores de alarma… y cuando hay que cambiar algo, hay que tocarlo 30 veces. Y al final, las pantallas no se parecen entre sí.

Esta plantilla maestra define la estructura común que se hereda en todas las pantallas: solo el área central varía.

---

## Estructura visual

```
┌────────────────────────────────────────────────────────────────────┐
│ [LOGO]  Mi Proyecto              29/04/2026  10:24    [ Iago ▼ ]   │   ← HEADER (fija)
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│                                                                    │
│                  ÁREA DE CONTENIDO ESPECÍFICA                      │   ← ÁREA libre
│                  (sinóptico, ajustes, recetas...)                  │
│                                                                    │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│ ⚠ 3 alarmas activas no reconocidas        [Inicio][Sinóp][Ajust]   │   ← FOOTER (fija)
└────────────────────────────────────────────────────────────────────┘
```

---

## Elementos del header

- **Logo** (placeholder editable).
- **Título del proyecto** (variable de texto editable desde Run-time Settings).
- **Reloj y fecha** vinculados a la hora del PLC.
- **Selector de usuario** con login/logout integrado.

## Elementos del área central

- Vacía — cada pantalla concreta hereda la plantilla y rellena esta área con su propio contenido.

## Elementos del footer

- **Indicador de alarmas activas** (badge con contador, parpadeante en rojo si > 0).
- **Botones de navegación principal**: Inicio, Sinóptico, Ajustes. Configurables.
- Botón opcional: Recetas, Tendencias, Diagnóstico (visibles según permiso de usuario).

---

## Cómo importarlo en TIA Portal

1. Descarga el archivo `plantilla-navegacion.xml`.
2. En TIA Portal HMI: clic derecho sobre **Plantillas globales** (Comfort) o **Master screens** (Unified) → **Importar**.
3. Una vez importada, ve a las propiedades de cada pantalla del proyecto y selecciona esta plantilla como "Plantilla" / "Master".

---

## Configuración tras importar

1. Sustituye el logo por el del cliente.
2. Edita el título y el footer-text en el catálogo de textos.
3. Configura los botones del footer para que apunten a las pantallas de tu proyecto (las pantallas destino deben existir).
4. Vincula el badge de alarmas a la variable que cuente alarmas activas (ej: `"DB_Alarmas".diActivas`).

---

## Notas / Limitaciones conocidas

- En **Basic Panels** las plantillas globales son muy limitadas — esta plantilla solo cubre la versión Comfort/Unified.
- Si tu cliente exige una guía de estilo corporativa (colores, tipografía), aplícala en la plantilla y se propagará a todas las pantallas.
- Para soporte multilenguaje, todos los textos están en el catálogo — añade traducciones en lugar de hard-codear strings en propiedades.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
