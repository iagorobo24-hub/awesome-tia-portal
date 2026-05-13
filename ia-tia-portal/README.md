# 🤖 IA + TIA Portal

> Recursos, herramientas y proyectos que conectan **Inteligencia Artificial** con **Siemens TIA Portal** para automatizar, asistir y acelerar el desarrollo de proyectos PLC.

---

## 📑 Tabla de contenido

- [¿Por qué esta sección?](#-por-qué-esta-sección)
- [Conceptos clave](#-conceptos-clave)
- [Proyectos destacados](#-proyectos-destacados)
- [Comparativa rápida](#-comparativa-rápida)
- [¿Cómo funciona la conexión IA → TIA Portal?](#-cómo-funciona-la-conexión-ia--tia-portal)
- [Guía de inicio rápido](#-guía-de-inicio-rápido)
- [Recursos y enlaces](#-recursos-y-enlaces)

---

## 🧠 ¿Por qué esta sección?

La IA está transformando la automatización industrial. Ya no es ciencia ficción: **hoy puedes pedirle a un asistente de IA que genere bloques SCL, configure hardware, compile proyectos y simule PLCs**, todo dentro de TIA Portal.

Esta sección recopila los proyectos más importantes que hacen posible esta conexión, explicados para que cualquier programador de PLCs pueda entenderlos y empezar a usarlos.

> **Nota**: Estos proyectos NO son bloques .xml para importar en TIA Portal. Son **herramientas de software** que conectan modelos de IA (como Claude, GPT, etc.) con TIA Portal a través de su API de Openness.

---

## 🔑 Conceptos clave

Antes de profundizar, necesitas conocer estos conceptos:

### TIA Portal Openness API

Es la API oficial de Siemens para automatizar TIA Portal por código. Permite:
- Abrir, crear y guardar proyectos programáticamente
- Leer y escribir bloques PLC (OB, FB, FC, DB)
- Configurar hardware (PLC, módulos, redes)
- Compilar y descargar a PLCs reales
- Exportar/importar bloques en formato XML (SimaticML)

> **Requisito**: Windows + TIA Portal instalado + usuario en grupo `Siemens TIA Openness`

### MCP (Model Context Protocol)

Es un protocolo abierto creado por Anthropic que permite a modelos de IA (como Claude) **interactuar con herramientas externas** de forma estandarizada. Piensa en él como un "enchufe universal" entre IA y aplicaciones.

- Un **MCP Server** expone herramientas (leer bloques, compilar, etc.)
- Un **MCP Client** (Claude Desktop, VS Code Copilot, Cursor) consume esas herramientas
- El modelo de IA decide cuándo y cómo usar cada herramienta

### TIA Scripting (Python)

Alternativa a la API Openness de C#, usando Python. Viene incluido con TIA Portal y es más accesible para scripting rápido y tareas de automatización simples.

---

## 🏆 Proyectos destacados

### 1. T-IA Connect + tiaportal-mcp — El más completo

| | |
|---|---|
| **Repositorio** | [heilingbrunner/tiaportal-mcp](https://github.com/heilingbrunner/tiaportal-mcp) |
| **Estrellas** | ⭐ 56 |
| **Extensión VS Code** | [vscode-tiaportal-mcp](https://github.com/heilingbrunner/vscode-tiaportal-mcp) (⭐ 41) |
| **TIA Portal** | V17 – V20+ |
| **Tecnología** | C# / .NET Framework 4.8 |
| **Protocolo** | MCP sobre stdio |
| **Agentes compatibles** | GitHub Copilot (VS Code), Claude Desktop |

**¿Qué hace?** Es un servidor MCP que se conecta a una instancia de TIA Portal en tu máquina y expone sus capacidades como herramientas que un modelo de IA puede usar directamente desde VS Code o Claude Desktop.

**Funcionalidades principales:**
- 📂 Conectar a TIA Portal y navegar proyectos
- 📖 Leer estructura de bloques (OB, FB, FC, DB)
- 📤 Exportar bloques como XML (SimaticML)
- 📥 Importar bloques desde documentos (.s7dcl / .s7res) — V20+
- 🔧 Compilar bloques y proyectos
- 🏷️ Gestionar tablas de tags y tipos de datos

**Requisitos:**
- Windows + .NET Framework 4.8
- TIA Portal V20 instalado (compatible con V18+ usando `--tia-major-version`)
- Variable de entorno `TiaPortalLocation` configurada
- Usuario en grupo `Siemens TIA Openness`

**Configuración para VS Code Copilot:**
```json
{
  "servers": {
    "vscode-tiaportal-mcp": {
      "command": "c:\\Users\\<user>\\.vscode\\extensions\\jheilingbrunner.vscode-tiaportal-mcp-<version>\\srv\\net48\\TiaMcpServer.exe",
      "args": ["--tia-major-version", "18"],
      "env": {}
    }
  }
}
```

**Configuración para Claude Desktop:**
```json
{
  "mcpServers": {
    "vscode-tiaportal-mcp": {
      "command": "<path-to>\\TiaMcpServer.exe",
      "args": [],
      "env": {}
    }
  }
}
```

> 📄 Ver análisis detallado → [`tia-portal-mcp-server/`](./tia-portal-mcp-server/)

---

### 2. T-IA Connect — Motor profesional con 126+ herramientas

| | |
|---|---|
| **Web** | [t-ia-connect.com](https://t-ia-connect.com/) |
| **Repositorio GenAI Bridge** | [feelautom/tia-copilot-genai-bridge](https://github.com/feelautom/tia-copilot-genai-bridge) (⭐ 6) |
| **Repositorio AgentGateway** | [feelautom/mcp-hack26-tia-connect-agentgateway](https://github.com/feelautom/mcp-hack26-tia-connect-agentgateway) (⭐ 7) |
| **TIA Portal** | V17 – V21 |
| **Tecnología** | C# / .NET Framework 4.8 (motor propietario) |
| **Protocolo** | MCP + REST API + SignalR |
| **Agentes compatibles** | Claude Desktop, Cursor, Claude Code, cualquier cliente MCP |

**¿Qué hace?** Es un producto profesional (con trial gratuito de 14 días) que expone **126+ herramientas MCP** de TIA Portal. A diferencia del proyecto anterior, el motor core es propietario, pero el bridge de IA es open-source.

**Funcionalidades principales (126+ herramientas):**
- 🏗️ Crear proyectos y configurar CPUs desde cero
- 📝 Generar bloques SCL desde lenguaje natural
- 🔍 Explorar estructura completa del proyecto (árbol de bloques, tags, hardware)
- ⚙️ Compilar dispositivos directamente
- 🧪 Automatizar pruebas con PLCSim Advanced
- 🏷️ Gestión completa de tags, UDTs, bloques
- 📡 Modo headless (sin GUI) — API REST en puerto 9000

**Arquitectura:**
```
┌─────────────────┐   ┌──────────────────┐   ┌───────────────┐
│   AI Agent      │   │   T-IA Connect   │   │   TIA Portal  │
│  (Claude, etc.) │──▶│   REST API       │──▶│  Openness API │
│                 │MCP│ + Deterministic  │   │  (headless)   │
│ "Create a pump  │or │   XML Engine     │   │               │
│  sequence..."   │HTTP│                  │   │  ┌─────────┐ │
└─────────────────┘   └──────────────────┘   │  │ FB_Pump │ │
                                              │  │compiled│ │
                                              │  └─────────┘ │
                                              └───────────────┘
```

**Flujo de trabajo:**
1. **Prompt** → El ingeniero describe qué necesita ("Generar secuencia de bomba con fallo térmico")
2. **IA Razona** → El LLM diseña la lógica en SCL/JSON
3. **Compilado Determinista** → El motor C# construye SimaticML XML estricto (sin alucinaciones de IA)
4. **Despliegue** → El bloque se importa y compila en TIA Portal vía Openness API

> **Resultado**: Prompt → Bloque PLC compilado en menos de 30 segundos

**Configuración MCP para Claude Desktop:**
```json
{
  "mcpServers": {
    "tia-connect": {
      "command": "C:\\Program Files\\T-IA Connect\\TiaPortalApi.App.exe",
      "args": ["--mcp"]
    }
  }
}
```

**API REST headless:**
```powershell
# Iniciar en modo headless
TiaPortalApi.App.exe --headless
# → API: http://localhost:9000/

# Abrir proyecto
curl -X POST http://localhost:9000/api/projects/open `
  -H "X-API-Key: your-key" `
  -H "Content-Type: application/json" `
  -d '{ "projectPath": "C:\\Projects\\WaterPlant.ap20" }'

# Generar bloque desde lenguaje natural
curl -X POST http://localhost:9000/api/blocks/generate `
  -H "X-API-Key: your-key" `
  -H "Content-Type: application/json" `
  -d '{
    "deviceName": "PLC_1",
    "blockType": "FB",
    "blockName": "FB_WaterPump",
    "description": "Water pump with Start/Stop, thermal fault (TON 5s), Manual/Auto mode",
    "language": "SCL"
  }'
```

> 📄 Ver análisis detallado → [`t-ia-connect/`](./t-ia-connect/)

---

### 3. Totally Integrated Claude — Plugin para Claude Code

| | |
|---|---|
| **Repositorio** | [Czarnak/totally-integrated-claude](https://github.com/Czarnak/totally-integrated-claude) (⭐ 8) |
| **TIA Portal** | V17+ |
| **Tecnología** | Python + C# (routed skills) |
| **Compatibilidad** | Claude Code, Gemini CLI, Codex |

**¿Qué hace?** Es un **plugin para Claude Code** (y otros agentes CLI) que proporciona un framework completo de skills para cubrir toda la API de Openness. Es el más ambicioso en cuanto a cobertura de la API.

**Funcionalidades principales:**
- 🛤️ **Routing automático** — Un skill entrada (`tia-openness-roadmap`) selecciona automáticamente Python o C# según la tarea
- 🐍 **Python TIA Scripting** — Cobertura completa de bloques, tags, HMI, librerías, ciclo de vida del proyecto
- 🔧 **C# Openness** — 9 skills de dominio cubriendo toda la API (PLC, HMI, redes, drives, import/export, multiuser, Teamcenter, testing)
- 🔌 **Add-In Development** — Workflow para desarrollar Add-Ins de TIA Portal desde VS Code
- 📝 **LSP Language Server** — Syntax highlighting, diagnóstticos e inteligencia de código para archivos `.scl`, `.st`, `.udt`, `.db`, `.awl`
- 🤖 **MCP interactivo** — Interacción directa con TIA Portal V21 vía MCP

**Skills disponibles:**

| Skill | Propósito |
|---|---|
| `tia-openness-roadmap` | **Punto de entrada** — Rutea todas las tareas al path correcto |
| `plc-code-analysis` | Análisis de seguridad y calidad de código PLC |
| `tia-portal-mcp` | Interacción directa vía MCP (V21) |
| `tia-python` | Python TIA Scripting (bloques, tags, HMI, librerías) |
| `tia-csharp-common` | Fundación C# (attach, ExclusiveAccess, Transaction) |
| `tia-project-general` | Ciclo de vida del proyecto (abrir, crear, guardar) |
| `tia-devices-general` | Hardware (catálogo, dispositivos, slots) |
| `tia-plc-operations` | Bloques PLC, tags, UDTs, Safety, OPC-UA, download |
| `tia-hmi-operations` | HMI Unified (screens, tags, alarmas, scripts) |
| `tia-networks` | Topología (subnets, IO systems, direcciones) |
| `tia-simatic-drives` | SINAMICS / Startdrive (motion control) |
| `tia-import-export` | Import/Export (SimaticML, AML/CAx, bloques, HMI) |
| `tia-multiuser` | Multiuser Engineering |
| `tia-teamcenter` | Integración Teamcenter |
| `tia-testsuite` | Testing automatizado |
| `addin-operations` | Desarrollo de Add-Ins |

**Instalación:**
```bash
# Claude Code
/plugin marketplace add Czarnak/totally-integrated-claude

# Gemini CLI
gemini extensions install https://github.com/Czarnak/totally-integrated-claude

# Codex
codex plugin marketplace add Czarnak/totally-integrated-claude
```

> 📄 Ver análisis detallado → [`totally-integrated-claude/`](./totally-integrated-claude/)

---

### 4. TIA Portal Openness MCP Server — CLI + Server

| | |
|---|---|
| **Repositorio** | [chewcw/tia-portal-openness-mcpserver](https://github.com/chewcw/tia-portal-openness-mcpserver) (⭐ 11) |
| **TIA Portal** | V20 |
| **Tecnología** | C# / .NET Framework 4.8 + TypeScript CLI |
| **Protocolo** | MCP sobre stdio |

**¿Qué hace?** Servidor MCP escrito en C# con cobertura extensa de la API Openness, acompañado de un CLI en TypeScript para facilitar instalación y configuración.

**Herramientas que expone:**
- 📂 Ciclo de vida del proyecto (crear, abrir, guardar, cerrar)
- 🔧 Hardware (dispositivos, slots, catálogo, atributos)
- 🧩 PLC Software (bloques, jerarquía, fuentes externas, UDTs, ProDiag)
- 🏷️ Tags completos (crear, listar, tablas, grupos, constantes, exportar)
- ⚙️ Compilación (proyecto y software)
- 📁 Importación de archivos (CSV, Excel, validación de formatos)
- 🖥️ HMI (targets, validación)
- 🤖 **Operaciones asistidas por LLM** (`sampling_generate_code`, `sampling_summarize_project`, `sampling_get_suggestions`)

**Instalación vía CLI:**
```bash
npx @chewcw/tia-portal-openness-mcpserver install --server-version v1.0.0
```

> 📄 Ver análisis detallado → [`tia-portal-openness-mcpserver/`](./tia-portal-openness-mcpserver/)

---

### 5. TIA Openness Agent Platform — Plataforma web completa

| | |
|---|---|
| **Repositorio** | [llambitintegration/multiverse-sdlc](https://github.com/llambitintegration/multiverse-sdlc) (⭐ 5) |
| **TIA Portal** | V17+ (planificado) |
| **Tecnología** | .NET 8 Backend + React 19 Frontend + SignalR |
| **Estado** | Wave 0 completo (infraestructura), Wave 1 en progreso |

**¿Qué hace?** Es una **plataforma web completa** para gestionar proyectos TIA Portal con asistencia de IA. A diferencia de los demás, no es solo un MCP Server sino una aplicación full-stack con UI.

**Arquitectura:**
- **Backend**: .NET 8 Web API + SignalR (WebSockets en tiempo real)
- **Frontend**: React 19 + TypeScript + TailwindCSS + Zustand
- **Patrón**: Clean Architecture con vertical slices

**Roadmap:**
- ✅ Wave 0 — Infraestructura base (API, frontend, SignalR, 45 tests)
- 🔄 Wave 1 — Conexión a TIA Portal (detección, sesiones, UI)
- ⏳ Wave 2 — Visualización de proyectos
- ⏳ Wave 3 — Seguridad y protección
- ⏳ Wave 4 — Expansión de features
- ⏳ Wave 5 — Chat con IA + templates
- ⏳ Wave 6 — Export git + sincronización PLC
- ⏳ Wave 7 — Testing y documentación

> 📄 Ver análisis detallado → [`tia-openness-agent-platform/`](./tia-openness-agent-platform/)

---

## ⚡ Comparativa rápida

| Proyecto | ⭐ | Versión TIA | Protocolo | Agentes | Tipo | Requisito clave |
|---|:---:|---|---|---|---|---|
| [tiaportal-mcp](https://github.com/heilingbrunner/tiaportal-mcp) | 56 | V17–V20+ | MCP stdio | Copilot, Claude | Open-source | TIA Portal + .NET 4.8 |
| [T-IA Connect](https://t-ia-connect.com/) | — | V17–V21 | MCP + REST | Claude, Cursor, cualquier MCP | Freemium (trial 14d) | T-IA Connect instalado |
| [totally-integrated-claude](https://github.com/Czarnak/totally-integrated-claude) | 8 | V17+ | Plugin skills | Claude Code, Gemini, Codex | Open-source | Claude Code CLI |
| [tia-portal-openness-mcpserver](https://github.com/chewcw/tia-portal-openness-mcpserver) | 11 | V20 | MCP stdio | Cualquier MCP client | Open-source | TIA Portal V20 + .NET 4.8 |
| [multiverse-sdlc](https://github.com/llambitintegration/multiverse-sdlc) | 5 | V17+ (planif.) | REST + SignalR | Web UI propia | Open-source | .NET 8 + Node.js |

---

## 🔗 ¿Cómo funciona la conexión IA → TIA Portal?

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

**Puntos clave del flujo:**

1. **La IA NO toca TIA Portal directamente** — Siempre pasa por un MCP Server que actúa como intermediario seguro
2. **El código SCL lo genera la IA, pero el XML lo construye el motor determinista** — Esto evita alucinaciones en el formato
3. **Todo requiere Windows + TIA Portal instalado** — La API Openness es COM-native y solo funciona en Windows
4. **El usuario SIEMPRE tiene control** — Los proyectos más maduros requieren confirmación antes de operaciones destructivas

---

## 🚀 Guía de inicio rápido

### Si usas VS Code + GitHub Copilot

1. Instala la extensión [TIA-Portal MCP-Server](https://marketplace.visualstudio.com/items?itemName=JHeilingbrunner.vscode-tiaportal-mcp)
2. Asegúrate de que TIA Portal está abierto con un proyecto cargado
3. Abre Copilot Chat en VS Code
4. Pregunta: *"¿Qué bloques tiene mi proyecto?"* o *"Crea un FC de escalado lineal"*

### Si usas Claude Desktop

1. Descarga [TiaMcpServer.exe](https://github.com/heilingbrunner/tiaportal-mcp/releases) o instala [T-IA Connect](https://t-ia-connect.com/)
2. Configura `claude_desktop_config.json` con el servidor MCP
3. Abre TIA Portal con un proyecto
4. Pregunta a Claude: *"Lista los bloques FB del proyecto"* o *"Genera un FB de control de válvula"*

### Si usas Claude Code (CLI)

1. Instala el plugin: `/plugin marketplace add Czarnak/totally-integrated-claude`
2. En un directorio de trabajo, pide a Claude: *"Analiza mi proyecto TIA Portal y busca mejoras"*

---

## 🔗 Recursos y enlaces

### Documentación oficial Siemens
- [TIA Portal Openness API](https://docs.tia.siemens.cloud/r/en-us/v21/tia-portal-openness-api-for-automation-of-engineering-workflows/)
- [TIA Scripting Python](https://support.industry.siemens.com/cs/document/109742322/)

### Proyectos del ecosistema
- [tiaportal-mcp](https://github.com/heilingbrunner/tiaportal-mcp) — MCP Server principal (⭐ 56)
- [vscode-tiaportal-mcp](https://github.com/heilingbrunner/vscode-tiaportal-mcp) — Extensión VS Code (⭐ 41)
- [tia-portal-openness-mcpserver](https://github.com/chewcw/tia-portal-openness-mcpserver) — MCP Server alternativo (⭐ 11)
- [totally-integrated-claude](https://github.com/Czarnak/totally-integrated-claude) — Plugin Claude Code (⭐ 8)
- [tia-copilot-genai-bridge](https://github.com/feelautom/tia-copilot-genai-bridge) — T-IA Connect GenAI Bridge (⭐ 6)
- [mcp-hack26-tia-connect-agentgateway](https://github.com/feelautom/mcp-hack26-tia-connect-agentgateway) — Zero-Trust proxy (⭐ 7)
- [multiverse-sdlc](https://github.com/llambitintegration/multiverse-sdlc) — Plataforma web (⭐ 5)
- [tia-portal-mcp (Czarnak)](https://github.com/Czarnak/tia-portal-mcp) — MCP Server V21 (⭐ 1)

### Artículos y videos
- [T-IA Connect + AgentGateway: Industrial Zero-Trust AI in Action](https://feelautom.fr/en/blog/t-ia-connect-agent-gateway-industrial-zero-trust-ia-in-action)
- [Demo YouTube — T-IA Connect + AgentGateway](https://www.youtube.com/watch?v=_OJYzbmBOvA)
- [T-IA Copilot en DevPost](https://devpost.com/software/t-ia-copilot-genai-for-industrial-plcs)

### Especificación MCP
- [Model Context Protocol — Anthropic](https://modelcontextprotocol.io/)
