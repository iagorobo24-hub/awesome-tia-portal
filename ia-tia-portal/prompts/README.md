# 📝 Guía de prompts efectivos

Aprende a escribir prompts efectivos para obtener los mejores resultados de IA al trabajar con TIA Portal.

---

## 📑 Tabla de contenido

- [Principios de prompts efectivos](#principios-de-prompts-efectivos)
- [Prompts para generación de bloques](#prompts-para-generación-de-bloques)
- [Prompts para análisis de código](#prompts-para-análisis-de-código)
- [Prompts para documentación](#prompts-para-documentación)
- [Prompts para refactorización](#prompts-para-refactorización)
- [Prompts para troubleshooting](#prompts-para-troubleshooting)

---

## 🎯 Principios de prompts efectivos

### 1. Sé específico

**❌ Mal:**
```
Haz un bloque de motor
```

**✅ Bien:**
```
Genera un FB de control de motor digital con las siguientes características:

- Nombre: FB_MotorControl
- Lenguaje: SCL
- UDT de E/S: UDT_Motor

Funcionalidades:
- Máquina de estados: STOPPED → STARTING → RUNNING → FAULT
- Comandos: Start, Stop, Reset
- Sensores: Running feedback, Overload, Overheat
- Timeout: 5 segundos para feedback
- Modo: Manual/Auto
- Diagnóstico: Códigos de fallo, timestamp
```

### 2. Define claramente la estructura

**❌ Mal:**
```
Haz un bloque con entradas y salidas
```

**✅ Bien:**
```
Genera un FC con la siguiente interfaz:

ENTRADAS (Input):
- rRawValue : REAL — Valor raw del sensor
- rMinRaw : REAL — Valor raw mínimo (0.0)
- rMaxRaw : REAL — Valor raw máximo (27648.0)
- rMinEng : REAL — Valor ingeniería mínimo (-50.0)
- rMaxEng : REAL — Valor ingeniería máximo (150.0)

SALIDAS (Output):
- rScaledValue : REAL — Valor escalado
- bOutOfRange : BOOL — Fuera de rango
- iErrorCode : INT — Código de error
```

### 3. Especifica el comportamiento

**❌ Mal:**
```
El bloque debe controlar el motor
```

**✅ Bien:**
```
El bloque debe implementar la siguiente lógica:

1. Al recibir comando START:
   - Transición a estado STARTING
   - Iniciar temporizador de 5 segundos
   - Esperar feedback de motor running

2. Si feedback recibido antes de timeout:
   - Transición a estado RUNNING
   - Activar salida de motor

3. Si timeout sin feedback:
   - Transición a estado FAULT
   - Asignar código de fallo 3 (timeout)
   - Activar alarma de timeout

4. Al recibir comando STOP:
   - Transición a estado STOPPED
   - Desactivar salida de motor
   - Resetear temporizadores
```

### 4. Incluye ejemplos

**❌ Mal:**
```
El bloque debe escalar valores
```

**✅ Bien:**
```
El bloque debe escalar valores linealmente según estos ejemplos:

Ejemplo 1:
- Raw: 0 → Escalado: -50.0
- Raw: 13824 → Escalado: 50.0
- Raw: 27648 → Escalado: 150.0

Ejemplo 2:
- Raw: 6912 → Escalado: 0.0
- Raw: 20736 → Escalado: 100.0

Fórmula:
Scaled = MinEng + ((Raw - MinRaw) / (MaxRaw - MinRaw)) * (MaxEng - MinEng)
```

### 5. Especifica restricciones

**❌ Mal:**
```
Haz un bloque seguro
```

**✅ Bien:**
```
El bloque debe cumplir las siguientes restricciones de seguridad:

1. Prioridad de STOP sobre START
2. No arrancar si hay fallo activo
3. Parada de emergencia inmediata
4. Validación de todas las entradas
5. Tiempo de respuesta < 100ms
6. Diagnóstico continuo
7. No usar variables globales
8. Usar solo instrucciones de TIA Portal V20+
```

### 6. Pide comentarios

**❌ Mal:**
```
Genera el código
```

**✅ Bien:**
```
Genera el código SCL con comentarios explicativos:

- Comentario de cabecera con propósito y autor
- Comentarios en cada sección principal
- Comentarios en lógica compleja
- Comentarios en fórmulas
- Comentarios en manejo de errores
```

---

## 🧩 Prompts para generación de bloques

### Prompt 1: FC de escalado lineal

```
Genera un FC de escalado lineal con las siguientes especificaciones:

NOMBRE: FC_Escalado_Temperatura
LENGUAJE: SCL

INTERFAZ:

ENTRADAS (Input):
- rRawValue : REAL — Valor raw del sensor (0-27648)
- rMinRaw : REAL — Valor raw mínimo (por defecto: 0.0)
- rMaxRaw : REAL — Valor raw máximo (por defecto: 27648.0)
- rMinEng : REAL — Valor ingeniería mínimo (por defecto: -50.0)
- rMaxEng : REAL — Valor ingeniería máximo (por defecto: 150.0)

SALIDAS (Output):
- rScaledValue : REAL — Valor escalado en unidades de ingeniería
- bOutOfRange : BOOL — TRUE si valor raw fuera de rango
- iErrorCode : INT — Código de error (0=OK, 1=Raw<Min, 2=Raw>Max)

LÓGICA:

1. Validar entrada:
   - Si rRawValue < rMinRaw: bOutOfRange=TRUE, iErrorCode=1
   - Si rRawValue > rMaxRaw: bOutOfRange=TRUE, iErrorCode=2
   - Si rRawValue en rango: bOutOfRange=FALSE, iErrorCode=0

2. Escalado lineal:
   - Usar fórmula: rScaledValue = rMinEng + ((rRawValue - rMinRaw) / (rMaxRaw - rMinRaw)) * (rMaxEng - rMinEng)

3. Clipping:
   - Si bOutOfRange=TRUE: rScaledValue = valor más cercano al rango

REQUISITOS ADICIONALES:
- Manejo de división por cero (si rMaxRaw = rMinRaw)
- Comentarios explicativos en cada paso
- Validación de parámetros
- Código robusto y mantenible

Por favor, genera el código SCL completo.
```

### Prompt 2: FB de control de motor

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

2. TRANSICIONES:
   - STOPPED → STARTING: Comando START
   - STARTING → RUNNING: Feedback recibido antes de timeout
   - STARTING → FAULT: Timeout sin feedback
   - RUNNING → STOPPED: Comando STOP
   - RUNNING → FAULT: Fallo detectado
   - FAULT → STOPPED: Comando RESET
   - Cualquier estado → STOPPED: Comando STOP (prioridad)

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

### Prompt 3: FB de control de válvula

```
Genera un FB de control de válvula con las siguientes especificaciones:

NOMBRE: FB_ValveControl
LENGUAJE: SCL

INTERFAZ:

ENTRADAS (Input):
- bOpenCommand : BOOL — Comando de abrir
- bCloseCommand : BOOL — Comando de cerrar
- bFeedbackOpen : BOOL — Feedback de válvula abierta
- bFeedbackClosed : BOOL — Feedback de válvula cerrada
- tTimeout : TIME — Timeout para feedback (por defecto: T#10S)

SALIDAS (Output):
- bOpenOutput : BOOL — Salida de abrir válvula
- bCloseOutput : BOOL — Salida de cerrar válvula
- iState : INT — Estado actual (0=Closed, 1=Opening, 2=Open, 3=Closing, 4=Fault)
- bFault : BOOL — Fallo activo
- iFaultCode : INT — Código de fallo

LÓGICA:

1. Estados:
   - CLOSED: Válvula cerrada, lista para abrir
   - OPENING: Abriendo, esperando feedback
   - OPEN: Válvula abierta, lista para cerrar
   - CLOSING: Cerrando, esperando feedback
   - FAULT: Fallo activo

2. Transiciones:
   - CLOSED → OPENING: Comando OPEN
   - OPENING → OPEN: Feedback OPEN recibido
   - OPENING → FAULT: Timeout sin feedback
   - OPEN → CLOSING: Comando CLOSE
   - CLOSING → CLOSED: Feedback CLOSED recibido
   - CLOSING → FAULT: Timeout sin feedback
   - FAULT → CLOSED: Comando CLOSE + feedback CLOSED

3. Interlocks:
   - No abrir si ya abierta
   - No cerrar si ya cerrada
   - No abrir y cerrar simultáneamente
   - Timeout configurable

4. Diagnóstico:
   - Códigos de fallo:
     * 1: Timeout al abrir
     * 2: Timeout al cerrar
     * 3: Feedback contradictorio (ambos TRUE)

Por favor, genera el código SCL completo.
```

---

## 🔍 Prompts para análisis de código

### Prompt 1: Análisis de calidad

```
Analiza este código PLC y genera un reporte de calidad.

CÓDIGO: [pegar código]

QUiero que identifiques:

1. CÓDIGO DUPLICADO:
   - Secciones de código repetidas
   - Lógica que puede extraerse a FCs/FBs
   - Patrones repetitivos

2. ANTI-PATTERNS:
   - Uso incorrecto de variables
   - Lógica compleja innecesaria
   - Falta de comentarios
   - Nombres de variables poco descriptivos
   - Uso de variables globales

3. OPORTUNIDADES DE MEJORA:
   - Simplificación de lógica
   - Mejora de legibilidad
   - Optimización de rendimiento
   - Mejor manejo de errores
   - Uso de mejores prácticas

4. COMPLEJIDAD:
   - Complejidad ciclomática
   - Niveles de anidamiento
   - Longitud de bloques
   - Número de variables

5. SEGURIDAD:
   - Posibles vulnerabilidades
   - Falta de validación
   - Condiciones de carrera
   - Manejo de errores

Por favor, genera un reporte detallado en formato Markdown con:
- Resumen ejecutivo
- Lista de problemas encontrados
- Recomendaciones de mejora
- Prioridad de cada recomendación
```

### Prompt 2: Análisis de seguridad

```
Analiza este código PLC desde el punto de vista de seguridad.

CÓDIGO: [pegar código]

QUiero que identifiques:

1. VULNERABILIDADES:
   - Posibles ataques
   - Falta de validación de entradas
   - Condiciones de carrera
   - Overflow/underflow
   - División por cero

2. INTERLOCKS FALTANTES:
   - Interlocks de seguridad que deberían existir
   - Validación de precondiciones
   - Verificación de postcondiciones

3. MANEJO DE ERRORES:
   - Falta de manejo de errores
   - Errores silenciosos
   - Errores no reportados

4. ESTADO DEL SISTEMA:
   - Posibles estados inválidos
   - Transiciones no válidas
   - Estados bloqueados

5. DIAGNÓSTICO:
   - Falta de diagnóstico
   - Falta de logging
   - Falta de alarmas

Por favor, genera un reporte de seguridad en formato Markdown con:
- Resumen de vulnerabilidades
- Lista de problemas de seguridad
- Recomendaciones de mitigación
- Prioridad de cada recomendación
```

---

## 📚 Prompts para documentación

### Prompt 1: Documentación de bloque

```
Genera documentación completa del bloque [NOMBRE_DEL_BLOQUE].

CÓDIGO: [pegar código]

QUiero que incluyas:

1. CABECERA:
   - Nombre del bloque
   - Tipo (FB/FC/OB)
   - Lenguaje (SCL/LAD/FBD)
   - Versión de TIA Portal
   - Autor
   - Fecha
   - Propósito

2. DESCRIPCIÓN:
   - Propósito del bloque
   - Funcionalidad principal
   - Casos de uso típicos
   - Limitaciones

3. INTERFAZ:
   - Tabla de entradas (Input)
   - Tabla de salidas (Output)
   - Tabla de entradas/salidas (InOut)
   - Tabla de variables estáticas (Static)
   - Tabla de temporizadores (Timer)
   - Tabla de contadores (Counter)

4. LÓGICA:
   - Descripción de la lógica principal
   - Máquina de estados (si aplica)
   - Algoritmos clave
   - Fórmulas usadas

5. DIAGRAMA DE FLUJO:
   - Diagrama ASCII de la lógica
   - Estados y transiciones
   - Condiciones de transición

6. DIAGNÓSTICO:
   - Códigos de fallo
   - Condiciones de error
   - Mensajes de diagnóstico

7. EJEMPLOS DE USO:
   - Ejemplo 1: Caso normal
   - Ejemplo 2: Caso de fallo
   - Ejemplo 3: Caso edge

8. NOTAS:
   - Limitaciones conocidas
   - Dependencias de otros bloques
   - Consideraciones de seguridad
   - Requisitos de mantenimiento

Organiza todo en formato Markdown con tablas y bloques de código.
```

### Prompt 2: Documentación de proyecto

```
Genera documentación completa de mi proyecto de TIA Portal.

QUiero que crees un documento Markdown con las siguientes secciones:

1. PORTADA:
   - Nombre del proyecto
   - Fecha de generación
   - Versión de TIA Portal
   - Resumen ejecutivo

2. ÍNDICE:
   - Tabla de contenidos con enlaces

3. INTRODUCCIÓN:
   - Propósito del proyecto
   - Alcance
   - Arquitectura general

4. ESTRUCTURA DEL PROYECTO:
   - Diagrama de arquitectura
   - Lista de PLCs
   - Lista de bloques por tipo
   - Jerarquía de bloques

5. DOCUMENTACIÓN DE BLOQUES:
   - Para cada bloque (OB, FB, FC, DB):
     * Cabecera
     * Descripción
     * Interfaz (tablas)
     * Lógica
     * Diagrama de flujo
     * Diagnóstico
     * Ejemplos de uso

6. TABLAS DE TAGS:
   - Lista de todas las tablas de tags
   - Descripción de cada tabla
   - Tags principales

7. UDTs:
   - Lista de todos los UDTs
   - Estructura de cada UDT
   - Descripción de cada campo

8. CONFIGURACIÓN DE HARDWARE:
   - Lista de dispositivos
   - Configuración de E/S
   - Redes y comunicaciones

9. SEGURIDAD:
   - Bloques de seguridad
   - Alarmas críticas
   - Consideraciones de seguridad

10. MANTENIMIENTO:
    - Procedimientos de mantenimiento
    - Puntos de ajuste
    - Parámetros configurables

11. APÉNDICES:
    - Glosario
    - Referencias
    - Historial de cambios

Por favor, genera el documento completo en formato Markdown.
```

---

## 🔄 Prompts para refactorización

### Prompt 1: Refactorización de código duplicado

```
Refactoriza este código PLC para eliminar código duplicado.

CÓDIGO: [pegar código]

REQUISITOS:

1. ELIMINAR CÓDIGO DUPLICADO:
   - Extraer lógica repetida a FCs
   - Crear FBs reutilizables
   - Usar UDTs para estructuras comunes

2. MEJORAR LEGIBILIDAD:
   - Nombres de variables descriptivos
   - Comentarios explicativos
   - Estructura clara del código
   - Separación de responsabilidades

3. SIMPLIFICAR LÓGICA:
   - Reducir anidamiento
   - Usar funciones auxiliares
   - Eliminar condiciones redundantes

4. MANTENER FUNCIONALIDAD:
   - El comportamiento debe ser idéntico
   - No introducir bugs
   - Validar con tests

Por favor, genera el código refactorizado completo en SCL.
```

### Prompt 2: Refactorización de complejidad

```
Refactoriza este código PLC para reducir complejidad.

CÓDIGO: [pegar código]

REQUISITOS:

1. REDUCIR COMPLEJIDAD:
   - Reducir complejidad ciclomática
   - Reducir niveles de anidamiento
   - Dividir en bloques más pequeños
   - Extraer lógica a FCs auxiliares

2. MEJORAR ESTRUCTURA:
   - Separar responsabilidades
   - Usar patrones de diseño
   - Crear interfaces claras

3. MEJORAR LEGIBILIDAD:
   - Nombres descriptivos
   - Comentarios claros
   - Estructura lógica

4. MANTENER FUNCIONALIDAD:
   - Comportamiento idéntico
   - No introducir bugs
   - Validar con tests

Por favor, genera el código refactorizado completo.
```

---

## 🐛 Prompts para troubleshooting

### Prompt 1: Debug de error de compilación

```
Tengo un error de compilación en este código.

CÓDIGO: [pegar código]
ERROR: [pegar mensaje de error]

Por favor:
1. Identifica la causa del error
2. Explica por qué ocurre
3. Propón una solución
4. Genera el código corregido
```

### Prompt 2: Debug de error de runtime

```
Tengo un error de runtime en este código.

CÓDIGO: [pegar código]
SÍNTOMAS: [describir síntomas]
CONDICIONES: [describir condiciones]

Por favor:
1. Identifica la causa del error
2. Explica por qué ocurre
3. Propón una solución
4. Genera el código corregido
5. Sugiere tests para validar la solución
```

---

## 💡 Consejos finales

1. **Itera si es necesario** — El primer intento no siempre es perfecto
2. **Sé específico** — Cuanto más detallado, mejor el resultado
3. **Pide ejemplos** — Los ejemplos clarifican requisitos
4. **Valida siempre** — La IA puede cometer errores
5. **Documenta prompts útiles** — Crea una librería de prompts

---

## 📚 Recursos adicionales

- [Tutoriales](../tutoriales/) — Aprende a usar IA + TIA Portal
- [Casos de uso](../casos-de-uso/) — Ejemplos reales
- [Best practices](../best-practices/) — Mejores prácticas
- [Troubleshooting](../troubleshooting/) — Solución de problemas
