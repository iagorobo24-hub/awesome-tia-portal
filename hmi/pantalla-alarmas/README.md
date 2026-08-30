---
name: Pantalla_Alarmas
type: hmi-pantalla
tia_version: V20
tia_compat: [V18, V19, V20]
plc_family: [s7-1200, s7-1500]
hmi_panel: [comfort, unified]
depends_on: [tipos-de-datos/udt-alarm]
used_by: []
tags: [alarmas, pantalla, hmi]
status: documented
---

# Pantalla de Alarmas

> Pantalla HMI base de gestión de alarmas — listado activo, histórico, filtros por prioridad/fuente y reconocimiento individual o masivo.

**Tipo:** `HMI Screen`
**Versión TIA Portal:** V20
**Panel objetivo:** Comfort Panels · Unified Comfort · WinCC Unified RT

**Depende de:** [`UDT_Alarm`](../../tipos-de-datos/udt-alarm/) (recomendado)

---

## ¿Qué problema resuelve?

La pantalla de alarmas es de las primeras que pide el cliente final y de las que más tiempo lleva diseñar bien: filtros, ordenación, reconocimiento, histórico, exportación a USB… Esta pantalla parte del esqueleto resuelto y se adapta al proyecto en minutos.

---

## Estructura visual

```
┌────────────────────────────────────────────────────────────────────┐
│ ALARMAS                                  [ACTIVAS] [HISTÓRICO]     │   ← tabs
├────────────────────────────────────────────────────────────────────┤
│  Filtro:  Prioridad ▼   Fuente ▼   [Solo no reconocidas]           │
├────────────────────────────────────────────────────────────────────┤
│  Hora            Prio  Fuente                Texto              ACK│
│  29/04 10:24:13   3    M01_BombaPrincipal    Térmico disparado  ☐ │
│  29/04 10:23:55   2    AI01_TempReactor      Temperatura HH     ☑ │
│  29/04 10:21:02   2    V01_AguaEntrada       Timeout abrir      ☐ │
│  ...                                                               │
├────────────────────────────────────────────────────────────────────┤
│  [ ACK SELECCIONADA ]    [ ACK TODAS ]    [ EXPORTAR USB ]         │
└────────────────────────────────────────────────────────────────────┘
```

---

## Componentes incluidos

- **Tabla de alarmas activas** vinculada al sistema de alarmas estándar de TIA Portal HMI (Discrete/Analog Alarms) **o** a un array `DB_Alarmas.aLista[1..N] OF UDT_Alarm` si prefieres gestionar alarmas en lógica.
- **Tab de histórico** con timestamp, fuente y texto.
- **Combo de filtros** (prioridad, fuente, solo no reconocidas).
- **Botones**: ack individual (selección), ack masivo, exportar a USB (Comfort) / archivar (Unified).
- **Indicador en cabecera de proyecto**: cuenta de alarmas activas no reconocidas (badge rojo).

---

## Cómo importarlo en TIA Portal

1. Descarga el archivo `pantalla-alarmas.xml`.
2. En TIA Portal HMI: clic derecho sobre **Pantallas** → **Importar** → confirma.
3. Si usas la opción "alarmas como UDT", asegúrate de tener importado [`UDT_Alarm`](../../tipos-de-datos/udt-alarm/) en el PLC y un `DB_Alarmas.aLista` declarado.

---

## Configuración mínima tras importar

1. **Vincular textos de alarma**:
   - Si usas el sistema de alarmas estándar de TIA Portal → todo se autovincula al exportar.
   - Si usas el array `UDT_Alarm` → la tabla está enlazada a `"DB_Alarmas".aLista`.
2. **Permisos**: el botón "ACK TODAS" requiere permiso del grupo `Operador` (configurable en propiedades del botón).
3. **Histórico**: configura la ruta de archivado en **Run-time Settings → Logs**.

---

## Notas / Limitaciones conocidas

- En **Basic Panels** la tabla de alarmas tiene capacidades reducidas (no permite filtros complejos). En ese caso, la plantilla usa una WinCC alarm view simplificada.
- En **Unified**, el componente "Alarm Control" es muy distinto al de Comfort — la versión Unified de esta pantalla está construida con `Alarm Control` nativo.
- Si trabajas con normativas (S88, GMP, FDA 21 CFR Part 11) hay que añadir comentarios obligatorios en los acks y firma electrónica — esta pantalla cubre el caso base, no el regulado.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
