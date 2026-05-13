# 📚 Tutoriales IA + TIA Portal

Tutoriales paso a paso para aprender a usar Inteligencia Artificial con Siemens TIA Portal. Cada tutorial está diseñado para completarse en 30-60 minutos.

---

## 📑 Tabla de contenido

- [Nivel 1: Primeros pasos](#nivel-1-primeros-pasos)
- [Nivel 2: Generación de código](#nivel-2-generación-de-código)
- [Nivel 3: Automatización avanzada](#nivel-3-automatización-avanzada)
- [Nivel 4: Integración completa](#nivel-4-integración-completa)

---

## 🎯 Nivel 1: Primeros pasos

### 1. Tu primer proyecto con IA + TIA Portal
**⏱️ Tiempo**: 45 minutos | **Dificultad**: ⭐ | **Prerrequisitos**: Ninguno

> [Ver tutorial completo →](./01-primeros-pasos-mcp.md)

**Objetivo**: Configurar tu entorno y generar tu primer bloque PLC con IA.

**Qué aprenderás:**
- ✅ Instalar y configurar un MCP Server
- ✅ Conectar Claude Desktop o VS Code Copilot
- ✅ Generar un FC de escalado simple
- ✅ Importar y compilar el bloque en TIA Portal

**Resultado**: Un FC de escalado funcional generado completamente por IA.

---

## 🎯 Nivel 2: Generación de código

### 2. Generar un FB de control desde lenguaje natural
**⏱️ Tiempo**: 60 minutos | **Dificultad**: ⭐⭐ | **Prerrequisitos**: Tutorial 1

> [Ver tutorial completo →](./02-generar-bloque-scl.md)

**Objetivo**: Generar un bloque de función complejo (FB) con lógica de estado.

**Qué aprenderás:**
- ✅ Escribir prompts efectivos para bloques complejos
- ✅ Generar FBs con máquinas de estado
- ✅ Usar UDTs como estructura de E/S
- ✅ Validar código generado por IA

**Resultado**: Un FB de control de motor con manual/auto, timeouts y diagnóstico.

---

### 3. Documentar todo tu proyecto con IA
**⏱️ Tiempo**: 40 minutos | **Dificultad**: ⭐⭐ | **Prerrequisitos**: Tutorial 1

> [Ver tutorial completo →](./03-documentacion-automatica.md)

**Objetivo**: Generar documentación completa de todos los bloques de tu proyecto.

**Qué aprenderás:**
- ✅ Analizar estructura de proyecto con IA
- ✅ Generar documentación estructurada
- ✅ Crear diagramas de flujo
- ✅ Exportar documentación en Markdown

**Resultado**: Documentación completa de tu proyecto en formato Markdown.

---

## 🎯 Nivel 3: Automatización avanzada

### 4. Migrar un proyecto antiguo con ayuda de IA
**⏱️ Tiempo**: 90 minutos | **Dificultad**: ⭐⭐⭐ | **Prerrequisitos**: Tutorial 2

> [Ver tutorial completo →](./04-migracion-proyecto.md)

**Objetivo**: Migrar un proyecto de TIA Portal V15 a V20 con IA.

**Qué aprenderás:**
- ✅ Analizar proyecto antiguo
- ✅ Identificar bloques obsoletos
- ✅ Generar bloques equivalentes modernos
- ✅ Validar funcionalidad tras migración

**Resultado**: Proyecto migrado y funcional en TIA Portal V20.

---

### 5. Crear tests automatizados con PLCSim + IA
**⏱️ Tiempo**: 75 minutos | **Dificultad**: ⭐⭐⭐ | **Prerrequisitos**: Tutorial 2

> [Ver tutorial completo →](./05-testing-automatizado.md)

**Objetivo**: Crear tests automatizados para tus bloques usando PLCSim Advanced.

**Qué aprenderás:**
- ✅ Configurar PLCSim Advanced
- ✅ Generar casos de prueba con IA
- ✅ Automatizar ejecución de tests
- ✅ Generar reportes de resultados

**Resultado**: Suite de tests automatizados para tus bloques PLC.

---

## 🎯 Nivel 4: Integración completa

### 6. Refactorizar código con IA
**⏱️ Tiempo**: 60 minutos | **Dificultad**: ⭐⭐⭐⭐ | **Prerrequisitos**: Tutorial 2

> [Ver tutorial completo →](./06-refactorizacion-inteligente.md)

**Objetivo**: Refactorizar código PLC existente para mejorar calidad y mantenibilidad.

**Qué aprenderás:**
- ✅ Detectar código duplicado
- ✅ Identificar anti-patterns
- ✅ Generar código refactorizado
- ✅ Validar que la funcionalidad se mantiene

**Resultado**: Código refactorizado, más limpio y mantenible.

---

## 📊 Roadmap visual

```
Nivel 1 (Principiante)
├── Tutorial 1: Primeros pasos con MCP
└── ⏱️ 45 min

Nivel 2 (Intermedio)
├── Tutorial 2: Generar FB complejo
├── Tutorial 3: Documentación automática
└── ⏱️ 100 min total

Nivel 3 (Avanzado)
├── Tutorial 4: Migración de proyectos
├── Tutorial 5: Testing automatizado
└── ⏱️ 165 min total

Nivel 4 (Experto)
└── Tutorial 6: Refactorización inteligente
    └── ⏱️ 60 min

Total: ~7 horas de aprendizaje
```

---

## 🏆 Badges de completado

Completa los tutoriales y obtén estos badges:

| Badge | Tutorial | Requisito |
|---|---|---|
| 🥉 **Principiante** | Tutorial 1 | Completar tutorial 1 |
| 🥈 **Intermedio** | Tutorials 1-3 | Completar tutoriales 1-3 |
| 🥇 **Avanzado** | Tutorials 1-5 | Completar tutoriales 1-5 |
| 💎 **Experto** | Tutorials 1-6 | Completar todos los tutoriales |

---

## 💡 Consejos para seguir los tutoriales

1. **Sigue el orden** — Los tutoriales están diseñados para seguirse secuencialmente
2. **No te saltes pasos** — Cada paso es importante para el siguiente
3. **Experimenta** — Una vez completado un tutorial, modifica el código y prueba
4. **Documenta** — Toma notas de lo que aprendes para referencia futura
5. **Comparte** — Si encuentras algo útil, compártelo con la comunidad

---

## 🆘 ¿Necesitas ayuda?

Si te encuentras con problemas durante un tutorial:

1. Revisa la sección [Troubleshooting](../troubleshooting/errores-comunes.md)
2. Consulta el [FAQ](../troubleshooting/faq.md)
3. Abre un [Issue](https://github.com/iagorobo24-hub/awesome-tia-portal/issues) con tu pregunta

---

## 📚 Recursos adicionales

- [Guía de prompts efectivos](../prompts/prompts-generacion-bloques.md)
- [Casos de uso reales](../casos-de-uso/)
- [Comparativas de proyectos](../comparativas/)
- [Best practices](../best-practices/)

---

## 🎓 ¿Listo para empezar?

Comienza con el [Tutorial 1: Tu primer proyecto con IA + TIA Portal](./01-primeros-pasos-mcp.md) 🚀
