# Matriz de Validación — Recursos PLC Awesome TIA Portal

> Estado de cada recurso según comprobaciones reales. Clasificación: VERIFICADO (evidencia de archivo + compilación + ejecución), REPORTADO (afirmado en README sin reproducción en esta sesión), INFERIDO (deducido de metadata), NO COMPROBADO (sin evidencia ejecutable).

## Recursos inspeccionados

| Recurso | Tipo | Archivo SCL | Archivo XML | Estado README | Estado compilación | Estado ejecución | Compatibilidad CPU | Veredicto general |
|---------|------|-------------|-------------|---------------|--------------------|------------------|--------------------|-------------------|
| `fb-alarm-latch` | FB | ✅ FB_AlarmLatch.scl | ✅ FB_AlarmLatch.xml | verified | V20, 0 errores/0 avisos (16/11/2026) | PLCSIM 65/65 pasos, 9 casos (21/10/2026) | S7-1500 6ES7513-1AM03-0AB0 | VERIFICADO (XML reimportado y compilado, sin descarga nueva) |
| `fc-escalado` | FC | ✅ FC_Escalado.scl | ✅ FC_Escalado.xml | verified | V20, 0 errores/0 avisos (16/11/2026) | PLCSIM 33/33 pasos, 9 casos (21/10/2026) | S7-1500 comprobada; S7-1200 no probada | VERIFICADO (XML reimportado y compilado, sin descarga nueva) |
| `fb-estado-maquina` | FB | ❌ (ficha de diseño) | ❌ | documented | NOT RUN | NOT RUN | S7-1200 / S7-1500 (declarado) | NO COMPROBADO (sin código) |
| `fb-secuenciador-pasos` | FB | ❌ (ficha de diseño) | ❌ | documented | NOT RUN | NOT RUN | S7-1200 / S7-1500 (declarado) | NO COMPROBADO (sin código) |
| `fb-control-pid` | FB | ❌ (ficha de diseño) | ❌ | documented | NOT RUN | NOT RUN | S7-1200 / S7-1500 (declarado) | NO COMPROBADO (sin código) |

## Detalle por recurso

### fb-alarm-latch (FB_AlarmLatch)

| Comprobación | Resultado | Evidencia | Notas |
|-------------|-----------|-----------|-------|
| Fuente SCL disponible | PASS | `FB_AlarmLatch.scl` (3675 bytes) | Código SCL real, versión 0.1 |
| Contrato funcional coherente | PASS | README con interfaz completa, estados esperados, casos de borde | Documentado por diseño |
| Importación en TIA V20 | PASS LIVE | Proyecto V20 desechable nuevo (16/11/2026) | XML original reconocido, readback FB2 SCL |
| Compilación | PASS LIVE | 0 errores, 0 avisos, V20, CPU 1513 (16/11/2026) | Readback: isFailsafe=false, isKnowHowProtected=false, isConsistent=true |
| Exportación XML | PASS | `FB_AlarmLatch.xml` (22170 bytes) | Exportado a SimaticML |
| Reimportación desde cero | PASS LIVE | [Evidencia 16/11/2026](evidencias/validacion-importacion-tia-v20-2026-11-16.json) | XML importado en proyecto nuevo, compilación 0/0; no se ejecutó PLCSIM ahora |
| Ejecución PLCSIM | REPORTADO | 65/65 pasos, 9 casos, 21/10/2026 | Evidencia: `evidencia-plcsim-2026-10-21.json` |
| Casos funcionales | REPORTADO | 9 transiciones de comportamiento | Documentado por diseño, no re-observado en esta sesión |
| Compatibilidad CPU | REPORTADO | S7-1500 6ES7513-1AM03-0AB0 | Solo este modelo verificado |

**Estado actual (16/11/2026):** XML reimportado y compilado 0/0 sobre proyecto V20 nuevo ([evidencia](evidencias/validacion-importacion-tia-v20-2026-11-16.json)). La ejecución PLCSIM permanece acreditada por pruebas del 21/10/2026, no se ha repetido sobre la fixture recién creada.

### fc-escalado (FC_Escalado)

| Comprobación | Resultado | Evidencia | Notas |
|-------------|-----------|-----------|-------|
| Fuente SCL disponible | PASS | `FC_Escalado.scl` (2127 bytes) | Código SCL real |
| Contrato funcional coherente | PASS | README con interfaz, lógica interna, casos de borde | Documentado por diseño |
| Importación en TIA V20 | PASS LIVE | Proyecto V20 desechable nuevo (16/11/2026) | XML original reconocido, readback FC1 SCL |
| Compilación | PASS LIVE | 0 errores, 0 avisos, V20, CPU 1513 (16/11/2026) | Readback: isFailsafe=false, isKnowHowProtected=false, isConsistent=true |
| Exportación XML | PASS | `FC_Escalado.xml` (10832 bytes) + `OB1_Arnes-ejecutado.xml` | Exportado a SimaticML |
| Reimportación desde cero | PASS LIVE | [Evidencia 16/11/2026](evidencias/validacion-importacion-tia-v20-2026-11-16.json) | XML importado en proyecto nuevo, compilación 0/0; no se ejecutó PLCSIM ahora |
| Ejecución PLCSIM | REPORTADO | 33/33 pasos, 9 casos de escalado | Evidencia: `evidencia-plcsim-2026-10-21.json` |
| Casos funcionales | REPORTADO | 9 casos con valores esperados vs observados | Todos coinciden (diferencia de precisión REAL documentada) |
| Compatibilidad CPU | REPORTADO | S7-1500 6ES7513-1AM03-0AB0 (declarado V18-V19 compatible sin prueba) | V18/V19 declarados pero no probados |

**Estado actual (16/11/2026):** XML reimportado y compilado 0/0 sobre proyecto V20 nuevo ([evidencia](evidencias/validacion-importacion-tia-v20-2026-11-16.json)). La ejecución PLCSIM permanece acreditada por pruebas del 21/10/2026, no se ha repetido sobre la fixture recién creada.

### fb-estado-maquina (FB_EstadoMaquina)

| Comprobación | Resultado | Evidencia | Notas |
|-------------|-----------|-----------|-------|
| Fuente SCL disponible | FAIL | Solo README (ficha de diseño) | Sin código SCL |
| Contrato funcional coherente | PENDING REVIEW | Interfaz definida, lógica de transición especificada | Pendiente revisión de diseño (sección 6 del plan) |
| Importación en TIA V20 | NOT RUN | No hay archivo para importar | No aplicable sin código |
| Compilación | NOT RUN | No hay código | No aplicable |
| Exportación XML | NOT RUN | No hay código | No aplicable |
| Reimportación desde cero | NOT RUN | No hay código | No aplicable |
| Ejecución PLCSIM | NOT RUN | No hay código | No aplicable |
| Casos funcionales | NOT RUN | No hay código | No aplicable |
| Compatibilidad CPU | NOT RUN | Declarado V20, S7-1200/S7-1500 | No probado |

**Estado final:** NO COMPROBADO (ficha de diseño sin código).

### fb-secuenciador-pasos (FB_SecuenciadorPasos)

| Comprobación | Resultado | Evidencia | Notas |
|-------------|-----------|-----------|-------|
| Fuente SCL disponible | FAIL | Solo README (ficha de diseño) | Sin código SCL |
| Contrato funcional coherente | PENDING REVIEW | Interfaz definida, lógica de avance especificada | Pendiente revisión de diseño (sección 6 del plan) |
| Importación en TIA V20 | NOT RUN | No hay archivo para importar | No aplicable sin código |
| Compilación | NOT RUN | No hay código | No aplicable |
| Exportación XML | NOT RUN | No hay código | No aplicable |
| Reimportación desde cero | NOT RUN | No hay código | No aplicable |
| Ejecución PLCSIM | NOT RUN | No hay código | No aplicable |
| Casos funcionales | NOT RUN | No hay código | No aplicable |
| Compatibilidad CPU | NOT RUN | Declarado V20, S7-1200/S7-1500 | No probado |

**Estado final:** NO COMPROBADO (ficha de diseño sin código).

### fb-control-pid (FB_ControlPID)

| Comprobación | Resultado | Evidencia | Notas |
|-------------|-----------|-----------|-------|
| Fuente SCL disponible | FAIL | Solo README (ficha de diseño) | Sin código SCL |
| Contrato funcional coherente | PENDING REVIEW | Ecuación PID especificada, pero `Ts` no declarado en interfaz | Pendiente revisión de diseño (sección 6 del plan) |
| Importación en TIA V20 | NOT RUN | No hay archivo para importar | No aplicable sin código |
| Compilación | NOT RUN | No hay código | No aplicable |
| Exportación XML | NOT RUN | No hay código | No aplicable |
| Reimportación desde cero | NOT RUN | No hay código | No aplicable |
| Ejecución PLCSIM | NOT RUN | No hay código | No aplicable |
| Casos funcionales | NOT RUN | No hay código | No aplicable |
| Compatibilidad CPU | NOT RUN | Declarado V20, S7-1200/S7-1500 | No probado |

**Estado final:** NO COMPROBADO (ficha de diseño sin código).

## Bloqueos recuperables identificados

| Bloqueo | Recurso afectado | Causa probable | Acción correctiva | Estado |
|---------|-----------------|----------------|-------------------|--------|
| Adjuntar TIA para descargar a CPU virtual | fb-alarm-latch, fc-escalado | La ejecución histórica PLCSIM requirió `AttachToOpenProject`; el modo headless actual sí permite importar y compilar offline | No confundir compilación headless con descarga a CPU simulada | PENDIENTE DE REPETIR SOLO PLCSIM |
| Reimportación XML desde cero | fb-alarm-latch, fc-escalado | Resuelto con `ImportBlock` Openness V20 | Bloques leídos y compilados 0/0 en proyecto nuevo | PASS LIVE 16/11/2026 |

## Problemas técnicos de diseño detectados

1. **FB_ControlPID**: La ecuación usa `Ts` (tiempo de muestreo) pero la interfaz no lo declara como parámetro. Hay dos convenciones de ganancias (con y sin `Ts`). Semántica del derivativo no especificada (signo).
2. **FB_EstadoMaquina**: Prioridades de reset/inicio no definidas. Ejemplo de llamada usa `abCondicion[0]` para estado 0 pero el array es 0..15 — verificar índice.
3. **FB_SecuenciadorPasos**: `iPasoTotal` semántica ambigua (¿máximo alcanzado o total configurado?). Ejemplo usa índices 1..4 en array 1..16.

## Próximas acciones necesarias

1. Ejecutar `Invoke-TiaDirectOpennessProbe.ps1` para verificar capa Openness V20.
2. Reejecutar casos de borde PLCSIM sobre el proyecto con ambos XML reimportados; la reimportación y compilación ya pasaron.
3. Revisar diseños de los 3 bloques nuevos antes de codificar (sección 6 del plan).
4. Escribir código SCL para los 3 bloques nuevos si se priorizan.
5. Actualizar READMEs para eliminar contradicciones (ej. fb-alarm-latch línea 69 vs líneas 27-32).
