# Primeros pasos con MCP y TIA Portal V20

> **Necesitas**: TIA Portal V20 con Openness (usuario en el grupo `Siemens TIA Openness`), un servidor MCP local y un proyecto de demostración desechable. Nada de descargas a hardware real. Allí están los requisitos reales, las tres capas de acceso, la comprobación `Doctor` y el recorrido seguro de lectura sobre un fixture.

## Resultado de este primer paso

Al terminar debes tener **evidencia fechada** de:

1. TIA Portal V20 y Openness instalados, usuario en el grupo `Siemens TIA Openness`.
2. Servidor MCP local iniciado en perfil de lectura y `Doctor` satisfactorio.
3. Proyecto de demostración identificado antes de abrir o adjuntar una sesión.
4. `GetProjectTree` y `GetSoftwareTree` completados, con las rutas reales guardadas.
5. Una fuente o metadato de bloque leídos sin escribir, descargar ni modificar hardware.

Un servidor que arranca o responde a `Doctor` **aún no demuestra** que pueda leer el proyecto deseado. No avances a generación/importación de bloques hasta completar la lectura y preparar un clon con backup. El flujo de escritura y sus bloqueos están documentados en la [guía V20](../guias/conexion-profesional-v20.md#4-primer-recorrido-seguro).
