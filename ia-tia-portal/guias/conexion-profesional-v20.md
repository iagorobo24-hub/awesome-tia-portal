# Conectar agentes de IA con TIA Portal V20

Esta guía explica la arquitectura que se ha probado en el workspace abierto [TIA-Claude](https://github.com/iagorobo24-hub/T-IA-Portal-RocaRoibas). Separa **la API**, **el puente para agentes**, **la interfaz gráfica** y **la simulación**, porque una prueba de conexión no valida las otras capas. El ejemplo local se realizó en Windows y TIA Portal V20; una instalación nueva debe repetir todas las comprobaciones.

## 1. Elige la vía correcta

| Vía | Sirve para | Alcance demostrado en el workspace de referencia |
|---|---|---|
| [Siemens TIA Portal Openness](https://docs.tia.siemens.cloud/r/en-us/v20/tia-portal-openness-api-for-automation-of-engineering-workflows/tia-portal-openness-api/general-functions/connecting-to-the-tia-portal) | API oficial .NET para objetos de ingeniería. | Carga V20 y enumeración de procesos desde un cliente .NET independiente; el cliente directo aún no ha leído un proyecto. |
| MCP `tia-inspect` | Expone a agentes lectura, búsqueda, exportación y compilación por Openness. | Doctor, árboles, fuentes y varias operaciones en fixtures. Perfil de lectura por defecto. |
| MCP `tia-create` | Creación de proyectos, hardware, red y HMI según el perfil y las herramientas presentes. | Scaffold y operaciones acotadas en copias; la presencia de una herramienta en `tools/list` no equivale a una prueba de uso. |
| Computer Use nativo | Maneja la ventana, editores y diálogos visibles. | Edición PLC y HMI ensayada en clones; depende del agente y del permiso de esa sesión. |
| PLCSIM Advanced / Runtime HMI | Comprueba comportamiento. | Adaptador virtual detectado; comportamiento PLC y Runtime Advanced V20 siguen pendientes. |

MCP no es otra API Siemens: sus servidores llaman a Openness. Una aplicación .NET puede llamar a la misma API **directamente**; ofrece control sobre lo que programes, pero exige implementar y verificar sus propias barreras. La API de scripting de CODESYS pertenece al entorno CODESYS y no conecta TIA Portal.

## 2. Prepara Windows y la versión

1. Instala **TIA Portal V20 con Openness** y los componentes de ingeniería que requiera tu proyecto. Una licencia o un HSP ausente puede impedir abrirlo aunque la API cargue.
2. Comprueba que tu usuario pertenece al grupo Windows `Siemens TIA Openness`; tras añadirlo, cierra e inicia sesión.
3. Clona el [workspace de referencia](https://github.com/iagorobo24-hub/T-IA-Portal-RocaRoibas) y sigue su `README.md` para compilar los dos servidores locales. Sus binarios no se distribuyen en Git.
4. Trabaja primero con un **fixture desechable** de la misma versión de TIA. Conserva el original y un backup aparte.

En ese workspace, el primer diagnóstico es:

```powershell

.\30-tools\scripts\Invoke-TiaMcp.ps1 -Calls @(@{ name = 'Doctor' })
```

Exige V20 activo, componentes `Engineering` y `Portal` disponibles y `isUserInGroup=true`. `Connected=false` solo dice que todavía no hay un proyecto conectado.

## 3. Identifica el proyecto antes de conectar

Si TIA ya tiene una ventana abierta, identifica visualmente **versión, proyecto y ventana**. Confirma que es el fixture que quieres probar. El servidor `tia-inspect` usado aquí no ofrece `Attach`; un `Connect` satisfactorio **no demuestra** que se haya adjuntado a la ventana visible. No abras una segunda instancia sobre un proyecto ajeno para compensar esa incertidumbre.

Si la ventana no está abierta, el runner aislado puede usar una instancia Openness sin interfaz para un fixture declarado con manifiesto y backup. Ejecuta toda la secuencia MCP bajo el lease único del workspace; Openness no debe recibir operaciones paralelas.

Solo después de `Doctor` y la identificación, lee `GetProjectTree` y `GetSoftwareTree`. Copia los **paths reales** que devuelven para `GetBlocks`, `GetBlockSource`, `GetTags` o `CompileSoftware`; nombres intuitivos no son rutas válidas.

## 4. Primer recorrido seguro

1. **Lectura:** árbol de proyecto y software, metadatos de bloques, protección, Safety, tags y fuente completa del bloque objetivo.
2. **Propuesta:** un cambio pequeño en una copia textual, con diff y objetivo funcional.
3. **Preflight de escritura:** proyecto exacto, backup, fixture, bloque estándar SCL con `isFailsafe=false`, sin know-how protection ni tags Safety desconocidos. Si falta un dato de clasificación, se detiene.
4. **Preview:** `dryRun` o vista previa de la herramienta, cuando exista.
5. **Aplicación en clon:** un bloque u objeto por vez. Compila con **0 errores antes de guardar**; después exporta la fuente y lee de nuevo el objeto.
6. **Prueba funcional:** para PLC, una CPU virtual desechable con adaptador y destino virtual inequívocos; para HMI, un Runtime compatible con el dispositivo. Registra entradas, salidas y resultado observable.

La guía del workspace [AGENTS.md](https://github.com/iagorobo24-hub/T-IA-Portal-RocaRoibas/blob/master/AGENTS.md) es la referencia operativa si vas a usar sus runners. En el perfil V20 documentado, la aplicación automática de propuestas SCL permanece bloqueada porque faltan los importadores requeridos; **un preview local no significa cambio aplicado**.

## 5. Lo que muestra cada evidencia

| Evidencia | Conclusión admisible |
|---|---|
| `Doctor` y `tools/list` | Entorno y superficie de herramientas disponibles. |
| `GetProjectTree` y fuente | Proyecto y objeto leídos desde una sesión identificada. |
| `CompileSoftware: 0 errores` | Consistencia de compilación en ese proyecto y versión. |
| Guardado, exportación y segunda lectura | Cambio persistido y objeto leído de nuevo. |
| Transición observada en PLCSIM o Runtime | Comportamiento comprobado en esas condiciones de prueba. |

El fichero local `70-runs/acceptance/status-latest.json` del workspace de referencia debe consultarse con su **fecha**: es generado por las pruebas y no está publicado en Git. Puede avanzar y no describe automáticamente tu máquina. En la evidencia local de septiembre de 2026, el Runtime Advanced V20 compatible y la prueba funcional PLC seguían sin verificar.

## 6. Límite con instalaciones reales

Escribir un proyecto y **descargar a una CPU** son operaciones diferentes. Las pruebas libres de descarga se limitan a una instancia PLCSIM virtual identificada. Una descarga a hardware físico necesita confirmación explícita para ese PLC y esos bloques en el momento de ejecutarla; si no se puede demostrar que el destino es virtual, se trata como físico. Los bloques F/Safety y protegidos quedan fuera de este flujo.

## Siguiente paso reproducible

Completa en tu máquina `Doctor → fixture V20 identificado → GetProjectTree → GetSoftwareTree → exportación → compilación → cierre/limpieza`, y conserva los resultados. Repite después una mutación pequeña permitida en otro fixture con backup y lectura posterior. Solo entonces considera conectar un proyecto de trabajo real en modo lectura.
