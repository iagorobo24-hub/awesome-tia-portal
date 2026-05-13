# 📚 Best practices y patrones

Guía de mejores prácticas y patrones para usar IA + TIA Portal de forma segura y efectiva.

---

## 📑 Tabla de contenido

- [Seguridad industrial](#seguridad-industrial)
- [Prompts efectivos](#prompts-efectivos)
- [Validación de código generado por IA](#validación-de-código-generado-por-ia)
- [Workflow recomendado](#workflow-recomendado)
- [Anti-patterns](#anti-patterns)

---

## 🔒 Seguridad industrial

### Principios de seguridad

1. **Validación siempre** — Nunca confíes ciegamente en código generado por IA
2. **Pruebas exhaustivas** — Prueba todo código en simulación antes de producción
3. **Revisión por pares** — Siempre revisa código crítico con otro ingeniero
4. **Documentación de cambios** — Documenta todos los cambios generados por IA
5. **Rollback plan** — Siempre ten un plan de rollback

### Checklist de seguridad

Antes de desplegar código generado por IA a producción:

- [ ] Código revisado manualmente
- [ ] Compilado sin errores
- [ ] Probado en simulación
- [ ] Probado en PLC de prueba
- [ ] Documentado
- [ ] Revisado por pares
- [ ] Plan de rollback definido
- [ ] Backup del proyecto anterior

### Niveles de criticidad

| Nivel | Requisitos | Ejemplos |
|-------|------------|----------|
| **Crítico** | Revisión por pares, pruebas exhaustivas, rollback plan | Seguridad, paradas de emergencia |
| **Alto** | Revisión manual, pruebas en simulación | Control de procesos principales |
| **Medio** | Revisión rápida, pruebas básicas | Control de procesos secundarios |
| **Bajo** | Validación básica | Diagnóstico, logging |

### Ejemplo de validación de seguridad

```
Valida este código generado por IA desde el punto de vista de seguridad.

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

Por favor, genera un reporte de seguridad en formato Markdown.
```

---

## 💬 Prompts efectivos

### Principios de prompts efectivos

1. **Sé específico** — Cuanto más detallado, mejor el resultado
2. **Define estructura** — Especifica claramente la interfaz
3. **Especifica comportamiento** — Describe la lógica paso a paso
4. **Incluye ejemplos** — Proporciona ejemplos de entrada/salida
5. **Especifica restricciones** — Define limitaciones y requisitos
6. **Pide comentarios** — Solicita código bien documentado

### Plantilla de prompt efectivo

```
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

### Ejemplos de prompts buenos vs malos

#### ❌ Mal: Demasiado genérico

```
Haz un bloque de motor
```

#### ✅ Bien: Específico y detallado

```
Genera un FB de control de motor digital con las siguientes características:

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

---

## ✅ Validación de código generado por IA

### Proceso de validación

#### 1. Validación sintáctica

```powershell
# Compilar bloque
tia-portal compile-block -block "FB_MotorControl"

# Verificar errores
if ($LASTEXITCODE -ne 0) {
    Write-Error "Errores de compilación detectados"
    exit 1
}
```

#### 2. Validación de lógica

```
Valida la lógica de este bloque generado por IA.

CÓDIGO: [pegar código]

QUiero que verifiques:

1. CORRECTEZ:
   - La lógica implementa los requisitos
   - No hay bugs obvios
   - Los casos edge están cubiertos

2. COMPLETITUD:
   - Todos los requisitos están implementados
   - No falta funcionalidad
   - El código es completo

3. ROBUSTEZ:
   - Manejo de errores
   - Validación de entradas
   - Casos edge cubiertos

4. LEGIBILIDAD:
   - Nombres descriptivos
   - Comentarios claros
   - Estructura lógica

Por favor, genera un reporte de validación en formato Markdown.
```

#### 3. Validación de seguridad

```
Valida este código desde el punto de vista de seguridad.

CÓDIGO: [pegar código]

QUiero que identifiques:

1. VULNERABILIDADES:
   - Posibles ataques
   - Falta de validación
   - Condiciones de carrera

2. INTERLOCKS FALTANTES:
   - Interlocks de seguridad
   - Validación de precondiciones

3. MANEJO DE ERRORES:
   - Falta de manejo de errores
   - Errores silenciosos

Por favor, genera un reporte de seguridad.
```

#### 4. Pruebas en simulación

```powershell
# Crear casos de prueba
$testCases = @(
    @{ Name = "Test 1"; Input = @{ Start = $true }; Expected = @{ Running = $true } }
    @{ Name = "Test 2"; Input = @{ Stop = $true }; Expected = @{ Running = $false } }
    @{ Name = "Test 3"; Input = @{ Overload = $true }; Expected = @{ Fault = $true } }
)

# Ejecutar pruebas
foreach ($test in $testCases) {
    Write-Host "Ejecutando: $($test.Name)"
    # Ejecutar test
    # Verificar resultado
}
```

### Checklist de validación

- [ ] Compila sin errores
- [ ] Lógica correcta
- [ ] Requisitos implementados
- [ ] Casos edge cubiertos
- [ ] Manejo de errores
- [ ] Validación de entradas
- [ ] Comentarios claros
- [ ] Nombres descriptivos
- [ ] Probado en simulación
- [ ] Revisado por pares

---

## 🔄 Workflow recomendado

### Flujo de trabajo completo

```
1. PLANIFICACIÓN
   ├── Definir requisitos
   ├── Diseñar arquitectura
   └── Crear prompt detallado

2. GENERACIÓN
   ├── Generar código con IA
   ├── Revisar código generado
   └── Iterar si es necesario

3. VALIDACIÓN
   ├── Compilar bloque
   ├── Validar lógica
   ├── Validar seguridad
   └── Probar en simulación

4. REVISIÓN
   ├── Revisar código manualmente
   ├── Revisar con pares
   └── Documentar cambios

5. DESPLIEGUE
   ├── Importar en TIA Portal
   ├── Compilar proyecto
   ├── Descargar a PLC de prueba
   └── Probar en PLC de prueba

6. PRODUCCIÓN
   ├── Descargar a PLC de producción
   ├── Monitorear comportamiento
   └── Documentar resultados
```

### Script de workflow

```powershell
# Workflow de desarrollo con IA
# workflow-ia-tia-portal.ps1

param(
    [string]$PromptFile,
    [string]$OutputPath
)

# 1. Leer prompt
$prompt = Get-Content $PromptFile

# 2. Generar código con IA
$code = Invoke-AIAPI -prompt $prompt

# 3. Guardar código
$code | Out-File "$OutputPath\generated.scl"

# 4. Compilar
tia-portal compile-block -file "$OutputPath\generated.scl"

# 5. Validar
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Compilación exitosa"

    # 6. Probar en simulación
    tia-portal test-in-simulation -file "$OutputPath\generated.scl"

    # 7. Revisar
    Write-Host "⚠️ Revisa el código manualmente antes de desplegar"
} else {
    Write-Host "❌ Errores de compilación"
    exit 1
}
```

---

## 🚫 Anti-patterns

### Anti-patterns comunes

#### 1. Confianza ciega en IA

**❌ Anti-pattern:**
```
Genera un bloque de control de motor.
[Usar código directamente sin revisar]
```

**✅ Correcto:**
```
Genera un bloque de control de motor con requisitos detallados.
[Revisar código]
[Validar lógica]
[Probar en simulación]
[Revisar con pares]
```

#### 2. Prompts demasiado genéricos

**❌ Anti-pattern:**
```
Haz un bloque
```

**✅ Correcto:**
```
Genera un FB de control de motor con:
- Máquina de estados: STOPPED → STARTING → RUNNING → FAULT
- Timeout de 5 segundos
- Modo manual/auto
- Diagnóstico completo
```

#### 3. Sin validación

**❌ Anti-pattern:**
```
[Generar código]
[Usar directamente en producción]
```

**✅ Correcto:**
```
[Generar código]
[Compilar]
[Validar lógica]
[Probar en simulación]
[Probar en PLC de prueba]
[Desplegar a producción]
```

#### 4. Sin documentación

**❌ Anti-pattern:**
```
[Generar código sin comentarios]
```

**✅ Correcto:**
```
Genera código con comentarios explicativos:
- Comentario de cabecera
- Comentarios en cada sección
- Comentarios en lógica compleja
```

#### 5. Sin plan de rollback

**❌ Anti-pattern:**
```
[Desplegar código nuevo]
[No tener backup]
```

**✅ Correcto:**
```
[Backup del proyecto anterior]
[Desplegar código nuevo]
[Monitorear comportamiento]
[Rollback si hay problemas]
```

### Lista de anti-patterns a evitar

| Anti-pattern | Por qué es malo | Cómo evitarlo |
|--------------|----------------|---------------|
| **Confianza ciega** | IA puede cometer errores | Siempre revisar y validar |
| **Prompts genéricos** | Resultados pobres | Ser específico y detallado |
| **Sin validación** | Bugs en producción | Validar exhaustivamente |
| **Sin documentación** | Código difícil de mantener | Pedir comentarios |
| **Sin rollback** | No se puede revertir | Tener siempre backup |
| **Sin pruebas** | Comportamiento inesperado | Probar en simulación |
| **Sin revisión por pares** | Errores pasan desapercibidos | Revisar con otros |
| **Sin logging** | Difícil de depurar | Añadir logging |
| **Sin alarmas** | Problemas no detectados | Añadir alarmas |
| **Sin diagnóstico** | Difícil de troubleshooting | Añadir diagnóstico |

---

## 📊 Resumen de best practices

| Categoría | Best practice | Implementación |
|-----------|---------------|----------------|
| **Seguridad** | Validar siempre | Checklist de seguridad |
| **Prompts** | Ser específico | Plantilla de prompt |
| **Validación** | Pruebas exhaustivas | Proceso de validación |
| **Workflow** | Flujo estructurado | Script de workflow |
| **Anti-patterns** | Evitar errores comunes | Lista de anti-patterns |

---

## 💡 Consejos finales

1. **Sé específico** — Cuanto más detallado el prompt, mejor el resultado
2. **Valida siempre** — Nunca confíes ciegamente en código generado por IA
3. **Itera si es necesario** — El primer intento no siempre es perfecto
4. **Documenta todo** — Documenta prompts, cambios y decisiones
5. **Mantén librería de prompts** — Reutiliza prompts exitosos

---

## 📚 Recursos adicionales

- [Tutoriales](../tutoriales/) — Aprende a usar IA + TIA Portal
- [Casos de uso](../casos-de-uso/) — Ejemplos reales
- [Guía de prompts](../prompts/) — Prompts efectivos
- [Troubleshooting](../troubleshooting/) — Solución de problemas
