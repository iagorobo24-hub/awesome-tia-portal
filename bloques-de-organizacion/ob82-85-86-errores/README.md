# OBs de errores — OB82 / OB85 / OB86

> Plantillas de los OBs de **diagnóstico, fallo de programa y fallo de rack** con gestión básica de eventos: registro, alarma y modo seguro.

**Tipo:** `Bloques de organización (OB82, OB85, OB86)`
**Versión TIA Portal:** V20 *(compatible con V18 y V19)*
**Familia PLC:** S7-1500 *(en S7-1200 algunos OBs no existen — ver notas)*

---

## ¿Qué problema resuelve?

Cuando un módulo I/O falla, un rack se cae o una variable se accede fuera de rango, el PLC dispara un OB de error específico. Si no existe ese OB, el PLC se va a STOP. Si existe pero está vacío, el PLC sigue corriendo sin que nadie se entere del fallo.

La práctica correcta es: **el OB existe, captura el evento, lo registra en una alarma, y aplica un modo seguro mínimo si toca**. Estas plantillas ofrecen ese esqueleto para los 3 OBs más usados.

---

## OB82 — Diagnostic Interrupt

Disparado cuando un módulo de la CPU reporta un fallo de diagnóstico (ej: cable cortado en una entrada analógica HART, sobretemperatura del módulo).

```scl
// Información del evento (los nombres exactos dependen de la versión)
"DB_Diagnostico".dwIdHardware := #IO_Status;
"DB_Diagnostico".bEventoEntrante := #Event_Class;

// Activar alarma de diagnóstico genérica
"DB_Alarmas".aLista[10].xActiva := TRUE;
"DB_Alarmas".aLista[10].sTexto := 'Fallo de diagnóstico en módulo de I/O';

// Si el fallo afecta a una entrada analógica crítica, marca calidad como mala
"DB_Analogicas".AI01_TempReactor.Raw.xCalidadOK := FALSE;
```

## OB85 — Program Cycle Error

Disparado por errores que normalmente parmarían el PLC: acceso a un OB inexistente, error de lectura/escritura periférica, etc.

```scl
// Registrar evento
"DB_Diagnostico".diOB85_Eventos += 1;
"DB_Diagnostico".sUltimoFalloOB85 := 'Error de programa OB85';

// Activar alarma
"DB_Alarmas".aLista[11].xActiva := TRUE;
"DB_Alarmas".aLista[11].sTexto := 'Error de programa OB85';
"DB_Alarmas".aLista[11].iPrioridad := 4;
```

## OB86 — Rack Failure

Disparado cuando se cae un rack completo de I/O distribuido (ej: una IM155 de PROFINET).

```scl
// Marca el sistema en modo seguro
"DB_Proceso".xModoSeguro := TRUE;

// Para todos los equipos por seguridad
"DB_Equipos".M01_BombaPrincipal.Comando.xParo := TRUE;
"DB_Equipos".M02_VentiladorExtraccion.Comando.xParo := TRUE;

// Activar alarma crítica
"DB_Alarmas".aLista[12].xActiva := TRUE;
"DB_Alarmas".aLista[12].sTexto := 'Caída de rack remoto — modo seguro activo';
"DB_Alarmas".aLista[12].iPrioridad := 4;
```

---

## Cómo importarlo en TIA Portal

1. Descarga `ob82-85-86-errores.xml` (contiene los 3 OBs en un único archivo)
2. En TIA Portal: clic derecho sobre **Bloques de programa** → **Importar** → confirma
3. Si ya tienes alguno de estos OBs, TIA Portal te avisará — fusiona el contenido manualmente

---

## Notas / Limitaciones conocidas

- **S7-1200** no soporta OB86 (no tiene racks remotos clásicos). Sí soporta OB82 y OB85.
- En **S7-1500** muchos eventos antes gestionados por OB85 ahora caen en OB121/OB122 (errores de programación) — añade los esqueletos según necesidad.
- La plantilla solo **registra y alarma**. Si tu proceso requiere acciones específicas (cerrar válvulas, parar todo), añádelas en cada OB según corresponda.
- En entornos críticos, considera además un **OB de Time Error (OB80)** y un **OB121 (Programming Error)**.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
