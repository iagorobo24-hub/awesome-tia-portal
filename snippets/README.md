# Snippets SCL reutilizables

Patrones pequeños y cerrados para copiar en tus bloques. Cada uno indica
su estado: solo el filtro TON está probado en uso real (dentro de
[FB_AlarmLatch](../bloques-de-funcion/fb-alarm-latch/)); el resto son
patrones ilustrativos pendientes de compilación aislada.

| Snippet | Qué hace | Estado |
|---|---|---|
| [Flanco de subida con R_TRIG](flanco-r-trig.md) | Un ciclo a `TRUE` al cambiar `0 → 1` | 📝 ilustrativo |
| [Filtro antirrebote con TON](filtro-ton.md) | Ignora pulsos más cortos que un tiempo | 🔧 probado en uso |
| [Saturación MIN/MAX](saturacion-min-max.md) | Recorta un REAL a un rango | 📝 ilustrativo |
