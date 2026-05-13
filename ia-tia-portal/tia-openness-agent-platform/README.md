# TIA Openness Agent Platform — Plataforma web completa

> **Repositorio**: [llambitintegration/multiverse-sdlc](https://github.com/llambitintegration/multiverse-sdlc) (⭐ 5)

---

## 📋 Resumen ejecutivo

Plataforma **web full-stack** (.NET 8 Backend + React 19 Frontend) para gestionar proyectos TIA Portal con asistencia de IA. A diferencia de los demás proyectos, no es solo un MCP Server sino una aplicación completa con UI propia, arquitectura limpia y roadmap de 8 waves.

**Punto fuerte**: Arquitectura profesional full-stack, roadmap estructurado, y UI propia para gestión de proyectos.

---

## 🎯 Qué hace

Proporciona una plataforma web para:

| Funcionalidad | Estado |
|---|---|
| **Backend API** | ✅ Wave 0 — REST endpoints + SignalR |
| **Frontend UI** | ✅ Wave 0 — React 19 + TailwindCSS |
| **Real-time comms** | ✅ Wave 0 — SignalR WebSockets |
| **TIA Portal connection** | 🔄 Wave 1 — Detección y conexión |
| **Project visualization** | ⏳ Wave 2 — Navegación de proyectos |
| **Safety gates** | ⏳ Wave 3 — Protección multi-nivel |
| **AI Agent chat** | ⏳ Wave 5 — Chat con IA |
| **Code templates** | ⏳ Wave 5 — Templates reutilizables |
| **Git export** | ⏳ Wave 6 — Export git-friendly |
| **PLC sync** | ⏳ Wave 6 — Sincronización bidireccional |

---

## 🏗️ Arquitectura

```
┌─────────────────┐   ┌──────────────────┐   ┌───────────────┐
│   Browser UI     │   │   Backend API     │   │   TIA Portal  │
│   (React 19)    │──▶│   (.NET 8)        │──▶│  Openness API │
│                 │   │                  │   │               │
│  ┌───────────┐  │   │  ┌────────────┐  │   │  ┌─────────┐  │
│  │  Pages    │  │   │  │ Controllers│  │   │  │ Project │  │
│  │  Components│  │   │  │ SignalR Hub│  │   │  │ .ap20   │  │
│  │  Stores   │  │   │  └────────────┘  │   │  └─────────┘  │
│  └───────────┘  │   └──────────────────┘   └───────────────┘
└─────────────────┘
```

**Stack Tecnológico:**

### Backend
- **Framework**: .NET 8 Web API (Windows-only, requisito TIA Portal)
- **Real-time**: SignalR para WebSockets
- **Logging**: Serilog estructurado
- **Documentation**: Swagger/OpenAPI
- **Testing**: xUnit, FluentAssertions, Moq

### Frontend
- **Framework**: React 19 + TypeScript
- **Build Tool**: Vite
- **Styling**: TailwindCSS 4.x
- **Routing**: React Router DOM 7
- **State**: Zustand
- **Real-time**: @microsoft/signalr

### Arquitectura
- **Pattern**: Clean Architecture con vertical slices
- **API**: REST para CRUD, WebSocket (SignalR) para real-time
- **Safety**: Todas las operaciones PLC requieren confirmación del usuario (futuro)

---

## 📦 Requisitos

### Backend
- **.NET 8 SDK**
- **Windows OS** (TIA Portal requirement)
- **Siemens TIA Portal V17+** (planificado)

### Frontend
- **Node.js 18+**
- **npm o yarn**

---

## 🚀 Instalación

### Backend Setup

```bash
cd backend/TiaOpenness.Api
dotnet restore
dotnet run
```

**Endpoints:**
- HTTP: `http://localhost:5000`
- HTTPS: `https://localhost:5001`
- Swagger UI: `http://localhost:5000`

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

**Frontend runs at:** `http://localhost:5173`

---

## 📊 Roadmap

El proyecto está organizado en **8 waves secuenciales** con **25 grupos paralelos**:

| Wave | Nombre | Grupos | Status |
|------|--------|--------|--------|
| **0** | Quick Wins - Scaffolding | 3 | ✅ **COMPLETE** |
| **1** | Connection Foundation | 3 | 🔄 **In Progress** (1/3) |
| 2 | Project Visualization | 3 | ⏳ Planned |
| 3 | Safety & Protection | 3 | ⏳ Planned |
| 4 | Feature Expansion | 4 | ⏳ Planned |
| 5 | Agent & Template UI | 2 | ⏳ Planned |
| 6 | Export & Sync | 4 | ⏳ Planned |
| 7 | Testing & Documentation | 3 | ⏳ Planned |

### Wave 0: Quick Wins — COMPLETE ✅

- ✅ Backend API Shell — .NET 8 Web API con REST endpoints
- ✅ Frontend App Shell — React + TypeScript SPA
- ✅ Real-time Infrastructure — SignalR bidireccional
- ✅ 45 Tests Passing — Cobertura unitaria e integración
- ✅ Type-safe Communication — TypeScript strict mode
- ✅ Production-ready — Zero vulnerabilidades de seguridad

### Wave 1: Connection Foundation — In Progress 🔄

- ✅ **Group 1A**: TIA Portal discovery and detection — COMPLETE
- 🔜 **Group 1B**: Connection manager con session handling
- 🔜 **Group 1C**: Connection UI con instance selection

### Wave 2-7: Planned

- Project visualization y browsing
- Safety gates y access control
- AI agent integration
- Code templates y tag management
- Git export y PLC synchronization
- Comprehensive testing y documentation

---

## 🛠️ API Reference

### REST Endpoints

```typescript
// Health & Info
GET  /health                 // Basic health check
GET  /health/detailed        // Detailed health status
GET  /api/info              // API information
GET  /api/status            // TIA Portal status (mock in Wave 0)

// TIA Portal Discovery (Wave 1, Group 1A)
GET  /api/tia/instances             // Discover all running TIA Portal instances
GET  /api/tia/instances/{processId} // Get specific instance details
GET  /api/tia/installation          // Check TIA Portal installation status
```

### SignalR Hub

```typescript
// Hub URL: /hubs/tia

// Server Methods
SendMessage(message: string): void
Heartbeat(): void

// Client Events
onReceiveMessage(callback: (message: string) => void)
```

**Full API documentation available at:** `http://localhost:5000` (Swagger UI)

---

## 🧪 Testing

### Backend Tests

```bash
cd backend
dotnet test
```

**Coverage:**
- 45 tests (unit + integration)
- ~95% code coverage
- Todos los paths críticos testeados

### Frontend Testing

```bash
cd frontend
npm run type-check   // TypeScript validation
npm run build        // Production build
npm run lint         // ESLint checking
```

---

## 📈 Performance

### Build Times
- Backend build: ~5 segundos
- Frontend build: ~1.77 segundos
- Frontend bundle: 251 kB (78 kB gzipped)

### Runtime Performance
- API response time: <50ms
- SignalR connection: <500ms
- Frontend initial load: <1s

---

## 🔒 Security

- ✅ No hardcoded secrets o credentials
- ✅ Environment-aware error messages
- ✅ CORS properly restricted
- ✅ HTTPS redirection enabled
- ✅ Input validation en todos los endpoints
- ✅ Structured logging sin sensitive data
- ✅ Dependencies up-to-date con no known vulnerabilities

---

## 📚 Documentación

### Getting Started
- [Project Overview](./CLAUDE.md) — Architecture, conventions, development workflow
- [Wave 0 Finalization](./WAVE_0_COMPLETE_FINALIZATION.md) — Detailed completion report
- [Integration Guide](./backend/INTEGRATION-GUIDE.md) — API and SignalR integration specs

### Backend Documentation
- [Backend README](./backend/README.md) — Setup and usage
- [API Integration Guide](./backend/INTEGRATION-GUIDE.md) — REST and SignalR endpoints
- [Integration Status](./backend/INTEGRATION-STATUS.md) — Current integration state
- [Review Report](./backend/GROUP_0A_REVIEW_REPORT.md) — Code review findings
- [Test Documentation](./backend/TiaOpenness.Api.Tests/README.md) — Test coverage

### Frontend Documentation
- [Frontend README](./frontend/README.md) — Setup and quick start
- [Implementation Guide](./frontend/IMPLEMENTATION.md) — Architecture and patterns
- [SignalR Setup](./frontend/SIGNALR_SETUP_INSTRUCTIONS.md) — Real-time configuration
- [Integration Guide](./frontend/GROUP_0C_INTEGRATION_GUIDE.md) — Usage examples

### OpenSpec
- [Roadmap](./openspec/changes/add-tia-openness-platform/roadmap.md) — Implementation waves and groups
- [Proposal](./openspec/changes/add-tia-openness-platform/proposal.md) — Project overview
- [Design Decisions](./openspec/changes/add-tia-openness-platform/design.md) — Architecture choices
- [Tasks](./openspec/changes/add-tia-openness-platform/tasks.md) — Implementation task breakdown

---

## 🎓 Casos de uso (futuros)

### 1. Visualización de proyectos
```
Muestra la estructura completa de mi proyecto TIA Portal
```
→ La UI navega el árbol de bloques, tags y hardware.

### 2. Chat con IA
```
Ayúdame a generar un FB de control de bomba
```
→ El chat con IA genera el bloque y lo importa.

### 3. Export git-friendly
```
Exporta todos los bloques como texto para version control
```
→ La plataforma exporta bloques en formato git-diffable.

### 4. Sincronización PLC
```
Sincroniza los tags del PLC con la base de datos
```
→ La plataforma lee/escribe tags bidireccionalmente.

---

## 🆚 Comparación con otros proyectos

| Característica | multiverse-sdlc | tiaportal-mcp | T-IA Connect |
|---|---|---|---|
| **Tipo** | Plataforma web full-stack | MCP Server | MCP Server + REST |
| **Backend** | .NET 8 | .NET Framework 4.8 | .NET Framework 4.8 |
| **Frontend** | React 19 | VS Code UI | Claude Desktop |
| **Real-time** | SignalR | ❌ | SignalR |
| **Roadmap** | 8 waves | — | — |
| **UI propia** | ✅ | ❌ | ❌ |
| **Open-source** | ✅ | ✅ | Freemium |
| **Estado** | Wave 0 complete | Production | Production |

---

## 🔗 Enlaces útiles

- **Repositorio**: https://github.com/llambitintegration/multiverse-sdlc
- **Wave 0 Finalization**: [WAVE_0_COMPLETE_FINALIZATION.md](https://github.com/llambitintegration/multiverse-sdlc/blob/main/WAVE_0_COMPLETE_FINALIZATION.md)
- **OpenSpec Roadmap**: [roadmap.md](https://github.com/llambitintegration/multiverse-sdlc/blob/main/openspec/changes/add-tia-openness-platform/roadmap.md)
- **TIA Portal Openness docs**: https://docs.tia.siemens.cloud/

---

## 📄 Licencia

MIT — Ver [LICENSE](https://github.com/llambitintegration/multiverse-sdlc/blob/main/LICENSE) en el repositorio original.
