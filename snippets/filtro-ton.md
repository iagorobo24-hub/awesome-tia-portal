# Filtro antirrebote con TON

> **Estado**: verificado en ejecución. Es el filtro `OnDelay` de
> [FB_AlarmLatch](../bloques-de-funcion/fb-alarm-latch/), que se compiló en V20 con 0/0, se
> descargó a una CPU virtual y se ejecutó en PLCSIM: el caso `retardo-500ms` comprueba que la
> alarma no aparece hasta que el retardo vence, y `reposo` que con `T#0MS` el filtrado se
> desactiva y la condición pasa inmediata. Evidencia:
> [`evidencia-plcsim-2026-10-21.json`](../bloques-de-funcion/fb-alarm-latch/evidencia-plcsim-2026-10-21.json).

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
