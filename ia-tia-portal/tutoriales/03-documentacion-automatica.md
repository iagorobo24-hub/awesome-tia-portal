# Tutorial 3: Documentar todo tu proyecto con IA

> **⏱️ Tiempo estimado**: 40 minutos
> **🎯 Dificultad**: ⭐⭐ (Intermedio)
> **📋 Prerrequisitos**: Tutorial 1 completado

---

## 🎯 Objetivo

Generar documentación completa de todos los bloques de tu proyecto usando Inteligencia Artificial. Al final de este tutorial tendrás:

- ✅ Documentación estructurada de todos los bloques
- ✅ Diagramas de flujo de la lógica
- ✅ Descripción de interfaces y variables
- ✅ Documentación en formato Markdown

---

## 📋 Prerrequisitos

Antes de empezar, asegúrate de haber completado:

- ✅ [Tutorial 1: Tu primer proyecto con IA + TIA Portal](./01-primeros-pasos-mcp.md)
- ✅ TIA Portal abierto con un proyecto que tenga varios bloques
- ✅ MCP Server configurado y funcionando

---

## 🎨 Paso 1: Analizar la estructura del proyecto

### 1.1 Pedir a Claude que analice el proyecto

En Claude Desktop, escribe:

```
Analiza mi proyecto de TIA Portal y genera un resumen estructurado.

Quiero que me proporciones:

1. ESTRUCTURA DEL PROYECTO:
   - Lista de todos los PLCs
   - Lista de todos los bloques (OB, FB, FC, DB)
   - Jerarquía de bloques (qué bloques llaman a otros)
   - Tablas de tags y UDTs

2. RESUMEN DE CADA BLOQUE:
   - Nombre y tipo (OB/FB/FC/DB)
   - Propósito principal
   - Entradas y salidas principales
   - Lógica general (en 2-3 frases)

3. ESTADÍSTICAS:
   - Número total de bloques
   - Número de bloques por tipo
   - Complejidad estimada (baja/media/alta)

Por favor, organiza la información en formato Markdown con tablas y listas.
```

### 1.2 Revisar el análisis

Claude generará un análisis completo. Revisa:

- ✅ ¿Se listan todos los bloques?
- ✅ ¿La jerarquía es correcta?
- ✅ ¿Las estadísticas son precisas?

Si falta información, pide más detalles:

```
El análisis está bien, pero:
1. Añade más detalles sobre los bloques FB
2. Incluye las interfaces de cada bloque
3. Muestra qué bloques llaman a otros
```

---

## 📝 Paso 2: Generar documentación de bloques individuales

### 2.1 Documentar un bloque específico

Elige un bloque de tu proyecto (por ejemplo, `FB_MotorControl`) y pide:

```
Genera documentación completa del bloque FB_MotorControl.

Quiero que incluyas:

1. CABECERA:
   - Nombre del bloque
   - Tipo (FB/FC/OB)
   - Lenguaje (SCL/LAD/FBD)
   - Versión de TIA Portal

2. DESCRIPCIÓN:
   - Propósito del bloque
   - Funcionalidad principal
   - Casos de uso típicos

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

Organiza todo en formato Markdown con tablas y bloques de código.
```

### 2.2 Revisar la documentación

Claude generará documentación detallada. Revisa:

- ✅ ¿La descripción es clara?
- ✅ ¿Las tablas de interfaz son correctas?
- ✅ ¿El diagrama de flujo es comprensible?
- ✅ ¿Los ejemplos son útiles?

Si algo falta, pide mejoras:

```
La documentación está bien, pero:
1. Añade más detalles en la sección de lógica
2. Mejora el diagrama de flujo
3. Añade más ejemplos de uso
```

---

## 📚 Paso 3: Generar documentación de todo el proyecto

### 3.1 Pedir documentación completa

En Claude Desktop, escribe:

```
Genera documentación completa de TODO mi proyecto de TIA Portal.

Quiero que crees un documento Markdown con las siguientes secciones:

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
     - Diagrama de flujo
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

### 3.2 Guardar la documentación

1. Copia la documentación generada
2. Guárdala en un archivo: `Documentacion_Proyecto.md`
3. Guárdalo en la carpeta de tu proyecto

---

## 🎨 Paso 4: Mejorar la documentación

### 4.1 Añadir diagramas visuales

Pide a Claude que genere diagramas ASCII:

```
Añade diagramas ASCII a la documentación:

1. Diagrama de arquitectura del sistema
2. Diagrama de flujo de cada FB
3. Diagrama de estados de las máquinas de estado
4. Diagrama de comunicación entre PLCs

Usa caracteres ASCII para crear diagramas claros y comprensibles.
```

### 4.2 Añadir ejemplos de código

Pide ejemplos de uso:

```
Añade ejemplos de código SCL para cada bloque:

1. Ejemplo de llamada al bloque desde OB1
2. Ejemplo de configuración de parámetros
3. Ejemplo de manejo de fallos
4. Ejemplo de diagnóstico

Incluye comentarios explicativos en cada ejemplo.
```

### 4.3 Añadir tablas de referencia

Pide tablas de referencia:

```
Añade tablas de referencia a la documentación:

1. Tabla de códigos de fallo
2. Tabla de alarmas
3. Tabla de parámetros configurables
4. Tabla de puntos de ajuste

Cada tabla debe incluir:
- Código/Nombre
- Descripción
- Rango válido
- Unidades
- Valor por defecto
```

---

## ✅ Paso 5: Revisar y finalizar

### 5.1 Revisar la documentación

Revisa la documentación generada:

- ✅ ¿Es completa?
- ✅ ¿Es clara y comprensible?
- ✅ ¿Tiene todos los bloques documentados?
- ✅ ¿Los diagramas son útiles?
- ✅ ¿Los ejemplos son prácticos?

### 5.2 Añadir información faltante

Si falta información, pide a Claude que la añada:

```
La documentación está casi completa, pero falta:
1. [indicar qué falta]
2. [indicar qué falta]

Por favor, añade esta información.
```

### 5.3 Formatear y organizar

Organiza la documentación:

1. Asegúrate de que el formato Markdown es correcto
2. Verifica que los enlaces internos funcionan
3. Revisa que las tablas están bien formateadas
4. Comprueba que los bloques de código tienen el formato correcto

---

## 🎉 ¡Felicidades!

Has generado documentación completa de tu proyecto con IA. Ahora puedes:

- ✅ Usar la documentación para referencia
- ✅ Compartirla con otros ingenieros
- ✅ Mantenerla actualizada fácilmente
- ✅ Continuar con el [Tutorial 4](./04-migracion-proyecto.md)

---

## 📚 Qué has aprendido

En este tutorial has aprendido:

1. ✅ Cómo analizar la estructura de un proyecto con IA
2. ✅ Cómo generar documentación de bloques individuales
3. ✅ Cómo generar documentación completa del proyecto
4. ✅ Cómo mejorar la documentación con diagramas y ejemplos
5. ✅ Cómo mantener la documentación actualizada

---

## 🔄 Próximos pasos

Ahora que ya has documentado tu proyecto, puedes:

- **Tutorial 4**: Migrar proyectos antiguos
- **Tutorial 5**: Crear tests automatizados
- **Guía de prompts**: Aprender prompts de documentación
- **Casos de uso**: Ver ejemplos de documentación

---

## 💡 Consejos adicionales

1. **Sé específico con el formato** — Indica exactamente qué formato quieres (Markdown, HTML, etc.)
2. **Pide ejemplos** — Los ejemplos hacen la documentación más útil
3. **Solicita diagramas** — Los diagramas visuales ayudan a entender la lógica
4. **Mantén la documentación actualizada** — Regenera la documentación cuando hagas cambios
5. **Usa plantillas** — Crea plantillas de documentación para mantener consistencia

---

## 📖 Recursos adicionales

- [Guía de prompts para documentación](../prompts/prompts-documentacion.md)
- [Best practices para documentación](../best-practices/workflow-ia-tia-portal.md)
- [Plantillas de documentación](../plantillas/plantilla-documentacion-bloque.md)

---

## 🏆 Badge de completado

¡Has completado el Tutorial 3! 🥈

**Badge obtenido**: 🥈 **Intermedio en IA + TIA Portal**

Continúa con el [Tutorial 4: Migración de proyectos](./04-migracion-proyecto.md) para avanzar hacia el badge de Avanzado.
