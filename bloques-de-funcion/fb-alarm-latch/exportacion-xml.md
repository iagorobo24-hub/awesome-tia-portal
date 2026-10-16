# Exportación del .xml (FB_AlarmLatch)

Procedimiento para convertir el recurso en el primer bloque importable
del repositorio (estado ✅ `available`). Solo tiene sentido con la
[prueba PLCSIM superada](protocolo-plcsim.md): primero comportamiento,
después artefacto.

## F1. Exportar desde TIA Portal V20

1. Partir del proyecto desechable con la prueba superada y guardada.
2. Clic derecho sobre el bloque `FB_AlarmLatch` y **Exportar**.
3. Guardar como `FB_AlarmLatch.xml` (exactamente ese nombre).
4. No exportar el DB de instancia `AlarmPump` ni la VAT: el recurso es el FB.

## F2. Higiene antes de publicar (obligatorio)

1. Abrir el `.xml` en un editor de texto y comprobar que no contiene IPs, usuarios, rutas de máquina ni nombres de cliente.
2. Ejecutar desde la raíz del repo:

```bash
python3 scripts/validate-xml.py
```

Debe terminar en verde. Si protesta, corregir en TIA y reexportar (no editar el XML a mano salvo datos sensibles evidentes, y documentarlo).

1. Comprobar UTF-8 sin BOM y finales de línea LF.

## F3. Prueba de importación desde cero (STYLE §10)

1. Crear un proyecto V20 **vacío** nuevo (desechable).
2. Importar `FB_AlarmLatch.xml` (clic derecho en Bloques de programa, Importar).
3. Compilar: exigido **0 errores y 0 advertencias**.
4. Anotar versión, CPU y resultado en la evidencia de exportación.

## F4. Publicar en el repo

1. Copiar `FB_AlarmLatch.xml` a `bloques-de-funcion/fb-alarm-latch/`.
2. Actualizar la ficha (`README.md`): estado ✅, archivo disponible, evidencia de importación.
3. Cambiar el frontmatter a `status: available`.
4. Regenerar el catálogo:

```bash
python3 scripts/generate_catalog.py
```

1. Commitear `.xml` + ficha + `CATALOG.md` juntos.

## Criterios de DONE (primer ✅)

- `.xml` exportado desde el proyecto probado, en verde con `validate-xml.py`.
- Importación desde cero compilando 0/0, con evidencia.
- Ficha y `CATALOG.md` actualizados. Nada de esto acredita uso en instalación real.
