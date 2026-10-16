# Rutas de aprendizaje

Tres caminos según tu punto de partida. Cada parada indica qué necesitas
y qué te llevas. Los niveles coinciden con la columna `Nivel` del
[catálogo](../../CATALOG.md).

## Principiante: tu primer bloque en PLCSIM

Para quien abre TIA Portal y quiere ver algo funcionando en simulación.

| Orden | Parada | Necesitas | Te llevas |
|---|---|---|---|
| 1 | [FC_Escalado](../../bloques-de-funcion/fc-escalado/) | TIA V20, nociones de SCL | Convertir 0–27648 a ingeniería sin errores típicos |
| 2 | [UDT_Motor](../../tipos-de-datos/udt-motor/) + [FB_Motor](../../bloques-de-funcion/fb-motor/) | Lo anterior | El patrón UDT como contrato dato–bloque–HMI |
| 3 | [OB1 plantilla](../../bloques-de-organizacion/ob1-plantilla/) | Lo anterior | Llamar bloques desde el ciclo con orden |
| 4 | [Tutorial 5](../../ia-tia-portal/tutoriales/05-testing-automatizado.md) | PLCSIM | Probar lo anterior sin hardware |

## Intermedio: alarmas y diagnóstico

Para quien ya mueve bloques y quiere una instalación presentable.

| Orden | Parada | Necesitas | Te llevas |
|---|---|---|---|
| 1 | [FB_AlarmLatch](../../bloques-de-funcion/fb-alarm-latch/) | Ruta principiante | Enclavamiento con reconocimiento y sirena, con evidencia |
| 2 | [Pantalla de Alarmas](../../hmi/pantalla-alarmas/) + [UDT_Alarm](../../tipos-de-datos/udt-alarm/) | Lo anterior | Listado, filtros y reconocimiento en HMI |
| 3 | [OB82/85/86](../../bloques-de-organizacion/ob82-85-86-errores/) | CPU S7-1500 o PLCSIM | No dejar la CPU en STOP ante un fallo de hardware |
| 4 | [Guía de conexión V20](../../ia-tia-portal/guias/conexion-profesional-v20.md) | TIA + Windows | Leer tu proyecto con un agente sin romper nada |

## Avanzado: líneas modulares e IA

Para quien estructura proyectos multi-PLC y automatiza ingeniería.

| Orden | Parada | Necesitas | Te llevas |
|---|---|---|---|
| 1 | [Plantilla línea modular](../../plantillas-de-proyecto/plantilla-linea-modular/) | Ruta intermedia | Varios PLC con librerías compartidas |
| 2 | [Tutorial 4](../../ia-tia-portal/tutoriales/04-migracion-proyecto.md) | Proyecto en versión anterior | Migrar versiones con ayuda de IA |
| 3 | [Tutorial 6](../../ia-tia-portal/tutoriales/06-refactorizacion-inteligente.md) | Código propio abundante | Limpiar código heredado con criterio |
| 4 | [IA + TIA Portal](../../ia-tia-portal/) completo | Todo lo anterior | Openness, MCP y límites verificados |

## Preguntas para elegir

- ¿Nunca compilaste un SCL? Empieza en **Principiante**, paso 1.
- ¿Ya tienes bloques pero las alarmas son un caos? Entra en **Intermedio**.
- ¿Vienes del otro proyecto (T-IA) y ya conectas agentes? Ve directo a **Avanzado**, paso 4.
