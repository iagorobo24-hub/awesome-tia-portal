---
name: Faceplate_Motor
type: hmi-faceplate
tia_version: V20
tia_compat: [V18, V19, V20]
plc_family: [s7-1200, s7-1500]
hmi_panel: [comfort, unified]
depends_on: [tipos-de-datos/udt-motor, bloques-de-funcion/fb-motor]
used_by: []
tags: [motor, faceplate, hmi]
status: documented
---

# Faceplate_Motor

> Faceplate HMI vinculado a `UDT_Motor` — pop-up con comandos manuales, indicadores de estado, lista de fallos y métricas.

**Tipo:** `HMI Faceplate`
**Versión TIA Portal:** V20
**Panel objetivo:** Comfort Panels (TP/KP) · Unified Comfort · WinCC Unified RT

**Depende de:** [`UDT_Motor`](../../tipos-de-datos/udt-motor/)

---

## ¿Qué problema resuelve?

Cada motor en el HMI necesita los mismos elementos: botones marcha/paro, indicadores verde/rojo, modo manual/auto, lista de fallos, horas… Si los dibujas a mano para cada motor del proyecto pierdes horas y al final no son consistentes.

`Faceplate_Motor` es **un único faceplate parametrizado** que se enlaza a una instancia de `UDT_Motor` con un solo *binding*. Lo arrastras, le pasas la variable estructurada, y queda funcional al instante.

---

## Estructura visual

```
┌─────────────────────────────────────────┐
│ M01_BombaPrincipal       [ Modo Auto ▼ ]│   ← cabecera (texto + selector modo)
├─────────────────────────────────────────┤
│  ●  En marcha                            │   ← círculo verde dinámico
│  ○  Parado                               │
│  ●  Listo                                │
│  ●  Fallo                                │   ← círculo rojo parpadea si fallo
├─────────────────────────────────────────┤
│  [ MARCHA ]            [ PARO ]          │   ← botones manual (deshabilitados en auto)
│  [ RESET FALLO ]                         │
├─────────────────────────────────────────┤
│ FALLOS:                                  │
│  □ Térmico                               │   ← cuadrados rojos cuando activos
│  □ Guardamotor                           │
│  □ Timeout arranque                      │
│  □ Timeout paro                          │
│  □ Parada emergencia                     │
├─────────────────────────────────────────┤
│ Horas: 1234.5 h     Arranques: 567       │   ← métricas
│ Estado: "En marcha"                      │
└─────────────────────────────────────────┘
```

---

## Interfaz del faceplate

El faceplate expone una única **interfaz de propiedad** llamada `Motor` de tipo `UDT_Motor`. Todos los elementos internos están enlazados a sub-campos de esa interfaz vía expresiones del estilo `{Motor}.Estado.xEnMarcha`.

### Comandos generados desde HMI

- Pulsar `[ MARCHA ]` → escribe `TRUE` en `{Motor}.Comando.xMarcha` durante 200ms (botón pulso).
- Pulsar `[ PARO ]` → escribe `TRUE` en `{Motor}.Comando.xParo` durante 200ms.
- Pulsar `[ RESET FALLO ]` → pulso en `{Motor}.Comando.xReset`.
- Selector modo → escribe en `{Motor}.Comando.xModoAuto`.

### Lecturas mostradas

- Indicador "En marcha" → `{Motor}.Estado.xEnMarcha`.
- Indicador "Fallo" parpadeante → `{Motor}.Estado.xFallo` con animación parpadeo a 1Hz.
- Cada cuadrado de fallo → bit correspondiente de `{Motor}.Fallos.*`.
- Métricas → `{Motor}.Diagnostico.rHorasFuncionamiento`, `diArranques`, `sEstado`.

---

## Cómo importarlo en TIA Portal

1. Asegúrate de tener importado primero el [`UDT_Motor`](../../tipos-de-datos/udt-motor/) en el PLC.
2. Descarga el archivo `faceplate-motor.xml`.
3. En TIA Portal, abre la sección HMI del proyecto.
4. Clic derecho sobre **Faceplates** (o **Plantillas → Faceplates** en Comfort) → **Importar**.
5. Confirma.

---

## Ejemplo de uso

1. Arrastra el faceplate al lugar de la pantalla donde quieras mostrar el motor.
2. En las propiedades del faceplate, en la propiedad **`Motor`**, selecciona la variable estructurada del PLC:
   ```
   "DB_Equipos".M01_BombaPrincipal
   ```
3. Listo — el faceplate ya está funcional. Para más motores, repite con la variable correspondiente.

---

## Notas / Limitaciones conocidas

- Este faceplate está pensado para **Comfort Panels y Unified**. En **Basic Panels** (KTP400/700/900/1200 Basic) no existen faceplates — habría que copiar los elementos a la pantalla y enlazarlos manualmente.
- El estilo visual es minimalista (Siemens default). Si tu proyecto usa una guía de estilo corporativa, ajusta colores, fuentes y bordes desde el editor del faceplate.
- Para idiomas múltiples, los textos están definidos en el catálogo de textos del HMI — añade traducciones según necesidad.
- El parpadeo del indicador de fallo usa la marca de ciclo del HMI; si tu panel tiene una marca distinta, ajústala en la animación.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
