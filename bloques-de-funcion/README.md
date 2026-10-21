# Bloques de función

Aquí se recopilan **Function Blocks (FB)** y **Functions (FC)**, con el estado de cada recurso indicado en su ficha.

- **FB** → tiene memoria interna, necesita bloque de datos de instancia
- **FC** → sin memoria, solo entradas/salidas

Cada recurso tiene su propia subcarpeta y un `README.md`. Solo se anuncian archivos que realmente están presentes.

---

Recursos incluidos (el detalle de qué hay en cada carpeta está en la
[matriz de trazabilidad](../MATRIZ-TRAZABILIDAD.md)):

- [`fb-alarm-latch`](fb-alarm-latch/) 🏆 (fuente SCL y XML, compilada en V20 con 0/0, ejecutada en PLCSIM: 9 casos)
- [`fc-escalado`](fc-escalado/) 🏆 (fuente SCL y XML, compilada en V20 con 0/0, ejecutada en PLCSIM: 9 casos)
- [`fb-analog-input`](fb-analog-input/) 📝
- [`fb-edge-counter`](fb-edge-counter/) 📝
- [`fb-hourmeter`](fb-hourmeter/) 📝
- [`fb-motor`](fb-motor/) 📝
- [`fb-pulse-gen`](fb-pulse-gen/) 📝
- [`fb-valve`](fb-valve/) 📝

Salvo `fb-alarm-latch` y `fc-escalado`, las carpetas contienen fichas de diseño, sin bloque
importable todavía. Consulta el [catálogo](../CATALOG.md).

¿Quieres aportar uno? Lee [cómo contribuir](../CONTRIBUTING.md).
