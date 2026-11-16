# Guía de reproducción — bloques verificados en TIA Portal V20

**Edición:** 2026-11-16. Alcance: pruebas sobre una **CPU S7-1500 virtual de laboratorio**; nunca un PLC de producción. La existencia de un XML no implica certificación industrial.

## Material disponible

| Recurso | Archivo de importación | Fuente SCL | Compilación V20 (16/11) | PLCSIM (21/10) |
|---|---|---|---|---|
| FB_AlarmLatch | [FB_AlarmLatch.xml](../bloques-de-funcion/fb-alarm-latch/FB_AlarmLatch.xml) | [FB_AlarmLatch.scl](../bloques-de-funcion/fb-alarm-latch/FB_AlarmLatch.scl) | PASS 0/0 | 65/65 pasos, 9 casos |
| FC_Escalado | [FC_Escalado.xml](../bloques-de-funcion/fc-escalado/FC_Escalado.xml) | [FC_Escalado.scl](../bloques-de-funcion/fc-escalado/FC_Escalado.scl) | PASS 0/0 | 33/33 pasos, 9 casos |

Los dos XML se reimportaron el 16/11 en **un proyecto nuevo** `AW20_Import`, CPU `6ES7513-1AM03-0AB0`. [Informe estructurado](evidencias/validacion-importacion-tia-v20-2026-11-16.json). El XML `OB1_Arnes-ejecutado.xml` de escalado es un artefacto auxiliar y **no** se reimportó en esa tanda.

## Procedimiento seguro para repetir la importación

1. Verificar que TIA Portal V20 y Openness están instalados; no usar proyectos de cliente ni abrir un segundo proyecto mientras otro agente lo tenga en uso.
2. Crear **un proyecto V20 nuevo en carpeta corta y exclusiva**, con CPU de prueba 1513 no Safety; conservar copia completa del proyecto antes de importar.
3. Importar `FB_AlarmLatch.xml` y `FC_Escalado.xml` desde las rutas anteriores a la raíz de bloques de programa. Comprobar los nombres y números reales (FB2/FC1 en esta prueba); no asumirlos en otro proyecto.
4. Leer el resultado de la importación y atributos: `programmingLanguage=SCL`, `isFailsafe=false`, `isKnowHowProtected=false` e `isConsistent=true`. Si falta confirmación, detenerse.
5. Compilar software PLC completo y exigir **0 errores / 0 advertencias**; guardar únicamente tras compilación correcta. Conservar hash del XML, versión/build de TIA, CPU y diagnóstico.
6. Para probar comportamiento, preparar **por separado** las llamadas OB1, DB de instancia y tags de los arneses [alarma](../bloques-de-funcion/fb-alarm-latch/arnes-ob1.md) y [escalado](../bloques-de-funcion/fc-escalado/arnes-ob1.md), validar compilación y seleccionar **únicamente una instancia PLCSIM Advanced V7 identificada inequívocamente**, con evidencia de interfaz virtual. Nunca descargar por heurística IP o por orden de dispositivos.
7. Ejecutar [protocolo de alarma](../bloques-de-funcion/fb-alarm-latch/protocolo-plcsim.md) y [casos de escalado](../bloques-de-funcion/fc-escalado/arnes-ob1.md), registrando valores observados, desviaciones y limpieza/apagado de la CPU virtual.

**Resultado de esta tanda:** pasos 1–5 verificados el 16/11. Los pasos 6–7 **no se repitieron sobre el proyecto de nueva importación**. Los ensayos PLCSIM previos del 21/10 son evidencia válida de aquella ejecución, no una prueba automática del nuevo artefacto.

## Compatibilidad y límites

Solo se ha observado directamente la reimportación con TIA V20 y una S7-1500 CPU 1513. Las anotaciones de compatibilidad V18/V19 o S7-1200 de otras fichas son **declaraciones sin prueba reproducida**. Ninguno de estos bloques es un componente F/Safety ni está certificado para proteger personas o instalaciones.
