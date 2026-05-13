# Totally Integrated Claude — Plugin para Claude Code

> **Repositorio**: [Czarnak/totally-integrated-claude](https://github.com/Czarnak/totally-integrated-claude) (⭐ 8)

---

## 📋 Resumen ejecutivo

Plugin para **Claude Code** (y otros agentes CLI como Gemini CLI y Codex) que proporciona un framework completo de **skills** para cubrir toda la API de Openness. Es el proyecto más ambicioso en cuanto a cobertura de la API, con 15+ skills especializados.

**Punto fuerte**: Framework de skills con routing automático, cobertura completa de la API (Python + C#), y LSP server para archivos PLC.

---

## 🎯 Qué hace

Proporciona un framework de skills que Claude Code puede cargar dinámicamente para interactuar con TIA Portal:

| Categoría | Skills |
|---|---|
| **Routing** | `tia-openness-roadmap` — Punto de entrada que selecciona Python o C# |
| **Python TIA Scripting** | `tia-python` — Bloques, tags, HMI, librerías, ciclo de vida |
| **C# Openness** | 9 skills cubriendo toda la API (PLC, HMI, redes, drives, etc.) |
| **Add-In Development** | `addin-operations` — Workflow para desarrollar Add-Ins |
| **LSP Server** | Syntax highlighting para `.scl`, `.st`, `.udt`, `.db`, `.awl` |
| **MCP Interactivo** | `tia-portal-mcp` — Interacción directa con TIA Portal V21 |

---

## 🏗️ Arquitectura

```
┌─────────────────┐   ┌──────────────────┐   ┌───────────────┐
│   Claude Code   │   │  Plugin Skills   │   │   TIA Portal  │
│   (CLI)         │──▶│  (Python + C#)   │──▶│  Openness API │
│                 │   │                  │   │               │
│ "Analiza mi     │   │  tia-openness-   │   │  ┌─────────┐  │
│  proyecto..."   │   │  roadmap         │   │  │ Project │  │
└─────────────────┘   └──────────────────┘   │  │ .ap20   │  │
                                              │  └─────────┘  │
                                              └───────────────┘
```

**Componentes:**

1. **Plugin Framework** — Estructura de skills que Claude Code puede cargar
2. **Routing Skill** — `tia-openness-roadmap` selecciona automáticamente Python o C#
3. **Python Skills** — TIA Scripting para tareas comunes
4. **C# Skills** — Openness API para tareas avanzadas
5. **LSP Server** — `siemens-lsp.exe` para inteligencia de código

---

## 📦 Requisitos

### Software
- **Claude Code CLI** — Agente de Anthropic para desarrollo
- **Windows 10/11** — Openness API es COM-native
- **Siemens TIA Portal V17+** — Cualquier versión moderna

### Permisos
- Usuario en grupo `Siemens TIA Openness`
- TIA Scripting Python instalado (viene con TIA Portal)

---

## 🚀 Instalación

### Claude Code

```bash
/plugin marketplace add Czarnak/totally-integrated-claude
```

### Gemini CLI

```bash
gemini extensions install https://github.com/Czarnak/totally-integrated-claude
```

### Codex

```bash
codex plugin marketplace add Czarnak/totally-integrated-claude
```

### Desarrollo local

```bash
git clone https://github.com/Czarnak/totally-integrated-claude.git
cd totally-integrated-claude
gemini extensions link .
```

---

## ⚙️ Uso

### Flujo típico

1. **Cargar el routing skill**:
   ```
   ¿Cómo leo todos los bloques PLC de mi proyecto TIA Portal?
   ```

2. **Claude carga automáticamente**:
   - `tia-openness-roadmap` (routing)
   - `tia-python` o `tia-csharp-common` + skill de dominio
   - Ejecuta la tarea

3. **Resultado**:
   - Claude lista todos los bloques
   - Explica la estructura del proyecto
   - Sugiere mejoras si las encuentra

### Ejemplos de prompts

**Explorar proyecto:**
```
Analiza mi proyecto TIA Portal y explícame su estructura
```

**Leer bloques:**
```
Muéstrame el código del bloque FB_MotorControl
```

**Generar documentación:**
```
Genera documentación de todos los bloques FB del proyecto
```

**Crear Add-In:**
```
Ayúdame a crear un Add-In de TIA Portal que exporte bloques
```

---

## 🛠️ Skills disponibles

### Routing y análisis

| Skill | Propósito |
|---|---|
| `tia-openness-roadmap` | **Punto de entrada** — Rutea todas las tareas al path correcto (Python o C#) |
| `plc-code-analysis` | Análisis de seguridad y calidad de código PLC (standalone) |
| `tia-portal-mcp` | Interacción directa vía MCP (V21) |

### Python TIA Scripting

| Skill | Propósito |
|---|---|
| `tia-python` | Cobertura completa: bloques, tags, HMI, librerías, ciclo de vida del proyecto |

**Funcionalidades:**
- Leer/escribir bloques PLC (OB, FB, FC, DB)
- Gestionar tablas de tags y UDTs
- Exportar/importar bloques
- Gestionar HMI (screens, tags, alarmas)
- Ciclo de vida del proyecto (abrir, guardar, cerrar)

### C# Openness — Foundation

| Skill | Propósito |
|---|---|
| `tia-csharp-common` | Fundación C#: attach, ExclusiveAccess, Transaction, disposable patterns |

**Patrones implementados:**
- Attach a proceso TIA Portal
- ExclusiveAccess para operaciones exclusivas
- Transaction para cambios atómicos
- Disposable patterns para limpieza de recursos

### C# Openness — Dominios

| Skill | Propósito |
|---|---|
| `tia-project-general` | Ciclo de vida del proyecto (abrir, crear, guardar, archivar, recuperar) |
| `tia-devices-general` | Hardware (catálogo, dispositivos, slots, subslots, redes) |
| `tia-plc-operations` | Bloques PLC, tags, UDTs, Safety, OPC-UA, online/download, compare |
| `tia-hmi-operations` | HMI Unified (screens, items, tags, alarmas, scripts, conexiones) |
| `tia-networks` | Topología (subnets, nodos, IO systems, puertos, direcciones) |
| `tia-simatic-drives` | SINAMICS / Startdrive (motion control) |
| `tia-import-export` | Import/Export (SimaticML, AML/CAx, bloques, HMI, hardware) |
| `tia-multiuser` | Multiuser Engineering (server projects, sesiones locales) |
| `tia-teamcenter` | Integración Teamcenter (almacenamiento, proyectos gestionados) |
| `tia-testsuite` | TestSuite & Application Test (test sets, style-guide rules) |

### Add-In Development

| Skill | Propósito |
|---|---|
| `addin-operations` | Desarrollo de Add-Ins (estructura, VS Code workflow, lifecycle, menús) |

---

## 📝 LSP Language Server

El plugin incluye un LSP server compilado (`bin/siemens-lsp.exe`) que proporciona:

### Lenguajes soportados

| Extensión | Lenguaje |
|---|---|
| `.scl` | Structured Control Language |
| `.st` | Structured Text (IEC 61131-3) |
| `.s7res` | S7 Resource |
| `.s7dcl` | S7 Declaration |
| `.udt` | User-Defined Type |
| `.db` | Data Block |
| `.awl` | Statement List (AWL/STL) |

### Funcionalidades

- ✅ Syntax highlighting
- ✅ Diagnósticos en tiempo real
- ✅ Code intelligence (autocompletado, go-to-definition)
- ✅ Validación de sintaxis

---

## 🔄 Routing automático

El skill `tia-openness-roadmap` decide automáticamente qué usar:

| Tarea | Path | Skill |
|---|---|---|
| Explorar proyecto interactivamente | MCP | `tia-portal-mcp` |
| Analizar SimaticML XML para seguridad | Standalone | `plc-code-analysis` |
| Leer/escribir bloques y tags | Python | `tia-python` |
| HMI screens y export | Python | `tia-python` |
| Manipulación de slots/subslots | C# | `tia-devices-general` |
| Configuración de subnets y IO-systems | C# | `tia-networks` |
| Engineering de SINAMICS drives | C# | `tia-simatic-drives` |
| Servicios PLC online/seguridad avanzados | C# | `tia-plc-operations` |
| Multiuser Engineering (server projects) | C# | `tia-multiuser` |
| Proyectos gestionados por Teamcenter | C# | `tia-teamcenter` |
| Testing automatizado PLC/HMI | C# | `tia-testsuite` |
| Proyecto de Add-In de TIA Portal | C# | `addin-operations` |

---

## 🧪 Testing

El plugin incluye tests para validar:

- Routing correcto de tareas
- Carga de skills
- Ejecución de operaciones Python
- Ejecución de operaciones C#
- Integración con TIA Portal

---

## 📚 Documentación adicional

- [README principal](https://github.com/Czarnak/totally-integrated-claude)
- [TIA Portal Openness docs](https://docs.tia.siemens.cloud/r/en-us/v21/tia-portal-openness-api-for-automation-of-engineering-workflows/)
- [TIA Scripting Python](https://support.industry.siemens.com/cs/document/109742322/)
- [Siemens LSP](https://marketplace.visualstudio.com/items?itemName=DynamicEngineering.dynamic-siemens-language-support)

---

## 🎓 Casos de uso

### 1. Análisis de código PLC
```
Analiza el bloque FB_PumpControl y busca vulnerabilidades de seguridad
```
→ Claude carga `plc-code-analysis` y genera un reporte de seguridad.

### 2. Documentación automática
```
Genera documentación de todos los bloques del proyecto
```
→ Claude carga `tia-python` y documenta cada bloque.

### 3. Refactorización
```
Busca bloques con código duplicado y propón refactorización
```
→ Claude analiza todos los bloques y sugiere mejoras.

### 4. Desarrollo de Add-In
```
Ayúdame a crear un Add-In que exporte todos los bloques como XML
```
→ Claude carga `addin-operations` y guía el desarrollo.

### 5. Configuración de hardware
```
Configura un S7-1500 con módulos de E/S y comunicación PROFINET
```
→ Claude carga `tia-devices-general` y `tia-networks`.

---

## 🆚 Comparación con otros proyectos

| Característica | totally-integrated-claude | tiaportal-mcp | T-IA Connect |
|---|---|---|---|
| **Skills/Framework** | 15+ skills | ~20 herramientas MCP | 126+ herramientas MCP |
| **Python TIA Scripting** | ✅ | ❌ | ❌ |
| **C# Openness completo** | ✅ | ✅ | ✅ |
| **LSP Server** | ✅ | ❌ | ❌ |
| **Add-In Development** | ✅ | ❌ | ❌ |
| **Claude Code** | ✅ | ❌ | ❌ |
| **Claude Desktop** | ✅ (plugin) | ✅ | ✅ |
| **VS Code Copilot** | ❌ | ✅ | ❌ |
| **Modo headless** | ❌ | ❌ | ✅ |
| **Open-source** | ✅ | ✅ | Freemium |

---

## 🔗 Enlaces útiles

- **Repositorio**: https://github.com/Czarnak/totally-integrated-claude
- **TIA Portal Openness docs**: https://docs.tia.siemens.cloud/
- **TIA Scripting Python**: https://support.industry.siemens.com/cs/document/109742322/
- **Siemens LSP**: https://marketplace.visualstudio.com/items?itemName=DynamicEngineering.dynamic-siemens-language-support
- **Claude Code**: https://claude.ai/code

---

## 📄 Licencia

MIT — Ver [LICENSE](https://github.com/Czarnak/totally-integrated-claude/blob/main/LICENSE) en el repositorio original.
