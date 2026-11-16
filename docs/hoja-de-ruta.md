# Hoja de ruta editorial

El repositorio crece por recursos **comprobables**, no por cantidad de fichas.

## Base disponible

- Portada navegable, ilustración conceptual, catálogo con estados y criterios de contribución.
- Guía de conexión IA ↔ TIA Portal V20 con límites de Openness, MCP, Computer Use y simulación.
- Dos bloques con fuentes SCL y XML: `FB_AlarmLatch` y `FC_Escalado`, con evidencias documentadas de compilación V20 y ejecución PLCSIM; la reimportación desde cero de ambos bloques se acreditó el 16/11/2026 ([evidencia](evidencias/validacion-importacion-tia-v20-2026-11-16.json)).

## Próximos hitos

1. **Capturas reales:** proyecto de demostración desechable, inspección de bloques y prueba HMI compatible, con contexto y datos anonimizados.
2. **Regresión en PLCSIM:** reejecutar los casos de borde sobre los XML reimportados (el 16/11 se verificó la compilación, pero no la descarga ni el comportamiento); después incorporar otros bloques propios uno a uno.
3. **Tutorial reproducible:** ejecutar la guía V20 en una instalación limpia y corregir los pasos que no resulten portables.
4. **Catálogo curado:** revisar enlaces externos, licencias, versiones y criterios de admisión; actualizar fichas históricas que todavía describen capacidades no comprobadas.
5. **Comunidad:** recibir issues y PR con pruebas, añadir traducciones y publicar demostraciones breves cuando el proceso de captura sea repetible.

Para cada hito se registrará qué está verificado, qué está pendiente y la evidencia que permite reproducir la conclusión.
