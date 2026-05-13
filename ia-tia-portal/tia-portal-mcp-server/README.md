# TIA Portal MCP Server

> **Repositorio**: [heilingbrunner/tiaportal-mcp](https://github.com/heilingbrunner/tiaportal-mcp) (⭐ 56)
>
> **Extensión VS Code**: [vscode-tiaportal-mcp](https://github.com/heilingbrunner/vscode-tiaportal-mcp) (⭐ 41)

---

## 📋 Resumen ejecutivo

Servidor MCP (Model Context Protocol) que conecta **GitHub Copilot** y **Claude Desktop** directamente con **Siemens TIA Portal**. Es el proyecto más popular y estable del ecosistema, con 56 estrellas y una extensión VS Code oficial.

**Punto fuerte**: Integración nativa con VS Code + GitHub Copilot, ideal para desarrolladores que ya usan este entorno.

---

## 🎯 Qué hace

Expone las capacidades de TIA Portal como herramientas MCP que un modelo de IA puede usar:

| Categoría | Herramientas MCP |
|---|---|
| **Proyecto** | Conectar, abrir, guardar, cerrar proyectos |
| **Bloques** | Listar, leer, exportar bloques (OB, FB, FC, DB) |
| **Import/Export** | Exportar bloques como XML, importar desde documentos |
| **Compilación** | Compilar bloques y proyectos |
| **Tags** | Leer tablas de tags y tipos de datos |
| **Hardware** | Leer configuración de dispositivos |

---

## 🏗️ Arquitectura

```
┌─────────────────┐   ┌──────────────────┐   ┌───────────────┐
│   AI Agent      │   │   TIA Portal     │   │   TIA Portal  │
│  (Copilot,      │   │   MCP Server     │   │   (Openness)  │
│   Claude)       │──▶│   (C# / .NET)    │──▶│   API         │
│                 │MCP│                  │   │               │
│ "Lista bloques" │   │  TiaMcpServer.exe│   │  ┌─────────┐  │
└─────────────────┘   └──────────────────┘   │  │ Project │  │
                                              │  │ .ap20   │  │
                                              │  └─────────┘  │
                                              └───────────────┘
```

**Componentes:**
- **TiaMcpServer.exe** — Aplicación .NET Framework 4.8 que implementa el protocolo MCP
- **Transporte stdio** — Comunicación vía entrada/salida estándar
- **Openness API** — API oficial de Siemens para automatizar TIA Portal

---

## 📦 Requisitos

### Software
- **Windows 10/11** — La API Openness es COM-native, solo funciona en Windows
- **.NET Framework 4.8** — Runtime de .NET para ejecutar el servidor
- **Siemens TIA Portal V20** (compatible con V18+ usando argumento)
- **TIA Portal Openness** — Debe estar instalado con TIA Portal

### Permisos
- Usuario debe estar en el grupo **`Siemens TIA Openness`**
- Variable de entorno `TiaPortalLocation` configurada:
  ```
  TiaPortalLocation = C:\Program Files\Siemens\Automation\Portal V20
  ```

---

## 🚀 Instalación

### Opción 1: Extensión VS Code (recomendada para Copilot)

1. Instala la extensión desde [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=JHeilingbrunner.vscode-tiaportal-mcp)
2. Abre VS Code y asegúrate de que TIA Portal está abierto con un proyecto cargado
3. Copilot detectará automáticamente el servidor MCP

### Opción 2: Ejecutable standalone (para Claude Desktop)

1. Descarga la última release desde [GitHub Releases](https://github.com/heilingbrunner/tiaportal-mcp/releases)
2. Descomprime `TiaMcpServer.exe` en una carpeta
3. Configura tu cliente MCP (ver abajo)

---

## ⚙️ Configuración

### VS Code + GitHub Copilot

El archivo `mcp.json` se crea automáticamente al instalar la extensión. Para TIA Portal V18:

```json
{
  "servers": {
    "vscode-tiaportal-mcp": {
      "command": "c:\\Users\\<user>\\.vscode\\extensions\\jheilingbrunner.vscode-tiaportal-mcp-<version>\\srv\\net48\\TiaMcpServer.exe",
      "args": [
        "--tia-major-version",
        "18"
      ],
      "env": {}
    }
  }
}
```

### Claude Desktop

Edita `C:\Users\<user>\AppData\Roaming\Claude\claude_desktop_config.json`:

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

---

## 🛠️ Uso

### Ejemplos de prompts

**Explorar proyecto:**
```
¿Qué bloques FB tiene mi proyecto TIA Portal?
```

**Leer un bloque:**
```
Muéstrame el código del bloque FB_Motor
```

**Exportar bloque:**
```
Exporta el bloque FC_Escalado como XML
```

**Compilar:**
```
Compila el proyecto actual
```

### Flujo típico de trabajo

1. **Abrir TIA Portal** con tu proyecto cargado
2. **Iniciar el servidor MCP** (VS Code lo hace automáticamente)
3. **Preguntar al IA** sobre tu proyecto
4. **El IA llama las herramientas MCP** necesarias
5. **TIA Portal responde** con la información solicitada

---

## 🔧 Herramientas MCP disponibles

| Herramienta | Descripción |
|---|---|
| `connect` | Conectar a una instancia de TIA Portal |
| `list_blocks` | Listar todos los bloques del proyecto |
| `get_block` | Obtener el contenido de un bloque específico |
| `export_block` | Exportar un bloque como XML (SimaticML) |
| `import_block` | Importar un bloque desde documento (.s7dcl/.s7res) |
| `compile_block` | Compilar un bloque específico |
| `compile_project` | Compilar todo el proyecto |
| `list_tags` | Listar tablas de tags |
| `get_tag_table` | Obtener contenido de una tabla de tags |

---

## ⚠️ Limitaciones conocidas

### Importación de Ladder (LAD)
- Requiere que el archivo `.s7res` contenga tags en-US para todos los items
- Si no, la importación puede fallar (bug conocido de TIA Portal Openness)

### ExportBlock
- Requiere ruta completa del bloque: `Group/Subgroup/Name`
- Si solo das el nombre, devuelve `InvalidParams` con sugerencias

### Versiones TIA Portal
- **V20** es la versión por defecto
- V18/V19 compatible con `--tia-major-version`
- Export/Import de documentos requiere V20+

---

## 🧪 Testing

El proyecto incluye tests unitarios y de integración:

```bash
# Ejecutar todos los tests
dotnet test

# Solo tests unitarios
dotnet test --filter "Category!=Integration"

# Solo tests de integración
dotnet test --filter "Category=Integration"
```

> **Nota**: Los tests de integración requieren TIA Portal instalado y un proyecto de prueba configurado.

---

## 📚 Documentación adicional

- [README principal del repo](https://github.com/heilingbrunner/tiaportal-mcp)
- [Tests README](https://github.com/heilingbrunner/tiaportal-mcp/blob/main/tests/TiaMcpServer.Test/README.md)
- [Error model docs](https://github.com/heilingbrunner/tiaportal-mcp/blob/main/docs/error-model.md)
- [AGENTS.md](https://github.com/heilingbrunner/tiaportal-mcp/blob/main/AGENTS.md) — Guía para trabajar con agentes

---

## 🔄 Versiones TIA Portal soportadas

| Versión | Estado | Notas |
|---|---|---|
| V20 | ✅ Full | Versión por defecto |
| V19 | ✅ Compatible | Usa `--tia-major-version 19` |
| V18 | ✅ Compatible | Usa `--tia-major-version 18` |
| V17 | ⚠️ Parcial | No probado oficialmente |
| V21 | ⚠️ Parcial | No probado oficialmente |

---

## 🎓 Casos de uso

### 1. Documentación automática
```
Genera documentación de todos los bloques FB del proyecto
```
→ El IA lista todos los bloques, lee cada uno y genera documentación estructurada.

### 2. Revisión de código
```
Busca bloques con código duplicado o patrones sospechosos
```
→ El IA analiza todos los bloques buscando redundancias.

### 3. Migración de proyectos
```
Exporta todos los bloques del proyecto como XML
```
→ El IA itera sobre todos los bloques y los exporta para backup o migración.

### 4. Aprendizaje
```
Explícame cómo funciona el bloque FB_PumpControl
```
→ El IA lee el bloque y explica la lógica paso a paso.

---

## 🆚 Comparación con otros proyectos

| Característica | tiaportal-mcp | T-IA Connect | totally-integrated-claude |
|---|---|---|---|
| **Estrellas** | 56 | — | 8 |
| **Extensión VS Code** | ✅ Oficial | ❌ | ❌ |
| **Claude Desktop** | ✅ | ✅ | ✅ (plugin) |
| **Herramientas MCP** | ~20 | 126+ | ~50 (via skills) |
| **Modo headless** | ❌ | ✅ | ❌ |
| **Open-source** | ✅ | Freemium | ✅ |
| **TIA Portal V21** | ⚠️ Parcial | ✅ | ✅ |

---

## 📝 Notas de desarrollo

### Transportes soportados

**Actualmente:**
- ✅ `stdio` — Comunicación vía entrada/salida estándar

**Futuro (planificado):**
- ⏳ `stream` — Streams personalizados (TCP, etc.)
- ⏳ `HTTP` — Servidor HTTP con endpoint `/mcp`
- ⏳ `Streamable HTTP` — Especificación MCP para HTTP streaming

### Logging

- Los logs van a **stderr** para no corromper el JSON-RPC de stdio
- Logs también se guardan en archivo rolling en `TiaMcpServer/logs/`

### Error handling

- Excepciones de Portal se mapean a códigos McpException
- `ExportFailed` incluye razón concisa del error
- `NotFound` devuelve `InvalidParams` con sugerencias de rutas

---

## 🔗 Enlaces útiles

- **Repositorio**: https://github.com/heilingbrunner/tiaportal-mcp
- **Extensión VS Code**: https://marketplace.visualstudio.com/items?itemName=JHeilingbrunner.vscode-tiaportal-mcp
- **Repositorio VS Code**: https://github.com/heilingbrunner/vscode-tiaportal-mcp
- **MCP Specification**: https://modelcontextprotocol.io/
- **TIA Portal Openness Docs**: https://docs.tia.siemens.cloud/

---

## 📄 Licencia

MIT — Ver [LICENSE](https://github.com/heilingbrunner/tiaportal-mcp/blob/main/LICENSE) en el repositorio original.
