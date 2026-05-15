---
name: UDT_Motor
type: udt
tia_version: V20
tia_compat: [V18, V19, V20]
plc_family: [s7-1200, s7-1500]
depends_on: []
used_by: [bloques-de-funcion/fb-motor, hmi/faceplate-motor]
tags: [motor, control, udt]
status: documented
---

# UDT_Motor

> Estructura unificada para el control y diagnóstico de un motor digital (marcha/paro con confirmación física).

**Tipo:** `UDT`
**Versión TIA Portal:** V20 *(compatible con V18 y V19)*
**Familia PLC:** S7-1200 / S7-1500

---

## ¿Qué problema resuelve?

En cada proyecto se acaba escribiendo "a mano" la misma estructura para gestionar un motor: comandos, feedback del contactor, fallos, contador de horas, etc. Cada programador lo organiza distinto, y el HMI termina enganchado a variables sueltas que no se reutilizan en el siguiente proyecto.

`UDT_Motor` define **una única interfaz estándar** para cualquier motor digital: el bloque de control (`FB_Motor`) la consume, el HMI la enlaza y el diagnóstico se gestiona siempre igual. Cambias de proyecto y todo encaja.

---

## Variables / Interfaz

El UDT está organizado en 5 sub-estructuras para que la lectura sea limpia tanto desde lógica como desde HMI.

### `Comando` — escrituras desde la lógica/HMI hacia el motor

| Variable | Tipo | Descripción |
|---|---|---|
| `xMarcha` | BOOL | Pulso (o nivel, según FB) para arrancar el motor |
| `xParo` | BOOL | Pulso (o nivel) para parar el motor |
| `xReset` | BOOL | Pulso para reconocer/borrar fallos |
| `xModoAuto` | BOOL | `TRUE` = modo automático (lo gobierna la receta/secuencia) · `FALSE` = manual (lo gobierna el HMI) |

### `Estado` — lecturas del estado real del motor

| Variable | Tipo | Descripción |
|---|---|---|
| `xEnMarcha` | BOOL | Confirmación física de marcha (KM cerrado / feedback contactor) |
| `xParado` | BOOL | Motor confirmado parado |
| `xListo` | BOOL | Sin fallos activos y disponible para arrancar |
| `xFallo` | BOOL | OR de todos los fallos individuales — se usa como "luz roja" en HMI |
| `xModoAutoActivo` | BOOL | Refleja en qué modo está operando realmente |

### `Fallos` — desglose de fallos para diagnóstico

| Variable | Tipo | Descripción |
|---|---|---|
| `xTermico` | BOOL | Disparo del relé térmico |
| `xGuardamotor` | BOOL | Disparo del guardamotor magnetotérmico |
| `xTimeoutArranque` | BOOL | No se confirmó la marcha dentro de `Config.tTimeoutArranque` |
| `xTimeoutParo` | BOOL | No se confirmó el paro dentro de `Config.tTimeoutParo` |
| `xParadaEmergencia` | BOOL | Cadena de seguridad / seta abierta |

### `Diagnostico` — métricas y texto de estado

| Variable | Tipo | Descripción |
|---|---|---|
| `rHorasFuncionamiento` | REAL | Horas acumuladas con el motor en marcha (persistente) |
| `diArranques` | DINT | Contador de arranques desde la puesta en marcha |
| `sEstado` | STRING[40] | Texto descriptivo del estado actual ("En marcha", "Fallo térmico"...) |

### `Config` — parámetros de comportamiento

| Variable | Tipo | Descripción |
|---|---|---|
| `tTimeoutArranque` | TIME | Tiempo máximo esperando confirmación de marcha tras orden |
| `tTimeoutParo` | TIME | Tiempo máximo esperando confirmación de paro tras orden |
| `tFiltroFeedback` | TIME | Filtro anti-rebote sobre la señal de feedback del contactor |

---

## Cómo importarlo en TIA Portal

1. Descarga el archivo `udt-motor.xml`
2. En TIA Portal, abre tu proyecto
3. En el árbol del proyecto, clic derecho sobre **Tipos de datos PLC**
4. Selecciona **Importar**
5. Busca el `.xml` descargado y confirma

El UDT aparecerá en `Tipos de datos PLC > UDT_Motor`, listo para usar como tipo en cualquier DB, FB o variable.

---

## Ejemplo de uso

Declara una variable del tipo `UDT_Motor` por cada motor de la instalación, normalmente dentro de un DB global de "Equipos":

```
DB_Equipos.M01_BombaPrincipal : UDT_Motor
DB_Equipos.M02_VentiladorExtraccion : UDT_Motor
```

Desde el HMI enlazas directamente la sub-estructura completa al faceplate (un único enlace en lugar de 20 variables sueltas):

```
Faceplate_Motor.Tag = "DB_Equipos".M01_BombaPrincipal
```

Y desde un `FB_Motor` (que próximamente subiremos al repo) le pasas la instancia entera como `InOut`:

```
"FB_Motor"(
    Motor := "DB_Equipos".M01_BombaPrincipal,
    xEntradaTermico := %I0.0,
    xEntradaFeedback := %I0.1,
    qSalidaContactor => %Q0.0
);
```

---

## Notas / Limitaciones conocidas

- Pensado para **motores digitales** (marcha/paro con confirmación). Para variadores de frecuencia hay un UDT específico (`UDT_Drive` — pendiente).
- El campo `rHorasFuncionamiento` debe declararse como **retentivo** en el DB que contenga la instancia para que sobreviva a un corte de tensión.
- Si tu motor no tiene feedback físico de contactor, deja `Config.tTimeoutArranque := T#0ms` para deshabilitar la vigilancia de timeout (el FB de control debe interpretarlo como "no exigir feedback").
- Los textos de `Diagnostico.sEstado` los rellena el `FB_Motor`, no se escriben directamente desde lógica externa.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
