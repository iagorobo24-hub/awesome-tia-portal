# Tutorial 6: Refactorizar código con IA

> **⏱️ Tiempo estimado**: 60 minutos
> **🎯 Dificultad**: ⭐⭐⭐⭐ (Experto)
> **📋 Prerrequisitos**: Tutorial 2 completado

---

## 🎯 Objetivo

Refactorizar código PLC existente para mejorar calidad y mantenibilidad con IA. Al final tendrás:

- ✅ Código refactorizado y limpio
- ✅ Mejoras en legibilidad
- ✅ Eliminación de código duplicado
- ✅ Validación de funcionalidad

---

## 📋 Prerrequisitos

- ✅ [Tutorial 2: Generar un FB de control](./02-generar-bloque-scl.md)
- ✅ Código PLC existente para refactorizar
- ✅ MCP Server configurado

---

## 🔍 Paso 1: Analizar el código existente

### 1.1 Identificar problemas

En Claude Desktop:

```
Analiza este código PLC e identifica problemas de calidad.

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

3. OPORTUNIDADES DE MEJORA:
   - Simplificación de lógica
   - Mejora de legibilidad
   - Optimización de rendimiento
   - Mejor manejo de errores

4. COMPLEJIDAD:
   - Bloques más complejos
   - Secciones que requieren refactorización

Por favor, genera un reporte detallado en formato Markdown.
```

---

## 🔄 Paso 2: Generar código refactorizado

### 2.1 Refactorizar bloques complejos

Para cada bloque identificado:

```
Refactoriza este bloque PLC para mejorar calidad y mantenibilidad.

CÓDIGO ORIGINAL: [pegar código]

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

4. MEJORAR MANEJO DE ERRORES:
   - Validación de inputs
   - Manejo de casos edge
   - Diagnóstico claro

5. MANTENER FUNCIONALIDAD:
   - El comportamiento debe ser idéntico
   - No introducir bugs
   - Validar con tests

Por favor, genera el código refactorizado completo en SCL.
```

---

## ✅ Paso 3: Validar la refactorización

### 3.1 Compilar y comparar

1. Importa el código refactorizado
2. Compila el bloque
3. Compara con el original
4. Verifica que la funcionalidad es idéntica

### 3.2 Ejecutar tests

1. Ejecuta los tests existentes
2. Verifica que todos pasan
3. Si hay fallos, corrige el código

---

## 📊 Paso 4: Medir mejoras

### 4.1 Comparar métricas

```
Compara el código original y el refactorizado.

MÉTRICAS:
1. Líneas de código
2. Complejidad ciclomática
3. Número de bloques
4. Código duplicado
5. Comentarios

Genera una tabla comparativa en formato Markdown.
```

---

## 🎉 ¡Felicidades!

Has refactorizado tu código con IA.

---

## 📚 Qué has aprendido

1. ✅ Cómo detectar código duplicado
2. ✅ Cómo identificar anti-patterns
3. ✅ Cómo generar código refactorizado
4. ✅ Cómo validar que la funcionalidad se mantiene
5. ✅ Cómo medir mejoras

---

## 🏆 Badge de completado

¡Has completado el Tutorial 6! 💎

**Badge obtenido**: 💎 **Experto en IA + TIA Portal**

¡Has completado todos los tutoriales! 🎉

---

## 🎓 ¿Qué sigue?

Ahora que eres un experto, puedes:

- Contribuir a la comunidad
- Crear tus propias herramientas
- Compartir tu conocimiento
- Explorar proyectos avanzados
