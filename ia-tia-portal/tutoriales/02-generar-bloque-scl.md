# Tutorial 2: Generar un FB de control desde lenguaje natural

> **⏱️ Tiempo estimado**: 60 minutos
> **🎯 Dificultad**: ⭐⭐ (Intermedio)
> **📋 Prerrequisitos**: Tutorial 1 completado

---

## 🎯 Objetivo

Generar un bloque de función complejo (FB) con lógica de estado usando Inteligencia Artificial. Al final de este tutorial tendrás:

- ✅ Un FB de control de motor con máquina de estados
- ✅ Estructura de E/S basada en UDT
- ✅ Lógica de manual/auto con timeouts
- ✅ Sistema de diagnóstico y alarmas

---

## 📋 Prerrequisitos

Antes de empezar, asegúrate de haber completado:

- ✅ [Tutorial 1: Tu primer proyecto con IA + TIA Portal](./01-primeros-pasos-mcp.md)
- ✅ TIA Portal abierto con un proyecto
- ✅ MCP Server configurado y funcionando

---

## 🎨 Paso 1: Preparar el UDT de motor

### 1.1 Crear el UDT

En TIA Portal, crea un UDT llamado `UDT_Motor` con la siguiente estructura:

```scl
TYPE "UDT_Motor" : STRUCT
    // Comandos
    bStart : BOOL;        // Comando de arranque
    bStop : BOOL;         // Comando de parada
    bReset : BOOL;        // Reset de fallos

    // Estado
    bRunning : BOOL;      // Motor en marcha
    bStopped : BOOL;      // Motor parado
    bFault : BOOL;        // Fallo activo
    bWarning : BOOL;      // Aviso activo

    // Fallos
    bOverload : BOOL;     // Sobrecarga
    bOverheat : BOOL;     // Sobrecalentamiento
    bEmergency : BOOL;    // Parada de emergencia

    // Diagnóstico
    iFaultCode : INT;     // Código de fallo
    tFaultTime : TIME;    // Timestamp del fallo
    rRuntime : REAL;      // Horas de funcionamiento

    // Configuración
    tTimeout : TIME;      // Timeout para feedback
    bAutoMode : BOOL;     // Modo automático
END_STRUCT
END_TYPE
```

### 1.2 Guardar el UDT

Guarda el UDT en tu proyecto. Lo usaremos como estructura de E/S del FB.

---

## 🤖 Paso 2: Generar el FB con IA

### 2.1 Escribir un prompt detallado

En Claude Desktop, escribe:

```
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

2. LÓGICA DE CONTROL:
   - Comando START: Transición STOPPED → STARTING
   - Comando STOP: Transición cualquier estado → STOPPED
   - Feedback RUNNING: Transición STARTING → RUNNING
   - Timeout sin feedback: Transición STARTING → FAULT
   - Fallo detectado: Transición cualquier estado → FAULT
   - Comando RESET: Transición FAULT → STOPPED

3. TIMEOUTS:
   - Timeout de feedback: 5 segundos (configurable)
   - Si no hay feedback en STARTING, ir a FAULT

4. MODO MANUAL/AUTO:
   - Manual: Comandos START/STOP desde HMI
   - Auto: Comandos desde sistema externo
   - Selector de modo en UDT

5. DIAGNÓSTICO:
   - Registrar timestamp de cada transición de estado
   - Asignar código de fallo según tipo:
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
   - Añadir comentarios explicativos en cada sección
   - Documentar la máquina de estados
   - Explicar la lógica de timeouts

El FB debe ser robusto, bien documentado y fácil de mantener.
```

### 2.2 Revisar el código generado

Claude generará un FB completo. Revisa:

- ✅ La máquina de estados está bien definida
- ✅ Los timeouts se implementan correctamente
- ✅ El diagnóstico es completo
- ✅ Hay comentarios explicativos
- ✅ La lógica de seguridad es correcta

Si algo no te gusta, pide mejoras:

```
El código está bien, pero:
1. Añade más comentarios en la sección de timeouts
2. Mejora la legibilidad de la máquina de estados
3. Añade una sección de inicialización
```

---

## 📥 Paso 3: Importar el FB en TIA Portal

### 3.1 Crear el FB

1. En TIA Portal, ve a tu PLC
2. Haz clic derecho en "Bloques de programa"
3. Selecciona "Añadir nuevo bloque"
4. Elige "FB" (Function Block)
5. Nombre: `FB_MotorControl`
6. Lenguaje: SCL
7. Clic en "Añadir"

### 3.2 Configurar la interfaz

1. Abre el bloque
2. En la sección "Interface", añade:
   - **Entrada**: `Motor` de tipo `UDT_Motor`
   - **Salida**: `Motor` de tipo `UDT_Motor`
   - **Entrada/Salida**: `Motor` de tipo `UDT_Motor`

> **Nota**: Para este ejemplo, usaremos `Motor` como entrada/salida (InOut).

### 3.3 Pegar el código

1. Borra el código por defecto
2. Pega el código generado por Claude
3. Guarda el bloque (Ctrl+S)

---

## ✅ Paso 4: Compilar y verificar

### 4.1 Compilar el bloque

1. Haz clic derecho en el bloque
2. Selecciona "Compilar"
3. Verifica que no haya errores

Si hay errores, pide a Claude que los corrija:

```
El bloque tiene errores de compilación:
[pegar errores aquí]

Por favor, corrige el código para que compile sin errores.
```

### 4.2 Verificar la lógica

Revisa el código generado:

1. **Máquina de estados** — ¿Están bien definidos los estados?
2. **Timeouts** — ¿Se implementan correctamente?
3. **Diagnóstico** — ¿Se registran los fallos?
4. **Seguridad** — ¿Hay prioridad de STOP sobre START?

---

## 🧪 Paso 5: Probar el FB

### 5.1 Crear una instancia del FB

1. En OB1, crea una instancia del FB:
   ```scl
   "Motor_1" : "FB_MotorControl";
   ```

2. Crea una DB para la instancia:
   ```scl
   "DB_Motor_1" : { "Motor_1" };
   ```

### 5.2 Crear una tabla de variables

1. Abre la tabla de variables
2. Añade las siguientes variables:

| Variable | Tipo | Valor inicial |
|----------|------|---------------|
| Motor_1.Motor.bStart | BOOL | FALSE |
| Motor_1.Motor.bStop | BOOL | FALSE |
| Motor_1.Motor.bReset | BOOL | FALSE |
| Motor_1.Motor.bRunning | BOOL | FALSE |
| Motor_1.Motor.bFault | BOOL | FALSE |
| Motor_1.Motor.bOverload | BOOL | FALSE |
| Motor_1.Motor.tTimeout | TIME | T#5S |

### 5.3 Probar la máquina de estados

**Test 1: Arranque normal**

1. Pon `Motor_1.Motor.bStart` a TRUE
2. Observa que el estado cambia a STARTING
3. Después de 5 segundos, el estado debería cambiar a RUNNING
4. `Motor_1.Motor.bRunning` debería ser TRUE

**Test 2: Parada normal**

1. Pon `Motor_1.Motor.bStop` a TRUE
2. Observa que el estado cambia a STOPPED
3. `Motor_1.Motor.bRunning` debería ser FALSE

**Test 3: Timeout de feedback**

1. Pon `Motor_1.Motor.bStart` a TRUE
2. No simules feedback (deja `Motor_1.Motor.bRunning` en FALSE)
3. Después de 5 segundos, el estado debería cambiar a FAULT
4. `Motor_1.Motor.bFault` debería ser TRUE
5. `Motor_1.Motor.iFaultCode` debería ser 3 (timeout)

**Test 4: Reset de fallo**

1. Pon `Motor_1.Motor.bReset` a TRUE
2. Observa que el estado cambia a STOPPED
3. `Motor_1.Motor.bFault` debería ser FALSE

**Test 5: Fallo de sobrecarga**

1. Pon `Motor_1.Motor.bOverload` a TRUE
2. El estado debería cambiar a FAULT inmediatamente
3. `Motor_1.Motor.iFaultCode` debería ser 1 (sobrecarga)

---

## 🎉 ¡Felicidades!

Has generado un FB de control complejo con IA. Ahora puedes:

- ✅ Usar este FB en tu proyecto
- ✅ Modificarlo según tus necesidades
- ✅ Generar más FBs con IA
- ✅ Continuar con el [Tutorial 3](./03-documentacion-automatica.md)

---

## 📚 Qué has aprendido

En este tutorial has aprendido:

1. ✅ Cómo escribir prompts detallados para bloques complejos
2. ✅ Cómo generar FBs con máquinas de estado
3. ✅ Cómo usar UDTs como estructura de E/S
4. ✅ Cómo implementar timeouts y diagnóstico
5. ✅ Cómo probar bloques generados por IA

---

## 🔄 Próximos pasos

Ahora que ya has generado un FB complejo, puedes:

- **Tutorial 3**: Documentar tu proyecto con IA
- **Tutorial 4**: Migrar proyectos antiguos
- **Guía de prompts**: Aprender prompts avanzados
- **Casos de uso**: Ver ejemplos reales

---

## 💡 Consejos adicionales

1. **Sé específico con los requisitos** — Cuanto más detallado sea tu prompt, mejor será el código
2. **Define claramente la máquina de estados** — Dibuja el diagrama antes de pedir el código
3. **Especifica todos los casos edge** — Piensa en qué puede salir mal
4. **Pide comentarios** — El código generado es más fácil de mantener si está bien documentado
5. **Itera si es necesario** — Si el código no es perfecto, pide mejoras específicas

---

## 📖 Recursos adicionales

- [Guía de prompts para bloques complejos](../prompts/prompts-generacion-bloques.md)
- [Best practices para FBs](../best-practices/prompts-efectivos.md)
- [Casos de uso de control de motores](../casos-de-uso/)

---

## 🏆 Badge de completado

¡Has completado el Tutorial 2! 🥈

**Badge obtenido**: 🥈 **Intermedio en IA + TIA Portal**

Continúa con el [Tutorial 3: Documentación automática](./03-documentacion-automatica.md) para avanzar hacia el badge de Avanzado.
