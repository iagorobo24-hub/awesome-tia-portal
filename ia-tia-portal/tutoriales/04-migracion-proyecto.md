# Tutorial 4: Migrar un proyecto antiguo con ayuda de IA

> **⏱️ Tiempo estimado**: 90 minutos
> **🎯 Dificultad**: ⭐⭐⭐ (Avanzado)
> **📋 Prerrequisitos**: Tutorial 2 completado

---

## 🎯 Objetivo

Migrar un proyecto de TIA Portal V15 a V20 con ayuda de Inteligencia Artificial. Al final de este tutorial tendrás:

- ✅ Proyecto migrado a TIA Portal V20
- ✅ Bloques obsoletos reemplazados
- ✅ Funcionalidad validada
- ✅ Documentación de cambios

---

## 📋 Prerrequisitos

- ✅ [Tutorial 2: Generar un FB de control](./02-generar-bloque-scl.md)
- ✅ Proyecto en TIA Portal V15 (o versión anterior)
- ✅ TIA Portal V20 instalado
- ✅ MCP Server configurado

---

## 🚀 Paso 1: Analizar el proyecto antiguo

### 1.1 Exportar bloques del proyecto antiguo

En TIA Portal V15:

1. Abre el proyecto
2. Exporta todos los bloques como XML (SimaticML)
3. Guarda los archivos en una carpeta

### 1.2 Analizar con IA

En Claude Desktop:

```
Analiza estos bloques exportados de TIA Portal V15.

Quiero que identifiques:

1. BLOQUES OBSOLETOS:
   - Bloques que usan instrucciones obsoletas
   - Bloques con patrones desaconsejados
   - Bloques que pueden mejorarse

2. INSTRUCCIONES OBSOLETAS:
   - Lista de instrucciones obsoletas usadas
   - Instrucciones equivalentes en V20
   - Ejemplos de migración

3. PATRONES A MEJORAR:
   - Código duplicado
   - Anti-patterns
   - Oportunidades de refactorización

4. COMPLEJIDAD:
   - Bloques más complejos
   - Bloques que requieren más atención

Por favor, genera un reporte detallado en formato Markdown.
```

---

## 🔄 Paso 2: Generar bloques equivalentes modernos

### 2.1 Migrar bloques obsoletos

Para cada bloque obsoleto, pide:

```
Genera una versión moderna de este bloque para TIA Portal V20.

BLOQUE ORIGINAL: [pegar código del bloque antiguo]

REQUISITOS:
1. Reemplazar instrucciones obsoletas por equivalentes modernas
2. Mantener la misma funcionalidad
3. Mejorar la legibilidad
4. Añadir comentarios explicativos
5. Usar mejores prácticas de V20

Por favor, genera el código SCL completo.
```

### 2.2 Validar la funcionalidad

1. Importa el bloque generado en TIA Portal V20
2. Compila el bloque
3. Compara la lógica con el original
4. Verifica que la funcionalidad es equivalente

---

## ✅ Paso 3: Validar el proyecto migrado

### 3.1 Compilar todo el proyecto

1. Importa todos los bloques migrados
2. Compila el proyecto completo
3. Corrige errores de compilación

### 3.2 Probar funcionalidad crítica

1. Identifica la funcionalidad crítica del proyecto
2. Crea casos de prueba
3. Ejecuta los tests
4. Verifica que todo funciona correctamente

---

## 📝 Paso 4: Documentar cambios

### 4.1 Generar reporte de migración

```
Genera un reporte de migración del proyecto.

INCLUYE:
1. Resumen de cambios
2. Bloques migrados
3. Instrucciones reemplazadas
4. Mejoras realizadas
5. Problemas encontrados y soluciones
6. Recomendaciones futuras

Formato: Markdown
```

---

## 🎉 ¡Felicidades!

Has migrado tu proyecto a TIA Portal V20 con IA.

---

## 📚 Qué has aprendido

1. ✅ Cómo analizar proyectos antiguos
2. ✅ Cómo identificar bloques obsoletos
3. ✅ Cómo generar bloques equivalentes modernos
4. ✅ Cómo validar la migración
5. ✅ Cómo documentar cambios

---

## 🏆 Badge de completado

¡Has completado el Tutorial 4! 🥇

**Badge obtenido**: 🥇 **Avanzado en IA + TIA Portal**

Continúa con el [Tutorial 5: Testing automatizado](./05-testing-automatizado.md).
