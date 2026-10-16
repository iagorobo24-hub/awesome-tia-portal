# Glosario ES ↔ EN (TIA Portal / S7)

Porque la mitad de la documentación y de los foros está en inglés.
Primero el término que usamos en este repo, luego el equivalente.

| Español (repo) | English | Nota |
|---|---|---|
| Bloque de función (FB) | Function Block (FB) | Con memoria (DB de instancia) |
| Función (FC) | Function (FC) | Sin memoria |
| Bloque de organización (OB) | Organization Block (OB) | OB1 = ciclo principal |
| Tipo de datos de PLC (UDT) | PLC Data Type (UDT) | Estructura reutilizable |
| Enclavamiento | Latch | Mantener un estado hasta reconocer |
| Reconocimiento (ack) | Acknowledge (ack) | Confirmación del operador |
| Sirena / petición de sirena | Horn | Aviso acústico pendiente |
| Flanco (subida/bajada) | Edge (rising/falling), FP/R_TRIG | Detección de cambio |
| Memoria (M) | Memory / flag | Área de marcas |
| Tabla de observación / VAT | Watch table | Forzar y observar en PLCSIM |
| Forzar | Force | Escribir un valor en RUN (con cuidado) |
| Escalado | Scaling (SCALE_X / NORM_X) | Raw a ingeniería |
| Instancia / DB de instancia | Instance / instance DB | Datos de un FB concreto |
| Puesta en marcha | Commissioning | FAT en fábrica, SAT en planta |
| Aviso / fallo | Warning / fault | Sin parar frente a con parada |
| Runtime (HMI) | Runtime | HMI en ejecución |
| Faceplate | Faceplate | Plantilla gráfica reutilizable |
| Openness | Openness | API oficial para automatizar TIA |
| PLCSIM | PLCSIM (Advanced) | Simulación sin hardware |

¿Falta un término? Propón la fila en un issue o PR.
