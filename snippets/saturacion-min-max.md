# Saturación MIN/MAX

> **Estado**: patrón ilustrativo, pendiente de compilación aislada.

Recorta un `REAL` a un rango `[rMin, rMax]`. Complementa a
[FC_Escalado](../bloques-de-funcion/fc-escalado/), que no satura su salida.

```scl
#rLimitado := MIN(IN1 := MAX(IN1 := #rMedida, IN2 := #rMin), IN2 := #rMax);
```

## Requisitos

- Cumplir `rMin <= rMax`; si no, el resultado es `rMax` (documentar el caso).
- Tipos `REAL` en las tres patas (o conversiones explícitas).

## Límites

- Esto recorta, no escala: para convertir rangos usa `FC_Escalado` antes.
- Con entradas inválidas (`NaN`) el resultado es inválido: sanear aguas arriba.
