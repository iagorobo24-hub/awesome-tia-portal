# Filtro antirrebote con TON

> **Estado**: probado en uso dentro de [FB_AlarmLatch](../bloques-de-funcion/fb-alarm-latch/) (compilado en V20, 0/0). Aquí aislado como patrón, pendiente de compilación aislada.

Ignora activaciones más cortas que `OnDelay`. Con `T#0MS` el filtro se
desactiva y la condición pasa inmediata.

```scl
#tonFilter(IN := #Condition AND #Enable, PT := #OnDelay);
#tempActive := #tonFilter.Q OR (#Condition AND #Enable AND #OnDelay = T#0MS);
```

## Requisitos

- Instancia de `TON_TIME` (o `TON`) en `VAR`.
- `OnDelay >= T#0MS`; valores negativos no tienen sentido.

## Límites

- Retrasa la activación exactamente `OnDelay`: no usar en seguridades.
- El flanco de bajada no se filtra (pasa inmediato).
