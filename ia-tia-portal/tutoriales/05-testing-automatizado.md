# Tutorial 5: Crear tests automatizados con PLCSim + IA

> **⏱️ Tiempo estimado**: 75 minutos
> **🎯 Dificultad**: ⭐⭐⭐ (Avanzado)
> **📋 Prerrequisitos**: Tutorial 2 completado

---

## 🎯 Objetivo

Crear tests automatizados para tus bloques usando PLCSim Advanced e IA. Al final tendrás:

- ✅ Suite de tests automatizados
- ✅ Casos de prueba generados por IA
- ✅ Reportes de resultados
- ✅ Integración con PLCSim Advanced

---

## 📋 Prerrequisitos

- ✅ [Tutorial 2: Generar un FB de control](./02-generar-bloque-scl.md)
- ✅ PLCSim Advanced instalado
- ✅ Bloques para testear
- ✅ MCP Server configurado

---

## 🧪 Paso 1: Configurar PLCSim Advanced

### 1.1 Crear instancia de simulación

1. Abre PLCSim Advanced
2. Crea una nueva instancia
3. Carga tu proyecto
4. Inicia la simulación

---

## 🤖 Paso 2: Generar casos de prueba con IA

### 2.1 Generar tests para un bloque

En Claude Desktop:

```
Genera casos de prueba automatizados para el bloque FB_MotorControl.

REQUISITOS:

1. CASOS DE PRUEBA:
   - Test de arranque normal
   - Test de parada normal
   - Test de timeout de feedback
   - Test de fallo de sobrecarga
   - Test de fallo de sobrecalentamiento
   - Test de reset de fallo
   - Test de modo manual
   - Test de modo automático

2. PARA CADA TEST:
   - Nombre del test
   - Descripción
   - Precondiciones (valores iniciales)
   - Acciones (qué inputs cambiar)
   - Resultados esperados (qué outputs verificar)
   - Criterios de éxito

3. SCRIPT DE TEST:
   - Código SCL para ejecutar el test
   - Código para verificar resultados
   - Código para reportar resultados

4. REPORTES:
   - Formato de reporte de resultados
   - Métricas a recopilar

Por favor, genera todo en formato Markdown.
```

---

## 📝 Paso 3: Implementar los tests

### 3.1 Crear bloque de test

1. Crea un FB llamado `FB_Test_MotorControl`
2. Añade lógica para ejecutar casos de prueba
3. Añade lógica para verificar resultados
4. Añade lógica para generar reportes

### 3.2 Integrar con PLCSim

1. Conecta el bloque de test con PLCSim
2. Configurar comunicación OPC UA
3. Implementar lectura/escritura de tags

---

## ✅ Paso 4: Ejecutar tests

### 4.1 Ejecutar suite de tests

1. Inicia la simulación en PLCSim
2. Ejecuta el bloque de test
3. Observa los resultados
4. Genera reporte

### 4.2 Analizar resultados

Revisa el reporte:

- ✅ ¿Todos los tests pasaron?
- ✅ ¿Hay tests que fallaron?
- ✅ ¿Hay casos edge no cubiertos?

---

## 🎉 ¡Felicidades!

Has creado tests automatizados con IA.

---

## 📚 Qué has aprendido

1. ✅ Cómo configurar PLCSim Advanced
2. ✅ Cómo generar casos de prueba con IA
3. ✅ Cómo implementar tests automatizados
4. ✅ Cómo ejecutar y analizar tests
5. ✅ Cómo generar reportes de resultados

---

## 🏆 Badge de completado

¡Has completado el Tutorial 5! 🥇

**Badge obtenido**: 🥇 **Avanzado en IA + TIA Portal**

Continúa con el [Tutorial 6: Refactorización inteligente](./06-refactorizacion-inteligente.md).
