# ☁️ Entorno Cloud para desarrollar el repo + conectar con TIA Portal

Guía para dejar configurado un **entorno de desarrollo en la nube** (Cursor Cloud Agents) que permita **seguir mejorando y desarrollando este repositorio de forma automática**, y para entender **cómo conectar ese flujo con TIA Portal** a través de la API de Openness.

> **TL;DR**
> - El repo (Markdown + recursos `.xml` + validación) **sí** se puede desarrollar 100% en un Cloud Agent Linux, de forma persistente y automática. Ya está configurado en [`.cursor/environment.json`](../../.cursor/environment.json).
> - TIA Portal + Openness **NO** puede ejecutarse dentro del Cloud Agent (es solo Windows/COM). La parte que toca TIA Portal tiene que correr en **tu máquina Windows** y conectarse mediante un puente (MCP/REST) o un **worker self-hosted**.

---

## 1. Las dos capas del problema

Conectar "IA en la nube" con "TIA Portal" son en realidad **dos entornos distintos** que se comunican, no uno solo:

```
┌────────────────────────────┐        ┌──────────────────────────────┐
│  CAPA A — Nube (Linux)     │        │  CAPA B — Tu Windows          │
│  Cursor Cloud Agent VM     │        │  (PC / VM / Servidor)         │
│                            │  MCP/  │                               │
│  • Edita el repo           │  REST  │  • TIA Portal V17–V21         │
│  • Genera SCL / docs       │◀──────▶│  • Openness API (COM/.NET)    │
│  • Valida recursos         │  (red) │  • Puente: T-IA Connect /     │
│  • Abre PRs                │        │    tiaportal-mcp / etc.       │
└────────────────────────────┘        └──────────────────────────────┘
        SÍ automatizable                  Requiere Windows + licencia
```

- **Capa A (esta nube)**: desarrollar el repositorio `awesome-tia-portal` (documentación, catálogo, plantillas, validación de estructura). No necesita TIA Portal para nada.
- **Capa B (tu Windows)**: la única capa que puede hablar con TIA Portal de verdad (importar/compilar bloques, leer proyectos, PLCSIM...).

---

## 2. ¿Por qué TIA Portal no puede vivir en el Cloud Agent?

La API de Openness es **COM/DCOM nativa de Windows** y no tiene versión Linux ni contenedor:

| Requisito de Openness | Realidad del Cloud Agent |
|---|---|
| Windows 10/11 / Server | El VM es **Linux x86_64** |
| `Siemens.Engineering.dll` firmada + `.NET Framework 4.8` | No hay TIA Portal que aporte esa DLL |
| Instalación de TIA Portal con **licencia** | No instalable en Linux ni en Docker Linux |
| Usuario en el grupo `Siemens TIA Openness` + permisos DCOM | Concepto exclusivo de Windows |

Siemens lo confirma explícitamente: *"Why is Windows required? Because TIA Portal supports only Windows!"*. Wine tampoco soporta TIA Portal (rating *None*). Por eso **no existe** una forma de "instalar TIA Portal en el entorno cloud": hay que puentear a una máquina Windows real.

Referencia interna: ver [`../README.md`](../README.md) (sección *"Todo requiere Windows + TIA Portal instalado"*).

---

## 3. Capa A — Entorno cloud del repositorio (ya configurado)

Este repo ya trae un entorno reproducible para Cloud Agents:

- **[`.cursor/environment.json`](../../.cursor/environment.json)** — Imagen por defecto de Cursor (trae `git`, `bash`, `python3`, coreutils). No hace falta Dockerfile porque el repo es documentación + recursos, sin dependencias que compilar.
- **`install`** — Ejecuta [`scripts/validate-resources.sh`](../../scripts/validate-resources.sh), que valida que cada recurso tenga su `README.md` (y avisa de los `.xml` pendientes). Es idempotente y sirve como comprobación de salud en cada arranque.
- El mismo script es la **fuente única** que usa el workflow de CI [`.github/workflows/check-resources.yml`](../../.github/workflows/check-resources.yml).

Con esto, un Cloud Agent puede, de forma autónoma: añadir/editar recursos y su documentación, mantener el `CATALOG.md`, validar la estructura y abrir Pull Requests — sin ninguna dependencia de TIA Portal.

### Validar en local o en el agente

```bash
bash scripts/validate-resources.sh
```

---

## 4. Capa B — Conectar el flujo con TIA Portal (tu Windows)

Elige **una** de estas arquitecturas según lo que quieras. Si tu objetivo principal es *usar TIA Portal desde la IA*, la **Opción 0 (Cursor en local)** es la más sencilla.

### Opción 0 (la más simple): Cursor en local en tu propio Windows

Instalas **Cursor Desktop en el mismo Windows** donde tienes TIA Portal. El agente de Cursor corre en tu máquina, así que se conecta **directamente** a TIA Portal vía un servidor MCP local. No hace falta nube, ni worker self-hosted, ni túnel, ni allowlist de egress.

1. En tu Windows: TIA Portal V17–V21 **con licencia** y tu usuario en el grupo `Siemens TIA Openness`.
2. Instala Cursor Desktop (versión Windows nativa) y clona este repo en local.
3. Instala un servidor MCP de TIA Portal (open-source o comercial):
   - [`tiaportal-mcp`](../tia-portal-mcp-server/) → ejecutable `TiaMcpServer.exe` (open-source, ⭐ 56)
   - [`T-IA Connect`](../t-ia-connect/) → `TiaPortalApi.App.exe --mcp` (126+ herramientas, trial 14 días)
4. Regístralo como MCP en Cursor. Crea `~/.cursor/mcp.json` (global) o `.cursor/mcp.json` (por proyecto):
   ```json
   {
     "mcpServers": {
       "tiaportal": {
         "command": "C:\\ruta\\a\\TiaMcpServer.exe",
         "args": [],
         "env": {}
       }
     }
   }
   ```
   (Con T-IA Connect: `"command": "C:\\Program Files\\T-IA Connect\\TiaPortalApi.App.exe"`, `"args": ["--mcp"]`.)
5. Abre TIA Portal con tu proyecto, abre el chat del agente en Cursor y verifica en **Settings → MCP** que las herramientas del servidor aparecen activas. Pide, p. ej.: *"Lista los bloques FB del proyecto"* o *"Genera un FC de escalado lineal"*.

> **Ventaja**: es la vía más directa y sin fricción para desarrollo asistido. **Contrapartida**: solo funciona mientras tú tienes Cursor abierto en ese Windows (no es automatización desatendida 24/7). Si quieres que trabaje "solo" aunque no estés delante, usa la Opción 1.

> **Compatibilidad**: el propio catálogo lista Cursor como cliente MCP compatible (ver [`../t-ia-connect/README.md`](../t-ia-connect/README.md)).

### Opción 1 (desatendida): Worker self-hosted de Cursor sobre Windows

Ejecutas el proceso de worker de Cursor **en tu máquina Windows con TIA Portal instalado**. Así, un Cursor Cloud Agent puede ejecutarse *sobre esa máquina* y usar las herramientas MCP de TIA Portal localmente.

1. En el Windows con TIA Portal V17–V21 + licencia, añade tu usuario al grupo `Siemens TIA Openness`.
2. Instala un puente MCP de TIA Portal (elige uno del catálogo [`../`](../)):
   - [`tiaportal-mcp`](../tia-portal-mcp-server/) (open-source, ⭐ 56)
   - [`T-IA Connect`](../t-ia-connect/) (126+ herramientas, modo headless, trial 14 días)
3. Arranca el worker self-hosted de Cursor en esa máquina (`cursor worker start`).
4. Dirige tus agentes a ese worker. Ahora el agente corre donde vive TIA Portal.

> Ventaja: es la forma "siempre disponible" que buscas — mientras el worker esté encendido, tus agentes pueden trabajar con TIA Portal sin que tú estés delante.

### Opción 2: Puente remoto (MCP/REST) hacia tu Windows

Dejas TIA Portal + puente corriendo en Windows y expones su endpoint para que el agente lo consuma por red.

1. En Windows, arranca el puente en modo headless. Ejemplo con **T-IA Connect**:
   ```powershell
   TiaPortalApi.App.exe --headless
   # API: http://localhost:9000/  (Swagger en /swagger)
   ```
2. Expón el endpoint de forma **segura** (túnel/VPN + API key). Recomendado añadir [AgentGateway](https://github.com/agentgateway/agentgateway) como proxy Zero-Trust para filtrar herramientas peligrosas y auditar.
3. Registra ese endpoint como servidor MCP para el agente y añade el dominio al **allowlist de egress** del entorno.

> Detalles y ejemplos de `curl` de generación/compilación de bloques: [`../t-ia-connect/README.md`](../t-ia-connect/README.md).

---

## 5. Flujo completo objetivo

```
Cloud Agent (Linux)          Puente en Windows            TIA Portal
──────────────────           ─────────────────            ──────────
1. Mejora el repo  ─PR──▶ GitHub
2. Genera SCL/XML  ─MCP─▶  T-IA Connect / tiaportal-mcp ─Openness─▶ Importa + compila
3. Recibe resultado ◀────  (respuesta MCP/REST)         ◀─────────  bloque compilado
```

- La IA **nunca** toca TIA Portal directamente: siempre a través del puente.
- El código SCL lo propone la IA; el **XML SimaticML** lo construye el motor determinista del puente (evita errores de formato).

---

## 6. Checklist para dejarlo "siempre disponible"

- [x] Entorno cloud del repo configurado y guardado ([`.cursor/environment.json`](../../.cursor/environment.json)).
- [ ] Máquina Windows con TIA Portal V17–V21 + licencia y usuario en `Siemens TIA Openness`.
- [ ] Puente MCP/REST instalado en Windows ([`tiaportal-mcp`](../tia-portal-mcp-server/) o [`T-IA Connect`](../t-ia-connect/)).
- [ ] **Opción 0 (local)**: Cursor Desktop en ese Windows + `mcp.json` apuntando al servidor MCP — la vía más simple para desarrollo asistido interactivo.
- [ ] Opción 1: worker self-hosted de Cursor encendido en ese Windows (automatización desatendida), **o** Opción 2: endpoint del puente expuesto de forma segura + dominio en el allowlist de egress.
- [ ] (Opción 2) AgentGateway como proxy Zero-Trust para políticas y auditoría.

---

## 🔗 Enlaces

- Catálogo de puentes IA ↔ TIA Portal: [`../README.md`](../README.md)
- Documentación oficial Openness: <https://docs.tia.siemens.cloud/>
- Cursor Cloud Agents: <https://cursor.com/docs/cloud-agent/setup>
