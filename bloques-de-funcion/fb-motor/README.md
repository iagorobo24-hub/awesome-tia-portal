# FB_Motor

> Bloque de control digital de motor — gestiona marcha/paro, modo manual/auto, vigilancia de feedback con timeout, contador de horas y arranques.

**Tipo:** `Bloque de función (FB)`
**Versión TIA Portal:** V20 *(compatible con V18 y V19)*
**Familia PLC:** S7-1200 / S7-1500

**Depende de:** [`UDT_Motor`](../../tipos-de-datos/udt-motor/)

---

## ¿Qué problema resuelve?

Controlar un motor digital "bien hecho" implica más que cerrar un contactor: hay que gestionar manual/auto, esperar la confirmación física del KM, tratar el timeout, sumar horas, contar arranques, exponer el estado al HMI… Cada programador termina escribiendo su propio FB con sus propios nombres.

`FB_Motor` es **un FB único, parametrizado y reutilizable** que consume `UDT_Motor` como InOut y resuelve toda la lógica estándar de control de motor de un golpe.

---

## Variables / Interfaz

### Entradas (Input) — señales físicas y enclavamientos

| Variable | Tipo | Descripción |
|---|---|---|
| `xEntradaTermico` | BOOL | Entrada física del relé térmico (lógica positiva = activo bajo en NC) |
| `xEntradaGuardamotor` | BOOL | Entrada física del guardamotor |
| `xEntradaFeedback` | BOOL | Entrada física del contacto KM (confirmación marcha) |
| `xParoEmergencia` | BOOL | `TRUE` cuando la cadena de seguridad está OK |
| `xPermisoArranque` | BOOL | Permiso externo de arranque (enclavamientos de proceso) |

### InOut

| Variable | Tipo | Descripción |
|---|---|---|
| `Motor` | UDT_Motor | Estructura completa del motor (comando, estado, fallos, diagnóstico, config) |

### Salidas (Output)

| Variable | Tipo | Descripción |
|---|---|---|
| `qSalidaContactor` | BOOL | Salida hacia la bobina del KM |
| `qLamparaMarcha` | BOOL | Lámpara verde marcha (conectable a salida o HMI) |
| `qLamparaFallo` | BOOL | Lámpara roja parpadeante en fallo |

### Estáticas (Static) destacadas

| Variable | Tipo | Descripción |
|---|---|---|
| `tonTimeoutArranque` | TON | Temporizador de timeout de arranque |
| `tonTimeoutParo` | TON | Temporizador de timeout de paro |
| `rtrigTermico` | R_TRIG | Detección de flanco de fallo térmico |
| `rtrigArranque` | R_TRIG | Flanco para incrementar `diArranques` |
| `tInternalCounter` | TIME | Acumulador interno para horas de funcionamiento |

---

## Cómo importarlo en TIA Portal

1. Asegúrate de tener importado primero el [`UDT_Motor`](../../tipos-de-datos/udt-motor/).
2. Descarga el archivo `fb-motor.xml`.
3. En TIA Portal, abre tu proyecto.
4. Clic derecho sobre **Bloques de programa** → **Importar** → confirma.

---

## Ejemplo de uso

```scl
// Bomba principal, KM en %Q0.0, térmico en %I0.0, feedback en %I0.1
"FB_Motor"(
    xEntradaTermico     := %I0.0,
    xEntradaGuardamotor := FALSE,                  // sin guardamotor
    xEntradaFeedback    := %I0.1,
    xParoEmergencia     := "DB_Seguridad".xCadenaOK,
    xPermisoArranque    := "DB_Proceso".xPermisoBomba,
    Motor               := "DB_Equipos".M01_BombaPrincipal,
    qSalidaContactor    => %Q0.0,
    qLamparaMarcha      => %Q0.1,
    qLamparaFallo       => %Q0.2
);
```

---

## Lógica resumida

1. **Modo manual** → `Motor.Comando.xMarcha`/`xParo` vienen del HMI.
2. **Modo automático** → `Motor.Comando.xMarcha`/`xParo` vienen de la receta/secuencia.
3. **Comando de marcha** → cierra `qSalidaContactor`. Arranca `tonTimeoutArranque`.
4. Si llega `xEntradaFeedback` antes de `Config.tTimeoutArranque` → `Estado.xEnMarcha := TRUE`.
5. Si NO llega → `Fallos.xTimeoutArranque := TRUE` y se desenclava la salida.
6. Cualquier fallo (`Fallos.*`) abre el contactor y enclava el fallo hasta `Comando.xReset`.
7. Mientras `Estado.xEnMarcha = TRUE` se incrementa `Diagnostico.rHorasFuncionamiento`.

---

## Notas / Limitaciones conocidas

- El campo `Diagnostico.rHorasFuncionamiento` debe ser **retentivo** en el DB que aloje la instancia.
- `iEntradaTermico` se asume con la lógica del repo: `TRUE` = térmico activo (térmico disparado). Si tu cableado es al revés, niégalo en la llamada.
- Si tu motor no tiene feedback físico, configura `Motor.Config.tTimeoutArranque := T#0ms` y el FB no exigirá el feedback.
- Para arranques estrella-triángulo, este FB no basta — necesitas un FB específico (no incluido).

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
