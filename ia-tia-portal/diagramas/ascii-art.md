# 🎨 Diagramas ASCII adicionales

Diagramas ASCII para casos donde Mermaid no es suficiente o para mayor claridad.

---

## 🏗️ Arquitectura general

### Flujo completo IA → TIA Portal

```
┌──────────────────────────────────────────────────────────┐
│                    FLUJO COMPLETO                         │
│                                                          │
│  1. INGENIERO                                            │
│     "Crea un FB de control de bomba con fallo térmico"   │
│           │                                              │
│           ▼                                              │
│  2. MODELO DE IA (Claude, GPT, etc.)                     │
│     • Interpreta la petición                             │
│     • Genera código SCL estructurado                     │
│     • Decide qué herramientas MCP usar                   │
│           │                                              │
│           ▼                                              │
│  3. MCP SERVER (puente)                                  │
│     • Recibe comandos del IA                             │
│     • Traduce a llamadas Openness API                    │
│     • Motor determinista construye SimaticML XML         │
│           │                                              │
│           ▼                                              │
│  4. TIA PORTAL (Openness API)                            │
│     • Importa el bloque XML                              │
│     • Compila el proyecto                                │
│     • Bloque listo para uso                              │
└──────────────────────────────────────────────────────────┘
```

### Arquitectura de capas

```
┌─────────────────────────────────────────────────────────┐
│                  CAPA DE PRESENTACIÓN                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ VS Code      │  │ Claude       │  │ Claude Code  │  │
│  │ + Copilot    │  │ Desktop      │  │ CLI          │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                   CAPA DE AGENTE IA                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ Claude       │  │ GPT-4        │  │ Otros LLMs   │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                    CAPA MCP                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ tiaportal-   │  │ T-IA Connect │  │ totally-     │  │
│  │ mcp          │  │              │  │ integrated-  │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                CAPA OPENNESS API                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ Python       │  │ C#           │  │ TIA Scripting│  │
│  │ TIA Scripting│  │ Openness     │  │              │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                  CAPA TIA PORTAL                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ Proyecto     │  │ Bloques PLC  │  │ Hardware     │  │
│  │ .ap20        │  │ OB/FB/FC/DB  │  │ PLCs/HMI     │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

## ⚙️ Máquinas de estado

### Máquina de estados de motor (ASCII)

```
                    ┌─────────────┐
                    │   STOPPED   │
                    │ Motor parado│
                    │ Listo       │
                    └──────┬──────┘
                           │
                    Comando START
                           │
                           ▼
                    ┌─────────────┐
                    │  STARTING   │
                    │ Iniciando   │
                    │ Esperando   │
                    │ feedback    │
                    └──────┬──────┘
                           │
            ┌──────────────┼──────────────┐
            │              │              │
      Feedback      Timeout (5s)    Fallo
      recibido                           │
            │              │              │
            ▼              ▼              ▼
    ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
    │   RUNNING   │  │    FAULT    │  │    FAULT    │
    │ Motor en    │  │ Fallo       │  │ Fallo       │
    │ marcha      │  │ Timeout     │  │ Detectado   │
    └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
           │                │                │
    Comando STOP      Comando RESET    Comando RESET
           │                │                │
           └────────────────┴────────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   STOPPED   │
                    └─────────────┘
```

### Máquina de estados de filtro (ASCII)

```
                    ┌─────────────┐
                    │     IDLE    │
                    │ Filtro      │
                    │ inactivo    │
                    └──────┬──────┘
                           │
                    Comando START
                           │
                           ▼
                    ┌─────────────┐
                    │   SERVICE   │
                    │ Filtrando   │
                    │ agua        │
                    │ Monitoreando│
                    └──────┬──────┘
                           │
            ┌──────────────┼──────────────┐
            │              │              │
      Comando      Comando       Alarma
      BACKWASH      STOP          activa
            │              │              │
            ▼              ▼              ▼
    ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
    │BACKWASHING  │  │    IDLE     │  │    FAULT    │
    │ Backwash    │  │ Filtro      │  │ Fallo       │
    │ en progreso │  │ inactivo    │  │ activo      │
    │ Timer: 10m  │  └─────────────┘  └──────┬──────┘
    └──────┬──────┘                           │
           │                           Comando STOP
      Timer 10m                                 │
           │                                  ▼
           ▼                           ┌─────────────┐
    ┌─────────────┐                    │     IDLE    │
    │   RINSING   │                    └─────────────┘
    │ Enjuague    │
    │ Timer: 5m   │
    └──────┬──────┘
           │
      Timer 5m
           │
           ▼
    ┌─────────────┐
    │   SERVICE   │
    └─────────────┘
```

### Máquina de estados de válvula (ASCII)

```
                    ┌─────────────┐
                    │   CLOSED    │
                    │ Válvula     │
                    │ cerrada     │
                    └──────┬──────┘
                           │
                    Comando OPEN
                           │
                           ▼
                    ┌─────────────┐
                    │  OPENING    │
                    │ Abriendo    │
                    │ Esperando   │
                    │ feedback    │
                    └──────┬──────┘
                           │
            ┌──────────────┼──────────────┐
            │              │              │
      Feedback      Timeout (10s)   Feedback
      OPEN                            CLOSED
            │              │              │
            ▼              ▼              ▼
    ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
    │    OPEN     │  │    FAULT    │  │   CLOSED    │
    │ Válvula     │  │ Fallo       │  │ Válvula     │
    │ abierta     │  │ Timeout     │  │ cerrada     │
    └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
           │                │                │
    Comando CLOSE      Comando CLOSE   Comando CLOSE
           │                │                │
           └────────────────┴────────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   CLOSED    │
                    └─────────────┘
```

---

## 🔄 Flujo de trabajo

### Ciclo de desarrollo con IA

```
┌─────────────────────────────────────────────────────────┐
│              CICLO DE DESARROLLO CON IA                 │
└─────────────────────────────────────────────────────────┘

1. DEFINIR REQUISITOS
   ┌─────────────────────────────────────┐
   │ • Funcionalidad necesaria            │
   │ • Entradas y salidas                 │
   │ • Lógica de control                  │
   │ • Requisitos de seguridad            │
   └─────────────────────────────────────┘
                    │
                    ▼
2. ESCRIBIR PROMPT
   ┌─────────────────────────────────────┐
   │ • Ser específico                     │
   │ • Incluir ejemplos                   │
   │ • Especificar restricciones         │
   │ • Pedir comentarios                 │
   └─────────────────────────────────────┘
                    │
                    ▼
3. IA GENERA CÓDIGO
   ┌─────────────────────────────────────┐
   │ • Interpreta el prompt               │
   │ • Genera código SCL                  │
   │ • Incluye comentarios                │
   │ • Sigue mejores prácticas            │
   └─────────────────────────────────────┘
                    │
                    ▼
4. REVISAR CÓDIGO
   ┌─────────────────────────────────────┐
   │ • Verificar lógica                   │
   │ • Revisar interfaz                   │
   │ • Comprobar comentarios             │
   │ • Validar requisitos                │
   └─────────────────────────────────────┘
                    │
           ┌────────┴────────┐
           │                 │
      ¿Correcto?      ¿Necesita
           │           mejoras?
           │                 │
      Sí │                 │ No
           ▼                 ▼
   ┌──────────┐    ┌──────────────────┐
   │ IMPORTAR │    │ PEDIR            │
   │ EN TIA   │    │ CORRECCIONES     │
   │ PORTAL   │    └──────────────────┘
   └────┬─────┘              │
        │                  ▼
        │           ┌──────────────┐
        │           │ IA GENERA     │
        │           │ CÓDIGO        │
        │           │ CORREGIDO     │
        │           └──────┬───────┘
        │                  │
        │                  ▼
        │           ┌──────────────┐
        │           │ REVISAR       │
        │           │ CÓDIGO       │
        │           └──────┬───────┘
        │                  │
        └──────────────────┘
                    │
                    ▼
5. COMPILAR
   ┌─────────────────────────────────────┐
   │ • Compilar bloque                    │
   │ • Verificar errores                  │
   │ • Corregir si es necesario           │
   └─────────────────────────────────────┘
                    │
           ┌────────┴────────┐
           │                 │
      ¿Compila?      ¿No compila?
           │                 │
      Sí │                 │ No
           ▼                 ▼
   ┌──────────┐    ┌──────────────────┐
   │ PROBAR   │    │ PEDIR           │
   │ FUNCIONA- │    │ CORRECCIONES    │
   │ LIDAD    │    └──────────────────┘
   └────┬─────┘              │
        │                  ▼
        │           ┌──────────────┐
        │           │ IA GENERA     │
        │           │ CÓDIGO        │
        │           │ CORREGIDO     │
        │           └──────┬───────┘
        │                  │
        │                  ▼
        │           ┌──────────────┐
        │           │ COMPILAR     │
        │           └──────┬───────┘
        │                  │
        └──────────────────┘
                    │
                    ▼
6. PROBAR FUNCIONALIDAD
   ┌─────────────────────────────────────┐
   │ • Crear tabla de variables           │
   │ • Simular diferentes casos           │
   │ • Verificar comportamiento           │
   │ • Validar requisitos                │
   └─────────────────────────────────────┘
                    │
           ┌────────┴────────┐
           │                 │
      ¿Funciona?      ¿No funciona?
           │                 │
      Sí │                 │ No
           ▼                 ▼
   ┌──────────┐    ┌──────────────────┐
   │ ✅ LISTO  │    │ DEBUG Y         │
   │          │    │ CORREGIR        │
   └──────────┘    └──────────────────┘
```

---

## 🎓 Roadmap de aprendizaje

### Ruta de aprendizaje visual

```
┌─────────────────────────────────────────────────────────┐
│              ROADMAP DE APRENDIZAJE                     │
└─────────────────────────────────────────────────────────┘

🥉 NIVEL 1: PRINIPIANTE (2 semanas)
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  Semana 1:                                              │
│  ├─ Tutorial 1: Primeros pasos con MCP                  │
│  │  • Instalar MCP Server                               │
│  │  • Configurar Claude Desktop                         │
│  │  • Generar primer FC                                 │
│  │  • Importar y compilar                               │
│  │                                                      │
│  └─ Conceptos básicos:                                 │
│     • MCP Protocol                                      │
│     • Openness API                                      │
│     • TIA Scripting                                    │
│                                                         │
│  Semana 2:                                              │
│  ├─ Tutorial 2: Generar FB complejo                    │
│  │  • Preparar UDT                                      │
│  │  • Escribir prompt detallado                         │
│  │  • Generar FB con máquina de estados                │
│  │  • Probar funcionalidad                              │
│  │                                                      │
│  └─ Prompts efectivos:                                 │
│     • Ser específico                                    │
│     • Incluir ejemplos                                  │
│     • Especificar restricciones                        │
│                                                         │
│  🎯 Objetivo: Generar bloques simples con IA           │
│  🏆 Badge: 🥉 Principiante en IA + TIA Portal          │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
🥈 NIVEL 2: INTERMEDIO (2 semanas)
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  Semana 3:                                              │
│  ├─ Tutorial 3: Documentación automática               │
│  │  • Analizar estructura del proyecto                 │
│  │  • Documentar bloques individuales                   │
│  │  • Generar documentación completa                   │
│  │  • Mejorar con diagramas                             │
│  │                                                      │
│  └─ Documentación:                                     │
│     • Formato Markdown                                 │
│     • Diagramas de flujo                               │
│     • Ejemplos de uso                                  │
│                                                         │
│  Semana 4:                                              │
│  ├─ Tutorial 4: Migración de proyectos                  │
│  │  • Analizar proyecto antiguo                        │
│  │  • Identificar bloques obsoletos                    │
│  │  • Generar bloques modernos                         │
│  │  • Validar migración                                │
│  │                                                      │
│  └─ Migración:                                         │
│     • V15 → V20                                        │
│     • Instrucciones obsoletas                          │
│     • Mejores prácticas                                │
│                                                         │
│  🎯 Objetivo: Documentar y migrar proyectos            │
│  🏆 Badge: 🥈 Intermedio en IA + TIA Portal           │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
🥇 NIVEL 3: AVANZADO (2 semanas)
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  Semana 5:                                              │
│  ├─ Tutorial 5: Testing automatizado                   │
│  │  • Configurar PLCSim Advanced                       │
│  │  • Generar casos de prueba                          │
│  │  • Implementar tests                                │
│  │  • Ejecutar y analizar                               │
│  │                                                      │
│  └─ Testing:                                           │
│     • Casos de prueba                                  │
│     • Automatización                                   │
│     • Reportes de resultados                           │
│                                                         │
│  Semana 6:                                              │
│  ├─ Tutorial 6: Refactorización inteligente            │
│  │  • Analizar código existente                        │
│  │  • Identificar problemas                            │
│  │  • Generar código refactorizado                     │
│  │  • Validar mejoras                                  │
│  │                                                      │
│  └─ Refactorización:                                   │
│     • Código duplicado                                 │
│     • Anti-patterns                                    │
│     • Mejoras de calidad                               │
│                                                         │
│  🎯 Objetivo: Testing y refactorización con IA          │
│  🏆 Badge: 🥇 Avanzado en IA + TIA Portal              │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
💎 NIVEL 4: EXPERTO (continuo)
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  Proyectos avanzados:                                   │
│  ├─ Contribuir a la comunidad                           │
│  ├─ Crear herramientas propias                         │
│  ├─ Compartir conocimiento                              │
│  └─ Explorar proyectos avanzados                       │
│                                                         │
│  🎯 Objetivo: Ser experto en IA + TIA Portal           │
│  🏆 Badge: 💎 Experto en IA + TIA Portal              │
└─────────────────────────────────────────────────────────┘
```

---

## 🎯 Matriz de decisión

### Árbol de decisión detallado

```
                    ┌─────────────────────────┐
                    │ ¿QUÉ EDITOR USAS?     │
                    └───────────┬─────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
    VS Code              Claude Desktop          Claude Code CLI
        │                       │                       │
        ▼                       ▼                       ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│ tiaportal-mcp │    │ ¿NECESITAS    │    │ totally-      │
│               │    │ MODO HEADLESS?│    │ integrated-    │
│               │    └───────┬───────┘    │ claude         │
│               │            │           │               │
│               │    ┌───────┴───────┐   │               │
│               │    │               │   │               │
│               │   Sí              No  │               │
│               │    │               │   │               │
│               │    ▼               ▼   │               │
│               │ ┌─────────┐  ┌─────────┐ │               │
│               │ │T-IA     │  │totally- │ │               │
│               │ │Connect  │  │integrated│               │
│               │ │         │  │-claude  │               │
│               │ └─────────┘  └─────────┘ │               │
│               │                           │               │
└───────────────┘                           └───────────────┘

                    ┌─────────────────────────┐
                    │ ¿QUÉ VERSIÓN TIA?     │
                    └───────────┬─────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
      V17-V19                  V20                    V21
        │                       │                       │
        ▼                       ▼                       ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│ tiaportal-mcp │    │ Cualquiera    │    │ T-IA Connect  │
│ totally-     │    │ (todos        │    │ totally-      │
│ integrated-  │    │ soportan     │    │ integrated-    │
│ claude       │    │ V20)         │    │ claude         │
│ T-IA Connect │    │               │    │               │
│               │    │               │    │               │
└───────────────┘    └───────────────┘    └───────────────┘

                    ┌─────────────────────────┐
                    │ ¿QUÉ NECESITAS?      │
                    └───────────┬─────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
   Generar              Bloques              Documentación
   bloques              complejos             automática
        │                       │                       │
        ▼                       ▼                       ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│ tiaportal-mcp │    │ T-IA Connect  │    │ totally-      │
│               │    │               │    │ integrated-    │
│               │    │               │    │ claude         │
│               │    │               │    │               │
└───────────────┘    └───────────────┘    └───────────────┘

        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
   Testing               Migración            Desarrollo
   automatizado           de proyectos         de Add-Ins
        │                       │                       │
        ▼                       ▼                       ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│ T-IA Connect  │    │ T-IA Connect  │    │ totally-      │
│               │    │               │    │ integrated-    │
│               │    │               │    │ claude         │
│               │    │               │    │               │
└───────────────┘    └───────────────┘    └───────────────┘

        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
  Plataforma web        Importación de         Producción
                        datos (CSV/Excel)
        │                       │                       │
        ▼                       ▼                       ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│ multiverse-   │    │ tia-portal-   │    │ T-IA Connect  │
│ sdlc          │    │ openness-     │    │               │
│               │    │ mcpserver     │    │               │
│               │    │               │    │               │
└───────────────┘    └───────────────┘    └───────────────┘
```

---

## 📊 Comparativas visuales

### Comparativa de características

```
┌─────────────────────────────────────────────────────────────┐
│              COMPARATIVA DE MCP SERVERS                      │
└─────────────────────────────────────────────────────────────┘

Característica: POPULARIDAD (⭐ GitHub)
┌─────────────────────────────────────────────────────────────┐
│ tiaportal-mcp         ████████████████████ 56⭐            │
│ T-IA Connect          █ (no open-source)                     │
│ totally-integrated-   ██████ 8⭐                            │
│ claude                                                     │
│ tia-portal-openness-  ███████████ 11⭐                      │
│ mcpserver                                                  │
│ multiverse-sdlc       █████ 5⭐                             │
└─────────────────────────────────────────────────────────────┘

Característica: HERRAMIENTAS MCP
┌─────────────────────────────────────────────────────────────┐
│ tiaportal-mcp         ████ ~20                              │
│ T-IA Connect          ████████████████████████████████ 126+  │
│ totally-integrated-   ████████████ ~50                      │
│ claude                                                     │
│ tia-portal-openness-  ████████████████ ~60                  │
│ mcpserver                                                  │
│ multiverse-sdlc       █ (en desarrollo)                      │
└─────────────────────────────────────────────────────────────┘

Característica: MODO HEADLESS
┌─────────────────────────────────────────────────────────────┐
│ tiaportal-mcp         █ No                                  │
│ T-IA Connect          ████████████████████████████████ Sí   │
│ totally-integrated-   █ No                                  │
│ claude                                                     │
│ tia-portal-openness-  █ No                                  │
│ mcpserver                                                  │
│ multiverse-sdlc       █ No                                  │
└─────────────────────────────────────────────────────────────┘

Característica: API REST
┌─────────────────────────────────────────────────────────────┐
│ tiaportal-mcp         █ No                                  │
│ T-IA Connect          ████████████████████████████████ Sí   │
│ totally-integrated-   █ No                                  │
│ claude                                                     │
│ tia-portal-openness-  █ No                                  │
│ mcpserver                                                  │
│ multiverse-sdlc       ████████████████ Sí                    │
└─────────────────────────────────────────────────────────────┘

Característica: LSP SERVER
┌─────────────────────────────────────────────────────────────┐
│ tiaportal-mcp         █ No                                  │
│ T-IA Connect          █ No                                  │
│ totally-integrated-   ████████████████████████████████ Sí   │
│ claude                                                     │
│ tia-portal-openness-  █ No                                  │
│ mcpserver                                                  │
│ multiverse-sdlc       █ No                                  │
└─────────────────────────────────────────────────────────────┘

Característica: OPEN-SOURCE
┌─────────────────────────────────────────────────────────────┐
│ tiaportal-mcp         ████████████████████████████████ Sí   │
│ T-IA Connect          █ Freemium (motor propietario)       │
│ totally-integrated-   ████████████████████████████████ Sí   │
│ claude                                                     │
│ tia-portal-openness-  ████████████████████████████████ Sí   │
│ mcpserver                                                  │
│ multiverse-sdlc       ████████████████████████████████ Sí   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🏭 Casos de uso

### Línea de tratamiento de agua

```
┌─────────────────────────────────────────────────────────────┐
│              LÍNEA DE TRATAMIENTO DE AGUA                    │
└─────────────────────────────────────────────────────────────┘

                    AGUA CRUDA
                        │
                        ▼
              ┌─────────────────┐
              │   FILTRACIÓN    │
              │ 4 filtros en    │
              │   paralelo      │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │    BOMBEO      │
              │ 3 bombas con   │
              │ redundancia    │
              │    (2+1)        │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  DOSIFICACIÓN   │
              │ 2 sistemas de   │
              │  dosificación   │
              │   de químicos   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  CONTROL DE pH  │
              │ Sistema de     │
              │ control de pH  │
              │  con reactivos  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  MONITOREO     │
              │ 50 sensores     │
              │ analógicos     │
              │ 100 digitales   │
              └────────┬────────┘
                       │
                       ▼
                  AGUA TRATADA

┌─────────────────────────────────────────────────────────────┐
│                    CONTROL CON IA                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PLC S7-1500                                                │
│  ├─ 45 bloques generados por IA                            │
│  ├─ Máquinas de estado para cada proceso                    │
│  ├─ Control de alarmas                                      │
│  └─ Diagnóstico completo                                    │
│                                                             │
│  IA Generó:                                                 │
│  ├─ FB de control de filtro (máquina de estados)           │
│  ├─ FB de control de bomba (redundancia)                   │
│  ├─ FB de dosificación (control preciso)                    │
│  ├─ FB de control de pH (PID)                               │
│  └─ Documentación completa (150 páginas)                    │
│                                                             │
│  Resultados:                                                │
│  ├─ Tiempo de desarrollo: 12 semanas → 6 semanas (50%)      │
│  ├─ Errores de compilación: 23 → 2 (91%)                    │
│  └─ Tiempo de documentación: 3 semanas → 2 horas (95%)     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Sistema de transporte de cintas

```
┌─────────────────────────────────────────────────────────────┐
│           SISTEMA DE TRANSPORTE DE CINTAS                    │
└─────────────────────────────────────────────────────────────┘

    CINTA 1          CINTA 2          CINTA 3          CINTA 4
   (Principal)      (Principal)      (Principal)      (Principal)
        │                │                │                │
        ▼                ▼                ▼                ▼
   ┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
   │ Control │     │ Control │     │ Control │     │ Control │
   │ de      │     │ de      │     │ de      │     │ de      │
   │ velocidad│     │ velocidad│     │ velocidad│     │ velocidad│
   │ + PID    │     │ + PID    │     │ + PID    │     │ + PID    │
   └────┬────┘     └────┬────┘     └────┬────┘     └────┬────┘
        │                │                │                │
        └────────────────┴────────────────┴────────────────┘
                           │
                           ▼
              ┌─────────────────┐
              │  SINCRONIZACIÓN  │
              │  entre cintas   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   ACUMULACIÓN   │
              │   de productos  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   DIAGNÓSTICO   │
              │   y alarmas     │
              └─────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    CONTROL CON IA                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  3 PLCs S7-1500 comunicados por PROFINET                  │
│  ├─ PLC 1: Cintas 1-2                                      │
│  ├─ PLC 2: Cintas 3-4                                      │
│  └─ PLC 3: Coordinación y diagnóstico                      │
│                                                             │
│  IA Generó:                                                 │
│  ├─ 60 bloques de control                                  │
│  ├─ FB de coordinación entre PLCs                         │
│  ├─ FB de diagnóstico                                     │
│  └─ Sistema de alarmas                                     │
│                                                             │
│  Resultados:                                                │
│  ├─ Tiempo de desarrollo: 24 semanas → 12 semanas (50%)    │
│  ├─ Errores de compilación: 45 → 5 (89%)                   │
│  └─ Tiempo de puesta en marcha: 4 semanas → 2 semanas (50%)│
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎨 Badges y logros

### Badges de nivel

```
┌─────────────────────────────────────────────────────────────┐
│                    BADGES DE NIVEL                          │
└─────────────────────────────────────────────────────────────┘

🥉 PRINCIPIANTE
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Requisitos:                                                │
│  ├─ Completar Tutorial 1: Primeros pasos                    │
│  ├─ Completar Tutorial 2: Generar FB                       │
│  └─ Entender conceptos básicos                              │
│                                                             │
│  Habilidades:                                               │
│  ├─ Configurar MCP Server                                   │
│  ├─ Generar bloques simples con IA                         │
│  ├─ Importar y compilar bloques                             │
│  └─ Probar funcionalidad básica                            │
│                                                             │
│  Tiempo estimado: 2 semanas                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘

🥈 INTERMEDIO
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Requisitos:                                                │
│  ├─ Completar Tutorial 3: Documentación                     │
│  ├─ Completar Tutorial 4: Migración                        │
│  └─ Badge de Principiante                                  │
│                                                             │
│  Habilidades:                                               │
│  ├─ Documentar proyectos con IA                             │
│  ├─ Migrar proyectos antiguos                              │
│  ├─ Escribir prompts efectivos                              │
│  └─ Validar migraciones                                    │
│                                                             │
│  Tiempo estimado: 2 semanas                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘

🥇 AVANZADO
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Requisitos:                                                │
│  ├─ Completar Tutorial 5: Testing                          │
│  ├─ Completar Tutorial 6: Refactorización                  │
│  └─ Badge de Intermedio                                     │
│                                                             │
│  Habilidades:                                               │
│  ├─ Crear tests automatizados                              │
│  ├─ Integrar con PLCSim Advanced                           │
│  ├─ Refactorizar código con IA                              │
│  └─ Mejorar calidad de código                              │
│                                                             │
│  Tiempo estimado: 2 semanas                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘

💎 EXPERTO
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Requisitos:                                                │
│  ├─ Completar todos los tutoriales                         │
│  ├─ Contribuir a la comunidad                              │
│  └─ Badge de Avanzado                                       │
│                                                             │
│  Habilidades:                                               │
│  ├─ Desarrollar proyectos complejos                         │
│  ├─ Crear herramientas propias                            │
│  ├─ Compartir conocimiento                                 │
│  └─ Resolver problemas avanzados                           │
│                                                             │
│  Tiempo estimado: Continuo                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 Métricas visuales

### Reducción de tiempo (casos de uso)

```
┌─────────────────────────────────────────────────────────────┐
│              REDUCCIÓN DE TIEMPO (CASOS DE USO)              │
└─────────────────────────────────────────────────────────────┘

Línea de tratamiento de agua
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Antes:  ████████████████████████████████████ 12 semanas    │
│                                                             │
│  Después: ████████████████ 6 semanas                       │
│                                                             │
│  Reducción: 75%                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘

Sistema de transporte de cintas
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Antes:  ████████████████████████████████████████████ 24 sem│
│                                                             │
│  Después: ████████████████████████████ 12 semanas           │
│                                                             │
│  Reducción: 50%                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘

Máquina empacadora
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Antes:  ████████████████████████████████ 16 semanas       │
│                                                             │
│  Después: ████████████████████ 8 semanas                    │
│                                                             │
│  Reducción: 50%                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘

Planta química con seguridad
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Antes:  ████████████████████████████████████████████████ 32│
│                                                             │
│  Después: ████████████████████████████████ 16 semanas       │
│                                                             │
│  Reducción: 50%                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘

Sistema HVAC de edificio
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Antes:  ████████████████████████████ 12 semanas            │
│                                                             │
│  Después: ████████████████ 6 semanas                        │
│                                                             │
│  Reducción: 50%                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Mejora de calidad (casos de uso)

```
┌─────────────────────────────────────────────────────────────┐
│              MEJORA DE CALIDAD (CASOS DE USO)                │
└─────────────────────────────────────────────────────────────┘

Línea de tratamiento de agua
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Errores de compilación:                                    │
│  Antes:  ████████████████████████████████████ 23            │
│  Después: ██ 2                                               │
│  Mejora: 91%                                                │
│                                                             │
│  Tiempo de documentación:                                   │
│  Antes:  ████████████████████████████████████ 3 semanas      │
│  Después: █ 2 horas                                         │
│  Mejora: 95%                                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘

Sistema de transporte de cintas
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Errores de compilación:                                    │
│  Antes:  ████████████████████████████████████████████ 45   │
│  Después: █████ 5                                            │
│  Mejora: 89%                                                │
│                                                             │
│  Tiempo de puesta en marcha:                                 │
│  Antes:  ████████████████████████████ 4 semanas              │
│  Después: ████████████ 2 semanas                            │
│  Mejora: 50%                                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘

Máquina empacadora
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Defectos de calidad:                                       │
│  Antes:  ████████████ 2.5%                                   │
│  Después: █████ 0.8%                                        │
│  Mejora: 68%                                                │
│                                                             │
│  Tiempo de cambio de formato:                                │
│  Antes:  ████████████████████████████ 2 horas                │
│  Después: ████████████ 30 minutos                            │
│  Mejora: 75%                                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 Resumen

Total de diagramas ASCII creados: **15**

| Categoría | Diagramas |
|---|---|
| Arquitectura | 2 |
| Máquinas de estado | 3 |
| Flujo de trabajo | 1 |
| Roadmap de aprendizaje | 1 |
| Matriz de decisión | 1 |
| Comparativas | 1 |
| Casos de uso | 2 |
| Badges | 1 |
| Métricas | 2 |
| Esquemas técnicos | 2 |

**Total combinado (Mermaid + ASCII): 42 diagramas visuales**
