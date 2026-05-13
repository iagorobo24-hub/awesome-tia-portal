# 📝 Plantillas y snippets

Colección de plantillas y snippets reutilizables para acelerar el desarrollo con IA + TIA Portal.

---

## 📑 Tabla de contenido

- [Plantilla de prompt para bloques](#plantilla-de-prompt-para-bloques)
- [Plantilla de configuración de MCP](#plantilla-de-configuración-de-mcp)
- [Snippets SCL comunes](#snippets-scl-comunes)
- [Plantilla de documentación de bloques](#plantilla-de-documentación-de-bloques)

---

## 📋 Plantilla de prompt para bloques

### Plantilla base

```markdown
Genera un [TIPO DE BLOQUE] con las siguientes especificaciones:

NOMBRE: [NOMBRE DEL BLOQUE]
LENGUAJE: [SCL/LAD/FBD]
UDT DE E/S: [UDT SI APLICA]

REQUISITOS:

1. [REQUISITO 1]
   - Detalle del requisito
   - Casos edge

2. [REQUISITO 2]
   - Detalle del requisito
   - Casos edge

INTERFAZ:

ENTRADAS (Input):
- [Variable] : [Tipo] — [Descripción]

SALIDAS (Output):
- [Variable] : [Tipo] — [Descripción]

LÓGICA:

1. [Paso 1]
   - Detalle del paso
   - Condiciones

2. [Paso 2]
   - Detalle del paso
   - Condiciones

REQUISITOS ADICIONALES:
- [Requisito adicional]
- [Requisito adicional]

Por favor, genera el código [LENGUAJE] completo.
```

### Ejemplo: Control de motor

```markdown
Genera un FB de control de motor digital con las siguientes especificaciones:

NOMBRE: FB_MotorControl
LENGUAJE: SCL
UDT DE E/S: UDT_Motor

REQUISITOS:

1. MÁQUINA DE ESTADOS:
   - Estado STOPPED: Motor parado, listo para arrancar
   - Estado STARTING: Iniciando, esperando feedback
   - Estado RUNNING: Motor en marcha normal
   - Estado FAULT: Fallo activo, requiere reset

2. TRANSICIONES:
   - STOPPED → STARTING: Comando START
   - STARTING → RUNNING: Feedback recibido antes de timeout
   - STARTING → FAULT: Timeout sin feedback
   - RUNNING → STOPPED: Comando STOP
   - RUNNING → FAULT: Fallo detectado
   - FAULT → STOPPED: Comando RESET

3. TIMEOUTS:
   - Timeout de feedback: 5 segundos (configurable)
   - Si no hay feedback en STARTING, ir a FAULT

4. MODO MANUAL/AUTO:
   - Manual: Comandos START/STOP desde HMI
   - Auto: Comandos desde sistema externo
   - Selector de modo en UDT

5. DIAGNÓSTICO:
   - Registrar timestamp de cada transición
   - Asignar código de fallo:
     * 1: Sobrecarga
     * 2: Sobrecalentamiento
     * 3: Timeout de feedback
     * 4: Parada de emergencia
   - Contador de horas de funcionamiento

6. ALARMAS:
   - Alarma de sobrecarga (bOverload)
   - Alarma de sobrecalentamiento (bOverheat)
   - Alarma de parada de emergencia (bEmergency)
   - Alarma de timeout

7. SEGURIDAD:
   - Prioridad de STOP sobre START
   - Parada de emergencia inmediata
   - No arrancar si hay fallo activo

8. COMENTARIOS:
   - Comentario de cabecera con propósito
   - Comentarios en cada sección
   - Comentarios en lógica de timeouts
   - Comentarios en máquina de estados

Por favor, genera el código SCL completo.
```

### Ejemplo: Control de válvula

```markdown
Genera un FB de control de válvula con las siguientes especificaciones:

NOMBRE: FB_ValveControl
LENGUAJE: SCL
UDT DE E/S: UDT_Valve

REQUISITOS:

1. MÁQUINA DE ESTADOS:
   - Estado CLOSED: Válvula cerrada
   - Estado OPENING: Abriendo, esperando feedback
   - Estado OPEN: Válvula abierta
   - State CLOSING: Cerrando, esperando feedback
   - Estado FAULT: Fallo activo, requiere reset

2. TRANSICIONES:
   - CLOSED → OPENING: Comando OPEN
   - OPENING → OPEN: Feedback abierto recibido antes de timeout
   - OPENING → FAULT: Timeout sin feedback
   - OPEN → CLOSING: Comando CLOSE
   - CLOSING → CLOSED: Feedback cerrado recibido antes de timeout
   - CLOSING → FAULT: Timeout sin feedback
   - FAULT → CLOSED: Comando RESET

3. TIMEOUTS:
   - Timeout de apertura: 10 segundos (configurable)
   - Timeout de cierre: 10 segundos (configurable)
   - Si no hay feedback en OPENING/CLOSING, ir a FAULT

4. INTERLOCKS:
   - No abrir si hay presión alta
   - No cerrar si hay flujo activo
   - Prioridad de CLOSE sobre OPEN

5. DIAGNÓSTICO:
   - Registrar timestamp de cada transición
   - Asignar código de fallo:
     * 1: Timeout de apertura
     * 2: Timeout de cierre
     * 3: Fallo de actuador
     * 4: Interlock activo
   - Contador de ciclos de apertura/cierre

6. ALARMAS:
   - Alarma de timeout de apertura
   - Alarma de timeout de cierre
   - Alarma de fallo de actuador
   - Alarma de interlock

7. SEGURIDAD:
   - Prioridad de CLOSE sobre OPEN
   - No abrir si hay interlock activo
   - No cerrar si hay interlock activo

8. COMENTARIOS:
   - Comentario de cabecera con propósito
   - Comentarios en cada sección
   - Comentarios en lógica de timeouts
   - Comentarios en máquina de estados

Por favor, genera el código SCL completo.
```

---

## ⚙️ Plantilla de configuración de MCP

### Plantilla base (JSON)

```json
{
  "mcpServers": {
    "tiaportal-mcp": {
      "command": "node",
      "args": [
        "/path/to/tiaportal-mcp/dist/index.js"
      ],
      "env": {
        "TIAPORTAL_PROJECT_PATH": "/path/to/project",
        "TIAPORTAL_OPENNESS_API_KEY": "your-api-key"
      }
    }
  }
}
```

### Plantilla base (YAML)

```yaml
mcpServers:
  tiaportal-mcp:
    command: node
    args:
      - /path/to/tiaportal-mcp/dist/index.js
    env:
      TIAPORTAL_PROJECT_PATH: /path/to/project
      TIAPORTAL_OPENNESS_API_KEY: your-api-key
```

### Ejemplo: Configuración completa

```json
{
  "mcpServers": {
    "tiaportal-mcp": {
      "command": "node",
      "args": [
        "/home/user/tiaportal-mcp/dist/index.js"
      ],
      "env": {
        "TIAPORTAL_PROJECT_PATH": "/home/user/projects/MyProject",
        "TIAPORTAL_OPENNESS_API_KEY": "sk-1234567890abcdef",
        "TIAPORTAL_LOG_LEVEL": "info",
        "TIAPORTAL_TIMEOUT": "30000"
      }
    },
    "tia-portal-openness-mcpserver": {
      "command": "python",
      "args": [
        "-m",
        "tia_portal_openness_mcpserver"
      ],
      "env": {
        "TIAPORTAL_PROJECT_PATH": "/home/user/projects/MyProject",
        "TIAPORTAL_OPENNESS_API_KEY": "sk-1234567890abcdef"
      }
    }
  }
}
```

### Ejemplo: Configuración con múltiples servidores

```json
{
  "mcpServers": {
    "tiaportal-mcp": {
      "command": "node",
      "args": [
        "/home/user/tiaportal-mcp/dist/index.js"
      ],
      "env": {
        "TIAPORTAL_PROJECT_PATH": "/home/user/projects/MyProject",
        "TIAPORTAL_OPENNESS_API_KEY": "sk-1234567890abcdef"
      }
    },
    "tia-portal-openness-mcpserver": {
      "command": "python",
      "args": [
        "-m",
        "tia_portal_openness_mcpserver"
      ],
      "env": {
        "TIAPORTAL_PROJECT_PATH": "/home/user/projects/MyProject",
        "TIAPORTAL_OPENNESS_API_KEY": "sk-1234567890abcdef"
      }
    },
    "totally-integrated-claude": {
      "command": "python",
      "args": [
        "/home/user/totally-integrated-claude/main.py"
      ],
      "env": {
        "TIAPORTAL_PROJECT_PATH": "/home/user/projects/MyProject",
        "TIAPORTAL_OPENNESS_API_KEY": "sk-1234567890abcdef"
      }
    }
  }
}
```

---

## 💻 Snippets SCL comunes

### Máquina de estados

```scl
// Máquina de estados básica
CASE eState OF
    0:  // Estado STOPPED
        // Lógica del estado STOPPED
        IF bStart THEN
            eState := 1;  // Transición a STARTING
        END_IF;

    1:  // Estado STARTING
        // Lógica del estado STARTING
        IF bFeedback THEN
            eState := 2;  // Transición a RUNNING
        END_IF;

    2:  // Estado RUNNING
        // Lógica del estado RUNNING
        IF bStop THEN
            eState := 0;  // Transición a STOPPED
        END_IF;

    3:  // Estado FAULT
        // Lógica del estado FAULT
        IF bReset THEN
            eState := 0;  // Transición a STOPPED
        END_IF;
END_CASE;
```

### Timer con timeout

```scl
// Timer con timeout
tonTimeout(IN := bStart, PT := tTimeout);

IF tonTimeout.Q THEN
    // Timeout alcanzado
    bTimeout := TRUE;
ELSE
    bTimeout := FALSE;
END_IF;
```

### Contador de ciclos

```scl
// Contador de ciclos
IF bRisingEdge AND NOT bLastState THEN
    iCycleCount := iCycleCount + 1;
END_IF;

bLastState := bRisingEdge;
```

### Promedio móvil

```scl
// Promedio móvil
rSum := rSum - arValues[iIndex] + rNewValue;
arValues[iIndex] := rNewValue;
iIndex := (iIndex + 1) MOD ARRAY_SIZE;
rAverage := rSum / ARRAY_SIZE;
```

### Filtro de paso bajo

```scl
// Filtro de paso bajo
rFiltered := rFiltered + (rInput - rFiltered) * rAlpha;
```

### Detección de flanco

```scl
// Detección de flanco ascendente
bRisingEdge := bInput AND NOT bLastInput;
bLastInput := bInput;

// Detección de flanco descendente
bFallingEdge := NOT bInput AND bLastInput;
bLastInput := bInput;
```

### Interlock básico

```scl
// Interlock básico
IF bCondition1 AND bCondition2 AND NOT bInterlock THEN
    bOutput := TRUE;
ELSE
    bOutput := FALSE;
END_IF;
```

### Manejo de errores

```scl
// Manejo de errores
IF bError THEN
    eState := 3;  // Ir a estado FAULT
    iErrorCode := iErrorNumber;
    dtErrorTime := NOW();
END_IF;
```

### Timestamp de eventos

```scl
// Timestamp de eventos
IF bEvent AND NOT bLastEvent THEN
    dtEventTime := NOW();
END_IF;

bLastEvent := bEvent;
```

### Validación de rangos

```scl
// Validación de rangos
IF rValue >= rMin AND rValue <= rMax THEN
    bInRange := TRUE;
ELSE
    bInRange := FALSE;
END_IF;
```

### Escalado de valores

```scl
// Escalado de valores
rScaled := (rInput - rInputMin) * (rOutputMax - rOutputMin) / (rInputMax - rInputMin) + rOutputMin;
```

### Histeresis

```scl
// Histeresis
IF rInput >= rHigh THEN
    bOutput := TRUE;
ELSIF rInput <= rLow THEN
    bOutput := FALSE;
END_IF;
```

### PID básico

```scl
// PID básico
rError := rSetpoint - rProcessValue;
rIntegral := rIntegral + rError * rSampleTime;
rDerivative := (rError - rLastError) / rSampleTime;
rOutput := rKp * rError + rKi * rIntegral + rKd * rDerivative;
rLastError := rError;
```

### Secuenciador

```scl
// Secuenciador
CASE iStep OF
    0:  // Paso 1
        IF bStep1Complete THEN
            iStep := 1;
        END_IF;

    1:  // Paso 2
        IF bStep2Complete THEN
            iStep := 2;
        END_IF;

    2:  // Paso 3
        IF bStep3Complete THEN
            iStep := 0;  // Volver al inicio
        END_IF;
END_CASE;
```

### Watchdog

```scl
// Watchdog
tonWatchdog(IN := NOT bHeartbeat, PT := tWatchdogTimeout);

IF tonWatchdog.Q THEN
    // Watchdog timeout
    bWatchdogTimeout := TRUE;
END_IF;
```

### Debounce

```scl
// Debounce
tonDebounce(IN := bInput, PT := tDebounceTime);

IF tonDebounce.Q THEN
    bOutput := TRUE;
ELSE
    bOutput := FALSE;
END_IF;
```

### Limitador de velocidad

```scl
// Limitador de velocidad
rRamp := rRamp + rRampRate * rSampleTime;

IF rInput > rRamp THEN
    rOutput := rRamp;
ELSIF rInput < rRamp THEN
    rOutput := rRamp;
ELSE
    rOutput := rInput;
END_IF;
```

### Selección de modo

```scl
// Selección de modo
IF bModeAuto THEN
    // Modo automático
    bOutput := bAutoCommand;
ELSE
    // Modo manual
    bOutput := bManualCommand;
END_IF;
```

### Prioridad de comandos

```scl
// Prioridad de comandos
IF bEmergencyStop THEN
    bOutput := FALSE;
ELSIF bStop THEN
    bOutput := FALSE;
ELSIF bStart THEN
    bOutput := TRUE;
END_IF;
```

### Diagnóstico de fallos

```scl
// Diagnóstico de fallos
IF bFault1 THEN
    iFaultCode := 1;
ELSIF bFault2 THEN
    iFaultCode := 2;
ELSIF bFault3 THEN
    iFaultCode := 3;
ELSE
    iFaultCode := 0;
END_IF;
```

### Logging de eventos

```scl
// Logging de eventos
IF bEvent AND NOT bLastEvent THEN
    // Registrar evento
    iEventCount := iEventCount + 1;
    dtLastEventTime := NOW();
END_IF;

bLastEvent := bEvent;
```

### Validación de precondiciones

```scl
// Validación de precondiciones
IF bPrecondition1 AND bPrecondition2 AND bPrecondition3 THEN
    bReady := TRUE;
ELSE
    bReady := FALSE;
END_IF;
```

### Verificación de postcondiciones

```scl
// Verificación de postcondiciones
IF bPostcondition1 AND bPostcondition2 AND bPostcondition3 THEN
    bSuccess := TRUE;
ELSE
    bSuccess := FALSE;
END_IF;
```

---

## 📖 Plantilla de documentación de bloques

### Plantilla base

```markdown
# [NOMBRE DEL BLOQUE]

## Descripción

[Breve descripción del propósito del bloque]

## Interfaz

### Entradas (Input)

| Variable | Tipo | Descripción |
|----------|------|-------------|
| [Variable] | [Tipo] | [Descripción] |

### Salidas (Output)

| Variable | Tipo | Descripción |
|----------|------|-------------|
| [Variable] | [Tipo] | [Descripción] |

## Máquina de estados

| Estado | Descripción |
|--------|-------------|
| [Estado] | [Descripción] |

## Transiciones

| Desde | Hasta | Condición |
|-------|-------|-----------|
| [Estado] | [Estado] | [Condición] |

## Timeout

| Timeout | Valor | Descripción |
|---------|-------|-------------|
| [Timeout] | [Valor] | [Descripción] |

## Alarmas

| Alarma | Descripción |
|--------|-------------|
| [Alarma] | [Descripción] |

## Códigos de fallo

| Código | Descripción |
|--------|-------------|
| [Código] | [Descripción] |

## Diagnóstico

| Variable | Descripción |
|----------|-------------|
| [Variable] | [Descripción] |

## Ejemplo de uso

```scl
// Ejemplo de uso
[Nombre del bloque](
    bStart := TRUE,
    bStop := FALSE,
    bFeedback := TRUE
);
```

## Notas

- [Nota 1]
- [Nota 2]

## Versión

- **Versión**: [Versión]
- **Fecha**: [Fecha]
- **Autor**: [Autor]
```

### Ejemplo: FB_MotorControl

```markdown
# FB_MotorControl

## Descripción

Control de motor digital con máquina de estados, diagnóstico y alarmas.

## Interfaz

### Entradas (Input)

| Variable | Tipo | Descripción |
|----------|------|-------------|
| bStart | Bool | Comando de arranque |
| bStop | Bool | Comando de parada |
| bReset | Bool | Comando de reset de fallo |
| bEmergency | Bool | Parada de emergencia |
| bFeedback | Bool | Feedback de motor en marcha |
| bModeAuto | Bool | TRUE = Auto, FALSE = Manual |
| bOverload | Bool | Sensor de sobrecarga |
| bOverheat | Bool | Sensor de sobrecalentamiento |
| tTimeout | Time | Timeout de feedback (5 segundos) |

### Salidas (Output)

| Variable | Tipo | Descripción |
|----------|------|-------------|
| bOutput | Bool | Salida al motor |
| bRunning | Bool | Motor en marcha |
| bFault | Bool | Fallo activo |
| bAlarmOverload | Bool | Alarma de sobrecarga |
| bAlarmOverheat | Bool | Alarma de sobrecalentamiento |
| bAlarmEmergency | Bool | Alarma de parada de emergencia |
| bAlarmTimeout | Bool | Alarma de timeout |
| iFaultCode | Int | Código de fallo |
| dtFaultTime | DateTime | Timestamp del fallo |
| rOperatingHours | Real | Horas de funcionamiento |

## Máquina de estados

| Estado | Descripción |
|--------|-------------|
| STOPPED | Motor parado, listo para arrancar |
| STARTING | Iniciando, esperando feedback |
| RUNNING | Motor en marcha normal |
| FAULT | Fallo activo, requiere reset |

## Transiciones

| Desde | Hasta | Condición |
|-------|-------|-----------|
| STOPPED | STARTING | Comando START |
| STARTING | RUNNING | Feedback recibido antes de timeout |
| STARTING | FAULT | Timeout sin feedback |
| RUNNING | STOPPED | Comando STOP |
| RUNNING | FAULT | Fallo detectado |
| FAULT | STOPPED | Comando RESET |

## Timeout

| Timeout | Valor | Descripción |
|---------|-------|-------------|
| tTimeout | T#5S | Timeout de feedback |

## Alarmas

| Alarma | Descripción |
|--------|-------------|
| bAlarmOverload | Alarma de sobrecarga |
| bAlarmOverheat | Alarma de sobrecalentamiento |
| bAlarmEmergency | Alarma de parada de emergencia |
| bAlarmTimeout | Alarma de timeout |

## Códigos de fallo

| Código | Descripción |
|--------|-------------|
| 1 | Sobrecarga |
| 2 | Sobrecalentamiento |
| 3 | Timeout de feedback |
| 4 | Parada de emergencia |

## Diagnóstico

| Variable | Descripción |
|----------|-------------|
| iFaultCode | Código de fallo actual |
| dtFaultTime | Timestamp del fallo |
| rOperatingHours | Horas de funcionamiento |

## Ejemplo de uso

```scl
// Ejemplo de uso
FB_MotorControl(
    bStart := bStartCommand,
    bStop := bStopCommand,
    bReset := bResetCommand,
    bEmergency := bEmergencyStop,
    bFeedback := bMotorFeedback,
    bModeAuto := bAutoMode,
    bOverload := bOverloadSensor,
    bOverheat := bOverheatSensor,
    tTimeout := T#5S
);
```

## Notas

- Prioridad de STOP sobre START
- Parada de emergencia inmediata
- No arrancar si hay fallo activo

## Versión

- **Versión**: 0.1
- **Fecha**: 2024-01-15
- **Autor**: Iago Durán
```

---

## 📊 Resumen de plantillas y snippets

| Categoría | Plantillas/Snippets | Uso |
|-----------|---------------------|-----|
| **Prompts** | 3 plantillas | Generar bloques con IA |
| **Configuración MCP** | 3 plantillas | Configurar servidores MCP |
| **Snippets SCL** | 25 snippets | Código reutilizable |
| **Documentación** | 2 plantillas | Documentar bloques |

---

## 💡 Consejos para usar plantillas y snippets

1. **Personaliza las plantillas** — Ajusta a tus necesidades
2. **Mantén librería de snippets** — Reutiliza código común
3. **Documenta tus snippets** — Añade comentarios
4. **Versiona tus plantillas** — Mantén historial de cambios
5. **Comparte con el equipo** — Mejora colaboración

---

## 📚 Recursos adicionales

- [Tutoriales](../tutoriales/) — Aprende a usar IA + TIA Portal
- [Casos de uso](../casos-de-uso/) — Ejemplos reales
- [Guía de prompts](../prompts/) — Prompts efectivos
- [Best practices](../best-practices/) — Mejores prácticas
