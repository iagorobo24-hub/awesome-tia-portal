# Preguntas frecuentes (FAQ)

## ¿Esto es una lista awesome al uso?

No exactamente. Es una biblioteca curada donde cada recurso indica su
estado real (documentado, fuente compilada, importable, probado). La
columna `Estado` del [catálogo](../CATALOG.md) manda; el resto es contexto.

## ¿Puedo usar estos bloques en una máquina real?

Solo los marcados ✅ `available`, y aun así **tras validarlos en tu
instalación**. Nada de aquí está certificado ni sustituye una revisión
de seguridad. Lee los [límites conocidos](../README.md#límites-conocidos).

## ¿Por dónde empiezo?

Por las [rutas de aprendizaje](rutas/). Si vienes con prisa: el bloque
[FB_AlarmLatch](../bloques-de-funcion/fb-alarm-latch/) es el único con
fuente compilada y protocolo de prueba completo.

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

## ¿Por qué no hay .xml todavía?

Porque publicar un exportado sin haberlo importado desde cero y probado
sería vender humo. El primero en camino es `FB_AlarmLatch`
(ver [exportacion-xml.md](../bloques-de-funcion/fb-alarm-latch/exportacion-xml.md)).
