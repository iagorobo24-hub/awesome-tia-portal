---
name: FB_Valve
type: fb
tia_version: V20
tia_compat: [V18, V19, V20]
plc_family: [s7-1200, s7-1500]
depends_on: [tipos-de-datos/udt-valve]
used_by: []
tags: [valvula, control, fb]
status: documented
---

# FB_Valve

> Bloque de control de válvula digital — gestiona apertura/cierre, modo manual/auto, vigilancia de feedback con timeout, detección de posición inválida.

**Tipo:** `Bloque de función (FB)`
**Versión TIA Portal:** V20 *(compatible con V18 y V19)*
**Familia PLC:** S7-1200 / S7-1500

**Depende de:** [`UDT_Valve`](../../tipos-de-datos/udt-valve/)

---

## ¿Qué problema resuelve?

Las válvulas digitales se gestionan en cualquier proceso y siempre con la misma lógica: comando → solenoide → esperar feedback → fallar si no llega. `FB_Valve` resuelve esa lógica una vez de forma reutilizable, consumiendo `UDT_Valve` como InOut.

---

## Variables / Interfaz

### Entradas (Input)

| Variable | Tipo | Descripción |
|---|---|---|
| `xFeedbackAbierta` | BOOL | Final de carrera de abierta |
| `xFeedbackCerrada` | BOOL | Final de carrera de cerrada |
| `xParoEmergencia` | BOOL | `TRUE` si la cadena de seguridad está OK |
| `xPermisoOperacion` | BOOL | Permiso externo (enclavamientos de proceso) |

### InOut

| Variable | Tipo | Descripción |
|---|---|---|
| `Valve` | UDT_Valve | Estructura completa de la válvula |

### Salidas (Output)

| Variable | Tipo | Descripción |
|---|---|---|
| `qSolenoideAbrir` | BOOL | Salida hacia la bobina de apertura |
| `qSolenoideCerrar` | BOOL | Salida hacia la bobina de cierre (déjala desconectada en válvulas de simple efecto) |
| `qLamparaAbierta` | BOOL | Indicación visual de abierta |
| `qLamparaCerrada` | BOOL | Indicación visual de cerrada |

### Estáticas (Static) destacadas

| Variable | Tipo | Descripción |
|---|---|---|
| `tonTimeoutAbrir` | TON | Temporizador de vigilancia de apertura |
| `tonTimeoutCerrar` | TON | Temporizador de vigilancia de cierre |
| `tonPosInvalida` | TON | Filtro anti-rebote para posición inválida (1s) |
| `rtrigAbrir` | R_TRIG | Detección de flanco para contar ciclos |
| `tInicioMovimiento` | TIME | Marca de tiempo del último movimiento |

---

## Cómo importarlo en TIA Portal

1. Asegúrate de tener importado primero el [`UDT_Valve`](../../tipos-de-datos/udt-valve/).
2. Descarga el archivo `fb-valve.xml`.
3. En TIA Portal: clic derecho sobre **Bloques de programa** → **Importar** → confirma.

---

## Ejemplo de uso

```scl
// En OB100, configura los timeouts una sola vez:
"DB_Equipos".V01_AguaEntrada.Config.tTimeoutAbrir       := T#5s;
"DB_Equipos".V01_AguaEntrada.Config.tTimeoutCerrar      := T#5s;
"DB_Equipos".V01_AguaEntrada.Config.xRequiereFeedback   := TRUE;

// En OB1:
"FB_Valve"(
    xFeedbackAbierta := %I1.0,
    xFeedbackCerrada := %I1.1,
    xParoEmergencia  := "DB_Seguridad".xCadenaOK,
    xPermisoOperacion:= TRUE,
    Valve            := "DB_Equipos".V01_AguaEntrada,
    qSolenoideAbrir  => %Q1.0,
    qSolenoideCerrar => %Q1.1,
    qLamparaAbierta  => %Q1.2,
    qLamparaCerrada  => %Q1.3
);
```

---

## Lógica resumida

1. Si `xFeedbackAbierta` y `xFeedbackCerrada` se activan a la vez durante más de 1s → `Fallos.xPosicionInvalida`.
2. Comando de abrir → `qSolenoideAbrir := TRUE`. `tonTimeoutAbrir` empieza a contar.
3. Llega `xFeedbackAbierta` antes del timeout → `Estado.xAbierta := TRUE`, se desactiva `xEnMovimiento`.
4. No llega → `Fallos.xTimeoutAbrir := TRUE`, se cierra el solenoide.
5. Cualquier fallo enclava la válvula y obliga a `Comando.xReset` para volver a operar.
6. En cada apertura completada se incrementa `Diagnostico.diCiclos`.

---

## Notas / Limitaciones conocidas

- Para **válvulas de simple efecto** (resorte): conecta solo `qSolenoideAbrir`, deja `qSolenoideCerrar` flotando, y configura `Config.xRequiereFeedback := FALSE` si no hay final de carrera de cerrada.
- En modo automático, `Comando.xAbrir` y `xCerrar` deberían ser **niveles** (mantenidos), no pulsos. En manual desde HMI son pulsos.
- `Diagnostico.diCiclos` y `tTiempoUltimoMovimiento` deben ser retentivos para sobrevivir a cortes.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
