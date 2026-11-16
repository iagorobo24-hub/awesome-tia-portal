# Preguntas frecuentes (FAQ)

## ¿Esto es una lista awesome al uso?

No exactamente. Es una biblioteca curada donde cada recurso indica su
estado real (documentado, fuente compilada, importable, probado). La
columna `Estado` del [catálogo](../CATALOG.md) manda; el resto es contexto.

## ¿Puedo usar estos bloques en una máquina real?

**Ningún recurso está certificado para utilizarse directamente en una máquina real.** Dos (`FB_AlarmLatch` y `FC_Escalado`) tienen evidencias de pruebas en simulación, pero aún requieren reimportación limpia y validación específica antes de usarlos en un proyecto real. Lee los [límites conocidos](../README.md#límites-conocidos).

## ¿Por dónde empiezo?

Por las [rutas de aprendizaje](rutas/). Si necesitas ejemplos con código y evidencias de simulación, empieza por [FB_AlarmLatch](../bloques-de-funcion/fb-alarm-latch/) o [FC_Escalado](../bloques-de-funcion/fc-escalado/). Ambos se reimportaron desde cero en TIA V20 el 16/11/2026, con compilación 0/0 ([evidencia](evidencias/validacion-importacion-tia-v20-2026-11-16.json)).

## ¿Necesito licencia de TIA Portal para usar el repo?

Para leer documentación, no. Para compilar, simular o importar, sí:
TIA Portal V20 con su licencia, en Windows.

## ¿Qué significa cada estado del catálogo?

Está en la leyenda del [CATALOG.md](../CATALOG.md): ✅ importable,
🔧 fuente compilada, 📝 solo documentado, ⏳ planificado. El nivel
(🟢 básico, 🟡 medio, 🔴 avanzado) indica dificultad, no calidad.

## He encontrado un enlace roto o un dato dudoso. ¿Qué hago?

Abre un issue con la URL y lo que esperabas encontrar. Los enlaces
externos se revisan cada domingo automáticamente.

## Quiero aportar un bloque. ¿Cómo?

Lee [CONTRIBUTING.md](../CONTRIBUTING.md): carpeta kebab-case, README
con la plantilla (incluido frontmatter con `status` y `level`), `.xml`
si lo tienes probado, y regenera el catálogo. CI te dirá si falta algo.

## ¿Aceptáis traducciones al inglés?

Sí. El repo es español primero; las contribuciones y traducciones en
inglés son bienvenidas e irán conviviendo por recurso.

## ¿Hay archivos XML importables?

Sí: existen **3 archivos XML** asociados a `FB_AlarmLatch`, `FC_Escalado` y su arnés de pruebas. Los XML de `FB_AlarmLatch` y `FC_Escalado` **se han reimportado y compilado desde cero** en TIA V20; el arnés OB1 del escalado es un XML auxiliar y no se ha validado por reimportación en esta tanda. Los demás recursos son fichas de diseño, no bloques exportados.
