# Run 20261016-fb-alarm-latch — F1: importación + arnés OB1-SCL + compilación 0/0

Estados: [VERIFICADO] = evidencia live en ficheros JSON del run; [NO VERIFICADO] = pendiente.

## Objetivo

Importar `FB_AlarmLatch` (60-library) en fixture desechable, montar arnés OB1 en SCL
(desviación aprobada: el pack original contemplaba CALL en OB1-LAD), compilar 0/0 y
exportar evidencia. Descarga solo a CPU virtual (PLCSIM), nunca a hardware físico.

## Fixture

- Raíz: `C:\ti-fx\20261016-alarm01\isolated-fixture\` (ruta corta, H5/H7)
- Proyecto: `AgentDemo_V20.ap20` (snapshot prístino del run 20260928, en 70-runs/.../isolated-fixture/backup/)
- Manifiesto `.tia-agent-fixture.json`: re-autorizado tras cada mutación verificada
  (sync backup←project + `New-TiaFixtureManifest.ps1 -ConfirmedDisposable`).

## Cadena de hashes SHA-256 del project dir / .ap20

| Momento | .ap20 SHA-256 |
|---|---|
| F0 antes de escrituras (proyecto = backup) | `1F7A19A7537E209633D165503F853F930BA2C21A7ACAD06EB07AA4E44131B526` |
| Tras B1 (FB generado+compilado+guardado) | `37C36C5A88F8D694263D9AEA5EA8C80A3A6AC9B34A3A64FF8E3EF94D404846E6` |
| Final F1 (OB1 arnés SCL + DB1 + VAT + 11 tags) | `37C36C5A...` (idéntico — ver H-6: el contenedor .ap20 se reescribe solo la 1ª vez; el contenido posterior vive en ficheros internos del directorio) |

## Preflight P0 (f1-preflight-20261016.json)

- `GetBlocks`: `Main` [OB1, LAD] y `FB_AgentDemo` [FB1, SCL] — ambos `isFailsafe=false`,
  `isKnowHowProtected=false`, no write-protected. [VERIFICADO]

- `GetTags`: 2 tags (`Cmd_Enable` %M0.0, `Status_Active` %M0.1), ambas `isSafety=false`, sin nulos. [VERIFICADO]
- Fuentes externas iniciales: 1 (`FB_AgentDemo.scl`). [VERIFICADO]

## Secuencia ejecutada (todas las sesiones via Invoke-McpToolSequence.ps1, lease Local\TIA-Claude-McpSession)

| Sesión | Servidor/perfil | Operaciones | Result |
|---|---|---|---|
| A0 | inspect (read, isolated) | Connect/Open/GetBlocks/GetTags/GetExternalSources/disconnect | ✓ |
| A1 | inspect write | fuentes añ x2, DeleteBlock Main | ✓ pero **sin SaveProject → no persistió** (H-9); re-ejecutada |
| A1b | inspect write | fuentes x2 + DeleteBlock Main + CompileSoftware 0/0 + SaveProject | ✓ persisted |
| B1 | create lite (ConnectIsolated) | GenerateBlocksFromExternalSource(FB_AlarmLatch.scl) → GetBlocks → CompileAndDiagnosePlc **0/0** → Save | ✓ FB_AlarmLatch FB2 SCL |
| A2 | inspect write | 9 tags + CreateInstanceDB(autoNumber=true) + VAT + Compile | ✗ DB número 0 (H-2) — abortado sin guardar |
| A2b | inspect write | 9 tags + CreateInstanceDB(**number=1**) + VAT + GetTags + Compile 0/0 + Save | ✓ |
| B2 | create lite | GenerateBlocksFromExternalSource(OB1_Arnes.scl v1) | ✗ sintaxis de cabecera OB (H-3) — no persistió |
| A2c | inspect write | DeleteExternalSource + re-add OB1_Arnes.scl v2 + Compile 0/0 + Save | ✓ |
| B2b | create lite | GenerateBlocksFromExternalSource(OB1_Arnes.scl v2) → GetBlocks → Compile **0/0 (Main OB1)** → Save/Close | ✓ |
| A3/A3b | inspect write | GetBlockSource (OB+FB XML), ExportBlock FB_AlarmLatch + AlarmPump → XML, GetSoftwareTree | ✓ |

## Resultado final (GetSoftwareTree live, 12:21) [VERIFICADO]

```text
PLC_1
├─ Program blocks
│  ├─ FB_AgentDemo  [FB1, SCL]
│  ├─ FB_AlarmLatch [FB2, SCL]
│  ├─ AlarmPump     [DB1, DB]  (InstanceOf FB_AlarmLatch)
│  └─ Main          [OB1, SCL] (Program cycle / ProgramCycle)
├─ Agent_Signals [11 tags]  (todas isSafety=false)
├─ Watch and force tables → VAT_AlarmLatch [Watch table]
└─ External sources: FB_AgentDemo.scl, FB_AlarmLatch.scl, OB1_Arnes.scl
```text

## SCL exacto del OB1-arnés ejecutado + secuencia usada (condición 3 del usuario)
Fuente: `inputs/OB1_Arnes.scl` (la que se importó; v2 final):

```scl
ORGANIZATION_BLOCK "Main"
{ S7_Optimized_Access := 'TRUE' }
VERSION : 0.1
BEGIN
   // Arnes de prueba para FB_AlarmLatch (bloques-de-funcion/fb-alarm-latch/arnes-ob1.md).
   // Llamada ciclica del DB de instancia AlarmPump con el mapa de memorias:
   //   Condition=M0.0 CmdAck=M0.1 Enable=M0.2 OnDelay=MD4
   //   Active=M2.0 Latched=M2.1 Unacked=M2.2 GoneUnacked=M2.3 Horn=M2.4
   "AlarmPump"(Condition := "Condition",
               CmdAck    := "CmdAck",
               Enable    := "Enable",
               OnDelay   := "OnDelay",
               Active      => "Active",
               Latched     => "Latched",
               Unacked     => "Unacked",
               GoneUnacked => "GoneUnacked",
               Horn        => "Horn");
END_ORGANIZATION_BLOCK
```scl

Secuencia real: `DeleteBlock(PLC_1,"Main")` [tia-inspect] → fuentes
`CreateExternalSourceFromFile("OB1_Arnes.scl")` → `GenerateBlocksFromExternalSource(externalSourceName="OB1_Arnes.scl")`
[tia-create lite] → `CompileAndDiagnosePlc` 0/0 → `SaveProject`.
Readback XML del OB1 compilado (`GetBlockSource Main`): call nest con
`BlockType="FB" Name="FB_AlarmLatch"`, instancia `AlarmPump`, 9 parámetros con
`HasQuotes=true` — coincide con lo de arriba. [VERIFICADO]

## Hallazgos (H)

- **H-1** [VERIFICADO] El build actual de `tia-inspect` no expone generador bloque-desde-fuente
  (`Generate*Source` solo exportan). La generación vive en `tia-create lite 2.7.2`
  (`GenerateBlocksFromExternalSource`). Flujo combinado en dos servidores, mismo fixture.

- **H-2** [VERIFICADO] `CreateInstanceDB` con `autoNumber=true` crea el DB con número 0 → error de
  compilación "invalid number 0". Con `number` explícito (DB1) compila 0/0.

- **H-3** [VERIFICADO] Fuente SCL de OB: braces/TITLE delante de `BEGIN` rechazados (3 errores).
  Forma válida mínima: declaración + `{S7_Optimized_Access}` + `VERSION : 0.1` + `BEGIN...END_ORGANIZATION_BLOCK`.

- **H-4** [VERIFICADO] `GenerateBlocksFromExternalSource` no consume la fuente externa (queda en el árbol).
- **H-5** [VERIFICADO] Aliasing de %M0.0/%M0.1 (2 tags por dirección) compila sin warnings (0/0).
- **H-6** [VERIFICADO] El hash del `.ap20` solo cambió en la primera escritura persistida; los saves
  posteriores no lo alteran (contenido en ficheros internos). Para vigilar mutaciones: fingerprint de directorio + manifiesto.

- **H-7** [VERIFICADO] Abrir el proyecto regenera `IM\HMI\DeviceFolders.dat` → `Assert-TiaFixtureManifest`
  exige refresh de manifiesto entre sesiones (falso positivo conocido 2026-09-25).

- **H-8** [VERIFICADO] `GenerateBlockSource` rechaza el OB (sin round-trip de fuente para OB).
  Fallback usado: `GetBlockSource(format=xml)` + el SCL de entrada como fuente exacta.

- **H-9** [VERIFICADO] "Changes stay in memory until SaveProject": cerrar sin guardar descarta.
  Toda sesión de escritura cierra con compilación 0/0 + SaveProject.

- **H-10** [VERIFICADO] FB_AlarmLatch reporta `PLCSimAdvancedSupport=true`; el OB1 `false` y
  `VirtualPlcSupport=false`. Pendiente de evaluar en F2 (flag de proyecto Support simulation during
  block compilation no tocado en F1).

## Evidencia

- `inputs/` — FB_AlarmLatch.scl (BOM UTF-8), OB1_Arnes.scl (v2 final)
- `outputs/` — `FB_AlarmLatch.xml` (22.173 B SimaticML V20), `AlarmPump.xml` (3.512 B)
- JSON de respuestas: `%LOCALAPPDATA%\Temp\opencode\f1-{preflight,a1b,b1,a2,a2b,a2c,b2,b2b,a3,a3b}*-20261016.json`
- Backup prístino intacto: `70-runs/e2e/20260928-objective-resume-hardware-compile/.../backup/`

## F2 — PLCSIM (avance en curso, 2026-10-16/19)

### Matriz de compatibilidad (leída del proyecto, no inferida)

| Elemento | Valor | Fuente live |
|---|---|---|
| CPU | **1513-1 PN**, `6ES7 513-1AM03-0AB0` | `DumpDeviceAttributes` (OrderNumber, PLC_1) |
| Firmware | **V3.0** | `DumpDeviceAttributes` (FirmwareVersion) |
| IP proyecto | `192.168.0.1` | `GetDeviceIpAddress` |
| TIA Portal | **V20** | Bootstrap (`tiaVersionInUse: 20`) |
| PLCSIM Advanced | **V7.0.0.0 / API 7.0** (Softbus) | adaptador `bin/v7` + ready del runtime |
| Compatibilidad | FW V3.0 ∈ [V1.8–V4.0] de Advanced V7 para TIA V14–V20 → **soportada** | matriz Siemens citada en R17 |

### Gates ejecutados antes de tocar la descarga

- `CompileSoftware` (sesión `tia-create --profile full`, attach a la GUI): **Success 0/0**. [VERIFICADO]
- `CheckDownloadReadiness`: `ready=true`, `isConsistent=true`, y **exactamente 1 ruta** `PG/IE / PLCSIM [no IP] -> 1 X1` (cero NICs físicas). [VERIFICADO]
- Preflight interno de `DownloadToPlc` en la misma sesión: *"F/Safety download preflight passed for PLC_1: 4 standard blocks, 11 non-Safety tags"*. [VERIFICADO]
- Instancia virtual: `status=ready`, `networkMode=SOFTBUS`, `interfaceName=PLCSIM`, `ip=null`, códigos `0x0`. [VERIFICADO]

### Hallazgos F2

- **H-11** [VERIFICADO] En Softbus el **nombre de la instancia PLCSIM debe coincidir con el nombre de dispositivo del proyecto**. Con la instancia registrada como `TIAClaudeAcceptance_1513` (convención del runner) la descarga falla con `Connect to module PLC_1 failed. Route used: PN/IE / PLCSIM [no IP] -> 1 X1`. El API 7.0 no expone `SetDeviceName`: el nombre de registro *es* el nombre de dispositivo. Re-registrada como `PLC_1` → se reintenta.
- **H-12** [VERIFICADO] `DownloadToPlc` por Openness **no abre el diálogo "Load preview"** en este build: la llamada va directa a descarga y devuelve. Durante 150 s no apareció ninguna ventana top-level nueva en el proceso TIA. Consecuencia para R17/PLCSIM: el testigo visual `CPU-1500 Simulation` + aviso de CPU simulada **no es obtenible por esta vía**; sustituto verificado = identidad del runtime (nombre/CPU/Softbus/códigos 0x0) + ruta única `PLCSIM` + preflight F/Safety en la misma sesión. Si se exige el diálogo literal, hay que descargar desde la GUI (clics manuales del usuario).
- **H-13** [VERIFICADO] Si muere el proceso que hospeda el adaptador, PLCSIM Advanced **destruye la instancia automáticamente** (`registeredCount` → 0). No hay riesgo de CPU virtual huérfana; sí hay que re-registrar.
- **H-14** [VERIFICADO] Esta sesión no puede leer imágenes (el `read` de PNG no está soportado). La inspección visual se sustituye por **UI Automation** (texto real de las ventanas TIA) + capturas guardadas para el usuario. UIA además confirma que el ribbon/proyecto de TIA V20 **no expone controles** (41 panes WinForms host, contenido WPF noAutomation), por lo que la GUI no es automatizable por UIA en este host.

### Estado de la descarga a PLCSIM: **BLOCKED** (6 intentos, evidencia completa)
`DownloadToPlc` falla siempre en el mismo punto, con gates previos en verde:

```text
Download to 'PLC_1' failed: 'Connect to module PLC_1 failed.'
Route used: PN/IE / PLCSIM [no IP] -> 1 X1
```

| # | Fecha | Combinación | Resultado |
|---|---|---|---|
| 1 | 2026-10-16 | GUI TIA (attach) + instancia `TIAClaudeAcceptance_1513` Softbus Run | `Connect to module PLC_1 failed` |
| 2 | 2026-10-19 | headless + instancia `PLC_1` Softbus Stop | `Connect to module PLC_1 failed` |
| 3 | 2026-10-19 | GUI TIA (attach) + instancia `PLC_1` Softbus Stop | `Connect to module PLC_1 failed` |
| 4 | 2026-10-19 | headless, Control Panel **abierto**, `Online Access=PLCSIM` | `Connect to module PLC_1 failed` |
| 5 | 2026-10-19 | GUI TIA (attach) + `GoOnline` (solo conectar, sin descargar) | `NotReachable` — confirma que el bloqueo es de conectividad, no del proveedor |
| 6 | 2026-10-19 | GUI TIA (attach) + instancia recién creada y Powered On (`0x0`) | `Connect to module PLC_1 failed` |
| 7 | 2026-10-19 | **S7-PLCSIM clásico V20 recién instalado** + interfaz `PLCSIM` | `Connect to module PLC_1 failed` |
| 8 | 2026-10-19 | clásico V20 instalado + **sin forzar interfaz** (TIA elige la preferida) | `Connect to module PLC_1 failed` |
| 9 | 2026-10-19 | clásico V20 instalado + `pgPcInterface=PLCSIM.TCPIP.1` | **Rechazada antes de conectar**: `No PG/PC interface matches 'PLCSIM.TCPIP.1'. Available routes: PN/IE / PLCSIM [no IP] -> 1 X1` |

Lo que SÍ está verificado en cada intento (no es un problema de compilación ni de seguridad):

- `CompileSoftware` → **Success 0 errores 0 avisos**.
- `CheckDownloadReadiness` → `ready=true`, `isConsistent=true`, **1 sola ruta** `PG/IE / PLCSIM [no IP] -> 1 X1` (cero NICs).
- Preflight interno de `DownloadToPlc` → *"F/Safety download preflight passed: 4 standard blocks, 11 non-Safety tags"*.
- Instancia PLCSIM viva: nombre `PLC_1`, CPU 1513, Softbus, IP `192.168.0.1`, todos los códigos API `0x0`.

- **H-15** [VERIFICADO] La descarga por Openness hacia Softbus **no logra resolver el target en este host** con las dos condiciones por separado y combinadas (nombre de instancia = `PLC_1`, TIA con GUI y headless). El runner canónico `Invoke-TiaSimulationAcceptance.ps1` tendría el mismo resultado: su llamada de descarga es idéntica (`pgPcInterface=PLCSIM`, sin IP). No es un problema de la fixture, del programa ni de la política F/Safety.
- **H-16** [VERIFICADO, 2026-10-19] **El bloqueo es de conectividad Softbus, no del proveedor de descarga**: `GoOnline` (conectar, sin descargar) también devuelve `state=NotReachable` / `Changing to online mode failed`, igual con TIA headless y con la GUI adjunta. Es decir: hoy, TIA V20 no alcanza ninguna CPU virtual por Softbus en esta máquina, aunque la instancia esté sana por API (`registerCode/powerOnCode/modeCode = 0x0`, CPU 1513, Softbus, IP 192.168.0.1).
  - Hipótesis a verificar (no afirmada): el host tiene **S7-PLCSIM clásico V19** instalado mientras TIA V20 requiere **S7-PLCSIM V20**; la interfaz PG/PC que TIA V20 enumera como `PLCSIM` (sin direcciones) podría ser la del simulador clásico con versión desalineada, mientras el Softbus de Advanced 7.0 publica su interfaz con otro nombre. La evidencia histórica del 24/09 (conexión Softbus OK) era con **Advanced V6**.
  - Rutas de salida, en orden de coste: (a) descarga manual desde la TIA GUI con la interfaz PG/PC elegida a mano — 1 clic del usuario y además produce el testigo visual de `CPU-1500 Simulation` que R17 exige; (b) instalar S7-PLCSIM V20, la pareja correcta de TIA V20 (cambio de sistema, requiere aprobación); (c) ruta TCP/IP local con la NIC Siemens, que exige consola elevada para fijar IP.

- **H-17** [VERIFICADO, 2026-10-19] Quinto intento fallido, ahora con el **Control Panel y el Runtime Manager de PLCSIM Advanced abiertos** y `Online Access = PLCSIM (Softbus)` confirmado por UIA (`Softbus radio selected=True`). Sigue el mismo `Connect to module PLC_1 failed`. Por tanto el Panel abierto **no** era la causa.
- **H-18** [VERIFICADO] La instancia recién registrada devuelve `PowerOn=0x0` desde el adaptador pero su estado real leído por `--inspect-registered-instance` es **`operatingState=Stop`** (y no `Run`). El botón RUN del Control Panel es un control custom no invocable por UIA (`InvokePattern` → "Error no reconocido") y el clic físico no lo activa porque actúa sobre la instancia seleccionada. Instancia y estado quedan pendientes de arranque manual.

- **H-19** [REFUTADO, 2026-10-19] *Hipótesis original (retirada):* se atribuyó el bloqueo a que **S7-PLCSIM clásico V19** ocupaba la interfaz PG/PC `PLCSIM`. **Se refutó empíricamente**: tras instalar **S7-PLCSIM clásico V20** (`S7PLCSIMV20.exe`, v2000.0.200.9871, presente en `_InstalledSW`) y repetir la descarga en tres variantes —interfaz `PLCSIM`, sin forzar interfaz, y `PLCSIM.TCPIP.1`— el resultado fue idéntico en las tres (intentos 7-9). La versión del simulador clásico **no es la causa**.
  - Lo que sí queda medido: TIA V20 en este host **no alcanza ninguna CPU virtual por Softbus**, ni con la instancia de Advanced sana (`registerCode/powerOnCode = 0x0`), ni con `GoOnline`, ni variando la interfaz seleccionada. `CheckDownloadReadiness` siempre enumera **una sola ruta** `PN/IE / PLCSIM [no IP] -> 1 X1` y nunca elige otra. El bloqueo está en cómo TIA V20 resuelve esa ruta en esta máquina, no en la versión del simulador.
  - Dato adicional del intento 9: la única ruta que TIA declara disponible es `PLCSIM [no IP]`. Pedir explícitamente `PLCSIM.TCPIP.1` es **rechazado por el propio servidor MCP** antes de intentar la conexión, lo que confirma de forma independiente que en esta máquina no hay una segunda interfaz de simulador que probar por API.
  - Conclusión operativa: **no reparable desde MCP ni desde la automatización del Control Panel**. El siguiente paso exige evidencia visual del diálogo de descarga en la TIA GUI (lista de destinos y aviso de CPU simulada), porque ninguna llamada por API aporta esa observación. El Ribbon de TIA V20 no expone controles por UI Automation en este host (solo 41 paneles WinForms shell), de modo que la inspección no puede automatizarse.
  - Nota de rigor: un primer intento de la variante 9 se ejecutó con un marcador inválido en la cadena y **abortó antes de descargar**; no cuenta como resultado. La variante 9 válida se relanzó y produjo el rechazo de interfaz descrito arriba. De los 9 intentos, **7 llegaron a la fase de conexión** y fallaron de forma idéntica; los 2 restantes no fueron pruebas de conexión.

## Pendiente (F2+)

1. F2: leer `10-kb/20-recetas/R17-aceptacion-plcsim.md` y arrancar PLCSIM (una instancia,
   Softbus local, sin mapeo TCP ni SetIPSuite pre-arranque).

2. F3: descarga con testigo visual (opción A del usuario) confirmando `CPU-1500 Simulation`.
3. F4: 9 casos del protocolo F0-F5.
4. VAT vacía: operandos se cargan en GUI (o ImportWatchTable XML) antes de F4.
5. Fase 2: prueba de importación desde cero con `FB_AlarmLatch.xml` en fixture nueva.
6. Fase 3: consolidación en awesome + actualización de arnes-ob1.md (la hace el usuario con
   el SCL/backup de este informe).
