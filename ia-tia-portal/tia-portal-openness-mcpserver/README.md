# TIA Portal Openness MCP Server

> **Repositorio**: [chewcw/tia-portal-openness-mcpserver](https://github.com/chewcw/tia-portal-openness-mcpserver) (⭐ 11)

---

## 📋 Resumen ejecutivo

Servidor MCP escrito en **C#** con cobertura extensa de la API Openness, acompañado de un **CLI en TypeScript** para facilitar instalación y configuración. Es una alternativa robusta a tiaportal-mcp con más herramientas y un CLI de gestión.

**Punto fuerte**: CLI TypeScript para instalación automatizada, cobertura extensa de la API, y herramientas de "sampling" asistidas por LLM.

---

## 🎯 Qué hace

Expone la API de TIA Portal como herramientas MCP organizadas en grupos:

| Grupo | Herramientas |
|---|---|
| **Project Lifecycle** | `projects_create`, `projects_open`, `projects_open_with_upgrade`, `projects_save`, `projects_close`, `projects_get_session_info` |
| **Hardware & Devices** | `devices_list`, `devices_create`, `devices_delete`, `devices_get_attributes`, `devices_set_attribute`, `devices_get_app_id`, `devices_set_app_id`, `devices_search_catalog` |
| **Device Items** | `deviceitems_list`, `deviceitems_get_attributes`, `deviceitems_plug_move`, `deviceitems_copy`, `deviceitems_delete`, `catalog_search_device_items` |
| **PLC Software** | `software_add_block`, `blocks_list`, `software_get_block_hierarchy` |
| **Advanced Blocks** | 19 herramientas para fuentes externas, ProDiag, UDTs, tipos, helpers de editor |
| **Tags** | `tags_create`, `tags_list`, `tags_tagtable_create`, `tags_tagtable_list`, `tags_tagtable_get`, `tags_tagtable_delete`, `tags_tagtable_export`, `tags_tagtable_open_editor`, `tags_group_create`, `tags_group_list`, `tags_group_find`, `tags_group_delete`, `tags_group_system_get`, `tags_constants_user_list`, `tags_constants_system_list` |
| **Compilation** | `compilation_project`, `compilation_software` |
| **File Import** | `files_read_csv`, `files_read_excel`, `files_list_sheets`, `files_validate_format`, `files_get_info` |
| **HMI Targets** | `hmi_targets_list`, `hmi_targets_get`, `hmi_targets_validate` |
| **Sampling/LLM** | `sampling_generate_code`, `sampling_summarize_project`, `sampling_get_suggestions` |
| **Utilities** | `utilities_elicit_user_input`, `utilities_get_project_info`, `utilities_list_libraries` |

**Total: ~60+ herramientas MCP**

---

## 🏗️ Arquitectura

```
┌─────────────────┐   ┌──────────────────┐   ┌───────────────┐
│   AI Agent      │   │   MCP Server     │   │   TIA Portal  │
│  (Claude,       │   │   (C# / .NET)    │   │  Openness API │
│   Cursor, etc.) │──▶│   TiaPortalMcp   │──▶│               │
│                 │MCP│   Server.exe     │   │  ┌─────────┐  │
│ "Lista bloques" │   │                  │   │  │ Project │  │
└─────────────────┘   └──────────────────┘   │  │ .ap20   │  │
                                              │  └─────────┘  │
                                              └───────────────┘
```

**Componentes:**

1. **TiaPortalMcpServer.exe** — Servidor MCP (C# / .NET Framework 4.8)
2. **CLI TypeScript** — `npx @chewcw/tia-portal-openness-mcpserver` para instalación
3. **Tests** — Unitarios y de integración

---

## 📦 Requisitos

### Software
- **Windows 10/11** — Openness API es COM-native
- **.NET Framework 4.8** — Runtime de .NET
- **Siemens TIA Portal V20** — Versión soportada

### Permisos
- Usuario en grupo `TIA Portal Openness Users`
- TIA Portal V20 instalado y licenciado

---

## 🚀 Instalación

### Opción 1: CLI (recomendada)

```bash
npx @chewcw/tia-portal-openness-mcpserver install --server-version v1.0.0
```

**Variables de entorno opcionales:**
- `GITHUB_TOKEN` — Token para acceso autenticado a GitHub API
- `TIA_MCP_INSTALL_DIR` — Override del directorio de instalación
- `TIA_MCP_AGENT_TYPE` — Override del tipo de agente detectado
- `TIA_MCP_SKILLS_PATH` — Override del path de skills

**Detección automática de agente:**
El CLI detecta automáticamente el tipo de agente desde:
- `OPENCODE_SESSION_ID`
- `OPENCODE_ROOT`
- `CLAUDE_AGENT_METADATA_FILE`
- `CURSOR_SESSION_ID`

### Opción 2: Build desde código

```bash
git clone https://github.com/chewcw/tia-portal-openness-mcpserver.git
cd tia-portal-openness-mcpserver
dotnet build tia-portal-openness-mcpserver.sln
dotnet run --project TiaPortalMcpServer/TiaPortalMcpServer.csproj
```

---

## ⚙️ Configuración

### Claude Desktop

Edita `C:\Users\<user>\AppData\Roaming\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "tia-portal-openness": {
      "command": "<path-to>\\TiaPortalMcpServer.exe",
      "args": [],
      "env": {}
    }
  }
}
```

### Cursor / Otros clientes MCP

Similar configuración, ajustando la ruta del ejecutable.

---

## 🛠️ Herramientas MCP destacadas

### Project Lifecycle

| Herramienta | Descripción |
|---|---|
| `projects_create` | Crear nuevo proyecto TIA Portal |
| `projects_open` | Abrir proyecto existente |
| `projects_open_with_upgrade` | Abrir proyecto con upgrade automático |
| `projects_save` | Guardar cambios del proyecto |
| `projects_close` | Cerrar proyecto |
| `projects_get_session_info` | Obtener información de la sesión actual |

### Hardware & Devices

| Herramienta | Descripción |
|---|---|
| `devices_list` | Listar todos los dispositivos del proyecto |
| `devices_create` | Crear nuevo dispositivo |
| `devices_delete` | Eliminar dispositivo |
| `devices_get_attributes` | Obtener atributos de dispositivo |
| `devices_set_attribute` | Establecer atributo de dispositivo |
| `devices_get_app_id` | Obtener Application ID |
| `devices_set_app_id` | Establecer Application ID |
| `devices_search_catalog` | Buscar en catálogo de hardware |

### Device Items

| Herramienta | Descripción |
|---|---|
| `deviceitems_list` | Listar items de dispositivo |
| `deviceitems_get_attributes` | Obtener atributos de item |
| `deviceitems_plug_move` | Mover item a otro slot |
| `deviceitems_copy` | Copiar item |
| `deviceitems_delete` | Eliminar item |
| `catalog_search_device_items` | Buscar items en catálogo |

### PLC Software

| Herramienta | Descripción |
|---|---|
| `software_add_block` | Añadir bloque a software |
| `blocks_list` | Listar bloques de software |
| `software_get_block_hierarchy` | Obtener jerarquía de bloques |

### Advanced Blocks (19 herramientas)

Cubre:
- Fuentes externas
- ProDiag
- UDTs
- Tipos
- Helpers de editor

### Tags

| Herramienta | Descripción |
|---|---|
| `tags_create` | Crear nuevo tag |
| `tags_list` | Listar tags |
| `tags_tagtable_create` | Crear tabla de tags |
| `tags_tagtable_list` | Listar tablas de tags |
| `tags_tagtable_get` | Obtener tabla de tags |
| `tags_tagtable_delete` | Eliminar tabla de tags |
| `tags_tagtable_export` | Exportar tabla de tags |
| `tags_tagtable_open_editor` | Abrir editor de tabla de tags |
| `tags_group_create` | Crear grupo de tags |
| `tags_group_list` | Listar grupos de tags |
| `tags_group_find` | Buscar grupo de tags |
| `tags_group_delete` | Eliminar grupo de tags |
| `tags_group_system_get` | Obtener grupos de sistema |
| `tags_constants_user_list` | Listar constantes de usuario |
| `tags_constants_system_list` | Listar constantes de sistema |

### Compilation

| Herramienta | Descripción |
|---|---|
| `compilation_project` | Compilar todo el proyecto |
| `compilation_software` | Compilar software específico |

### File Import

| Herramienta | Descripción |
|---|---|
| `files_read_csv` | Leer archivo CSV |
| `files_read_excel` | Leer archivo Excel |
| `files_list_sheets` | Listar hojas de Excel |
| `files_validate_format` | Validar formato de archivo |
| `files_get_info` | Obtener información de archivo |

### HMI Targets

| Herramienta | Descripción |
|---|---|
| `hmi_targets_list` | Listar targets HMI |
| `hmi_targets_get` | Obtener target HMI |
| `hmi_targets_validate` | Validar target HMI |

### Sampling/LLM (asistidas por LLM)

| Herramienta | Descripción |
|---|---|
| `sampling_generate_code` | Generar código con asistencia de LLM |
| `sampling_summarize_project` | Resumir proyecto con LLM |
| `sampling_get_suggestions` | Obtener sugerencias con LLM |

### Utilities

| Herramienta | Descripción |
|---|---|
| `utilities_elicit_user_input` | Elicitar input del usuario |
| `utilities_get_project_info` | Obtener información del proyecto |
| `utilities_list_libraries` | Listar librerías del proyecto |

---

## 🧪 Testing

### Ejecutar todos los tests

```bash
dotnet test TiaPortalMcpServer.Tests/TiaPortalMcpServer.Tests.csproj
```

### Solo tests unitarios

```bash
dotnet test --filter "Category!=Integration"
```

### Solo tests de integración

```bash
dotnet test --filter "Category=Integration"
```

### MCP Inspector

```bash
npx @modelcontextprotocol/inspector dotnet run --project TiaPortalMcpServer/TiaPortalMcpServer.csproj
```

---

## 📚 Documentación adicional

- [README principal](https://github.com/chewcw/tia-portal-openness-mcpserver)
- [CLI README](https://github.com/chewcw/tia-portal-openness-mcpserver/tree/main/cli)
- [Tests README](https://github.com/chewcw/tia-portal-openness-mcpserver/tree/main/TiaPortalMcpServer.Tests)
- [TIA Portal Openness docs](https://docs.tia.siemens.cloud/)

---

## 🎓 Casos de uso

### 1. Creación de proyecto
```
Crea un nuevo proyecto TIA Portal con un S7-1500
```
→ El IA usa `projects_create`, `devices_create`, `devices_search_catalog`.

### 2. Gestión de tags
```
Crea una tabla de tags para todas las entradas analógicas
```
→ El IA usa `tags_tagtable_create`, `tags_create`, `tags_tagtable_export`.

### 3. Compilación
```
Compila el software del PLC_1
```
→ El IA usa `compilation_software`.

### 4. Importación de datos
```
Importa tags desde un archivo Excel
```
→ El IA usa `files_read_excel`, `files_list_sheets`, `tags_create`.

### 5. Generación asistida por LLM
```
Genera código SCL para un control de bomba
```
→ El IA usa `sampling_generate_code`.

---

## 🆚 Comparación con otros proyectos

| Característica | tia-portal-openness-mcpserver | tiaportal-mcp | T-IA Connect |
|---|---|---|---|
| **Herramientas MCP** | ~60 | ~20 | 126+ |
| **CLI TypeScript** | ✅ | ❌ | ❌ |
| **Sampling/LLM tools** | ✅ | ❌ | ❌ |
| **File Import (CSV/Excel)** | ✅ | ❌ | ❌ |
| **HMI Targets** | ✅ | ❌ | ✅ |
| **TIA Portal V20** | ✅ | ✅ | ✅ |
| **Open-source** | ✅ | ✅ | Freemium |

---

## 🔗 Enlaces útiles

- **Repositorio**: https://github.com/chewcw/tia-portal-openness-mcpserver
- **CLI**: `npx @chewcw/tia-portal-openness-mcpserver`
- **MCP Inspector**: `npx @modelcontextprotocol/inspector`
- **TIA Portal Openness docs**: https://docs.tia.siemens.cloud/

---

## 📄 Licencia

MIT — Ver [LICENSE](https://github.com/chewcw/tia-portal-openness-mcpserver/blob/main/LICENSE) en el repositorio original.
