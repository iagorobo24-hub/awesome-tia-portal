# OB100 — Startup

> OB de arranque (`Startup`) con inicialización típica: textos de alarmas, configuración de equipos, valores por defecto.

**Tipo:** `Bloque de organización (OB100)`
**Versión TIA Portal:** V20 *(compatible con V18 y V19)*
**Familia PLC:** S7-1200 / S7-1500

---

## ¿Qué problema resuelve?

Muchos parámetros del proyecto (textos de alarma, umbrales por defecto, configuraciones de FBs…) deberían inicializarse **una sola vez al arrancar el PLC**, no en cada ciclo. Programadores nuevos los meten en el OB1 con un `IF FirstScan` que enseguida se olvida y cuesta de leer.

`OB100` es el lugar canónico de TIA Portal para esto. Esta plantilla muestra **qué tipo de inicializaciones se ponen aquí y cuáles no**, con ejemplos.

---

## Estructura

```scl
// =================================================================
// 1. TEXTOS DE ALARMAS
// =================================================================
"DB_Alarmas".aLista[1].sTexto    := 'Térmico bomba M01 disparado';
"DB_Alarmas".aLista[1].sFuente   := 'M01_BombaPrincipal';
"DB_Alarmas".aLista[1].iPrioridad := 3;
"DB_Alarmas".aLista[1].iCodigo   := 1001;

"DB_Alarmas".aLista[2].sTexto    := 'Timeout apertura válvula V01';
"DB_Alarmas".aLista[2].sFuente   := 'V01_AguaEntrada';
"DB_Alarmas".aLista[2].iPrioridad := 2;
"DB_Alarmas".aLista[2].iCodigo   := 2001;
// ...

// =================================================================
// 2. CONFIGURACIÓN DE EQUIPOS (UDT_Motor, UDT_Valve, ...)
// =================================================================
"DB_Equipos".M01_BombaPrincipal.Config.tTimeoutArranque := T#3s;
"DB_Equipos".M01_BombaPrincipal.Config.tTimeoutParo     := T#3s;
"DB_Equipos".M01_BombaPrincipal.Config.tFiltroFeedback  := T#100ms;

"DB_Equipos".V01_AguaEntrada.Config.tTimeoutAbrir       := T#5s;
"DB_Equipos".V01_AguaEntrada.Config.tTimeoutCerrar      := T#5s;

// =================================================================
// 3. UMBRALES DE ALARMAS ANALÓGICAS (UDT_AnalogInput)
// =================================================================
"DB_Analogicas".AI01_TempReactor.Escalado.rRangoMinIng := 0.0;
"DB_Analogicas".AI01_TempReactor.Escalado.rRangoMaxIng := 150.0;
"DB_Analogicas".AI01_TempReactor.Procesado.sUnidad     := 'ºC';
"DB_Analogicas".AI01_TempReactor.Alarmas.rLimiteHH     := 130.0;
"DB_Analogicas".AI01_TempReactor.Alarmas.rLimiteH      := 110.0;
"DB_Analogicas".AI01_TempReactor.Alarmas.rLimiteL      := 20.0;
"DB_Analogicas".AI01_TempReactor.Alarmas.rLimiteLL     := 5.0;
"DB_Analogicas".AI01_TempReactor.Alarmas.rHisteresis   := 1.0;

// =================================================================
// 4. ESTADO INICIAL DE PROCESO
// =================================================================
"DB_Proceso".eEstadoMaquina := #ESTADO_REPOSO;
"DB_Proceso".xPrimerArranqueOK := TRUE;

// =================================================================
// 5. LIMPIEZA DE FALLOS NO RETENTIVOS
// =================================================================
// (las marcas no retentivas ya se ponen a 0 automáticamente, no hace
//  falta forzarlas — solo limpiar las retentivas que toque resetear)
```

---

## Cómo importarlo en TIA Portal

1. Descarga el archivo `ob100-startup.xml`
2. En TIA Portal: clic derecho sobre **Bloques de programa** → **Importar** → confirma

---

## Qué SÍ poner aquí

- Textos de alarmas, fuentes, prioridades, códigos.
- Umbrales y constantes del proceso (rangos, timeouts, histéresis).
- Configuración de FBs que no cambia en runtime.
- Estado inicial de máquina/proceso.
- Reinicializar variables retentivas que NO deberían sobrevivir a un corte de tensión.

## Qué NO poner aquí

- Lógica de proceso (eso va en OB1).
- Lecturas de I/O (las I/O todavía no están listas en el OB de arranque, depende del PLC).
- Comandos a equipos físicos (nada se mueve aún).
- Sobrescribir variables retentivas que sí deben mantenerse (horas de funcionamiento, contadores).

---

## Notas / Limitaciones conocidas

- En S7-1500, las variables retentivas conservan valor entre arranques — no las inicialices aquí salvo que quieras forzar un reset al arranque (caso especial).
- Si la inicialización es muy larga, considera moverla a un FC dedicado (`FC_InitProyecto`) y llamarlo desde OB100 — mantiene el OB100 legible.
- TIA Portal V20 admite múltiples OBs de Startup ejecutados en orden — útil para separar inicialización por área.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
