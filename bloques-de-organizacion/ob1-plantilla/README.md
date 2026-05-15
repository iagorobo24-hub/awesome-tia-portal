---
name: OB1
type: ob
tia_version: V20
tia_compat: [V18, V19, V20]
plc_family: [s7-1200, s7-1500]
depends_on: []
used_by: []
tags: [ob, main, plantilla]
status: documented
---

# OB1 — Plantilla

> Esqueleto de OB1 (`Main`) con secciones comentadas y orden de ejecución estándar — para no empezar de cero en cada proyecto.

**Tipo:** `Bloque de organización (OB1)`
**Versión TIA Portal:** V20 *(compatible con V18 y V19)*
**Familia PLC:** S7-1200 / S7-1500

---

## ¿Qué problema resuelve?

Cada proyecto empieza con un OB1 vacío. El programador medio acaba metiendo la lógica de cualquier manera (entradas, salidas, control, alarmas… todo mezclado) y el código se vuelve imposible de mantener al cabo de unos meses.

Esta plantilla impone una **estructura clara y comentada** con 5 secciones siempre en el mismo orden — fácil de leer, fácil de mantener, fácil de revisar entre compañeros.

---

## Estructura del OB1

El bloque está organizado con **comentarios de bloque (region/separadores)** que dividen el código en secciones:

```
// =================================================================
// 1. LECTURA DE ENTRADAS Y PRE-PROCESADO
// =================================================================
//   - Lectura de entradas digitales y analógicas
//   - FB_AnalogInput por cada canal analógico
//   - Filtrado / antirrebote de entradas críticas

CALL "FB_AnalogInput", instance := "DB_Analogicas".AI01_TempReactor;
// ...

// =================================================================
// 2. ENCLAVAMIENTOS Y SEGURIDAD
// =================================================================
//   - Cadena de paro de emergencia
//   - Permisos cruzados entre equipos
//   - Comprobación de fallos críticos

"DB_Seguridad".xCadenaOK := "iSetaArmario" AND "iSetaCampo";
// ...

// =================================================================
// 3. LÓGICA DE CONTROL
// =================================================================
//   - Secuencias / receta
//   - Modos manual / automático
//   - PIDs

CALL "FB_Motor", instance := "DB_Equipos".M01_BombaPrincipal;
// ...

// =================================================================
// 4. ALARMAS Y DIAGNÓSTICO
// =================================================================
//   - Generación de alarmas (UDT_Alarm)
//   - Contadores (FB_Hourmeter, FB_EdgeCounter)
//   - Texto de estado de equipos

// ...

// =================================================================
// 5. ESCRITURA DE SALIDAS
// =================================================================
//   - Asignación final a salidas físicas
//   - NUNCA escribir salidas en mitad del programa
```

---

## Cómo importarlo en TIA Portal

1. Descarga el archivo `ob1-plantilla.xml`
2. En TIA Portal: clic derecho sobre **Bloques de programa** → **Importar** → confirma
3. Reemplaza tu OB1 actual con el importado *(o copia las secciones a tu OB1 existente)*

---

## Por qué este orden

1. **Lectura primero** → al final del programa todo opera con valores procesados, consistentes, no con raw mezclado.
2. **Seguridad antes de lógica** → ningún equipo puede arrancar con la cadena abierta.
3. **Lógica en el medio** → toma sus decisiones con el estado ya estabilizado.
4. **Alarmas después de la lógica** → ven la decisión final, no estados transitorios.
5. **Escritura al final** → todas las salidas físicas se actualizan en el mismo punto, único lugar a revisar para diagnosticar "qué se está enviando".

---

## Notas / Limitaciones conocidas

- Esta plantilla es **una propuesta** — puedes adaptarla a tu estilo, pero mantén el principio de "lectura → seguridad → lógica → diagnóstico → escritura".
- Si tu proyecto tiene secuencias largas, considera mover la lógica de control a un FB dedicado (`FB_SecuenciaPrincipal`) y solo llamarlo desde el OB1.
- El comentado por defecto está en español. Si tu equipo trabaja en inglés, traduce las secciones antes de usar la plantilla.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
