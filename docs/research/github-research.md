# Informe de investigación — Descubrimiento GitHub (Awesome TIA Portal)

> Fase 1 y 2 del plan de expansión. Informe generado localmente en la rama `feat/github-research-templates`.
> Informe original del 12/11/2026; la version publica filtrada para 13/11/2026 excluye README y arboles de archivos originales de terceros.

## 1. Alcance y método

- **Objetivo:** investigar el ecosistema público de GitHub relacionado con Siemens TIA Portal, S7-1200, S7-1500, WinCC, PLC, TIA Openness y librerías de automatización industrial, para ampliar el Awesome TIA Portal con referencias de alto valor y plantillas originales.
- **Herramientas usadas:** GitHub CLI (`gh`, autenticado como `iagorobo24-hub`, scopes `repo`, `workflow`), API REST de GitHub (búsqueda y core), lecturas directas de README/LICENSE de candidatos.
- **Límites registrados:** la API de búsqueda permite 30 consultas/min. Se realizaron 34 consultas. No se afirma haber encontrado todos los proyectos; se documenta el alcance real. Los forks no se contaron como proyectos independientes (el filtro `isFork=false` los excluyó). Los repositorios archivados se señalan.

## 2. Consultas de búsqueda realizadas

| # | Consulta | Archivo de resultados | Resultados |
|---|----------|-----------------------|------------|
| 01 | `TIA Portal` | `docs/research/busquedas/01_tia-portal.json` | 100 |
| 02 | `Siemens S7-1500` | `docs/research/busquedas/02_s7-1500.json` | 89 |
| 03 | `Siemens SCL` | `docs/research/busquedas/03_siemens-scl.json` | 39 |
| 04 | `PLCopen XML` | `docs/research/busquedas/04_plcopen-xml.json` | 24 |
| 05 | `Siemens S7-1200` | `docs/research/busquedas/05_s7-1200.json` | 100 |
| 06 | `Siemens OPC UA` | `docs/research/busquedas/06_siemens-opc-ua.json` | 5 |
| 07 | `Siemens Profinet` | `docs/research/busquedas/07_siemens-profinet.json` | 1 |
| 08 | `TIA Portal Openness` | `docs/research/busquedas/08-tia-openness.json` | 52 |
| 09 | `PLC state machine` | `docs/research/busquedas/09-plc-state-machine.json` | 6 |
| 10 | `Siemens HMI faceplates` | `docs/research/busquedas/10-siemens-hmi-faceplates.json` | 0 |
| 11 | `WinCC Unified` | `docs/research/busquedas/11-wincc-unified.json` | 77 |
| 12 | `PLCSIM Advanced` | `docs/research/busquedas/12-plcsim-advanced.json` | 27 |
| 13 | `TIA Portal examples` | `docs/research/busquedas/13-tia-portal-examples.json` | 1 |
| 14 | `Siemens Modbus TCP` | `docs/research/busquedas/14-siemens-modbus.json` | 2 |
| 15 | `Siemens MQTT` | `docs/research/busquedas/15-siemens-mqtt.json` | 2 |
| 16 | `Siemens PLC programming` | `docs/research/busquedas/16-siemens-plc-programming.json` | 6 |
| 17 | `Structured Control Language` | `docs/research/busquedas/17-structured-control-language.json` | 11 |
| 18 | `PLC coding standards` | `docs/research/busquedas/18-plc-coding-standards.json` | 0 |
| 19 | `TIA Portal code generation` | `docs/research/busquedas/19-tia-code-generation.json` | 0 |
| 20 | `Siemens TIA Portal Git integration` | `docs/research/busquedas/20-tia-git-integration.json` | 0 |
| 21 | `Siemens S7-300` | `docs/research/busquedas/21-s7-300.json` | 66 |
| 22 | `Siemens S7-400` | `docs/research/busquedas/22-s7-400.json` | 2 |
| 23 | `Totally Integrated Automation` | `docs/research/busquedas/23-tia.json` | 2 |
| 24 | `PLC function blocks` | `docs/research/busquedas/24-plc-function-blocks.json` | 1 |
| 25 | `PLC sequencer` | `docs/research/busquedas/25-plc-sequencer.json` | 6 |
| 26 | `PLC alarm management` | `docs/research/busquedas/26-plc-alarm-management.json` | 0 |
| 27 | `PLC diagnostics` | `docs/research/busquedas/27-plc-diagnostics.json` | 3 |
| 28 | `topic:tia-portal` | `docs/research/busquedas/28-topic-tia-portal.json` | 100 |
| 29 | `topic:siemens-plc` | `docs/research/busquedas/29-topic-siemens-plc.json` | 61 |
| 30 | `topic:s7-1500` | `docs/research/busquedas/30-topic-s7-1500.json` | 46 |
| 31 | `OSCAT` | `docs/research/busquedas/31-oscat.json` | 100 |
| 32 | `snap7` | `docs/research/busquedas/32-snap7.json` | 100 |
| 33 | `Siemens TIA Portal library` | `docs/research/busquedas/33-tia-library.json` | 3 |
| 34 | `topic:siemens` | `docs/research/busquedas/34-topic-siemens.json` | 100 |

- **Consultas totales:** 34.
- **Resultados brutos (con duplicados entre consultas):** 1132.
- **Repositorios únicos tras deduplicar:** 961.
- **Repositorios aparecidos en más de una consulta:** 99.
- **Forks:** 0 (excluidos por filtro `isFork=false`).
- **Archivados:** 3.
- **Sin licencia declarada:** varios (se trata como "licencia desconocida" → solo referencia externa, sin copiar código).

Datos consolidados: `docs/research/consolidado.json`.
Fichas publicas de metadatos de 70 candidatos: `docs/research/analisis.json`. Los README completos y arboles de archivos originales se conservan solo localmente y no se redistribuyen.

## 3. Repositorios más relevantes (clasificación A/B/C/D)

Criterios (sobre 100): utilidad práctica 25, reutilización/modularidad 20, calidad técnica 20, documentación 10, compatibilidad/integración 10, mantenimiento 10, interés comunitario 5.

### A — Integración prioritaria (enlazar en el Awesome List)

| Proyecto | URL | Licencia | Nota |
|---|---|---|---|
| [`siemens/tia-portal-openness-code-snippets`](https://github.com/siemens/tia-portal-openness-code-snippets) | — | MIT (código fuente) / condiciones royalty-free Siemens (binarios) | Snippets oficiales de Siemens de TIA Portal Openness API V20 (C#). Código fuente bajo MIT; binarios bajo condiciones royalty-free. Solo enlazar, no redistribuir binarios. |
| [`siemens/simatic-s7-webserver-api`](https://github.com/siemens/simatic-s7-webserver-api) | — | MIT | Librería .NET oficial de Siemens para el Webserver API de S7-1500 y S7-1200 G2/1200. Muy bien documentada, con tabla de compatibilidad por versión de PLC. |
| [`gijzelaerr/python-snap7`](https://github.com/gijzelaerr/python-snap7) | — | MIT | Librería Python pura para S7 (S7-300/400 y S7-1200/1500 con PUT/GET). Documentada en ReadTheDocs, con matriz de hardware probado. |

### B — Referencia recomendada

| Proyecto | URL | Licencia | Nota |
|---|---|---|---|
| [`robinson/gos7`](https://github.com/robinson/gos7) | — | BSD-3-Clause | Implementación de protocolo S7 en Go puro. |
| [`Gunders89/vscode-scl`](https://github.com/Gunders89/vscode-scl) | — | MIT | Soporte de lenguaje SCL y snippets para Visual Studio Code. Herramienta de productividad para editar fuentes SCL fuera de TIA. |
| [`enlyze/S7-Project-Explorer`](https://github.com/enlyze/S7-Project-Explorer) | — | MIT | Abre proyectos STEP 7 (.s7p, S7-300/400), navega variables y exporta CSV. Útil para ingeniería inversa/documentación de equipos legacy. |
| [`apache/plc4x`](https://github.com/apache/plc4x) | — | Apache-2.0 | Adaptador de protocolos industriales (S7 entre otros) bajo Apache Software Foundation. Estándar abierto, pero de propósito general IoT. |
| [`jasperdekeuk/PLCsim-Advanced-Manager`](https://github.com/jasperdekeuk/PLCsim-Advanced-Manager) | — | MIT | Gestor web de instancias PLCSIM Advanced (start/stop, read/write, snapshots, nodegraph). Requiere PLCSIM Advanced v5+ licenciado. |
| [`LeoSunSET/SIEMENS_SIMATIC_STEP7_Classic_Algorithms`](https://github.com/LeoSunSET/SIEMENS_SIMATIC_STEP7_Classic_Algorithms) | — | MIT | Colección de algoritmos clásicos para S7 en STL/SCL (S7-300/400/1200/1500). Referencia de bloques reutilizables. |
| [`bonk-dev/HarpoS7`](https://github.com/bonk-dev/HarpoS7) | — | MIT | Librería C# de autenticación de sesiones S7 Comm Plus (challenge V16-, TLS V17+). Avanzado; para integración de comunicación. |
| [`proemmer/dacs7`](https://github.com/proemmer/dacs7) | — | Apache-2.0 | Librería .NET para lectura/escritura en S7 por RFC1006. |

### C — Investigación futura (requiere verificación de licencia o trabajo)

| Proyecto | URL | Licencia | Nota |
|---|---|---|---|
| [`OttoMeister/Siemens-Tia-Portal-PID-Controller`](https://github.com/OttoMeister/Siemens-Tia-Portal-PID-Controller) | — | WTFPL | Bloques PID/PI en SCL estilo OSCAT para S7-1200/1500. Licencia WTFPL (permisiva pero no estándar); usar solo como referencia externa, no copiar sin revisar. |
| [`IgorCoraine/TIA_Add-In_VCI_Git_Connector`](https://github.com/IgorCoraine/TIA_Add-In_VCI_Git_Connector) | — | MIT | Add-In de TIA Portal para conectar VCI a Git. Basado en proyecto de soporte de Siemens. Útil para version control en TIA. |
| [`mking2203/CodeGeneratorOpenness`](https://github.com/mking2203/CodeGeneratorOpenness) | — | GPL-3.0 | Generador de código TIA Portal vía Openness (C#). **GPL-3.0 (copyleft)**: no integrar código en este repo MIT sin aprobación explícita; solo referencia externa con advertencia de licencia. |
| [`rickgaiser/TiaMcp`](https://github.com/rickgaiser/TiaMcp) | — | AGPL-3.0 | MCP server para TIA Portal. **AGPL-3.0 (copyleft fuerte)**: no integrar; solo referencia externa. |
| [`RoanBrand/MQTT-Siemens-S7-300`](https://github.com/RoanBrand/MQTT-Siemens-S7-300) | — | (no declarada) | Bloque MQTT en SCL para S7-300 con CP343-1. Licencia desconocida → solo referencia externa. |
| [`ChristofGroschke/MQTT-Siemens-S7-1500`](https://github.com/ChristofGroschke/MQTT-Siemens-S7-1500) | — | (no declarada) | Puerto del bloque MQTT a S7-1500 en SCL. Licencia desconocida → solo referencia externa. |
| [`Rynstick/LBS`](https://github.com/Rynstick/LBS) | — | (no declarada) | Librería WinCC Unified. Licencia desconocida → solo referencia externa. |
| [`Krusty84/awesome-siemens-dis`](https://github.com/Krusty84/awesome-siemens-dis) | — | MIT | Awesome list de Siemens Digital Industries (enfoque PLM/CAD, no solo TIA). Referencia meta. |

### D — Descartado

| Proyecto | URL | Motivo |
|---|---|---|
| [`Sadpainy/Stuxnet`](https://github.com/Sadpainy/Stuxnet) | — | Contenido de ICS/malware, no constructivo para automatización legítima; licencia AGPL-3.0. |
| Varios con licencia GPL/AGPL sin aprobación | — | No se integra código copyleft en este repo MIT sin aprobación explícita (regla 6 del plan). |
| Repositorios archivados (3) | — | Sin mantenimiento; solo referencia histórica si aplica. |

## 4. Licencias y trazabilidad

- Durante la investigacion se revisaron archivos LICENSE de 20 candidatos. Los textos completos de terceros no se redistribuyen; `docs/research/analisis.json` conserva metadatos y enlaces.
- **Regla aplicada:** licencia desconocida = solo referencia externa y análisis, sin copiar código (regla 1 y 9 del plan).
- **Copyleft:** GPL-3.0 (`mking2203/CodeGeneratorOpenness`, `miguelob/ICS-Hacking`, `slickz44/DT_PSA_OPCV_Siemens`, `Parozzz/TiaUtilities`) y AGPL-3.0 (`rickgaiser/TiaMcp`, `Sadpainy/Stuxnet`) no se integran; solo referencia externa con advertencia.
- **Siemens propietario:** los snippets de Openness tienen código fuente bajo MIT, pero las partes en objeto/binario siguen condiciones royalty-free de Siemens. No se redistribuyen binarios Siemens (regla 7).
- **WTFPL:** `OttoMeister/...PID-Controller` es permisivo pero no estándar; se trata como referencia externa, no como código a integrar.

## 5. Compatibilidad conocida (verificada contra archivos reales)

- `siemens/tia-portal-openness-code-snippets`: TIA Portal V20 (C#/.NET). README declara V20.
- `siemens/simatic-s7-webserver-api`: .NET 4.8 / Standard 2.0 / .NET 8-10. Tabla de compatibilidad PLC: S7-1500 (firmware 2.9-4.1) y S7-1200 (G2 y clásico).
- `gijzelaerr/python-snap7`: S7-300/400 y S7-1200/1500 (PUT/GET activado, no bloques optimizados). Python 3.10+.
- `LeoSunSET/...Classic_Algorithms`: S7-300, S7-400, TIA S7-1200, TIA S7-1500. Fuentes STL/SCL.
- El resto: compatibilidad con versión de TIA no confirmada en los archivos leídos; anotar como "no verificado" si se enlaza.

## 6. Recomendaciones para el Awesome List

1. Añadir sección "Referencias externas verificadas" al README con los proyectos A y B (enlace, descripción breve, licencia, utilidad).
2. No integrar código de terceros sin licencia explícita compatible con MIT; usar solo enlaces.
3. Añadir advertencia de licencia junto a `CodeGeneratorOpenness` (GPL-3.0) y `TiaMcp` (AGPL-3.0) si se enlazan.
4. Mantener `ia-tia-portal/` (IA + TIA) separado de esta sección de automatización general.

## 7. Limitaciones de cobertura

- Solo se agotó la cuota de búsqueda pública (30/min); quedaron términos por explorar (ej. "S7comm", "ISO-on-TCP", "RFC1006", "WinCC Professional", "faceplate", "S7-1500 PLC program example").
- No se clonaron repositorios para compilar ni probar; el análisis se basó en README, LICENSE y árbol de archivos vía API.
- No se verificó compilación en TIA Portal de ningún proyecto de terceros.
- No se afirmó exhaustividad: se documentan 961 únicos de 1132 brutos.

## 8. Alcance de los datos publicados

Los resultados de las 34 busquedas y el conjunto consolidado representan metadatos publicos del momento de la investigacion. El fichero `analisis.json` contiene 70 fichas sin README completos, codigo, textos de licencia ni arboles de archivos de terceros. El material bruto permanece solo en el worktree local de investigacion y no forma parte de la publicacion.
Las referencias de compatibilidad y licencias son observaciones historicas, no validaciones de uso industrial ni permisos para redistribuir fuentes ajenas.
