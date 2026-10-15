# IA + TIA Portal

La conexión para automatizar ingeniería en TIA Portal se basa en la [API oficial Siemens Openness](https://docs.tia.siemens.cloud/r/en-us/v20/tia-portal-openness-api-for-automation-of-engineering-workflows/basics/openness-tasks/introduction). Un servidor MCP hace que sus operaciones sean herramientas para un agente; una aplicación .NET también puede llamar a la API directamente. El control gráfico complementa la API cuando necesitas ver un editor, diálogo o HMI.

## Ruta de aprendizaje

1. [Conexión profesional V20](guias/conexion-profesional-v20.md): requisitos, capas, Doctor, identificación del proyecto, fixture y evidencia.
2. [Catálogo del repositorio](../CATALOG.md): distingue código real, fichas de diseño y recursos pendientes.
3. [Tutoriales históricos](tutoriales/): material anterior a la comprobación local completa; **revisa sus requisitos y enlaces** antes de ejecutar comandos. Se están actualizando por etapas.

## Herramientas abiertas para explorar

| Proyecto | Uso principal | Comprobación aquí |
|---|---|---|
| [heilingbrunner/tiaportal-mcp](https://github.com/heilingbrunner/tiaportal-mcp) | Lectura y análisis mediante MCP + Openness. | Compilado y utilizado en el [workspace TIA-Claude](https://github.com/iagorobo24-hub/T-IA-Portal-RocaRoibas), con perfil de solo lectura por defecto. |
| [bulaofen0036-coder/TIA_Portal_Openness_MCP](https://github.com/bulaofen0036-coder/TIA_Portal_Openness_MCP) | Creación de proyectos, hardware y HMI según perfil. | Binario V20 compilado y algunas operaciones probadas en fixtures; el inventario de herramientas no acredita todas ellas. |

Los nombres, opciones y requisitos de esos proyectos pueden cambiar. Comprueba su documentación y prueba una versión exacta en un clon antes de adoptar una receta.

## Límites que importan

- La descarga a una CPU real puede mover maquinaria. Identifica el target y obtén autorización explícita antes de hacerlo.
- `Doctor`, una lista de herramientas y una compilación limpia son pruebas diferentes. El comportamiento requiere PLCSIM o Runtime compatible.
- No subas proyectos de cliente, credenciales, capturas con datos sensibles ni binarios de TIA Portal.
- No existe aquí un “control total” acreditado de TIA: las funciones disponibles dependen de versión, API, servidor MCP, licencia, hardware y proyecto.

Puedes [proponer una herramienta o una corrección](../CONTRIBUTING.md) con versión, fuente y evidencia reproducible.
