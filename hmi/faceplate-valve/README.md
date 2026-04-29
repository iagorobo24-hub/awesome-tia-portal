---
name: Faceplate_Valve
type: hmi-faceplate
tia_version: V20
tia_compat: [V18, V19, V20]
plc_family: [s7-1200, s7-1500]
hmi_panel: [comfort, unified]
depends_on: [tipos-de-datos/udt-valve, bloques-de-funcion/fb-valve]
used_by: []
tags: [valvula, faceplate, hmi]
status: documented
---

# Faceplate_Valve

> Faceplate HMI vinculado a `UDT_Valve` — pop-up con comandos abrir/cerrar manual, indicadores de posición, lista de fallos y diagnóstico.

**Tipo:** `HMI Faceplate`
**Versión TIA Portal:** V20
**Panel objetivo:** Comfort Panels (TP/KP) · Unified Comfort · WinCC Unified RT

**Depende de:** [`UDT_Valve`](../../tipos-de-datos/udt-valve/)

---

## ¿Qué problema resuelve?

Igual que con motores, cada válvula del proyecto necesita botones de mando, indicadores y lista de fallos. `Faceplate_Valve` es la versión vinculada a `UDT_Valve`: un único *binding* y la válvula queda lista para mostrar y operar desde el HMI.

---

## Estructura visual

```
┌─────────────────────────────────────────┐
│ V01_AguaEntrada           [ Modo Auto ▼]│
├─────────────────────────────────────────┤
│  ●  Abierta                              │
│  ○  Cerrada                              │
│  ◐  En movimiento                        │
│  ●  Listo                                │
│  ●  Fallo                                │
├─────────────────────────────────────────┤
│  [ ABRIR ]              [ CERRAR ]       │
│  [ RESET FALLO ]                         │
├─────────────────────────────────────────┤
│ FALLOS:                                  │
│  □ Timeout abrir                         │
│  □ Timeout cerrar                        │
│  □ Posición inválida                     │
│  □ Parada emergencia                     │
├─────────────────────────────────────────┤
│ Ciclos: 12345                            │
│ Último mov.: 1.2 s                       │
│ Estado: "Abierta"                        │
└─────────────────────────────────────────┘
```

Adicionalmente, una **representación en planta de la válvula** (símbolo de proceso) cambia de color según el estado:
- **Verde** → abierta
- **Gris** → cerrada
- **Amarillo** → en movimiento
- **Rojo parpadeante** → fallo

---

## Interfaz del faceplate

Una única propiedad `Valve` de tipo `UDT_Valve`.

### Comandos generados

- `[ ABRIR ]` → pulso en `{Valve}.Comando.xAbrir` (200ms).
- `[ CERRAR ]` → pulso en `{Valve}.Comando.xCerrar`.
- `[ RESET FALLO ]` → pulso en `{Valve}.Comando.xReset`.
- Selector modo → escribe `{Valve}.Comando.xModoAuto`.

### Lecturas mostradas

- Indicadores → `{Valve}.Estado.xAbierta/xCerrada/xEnMovimiento/xListo/xFallo`.
- Cada cuadrado de fallo → bit correspondiente de `{Valve}.Fallos.*`.
- Métricas → `{Valve}.Diagnostico.diCiclos`, `tTiempoUltimoMovimiento`, `sEstado`.

---

## Cómo importarlo en TIA Portal

1. Asegúrate de tener importado primero el [`UDT_Valve`](../../tipos-de-datos/udt-valve/) en el PLC.
2. Descarga el archivo `faceplate-valve.xml`.
3. En TIA Portal HMI: clic derecho sobre **Faceplates** → **Importar** → confirma.

---

## Ejemplo de uso

```
Variable enlazada: "DB_Equipos".V01_AguaEntrada
```

Arrastra el faceplate, asigna la variable, y listo.

---

## Notas / Limitaciones conocidas

- Para Basic Panels habría que reconstruir los elementos a mano.
- En válvulas de **simple efecto** (sin botón de cerrar), oculta el botón `[ CERRAR ]` con una propiedad `xVisibleBotonCerrar` configurable en el faceplate.
- El símbolo de proceso es genérico; sustitúyelo por el símbolo P&ID que use tu cliente si difiere.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
