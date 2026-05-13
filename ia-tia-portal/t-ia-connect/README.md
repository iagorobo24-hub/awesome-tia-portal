# T-IA Connect — Motor profesional con 126+ herramientas

> **Web**: [t-ia-connect.com](https://t-ia-connect.com/)
>
> **Repositorio GenAI Bridge**: [feelautom/tia-copilot-genai-bridge](https://github.com/feelautom/tia-copilot-genai-bridge) (⭐ 6)
>
> **Repositorio AgentGateway**: [feelautom/mcp-hack26-tia-connect-agentgateway](https://github.com/feelautom/mcp-hack26-tia-connect-agentgateway) (⭐ 7)

---

## 📋 Resumen ejecutivo

**T-IA Connect** es un producto profesional que expone **126+ herramientas MCP** de TIA Portal, con un motor determinista que genera SimaticML XML sin alucinaciones de IA. Ofrece un **trial gratuito de 14 días** y es el proyecto más completo del ecosistema en cuanto a cobertura de la API.

**Punto fuerte**: Cobertura masiva de la API (126+ herramientas), modo headless, y motor determinista que garantiza XML válido.

---

## 🎯 Qué hace

Expone prácticamente toda la API de TIA Portal como herramientas MCP, permitiendo:

| Categoría | Herramientas MCP |
|---|---|
| **Proyecto** | Crear, abrir, guardar, cerrar, archivar, recuperar |
| **Hardware** | Configurar CPUs, módulos, slots, redes, catálogo |
| **Bloques PLC** | Crear, leer, escribir, compilar OB/FB/FC/DB |
| **Tags** | Gestionar tablas, grupos, constantes, UDTs |
| **HMI** | Screens, tags, alarmas, scripts, conexiones |
| **Safety** | Bloques de seguridad, alarmas, diagnósticos |
| **OPC UA** | Configurar nodos, métodos, tipos |
| **PLCSim** | Iniciar simulación, escribir tags, forzar valores |
| **Import/Export** | SimaticML, AML/CAx, bloques, HMI |
| **Multiuser** | Gestión de proyectos multiusuario |
| **Teamcenter** | Integración con Teamcenter |
| **Testing** | TestSuite, Application Test, style-guide rules |

**Total: 126+ herramientas MCP**

---

## 🏗️ Arquitectura

```
┌─────────────────┐   ┌──────────────────┐   ┌───────────────┐
│   AI Agent      │   │   T-IA Connect    │   │   TIA Portal  │
│  (Claude,       │   │   REST API        │   │  Openness API │
│   Cursor, etc.) │──▶│   + Deterministic │──▶│  (headless)   │
│                 │MCP│   XML Engine      │   │               │
│ "Create a pump  │or │                  │   │  ┌─────────┐  │
│  sequence..."   │HTTP│                  │   │  │ FB_Pump │  │
└─────────────────┘   └──────────────────┘   │  │compiled│  │
                                              │  └─────────┘  │
                                              └───────────────┘
```

**Componentes:**

1. **TiaPortalApi.App.exe** — Motor principal (propietario)
   - Expone API REST en puerto 9000
   - Expone MCP Server vía stdio
   - Motor determinista que construye SimaticML XML

2. **GenAI Bridge** (open-source)
   - Conecta modelos de IA (Qwen, GPT, etc.)
   - Traduce prompts a llamadas API
   - Maneja el flujo de trabajo completo

3. **AgentGateway** (opcional, open-source)
   - Proxy Zero-Trust para seguridad
   - Filtra herramientas MCP por políticas
   - Audit logging de todas las acciones

---

## 🔄 Flujo de trabajo

### Paso 1: Prompt
```
"Genera un FB de control de bomba con fallo térmico (TON 5s), modo manual/auto"
```

### Paso 2: IA Razona
El modelo de IA diseña la lógica en SCL/JSON:
```json
{
  "blockType": "FB",
  "blockName": "FB_WaterPump",
  "language": "SCL",
  "logic": {
    "stateMachine": "Manual/Auto",
    "thermalFault": "TON 5s",
    "interlocks": "..."
  }
}
```

### Paso 3: Compilado Determinista
El motor C# construye SimaticML XML estricto:
```xml
<Blocks xmlns="http://www.siemens.com/automation/Openness/SW/Blocks/v4">
  <FunctionBlock Name="FB_WaterPump">
    <InterfaceSections>
      <!-- Estructura estricta, sin alucinaciones -->
    </InterfaceSections>
    <Body>
      <ST>
        <!-- Código SCL generado -->
      </ST>
    </Body>
  </FunctionBlock>
</Blocks>
```

### Paso 4: Despliegue
El bloque se importa y compila en TIA Portal vía Openness API.

> **Resultado**: Prompt → Bloque PLC compilado en menos de 30 segundos

---

## 📦 Requisitos

### Software
- **Windows 10/11** — Openness API es COM-native
- **Siemens TIA Portal V17–V21** — Cualquier versión moderna
- **T-IA Connect** — Descargable desde [t-ia-connect.com](https://t-ia-connect.com/)

### Permisos
- Usuario en grupo `Siemens TIA Openness`
- Licencia de TIA Portal válida

---

## 🚀 Instalación

### 1. Descargar T-IA Connect

Visita [t-ia-connect.com](https://t-ia-connect.com/) y descarga el instalador. Trial gratuito de 14 días.

### 2. Instalar

Ejecuta el instalador y sigue los pasos. Por defecto se instala en:
```
C:\Program Files\T-IA Connect\
```

### 3. Configurar MCP

#### Claude Desktop

Edita `C:\Users\<user>\AppData\Roaming\Claude\claude_desktop_config.json`:

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

#### Cursor / Otros clientes MCP

Similar configuración, ajustando la ruta del ejecutable.

---

## ⚙️ Modo Headless (API REST)

T-IA Connect puede ejecutarse sin GUI, exponiendo una API REST:

### Iniciar modo headless

```powershell
TiaPortalApi.App.exe --headless

# Output:
#   T-IA Connect — Headless Mode
#   API: http://localhost:9000/
#   Swagger: http://localhost:9000/swagger
#   Press Ctrl+C to stop.
```

### Abrir proyecto

```powershell
curl -X POST http://localhost:9000/api/projects/open `
  -H "X-API-Key: your-key" `
  -H "Content-Type: application/json" `
  -d '{ "projectPath": "C:\\Projects\\WaterPlant.ap20" }'
```

### Generar bloque desde lenguaje natural

```powershell
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

### Compilar bloque

```powershell
curl -X POST http://localhost:9000/api/blocks/compile `
  -H "X-API-Key: your-key" `
  -H "Content-Type: application/json" `
  -d '{ "deviceName": "PLC_1", "blockName": "FB_WaterPump" }'
```

> **Nota**: La ventana de TIA Portal nunca se abre. Todo es headless.

---

## 🛠️ Herramientas MCP destacadas

### Gestión de proyectos
- `get_project_overview` — Entender toda la estructura del proyecto PLC
- `projects_create` — Crear proyecto nuevo
- `projects_open` — Abrir proyecto existente
- `projects_save` — Guardar cambios
- `projects_close` — Cerrar proyecto

### Bloques PLC
- `list_blocks` — Listar todos los bloques (OB, FB, FC, DB)
- `get_block_details` — Obtener detalles de un bloque específico
- `create_scl_block` — Crear bloque SCL desde código
- `import_scl_source` — Importar código SCL
- `delete_block` — Eliminar bloque

### Tags y UDTs
- `list_tag_tables` — Listar tablas de tags
- `get_tag_table` — Obtener contenido de una tabla
- `create_tag` — Crear nuevo tag
- `list_udts` — Listar tipos de datos definidos por usuario
- `get_udt` — Obtener definición de UDT

### Compilación y descarga
- `compile_device` — Compilar dispositivo
- `compile_software` — Compilar software
- `download_to_plc` — Descargar a PLC real
- `download_to_plcsim` — Descargar a PLCSim

### Simulación
- `plcsim_start_simulation` — Iniciar PLCSim Advanced
- `plcsim_write_tag` — Escribir valor en tag
- `plcsim_read_tag` — Leer valor de tag
- `plcsim_force_value` — Forzar valor

### HMI
- `list_screens` — Listar pantallas HMI
- `get_screen` — Obtener detalles de pantalla
- `list_hmi_tags` — Listar tags HMI
- `create_hmi_tag` — Crear tag HMI

### Hardware
- `list_devices` — Listar dispositivos
- `get_device` — Obtener detalles de dispositivo
- `add_device` — Añadir dispositivo
- `configure_slot` — Configurar slot de módulo

---

## 🔒 AgentGateway — Zero-Trust Security

[AgentGateway](https://github.com/agentgateway/agentgateway) es un proxy opcional que añade seguridad industrial:

### Arquitectura con AgentGateway

```
Claude Code → AgentGateway (port 4000) → T-IA Connect (port 9000)
                                              → T-IA Connect REST
```

### Políticas de seguridad

```yaml
policies:
  mcpAuthorization:
    rules:
    - deny: mcp.tool.name == "close_project"
    - deny: mcp.tool.name == "delete_block"
    - allow: mcp.tool.name == "read_*"
```

**Efecto**: Las herramientas bloqueadas desaparecen completamente de la vista del agente. No hay error, no hay bypass — simplemente no existen.

### Audit logging

Todas las acciones del IA se registran con:
- Timestamp
- Usuario
- Herramienta MCP usada
- Parámetros
- Resultado

---

## 🧪 Testing

El proyecto incluye tests E2E que demuestran:

1. **Headless WPF boot** → Arranque sin GUI
2. **TIA Portal silent open** → Abrir proyecto sin ventana
3. **MCP tools/call execution** → Ejecución de herramientas MCP
4. **Full lifecycle** → Ciclo completo sin interacción del usuario

---

## 📚 Documentación adicional

- [Sitio web](https://t-ia-connect.com/)
- [DevPost — T-IA Copilot](https://devpost.com/software/t-ia-copilot-genai-for-industrial-plcs)
- [Blog — AgentGateway](https://feelautom.fr/en/blog/t-ia-connect-agent-gateway-industrial-zero-trust-ia-in-action)
- [Demo YouTube](https://www.youtube.com/watch?v=_OJYzbmBOvA)
- [Repositorio GenAI Bridge](https://github.com/feelautom/tia-copilot-genai-bridge)
- [Repositorio AgentGateway](https://github.com/feelautom/mcp-hack26-tia-connect-agentgateway)

---

## 🎓 Casos de uso

### 1. Generación de bloques desde lenguaje natural
```
Crea un FB de control de válvula con feedback y timeout de 10s
```
→ El IA genera el bloque completo, lo importa y compila.

### 2. Documentación automática
```
Genera documentación de todos los bloques del proyecto
```
→ El IA explora el proyecto y genera documentación estructurada.

### 3. Migración de proyectos
```
Exporta todo el proyecto como SimaticML XML
```
→ El IA exporta bloques, tags, hardware y configuración.

### 4. Testing automatizado
```
Crea un test suite para el FB_PumpControl
```
→ El IA genera casos de prueba y los ejecuta en PLCSim.

### 5. Refactorización
```
Busca bloques con código duplicado y propón refactorización
```
→ El IA analiza todos los bloques y sugiere mejoras.

---

## 🆚 Comparación con otros proyectos

| Característica | T-IA Connect | tiaportal-mcp | totally-integrated-claude |
|---|---|---|---|
| **Herramientas MCP** | 126+ | ~20 | ~50 (via skills) |
| **Modo headless** | ✅ | ❌ | ❌ |
| **Motor determinista** | ✅ | ❌ | ❌ |
| **API REST** | ✅ | ❌ | ❌ |
| **Zero-Trust proxy** | ✅ (opcional) | ❌ | ❌ |
| **Extensión VS Code** | ❌ | ✅ | ❌ |
| **Claude Desktop** | ✅ | ✅ | ✅ (plugin) |
| **TIA Portal V21** | ✅ | ⚠️ | ✅ |
| **Open-source** | Freemium | ✅ | ✅ |
| **Trial gratuito** | 14 días | — | — |

---

## 💰 Licencia y precios

- **Trial gratuito**: 14 días con todas las funcionalidades
- **Licencia comercial**: Contactar en [t-ia-connect.com](https://t-ia-connect.com/)
- **GenAI Bridge**: Open-source (MIT)
- **AgentGateway**: Open-source (Apache 2.0)

---

## 🔗 Enlaces útiles

- **Web**: https://t-ia-connect.com/
- **Repositorio GenAI Bridge**: https://github.com/feelautom/tia-copilot-genai-bridge
- **Repositorio AgentGateway**: https://github.com/feelautom/mcp-hack26-tia-connect-agentgateway
- **AgentGateway**: https://github.com/agentgateway/agentgateway
- **MCP Specification**: https://modelcontextprotocol.io/
- **TIA Portal Openness Docs**: https://docs.tia.siemens.cloud/

---

## 📄 Licencia

- **T-IA Connect (motor)**: Propietario (freemium)
- **GenAI Bridge**: MIT
- **AgentGateway**: Apache 2.0
