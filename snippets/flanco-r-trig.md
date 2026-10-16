# Flanco de subida con R_TRIG

> **Estado**: patrón ilustrativo, pendiente de compilación aislada.

Detecta el cambio `FALSE → TRUE` de una condición y emite un único ciclo
a `TRUE`. Sirve para contadores, arranques por pulsador y reconocimientos
por flanco (a diferencia del `CmdAck` por nivel de `FB_AlarmLatch`).

```scl
#trigArranque(CLK := #PulsadorMarcha);
// #trigArranque.Q vale TRUE solo durante el ciclo del flanco
IF #trigArranque.Q THEN
    #MotorEnMarcha := TRUE;
END_IF;
```

## Requisitos

- Instancia de `R_TRIG` declarada en `VAR` (con memoria) o como multiinstancia.
- Si el pulsador puede rebotar, filtrarlo antes (ver [filtro TON](filtro-ton.md)).

## Límites

- `R_TRIG` necesita memoria: no vale en una FC sin DB.
- Un flanco perdido por ciclo (llamadas condicionales) no se recupera.
