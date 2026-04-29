# UDT_Valve

> Estructura unificada para válvulas digitales (todo/nada) con feedback de posición y vigilancia de timeout.

**Tipo:** `UDT`
**Versión TIA Portal:** V20 *(compatible con V18 y V19)*
**Familia PLC:** S7-1200 / S7-1500

---

## ¿Qué problema resuelve?

Las válvulas digitales aparecen en cualquier proceso. Cada programador termina creando su propia mezcla de marcas para "abrir/cerrar" + "feedback" + "fallo timeout" + "modo manual"… y el HMI se queda enlazado a 10 variables sueltas.

`UDT_Valve` define la interfaz estándar para una válvula digital (con o sin feedback): comando, estado, fallos, diagnóstico y configuración. El `FB_Valve` la consume, el faceplate de HMI se enlaza con un único *binding* y todo encaja igual de un proyecto al siguiente.

---

## Variables / Interfaz

El UDT está organizado en 5 sub-estructuras.

### `Comando` — escrituras desde la lógica/HMI

| Variable | Tipo | Descripción |
|---|---|---|
| `xAbrir` | BOOL | Comando de apertura |
| `xCerrar` | BOOL | Comando de cierre |
| `xReset` | BOOL | Pulso para reconocer/borrar fallos |
| `xModoAuto` | BOOL | `TRUE` = modo automático · `FALSE` = manual (HMI) |

### `Estado` — estado real de la válvula

| Variable | Tipo | Descripción |
|---|---|---|
| `xAbierta` | BOOL | Confirmada abierta (feedback final de carrera) |
| `xCerrada` | BOOL | Confirmada cerrada (feedback final de carrera) |
| `xEnMovimiento` | BOOL | Comandada pero aún sin confirmar posición destino |
| `xListo` | BOOL | Sin fallos activos y disponible |
| `xFallo` | BOOL | OR de todos los fallos individuales |
| `xModoAutoActivo` | BOOL | Refleja en qué modo está operando realmente |

### `Fallos` — desglose para diagnóstico

| Variable | Tipo | Descripción |
|---|---|---|
| `xTimeoutAbrir` | BOOL | No se confirmó la apertura dentro de `Config.tTimeoutAbrir` |
| `xTimeoutCerrar` | BOOL | No se confirmó el cierre dentro de `Config.tTimeoutCerrar` |
| `xPosicionInvalida` | BOOL | Feedback de abierta y cerrada activos simultáneamente (cableado o final de carrera roto) |
| `xParadaEmergencia` | BOOL | Cadena de seguridad / seta abierta |

### `Diagnostico` — métricas y texto

| Variable | Tipo | Descripción |
|---|---|---|
| `diCiclos` | DINT | Contador de ciclos de apertura desde la puesta en marcha |
| `tTiempoUltimoMovimiento` | TIME | Duración del último movimiento (ayuda a detectar desgaste) |
| `sEstado` | STRING[40] | Texto descriptivo del estado actual |

### `Config` — parámetros de comportamiento

| Variable | Tipo | Descripción |
|---|---|---|
| `tTimeoutAbrir` | TIME | Tiempo máximo esperando feedback de abierta |
| `tTimeoutCerrar` | TIME | Tiempo máximo esperando feedback de cerrada |
| `xRequiereFeedback` | BOOL | `FALSE` = válvula sin finales de carrera (no se vigila timeout) |

---

## Cómo importarlo en TIA Portal

1. Descarga el archivo `udt-valve.xml`
2. En TIA Portal, abre tu proyecto
3. En el árbol del proyecto, clic derecho sobre **Tipos de datos PLC**
4. Selecciona **Importar**
5. Busca el `.xml` descargado y confirma

---

## Ejemplo de uso

```
DB_Equipos.V01_AguaEntrada : UDT_Valve
DB_Equipos.V02_DescargaTanque : UDT_Valve
```

Desde el `FB_Valve`:

```
"FB_Valve"(
    xFeedbackAbierta := %I1.0,
    xFeedbackCerrada := %I1.1,
    Valve := "DB_Equipos".V01_AguaEntrada,
    qSolenoideAbrir => %Q1.0,
    qSolenoideCerrar => %Q1.1
);
```

---

## Notas / Limitaciones conocidas

- Pensado para **válvulas todo/nada** con dos finales de carrera. Para válvulas reguladoras (analógicas) hay un UDT específico previsto (`UDT_ValveAnalog`, no incluido aún).
- Para válvulas de **simple efecto** con resorte, deja `qSolenoideCerrar` desconectado y configura `xRequiereFeedback := FALSE` si no hay final de carrera de cerrada.
- `Diagnostico.diCiclos` debería marcarse como retentivo.
- El campo `xPosicionInvalida` se activa con un retardo de 1s para evitar falsos positivos durante el movimiento.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
