# FC_Escalado

> Escalado lineal genérico de un INT raw (0-27648) a un REAL en unidades de ingeniería.

**Tipo:** `Función (FC)`
**Versión TIA Portal:** V20 *(compatible con V18 y V19)*
**Familia PLC:** S7-1200 / S7-1500

---

## ¿Qué problema resuelve?

Cuando trabajas con entradas analógicas en formato 0-27648, hay que convertir ese valor crudo a la unidad de ingeniería real (ºC, bar, m³/h…). Cada vez se reescribe la misma fórmula y se acaba metiendo errores de signos, división por cero o conversión INT/REAL.

`FC_Escalado` hace esa conversión de forma parametrizable, segura y documentada — sin memoria interna, así que se puede llamar tantas veces como hagan falta sin DB de instancia.

Es el **caso de uso más universal** de TIA Portal y la primera pieza que cualquier proyecto necesita.

---

## Variables / Interfaz

### Entradas (Input)

| Variable | Tipo | Descripción |
|---|---|---|
| `iValorCrudo` | INT | Valor raw de la entrada analógica |
| `iRawMin` | INT | Valor raw correspondiente al mínimo de escala (típico 0 para 0-10V, 5530 para 4-20mA) |
| `iRawMax` | INT | Valor raw correspondiente al máximo de escala (típico 27648) |
| `rEscalaMin` | REAL | Valor en ingeniería correspondiente al raw mínimo |
| `rEscalaMax` | REAL | Valor en ingeniería correspondiente al raw máximo |

### Retorno (Return)

| Variable | Tipo | Descripción |
|---|---|---|
| `Ret_Val` | REAL | Valor escalado en unidades de ingeniería |

### Lógica interna (en SCL)

```scl
IF iRawMax = iRawMin THEN
    #Ret_Val := #rEscalaMin;   // protección división por cero
ELSE
    #Ret_Val := #rEscalaMin
              + (INT_TO_REAL(#iValorCrudo - #iRawMin)
                 / INT_TO_REAL(#iRawMax - #iRawMin))
              * (#rEscalaMax - #rEscalaMin);
END_IF;
```

---

## Cómo importarlo en TIA Portal

1. Descarga el archivo `fc-escalado.xml`
2. En TIA Portal, abre tu proyecto
3. En el árbol del proyecto, clic derecho sobre **Bloques de programa**
4. Selecciona **Importar**
5. Busca el `.xml` descargado y confirma

---

## Ejemplo de uso

```scl
// Sensor de pH (0-10V) escalado a 0.0-14.0 pH
"DB_Proceso".rPH_Reactor := "FC_Escalado"(
    iValorCrudo := %IW64,
    iRawMin     := 0,
    iRawMax     := 27648,
    rEscalaMin  := 0.0,
    rEscalaMax  := 14.0
);

// Sensor de presión 4-20mA → 0.0-10.0 bar
"DB_Proceso".rPresion_Linea := "FC_Escalado"(
    iValorCrudo := %IW66,
    iRawMin     := 5530,        // 4mA
    iRawMax     := 27648,       // 20mA
    rEscalaMin  := 0.0,
    rEscalaMax  := 10.0
);
```

---

## Notas / Limitaciones conocidas

- El bloque hace una conversión **lineal**. Para sensores no lineales (ej: termopares en mV crudos sin linealizar), usa los bloques `SCALE`/`SCALE_X` específicos de Siemens o aplica una linealización a tramos antes.
- Si `iRawMax = iRawMin` el bloque devuelve `rEscalaMin` para evitar división por cero (no salta excepción).
- El bloque **no satura** la salida — si el raw está fuera del rango configurado, devuelve un valor escalado fuera de `rEscalaMin` / `rEscalaMax`. Si necesitas saturación, envuélvelo con `MIN`/`MAX` en el sitio de llamada.
- Para módulos de alta resolución (-32768 a 32767), pasa esos valores como `iRawMin`/`iRawMax`.

---

## Autor

**GitHub:** [@iagorobo24-hub](https://github.com/iagorobo24-hub)
