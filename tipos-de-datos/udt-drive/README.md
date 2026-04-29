# UDT_Drive

> Estructura unificada para variadores de frecuencia (VFD) — comando, lectura, fallos comunes y configuración base.

**Tipo:** `UDT`
**Versión TIA Portal:** V20 *(compatible con V18 y V19)*
**Familia PLC:** S7-1200 / S7-1500

---

## ¿Qué problema resuelve?

Cada fabricante (Siemens G120/V20, ABB, Schneider, Yaskawa…) tiene su propio mapa de control word, status word y registros de fallo. Pero el 95% de las máquinas usan **siempre los mismos comandos básicos**: marcha, paro, sentido, consigna, lectura de velocidad y un puñado de fallos típicos.

`UDT_Drive` define una **capa de abstracción genérica del variador** que la lógica de máquina consume sin preocuparse del fabricante. Un FB específico por marca traduce entre el UDT y el telegrama propio del variador (PROFIBUS/PROFINET/Modbus).

---

## Variables / Interfaz

### `Comando` — escrituras desde la lógica/HMI

| Variable | Tipo | Descripción |
|---|---|---|
| `xMarcha` | BOOL | Comando de marcha |
| `xParo` | BOOL | Comando de paro (rampa) |
| `xParoRapido` | BOOL | Comando de paro rápido (rampa corta o por inercia) |
| `xReset` | BOOL | Reset de fallos |
| `xSentidoInverso` | BOOL | `FALSE` = adelante · `TRUE` = atrás |
| `xModoAuto` | BOOL | Modo auto (consigna desde lógica) o manual (consigna desde HMI) |
| `rConsignaVelocidad` | REAL | Consigna de velocidad en % o Hz (según `Config.eUnidadVelocidad`) |
| `rConsignaTorque` | REAL | Consigna de par en % (si el variador admite control de par) |

### `Estado` — lecturas reales del variador

| Variable | Tipo | Descripción |
|---|---|---|
| `xEnMarcha` | BOOL | Variador en marcha (motor energizado) |
| `xParado` | BOOL | Variador parado |
| `xListo` | BOOL | Listo para arrancar (sin fallos, alimentación OK) |
| `xFallo` | BOOL | Fallo activo |
| `xSentidoActual` | BOOL | Sentido actual de giro |
| `xConsignaAlcanzada` | BOOL | Velocidad real ≈ consigna |
| `rVelocidadActual` | REAL | Velocidad real (% o Hz) |
| `rTorqueActual` | REAL | Par real (%) |
| `rCorrienteActual` | REAL | Corriente del motor (A) |
| `rTension` | REAL | Tensión del bus DC (V) |
| `rPotencia` | REAL | Potencia activa (kW) |

### `Fallos` — fallos genéricos

| Variable | Tipo | Descripción |
|---|---|---|
| `xFalloComunicacion` | BOOL | Pérdida de comunicación con el variador |
| `xSobreCorriente` | BOOL | Disparo por sobrecorriente |
| `xSobreTension` | BOOL | Sobretensión en el bus DC |
| `xSubTension` | BOOL | Subtensión / fallo de red |
| `xSobreTemperatura` | BOOL | Variador o motor en sobretemperatura |
| `xFalloMotor` | BOOL | Fallo en el motor (cortocircuito, fuga a tierra) |
| `iCodigoFalloVendor` | INT | Código de fallo crudo del fabricante (para diagnóstico avanzado) |

### `Diagnostico` — métricas

| Variable | Tipo | Descripción |
|---|---|---|
| `rHorasFuncionamiento` | REAL | Horas acumuladas con el variador en marcha |
| `diArranques` | DINT | Contador de arranques |
| `sEstado` | STRING[40] | Texto del estado actual |

### `Config` — parámetros

| Variable | Tipo | Descripción |
|---|---|---|
| `rVelocidadMaxima` | REAL | Velocidad máxima permitida (% o Hz) |
| `rRampaAceleracion` | REAL | Rampa de aceleración (segundos para llegar al 100%) |
| `rRampaDeceleracion` | REAL | Rampa de deceleración (segundos del 100% a 0) |
| `eUnidadVelocidad` | INT | 0 = porcentaje, 1 = Hz, 2 = RPM |

---

## Cómo importarlo en TIA Portal

1. Descarga el archivo `udt-drive.xml`
2. En TIA Portal, abre tu proyecto
3. En el árbol del proyecto, clic derecho sobre **Tipos de datos PLC**
4. Selecciona **Importar**
5. Busca el `.xml` descargado y confirma

---

## Ejemplo de uso

Una variable por cada variador:

```
DB_Variadores.D01_BombaPrincipal : UDT_Drive
DB_Variadores.D02_VentiladorRefri : UDT_Drive
```

Pásalo al FB específico del fabricante (ej: `FB_DriveG120`, no incluido en este repo aún) que se ocupa del telegrama PROFINET:

```
"FB_DriveG120"(
    HwId := 271,                 // HW identifier del telegrama
    Drive := "DB_Variadores".D01_BombaPrincipal
);
```

Y desde el HMI enlazas el faceplate al UDT entero — el faceplate es **el mismo** para cualquier variador.

---

## Notas / Limitaciones conocidas

- Esta es una **capa de abstracción genérica**. La traducción al telegrama específico del variador (control word, status word) la hace un FB específico por fabricante (no incluido en este UDT).
- `Estado.rTension`, `rPotencia` y `Estado.rTorqueActual` no todos los variadores los exponen — déjalos a 0.0 si no aplica.
- Para variadores en modo control de par, `Comando.rConsignaTorque` tiene prioridad sobre `rConsignaVelocidad`.
- `Diagnostico.rHorasFuncionamiento` y `diArranques` deberían ser retentivos.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
