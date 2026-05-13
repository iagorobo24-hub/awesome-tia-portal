# 📚 Integraciones con otras herramientas

Guía de integración de IA + TIA Portal con otras herramientas de desarrollo y gestión de proyectos.

---

## 📑 Tabla de contenido

- [Integración con Git](#integración-con-git)
- [Integración con Jira](#integración-con-jira)
- [Integración con Confluence](#integración-con-confluence)
- [Integración con Microsoft Teams](#integración-con-microsoft-teams)
- [Integración con Power BI](#integración-con-power-bi)

---

## 🔀 Integración con Git

### Descripción

Integrar TIA Portal con Git para control de versiones de bloques PLC, tags y configuración.

### Flujo de trabajo

```
1. Exportar bloques como XML (SimaticML)
2. Commit en Git con mensaje descriptivo
3. Push a repositorio remoto
4. Pull requests para revisión
5. Merge a main
6. Importar bloques en TIA Portal
```

### Configuración

#### 1. Crear repositorio Git

```bash
# Inicializar repositorio
git init

# Crear estructura de carpetas
mkdir -p blocks tags hardware

# Crear .gitignore
cat > .gitignore << EOF
# Archivos temporales de TIA Portal
*.tmp
*.bak
~$*

# Archivos binarios grandes
*.ap17
*.ap18
*.ap19
*.ap20
*.ap21

# Archivos de sistema
.DS_Store
Thumbs.db
EOF
```

#### 2. Script de exportación

```powershell
# Exportar bloques a Git
# export-blocks-to-git.ps1

param(
    [string]$ProjectPath,
    [string]$GitPath
)

# Exportar bloques como XML
tia-portal export-blocks -project $ProjectPath -output $GitPath\blocks

# Exportar tags
tia-portal export-tags -project $ProjectPath -output $GitPath\tags

# Exportar configuración de hardware
tia-portal export-hardware -project $ProjectPath -output $GitPath\hardware

# Commit en Git
cd $GitPath
git add .
git commit -m "Export: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
git push
```

#### 3. Script de importación

```powershell
# Importar bloques desde Git
# import-blocks-from-git.ps1

param(
    [string]$ProjectPath,
    [string]$GitPath
)

# Pull últimos cambios
cd $GitPath
git pull

# Importar bloques
tia-portal import-blocks -project $ProjectPath -input $GitPath\blocks

# Importar tags
tia-portal import-tags -project $ProjectPath -input $GitPath\tags

# Importar configuración de hardware
tia-portal import-hardware -project $ProjectPath -input $GitPath\hardware
```

### Uso con IA

#### Generar commits descriptivos

```
Genera un mensaje de commit descriptivo para estos cambios.

CAMBIOS:
- Modificado FB_MotorControl
- Añadido FC_Escalado_Temperatura
- Actualizado UDT_Motor

Por favor, genera un mensaje de commit siguiendo el formato Conventional Commits:
- type: feat, fix, docs, style, refactor, test, chore
- scope: área afectada
- subject: descripción corta
- body: descripción detallada
```

#### Generar diff de bloques

```
Genera un diff legible entre dos versiones de este bloque.

VERSIÓN ANTERIOR: [pegar código anterior]
VERSIÓN ACTUAL: [pegar código actual]

Por favor, genera un diff en formato:
- Líneas añadidas marcadas con +
- Líneas eliminadas marcadas con -
- Resumen de cambios
```

### Best practices

1. **Commits atómicos** — Un commit por cambio lógico
2. **Mensajes descriptivos** — Usa Conventional Commits
3. **Branches por feature** — Usa branches para cada feature
4. **Pull requests** — Revisa código antes de merge
5. **Tags por versión** — Usa tags para releases

---

## 📋 Integración con Jira

### Descripción

Integrar TIA Portal con Jira para seguimiento de tareas, bugs y mejoras.

### Flujo de trabajo

```
1. Crear issue en Jira
2. Asignar issue a desarrollador
3. Desarrollar bloque en TIA Portal
4. Actualizar issue con progreso
5. Crear pull request con referencia a issue
6. Merge y cerrar issue
```

### Configuración

#### 1. Crear proyecto Jira

- **Nombre**: TIA Portal Development
- **Key**: TIA
- **Tipos de issue**: Task, Bug, Improvement, Epic

#### 2. Configurar campos personalizados

| Campo | Tipo | Descripción |
|-------|------|-------------|
| Bloque | Text | Nombre del bloque afectado |
| PLC | Text | PLC donde se implementa |
| Prioridad | Select | Critical, High, Medium, Low |
| Complejidad | Select | 1-5 |
| Tiempo estimado | Number | Horas estimadas |

#### 3. Integración con Git

Configurar Jira para:
- Mostrar commits en issues
- Cerrar issues automáticamente con commits
- Mostrar pull requests

### Uso con IA

#### Generar descripción de issue

```
Genera una descripción detallada de issue Jira para este cambio.

CAMBIO: [describir cambio]

Por favor, genera:
- Título corto y descriptivo
- Descripción detallada
- Criterios de aceptación
- Bloques afectados
- PLCs afectados
- Riesgos potenciales
- Dependencias

Formato: Markdown
```

#### Generar casos de prueba

```
Genera casos de prueba para este issue Jira.

ISSUE: [pegar descripción del issue]

Por favor, genera:
- Casos de prueba
- Pasos de prueba
- Resultados esperados
- Datos de prueba

Formato: Tabla
```

### Automatización

#### Script de actualización de Jira

```powershell
# Actualizar issue de Jira
# update-jira-issue.ps1

param(
    [string]$IssueKey,
    [string]$Status,
    [string]$Comment
)

# Actualizar estado
jira update-issue -key $IssueKey -status $Status

# Añadir comentario
jira add-comment -key $IssueKey -comment $Comment
```

---

## 📖 Integración con Confluence

### Descripción

Integrar TIA Portal con Confluence para documentación técnica, manuales y procedimientos.

### Flujo de trabajo

```
1. Generar documentación con IA
2. Crear página en Confluence
3. Formatear contenido
4. Añadir diagramas y tablas
5. Vincular a Jira issues
6. Mantener actualizada
```

### Configuración

#### 1. Crear espacio en Confluence

- **Nombre**: TIA Portal Documentation
- **Key**: TIA
- **Descripción**: Documentación técnica de proyectos TIA Portal

#### 2. Estructura de páginas

```
TIA Portal Documentation
├── Proyectos
│   ├── Proyecto A
│   │   ├── Descripción
│   │   ├── Arquitectura
│   │   ├── Bloques
│   │   ├── Tags
│   │   └── Procedimientos
│   └── Proyecto B
├── Estándares
│   ├── Naming conventions
│   ├── Best practices
│   └── Plantillas
└── Manuales
    ├── Instalación
    ├── Configuración
    └── Troubleshooting
```

### Uso con IA

#### Generar documentación para Confluence

```
Genera documentación en formato Confluence para este bloque.

BLOQUE: [pegar código]

Por favor, genera:
- Título
- Descripción
- Interfaz (tablas)
- Lógica
- Diagramas (ASCII)
- Ejemplos de uso
- Notas

Formato: Confluence Storage Format (si es posible) o Markdown
```

#### Generar procedimientos operativos

```
Genera procedimientos operativos para este sistema.

SISTEMA: [describir sistema]

Por favor, genera:
- Procedimiento de arranque
- Procedimiento de parada
- Procedimiento de emergencia
- Procedimiento de mantenimiento
- Procedimiento de diagnóstico

Formato: Pasos numerados con precauciones
```

### Automatización

#### Script de publicación a Confluence

```powershell
# Publicar documentación a Confluence
# publish-to-confluence.ps1

param(
    [string]$MarkdownFile,
    [string]$PageId
)

# Convertir Markdown a Confluence format
$confluenceFormat = Convert-MarkdownToConfluence -file $MarkdownFile

# Publicar a Confluence
confluence update-page -id $PageId -content $confluenceFormat
```

---

## 💬 Integración con Microsoft Teams

### Descripción

Integrar TIA Portal con Microsoft Teams para notificaciones, colaboración y monitoreo.

### Flujo de trabajo

```
1. Evento en TIA Portal (compilación, error, alarma)
2. Webhook envía notificación a Teams
3. Canal de Teams recibe notificación
4. Equipo puede responder y tomar acción
5. Seguimiento en Teams
```

### Configuración

#### 1. Crear webhook de Teams

1. Ve al canal de Teams
2. Configuración → Conectores
3. "Incoming Webhook"
4. Configurar nombre y webhook URL

#### 2. Configurar notificaciones

```powershell
# Configurar webhook de Teams
# configure-teams-webhook.ps1

param(
    [string]$WebhookUrl
)

# Guardar webhook URL en configuración
Set-Content -Path "config\webhook-url.txt" -Value $WebhookUrl
```

### Uso con IA

#### Generar mensajes de Teams

```
Genera un mensaje de Teams para esta notificación.

EVENTO: [describir evento]
DETALLES: [detalles del evento]

Por favor, genera un mensaje de Teams con:
- Título
- Descripción
- Detalles del evento
- Acciones recomendadas
- Enlaces a documentación

Formato: Adaptive Cards JSON
```

#### Generar alertas de Teams

```
Genera una alerta de Teams para esta alarma.

ALARMA: [describir alarma]
SEVERIDAD: [Critical/High/Medium/Low]
UBICACIÓN: [ubicación en el sistema]

Por favor, genera una alerta de Teams con:
- Severidad
- Descripción
- Ubicación
- Acciones recomendadas
- Enlaces a procedimientos

Formato: Adaptive Cards JSON con colores según severidad
```

### Automatización

#### Script de notificación a Teams

```powershell
# Enviar notificación a Teams
# send-teams-notification.ps1

param(
    [string]$Title,
    [string]$Message,
    [string]$Severity = "Info"
)

# Leer webhook URL
$webhookUrl = Get-Content "config\webhook-url.txt"

# Crear mensaje
$body = @{
    title = $Title
    text = $Message
    themeColor = switch ($Severity) {
        "Critical" { "FF0000" }
        "High" { "FFA500" }
        "Medium" { "FFFF00" }
        "Low" { "00FF00" }
        default { "0078D4" }
    }
} | ConvertTo-Json

# Enviar a Teams
Invoke-RestMethod -Uri $webhookUrl -Method Post -Body $body -ContentType "application/json"
```

---

## 📊 Integración con Power BI

### Descripción

Integrar TIA Portal con Power BI para dashboards, análisis de datos y monitoreo en tiempo real.

### Flujo de trabajo

```
1. Exportar datos de TIA Portal
2. Importar en Power BI
3. Crear dashboards
4. Publicar en Power BI Service
5. Compartir con stakeholders
```

### Configuración

#### 1. Configurar exportación de datos

```powershell
# Exportar datos de TIA Portal para Power BI
# export-data-for-powerbi.ps1

param(
    [string]$ProjectPath,
    [string]$OutputPath
)

# Exportar tags como CSV
tia-portal export-tags -project $ProjectPath -output $OutputPath\tags.csv

# Exportar alarmas como CSV
tia-portal export-alarms -project $ProjectPath -output $OutputPath\alarms.csv

# Exportar eventos como CSV
tia-portal export-events -project $ProjectPath -output $OutputPath\events.csv
```

#### 2. Crear dataset en Power BI

1. Abrir Power BI Desktop
2. Obtener datos → CSV
3. Importar archivos exportados
4. Crear relaciones entre tablas
5. Crear medidas DAX

### Uso con IA

#### Generar medidas DAX

```
Genera medidas DAX para este dashboard de Power BI.

DATASET: [describir dataset]
MÉTRICAS: [listar métricas deseadas]

Por favor, genera medidas DAX para:
- Total de alarmas
- Alarmas por severidad
- Tendencia de alarmas
- Tiempo medio de resolución
- Eficiencia del sistema

Formato: DAX
```

#### Generar visualizaciones

```
Genera recomendaciones de visualizaciones para este dashboard.

DATASET: [describir dataset]
OBJETIVO: [objetivo del dashboard]

Por favor, recomienda:
- Tipos de gráficos
- Métricas a mostrar
- Filtros a aplicar
- Drill-downs
- Alertas visuales

Formato: Lista con descripciones
```

### Ejemplos de dashboards

#### Dashboard de alarmas

```dax
// Total de alarmas
Total Alarmas = COUNTROWS(Alarmas)

// Alarmas por severidad
Alarmas por Severidad =
SUMMARIZE(
    Alarmas,
    Alarmas[Severidad],
    "Total", COUNTROWS(Alarmas)
)

// Tendencia de alarmas (últimos 7 días)
Tendencia Alarmas 7D =
CALCULATE(
    [Total Alarmas],
    DATESINPERIOD(
        'Calendario'[Fecha],
        TODAY(),
        -7,
        DAY
    )
)

// Tiempo medio de resolución
Tiempo Medio Resolución =
AVERAGEX(
    Alarmas,
    DATEDIFF(
        Alarmas[Inicio],
        Alarmas[Fin],
        MINUTE
    )
)
```

#### Dashboard de eficiencia

```dax
// Eficiencia del sistema
Eficiencia Sistema =
DIVIDE(
    [Tiempo Producción],
    [Tiempo Total]
)

// OEE (Overall Equipment Effectiveness)
OEE =
[Disponibilidad] * [Rendimiento] * [Calidad]

// Tendencia de OEE
Tendencia OEE =
CALCULATE(
    [OEE],
    DATESINPERIOD(
        'Calendario'[Fecha],
        TODAY(),
        -30,
        DAY
    )
)
```

### Automatización

#### Script de actualización de Power BI

```powershell
# Actualizar dataset de Power BI
# refresh-powerbi-dataset.ps1

param(
    [string]$WorkspaceId,
    [string]$DatasetId
)

# Actualizar dataset
powerbi refresh-dataset -workspace $WorkspaceId -dataset $DatasetId
```

---

## 📚 Resumen de integraciones

| Herramienta | Propósito | Complejidad | Beneficios |
|-------------|-----------|-------------|------------|
| **Git** | Control de versiones | Media | Historial, colaboración, rollback |
| **Jira** | Gestión de tareas | Baja | Seguimiento, asignación, reporting |
| **Confluence** | Documentación | Media | Centralizada, colaborativa, searchable |
| **Teams** | Notificaciones | Baja | Tiempo real, colaboración, alertas |
| **Power BI** | Dashboards | Alta | Visualización, análisis, reporting |

---

## 💡 Consejos finales

1. **Automatiza todo lo posible** — Usa scripts para tareas repetitivas
2. **Integra con IA** — Usa IA para generar contenido automáticamente
3. **Mantén consistencia** — Usa plantillas y estándares
4. **Documenta integraciones** — Crea documentación de cada integración
5. **Revisa regularmente** — Actualiza integraciones según necesidades

---

## 📚 Recursos adicionales

- [Tutoriales](../tutoriales/) — Aprende a usar IA + TIA Portal
- [Casos de uso](../casos-de-uso/) — Ejemplos reales
- [Guía de prompts](../prompts/) — Prompts efectivos
- [Best practices](../best-practices/) — Mejores prácticas
