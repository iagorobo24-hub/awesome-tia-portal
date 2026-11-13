# Awesome TIA Portal — Plan maestro de evolución y evaluación

- **Fecha de línea base:** 2026-11-12
- **Estado del documento:** PLANIFICADO, no es evidencia de ejecución.
- **Repositorio local:** `awesome-tia-portal`, Portatiltek.
- **Snapshot inspeccionado:** rama `feat/github-research-templates`, commit `60ca89f`; `main` y `origin/main` en `656213a`.
- **Regla de alcance:** planificar y auditar no autoriza fusionar, publicar, borrar ni desplegar; verificar rama, HEAD y modificaciones concurrentes antes de cada fase.

## 1. Objetivo y criterio de producto

Convertir el repositorio público en una **biblioteca curada y técnicamente reproducible** de ingeniería Siemens TIA Portal, con piezas usables, documentación honesta, procedencia clara y comunidad sostenible. No perseguir volumen de fichas ni estrellas como sustitutos de calidad.

**Alcance de v0.2.0:** fiabilidad editorial y de CI; dos recursos ya ejecutados con evidencia, reimportación desde cero demostrada cuando sea viable; experiencia de usuario sencilla; entrega versionada reproducible. Las nuevas fichas no serán presentadas como bloques funcionales.

**Alcance posterior:** componentes UDT–FB–HMI, ejemplos reutilizables, curación externa, gobernanza y difusión. No comprometer todas las fichas como "verificadas" en v0.2.0.

## 2. Línea base comprobada y límites

- Git local: rama `feat/github-research-templates` @ `60ca89f`; árbol limpio durante inspección. `main` @ `656213a`; no se ha hecho push del commit de investigación.
- Repositorio público a 2026-11-12: 3 estrellas, 0 forks, licencia MIT, GitHub Pages y Discussions habilitados; `main` sin protección. Métricas de tráfico no consultadas; **no inferir** visitas ni conversiones.
- Catálogo local: **26 recursos** principales (23 anteriores + 3 fichas nuevas); **2 registrados como `verified`** y **24 fichas `documented`**. No equivale a 26 recursos importables.
- Evidencia propia: `FB_AlarmLatch` y `FC_Escalado` tienen SCL y XML, registros de compilación y ejecución PLCSIM en proyecto de demostración. Aún se debe verificar importación de XML desde cero. Las evidencias se han inspeccionado documentalmente en esta sesión; no se ha reproducido TIA.
- Investigación local en `docs/research/`: 34 búsquedas, 1.132 resultados brutos y 961 únicos (cifras corroboradas en JSON); 70 registros con README y árbol de archivos; 12 referencias externas nuevas enlazadas en README (**11 clase A/B y 1 clase C**); 3 nuevas fichas de diseño. La clasificación de los 70 carece de puntuaciones numéricas almacenadas; no dar por validada una evaluación sobre 100 hasta crearla y comprobarla. No publicitar esta muestra como censo exhaustivo.
- Archivos de investigacion en la linea base: `analisis.json` bruto de unos 4,2 MB con README y arboles ajenos, y `consolidado.json` de unos 0,92 MB. Para publicar, el primero se ha reducido a metadatos; la fuente bruta permanece solo en la rama local de investigacion.
- Comprobaciones locales ejecutadas en esta sesión: `python scripts/generate_catalog.py --check` correcto; `python scripts/check-local-links.py`: **431 enlaces locales, 0 rotos**; `python scripts/validate-xml.py`: **3 XML y 4 SCL sin errores estáticos detectados**.
- GitHub Actions 2026-11-08 (commit público): job estructural `validate` correcto; `secretos`/Gitleaks en error; revisión externa/Lychee en error. No se ha determinado si existe secreto real o falso positivo; no rebajar filtros para obtener verde.
- Documentación desfasada: README, FAQ, rutas de aprendizaje y ciertas fichas indican que no existen XML o que PLCSIM está pendiente, en contradicción con archivos/evidencias posteriores.
- No se han evaluado a fondo todas las afirmaciones técnicas de los documentos extensos de `ia-tia-portal/`, ni se han reproducido pruebas de software o hardware reales. La auditoría exhaustiva de esas guías es una tarea independiente.

## 3. Hallazgos de diseño que requieren resolución

1. **PID nuevo (`fb-control-pid`)**: ecuación usa tiempo de muestreo `Ts`, pero la interfaz no lo declara; conviven dos convenciones de ganancias y la semántica del término derivativo requiere especificar signo y `Ts`. Antes de codificar, decidir si se necesita regulador propio o conviene documentar el bloque nativo de Siemens, y definir condiciones de error, saturación, cambio manual/automático y límites.
2. **Máquina de estados nueva (`fb-estado-maquina`)**: aclarar comportamiento de estado inicial 0, `xInicio`, reset, saltos forzados, prioridades y estado final; el ejemplo de llamada a elementos del array de entrada requiere verificación de sintaxis en SCL real. No presentar como ejecutable todavía.
3. **Secuenciador nuevo (`fb-secuenciador-pasos`)**: revisar estado final (paso 16/activo/completado), pulsos de un ciclo, pausa, rearme, señales de timeout y significado de `iPasoTotal`; verificar ejemplo de arrays.
4. **`FB_AlarmLatch`**: reconocimiento mantenido a TRUE puede reconocer alarma nueva en el mismo ciclo; conducta reportada y documentada pero requiere decisión contractual, no solamente test verde.
5. **Compatibilidad**: `tia_compat: [V18,V19,V20]` en diseños no equivale a prueba; registrar versiones declaradas, observadas y no comprobadas por separado.
6. **Estado `available`**: presencia y XML bien formado NO implica reimportación correcta; exigir generación/importación desde cero en proyecto limpio y observación de compilación.
7. **Investigación externa**: distinguir referencia curada de licencia concedida para copiar y de compatibilidad validada; evitar incorporar material de terceros por mera visibilidad pública.

## 4. Ejecución por fases

Todas las estimaciones son **horas de esfuerzo**, no plazos ni promesas de finalización. Se revisarán tras medir las primeras tareas. No abarcan transformar las 25 fichas en recursos probados.

### D0 — Inventario, línea base y contrato de versión (4–7 h)
- [ ] Volver a verificar Git (rama, HEAD, árbol, remotos, agentes concurrentes) y registrar snapshot.
- [ ] Inventariar 27 recursos, archivos reales, dependencias, estados y pruebas con criterio único de verdad.
- [ ] Definir requisitos verificables de `documented`, `source`, `compiled`, `exported`, `reimported`, `simulated`; distinguir seguridad de proceso y seguridad funcional.
- [ ] Registrar métricas iniciales, deficiencias y fronteras de v0.2.0; no reestructurar el repositorio por rutina.
**Cierre:** inventario comprobable y contrato de estados aprobados por evidencia; ninguna ambigüedad crítica oculta.

### D1 — Fiabilidad documental, CI y seguridad (12–22 h)
- [ ] Investigar fallo Gitleaks: logs/causa, secretos reales vs falsos positivos; resolver sin debilitar controles y gestionar incidentes si procede.
- [ ] Investigar fallo Lychee por URL concreta, rate limits, cambios de origen o configuración; establecer tratamiento honesto de excepciones.
- [ ] Rectificar README, FAQ, rutas, badges, `docs/visibilidad.md`, `docs/hoja-de-ruta.md` y fichas contradictorias.
- [ ] Evitar instrucciones de descarga de archivos inexistentes; proporcionar estado y próximos pasos reales.
- [ ] Mantener `CATALOG.md`, matriz y resumen del README sincronizados desde metadatos/validadores; añadir tests para estos validadores.
- [ ] Revisar exposición accidental de datos de instalaciones, credenciales, IP y procedencia; no tocar las configuraciones de clientes.
**Cierre:** documentación pública coherente, controles relevantes pasan o hay bloqueo real explícito; pruebas y razones registradas.

### D2 — Cierre técnico de dos recursos existentes (12–24 h)
- [ ] Revisar contratos de `FC_Escalado` y `FB_AlarmLatch`, semánticas límite y sus fuentes exactas frente a evidencias.
- [ ] Crear/usar fixture desechable TIA V20; **no descargar a PLC físico**.
- [ ] Importar XML desde cero en proyecto limpio y compilar; comparar interfaces y versión.
- [ ] Ejecutar/priorizar casos de borde y regresión en PLCSIM para confirmar, no simplemente asumir, la evidencia anterior.
- [ ] Documentar versión/build, CPU virtual, archivos, hash, entradas, salidas, resultados y restricciones.
- [ ] Preparar ejemplo mínimo reproducible por recurso y procedimiento de uso probado.
**Cierre:** cada recurso tiene trazabilidad del archivo a importación, compilación y comportamiento; de lo contrario queda explícitamente pendiente.

### D3 — Experiencia de uso y empaquetado (6–12 h)
- [ ] Portada orientada a "qué problema resuelve", recursos destacados probados, estado y descarga directa.
- [ ] Mejorar rutas de aprendizaje para que no prometan bloques inexistentes.
- [ ] Separar visiblemente "biblioteca PLC" de "guías IA/Openness", manteniendo las rutas y material vigente.
- [ ] Revisar Docsify/Pages, navegación, búsqueda, enlaces, visualización móvil y licencia/aprobación de recursos.
- [ ] Preparar guía breve de instalación/reproducción y sección inglesa básica, sin duplicar documentación extensa.
**Cierre:** un visitante nuevo identifica en pocos pasos qué puede utilizar ahora y qué está todavía en diseño.

### D4 — Release candidata v0.2.0 (6–12 h)
- [ ] Revalidar enlaces locales, catálogo, formatos, estructura, seguridad, atribuciones y diffs.
- [ ] Definir changelog verificable, matriz de compatibilidad y contenido distribuible.
- [ ] Revisar los 11 enlaces de terceros por utilidad/licencia y eliminar descripciones no verificables.
- [ ] Validar flujo en entorno limpio y recoger limitaciones; establecer criterios de aprobación de release.
- [ ] Preparar release y publicación **sin ejecutarlas** hasta autorización específica de merge/push/tag/release.
**Cierre:** candidato con evidencia y sin fallos críticos no explicados; documentación y artefactos reproducibles.

### D5 — Auditoría de aceptación v0.2.0 (4–8 h)
- [ ] Recontar recursos documentados, importables, compilados, simulados y compatibilidad realmente verificada.
- [ ] Auditar fallos abiertos, experiencia de usuario y repetibilidad de cero a resultado.
- [ ] Evaluar con rúbrica del apartado 7; presentar comparativa inicial vs candidata, límites y pendientes.
**Cierre:** informe de aceptación trazable, sin declarar éxito a partir de una etiqueta o badge.

**Subtotal previsto v0.2.0: 44–85 h.**

### D6 — Investigación y catálogo externo de calidad (8–16 h; evolución)
- [ ] Revisar por muestreo el inventario de 961 repositorios y el análisis profundo de 70; recalcular coberturas y duplicados.
- [ ] Reducir ruido del material JSON si corresponde, sin perder reproducibilidad ni atribuciones.
- [ ] Puntuar los candidatos relevantes con criterios reproducibles y evidencia, registrando campos de puntuación, incertidumbre y motivos de descarte; no confundir metadata o README leído con revisión profunda certificada.
- [ ] Curar solo enlaces comprobados y útiles, con fecha de revisión, versión, licencia y política de caducidad.
- [ ] Analizar proyectos cercanos (Awesome Structured Text, Awesome PLC AI, bibliotecas Siemens, herramientas oficiales), priorizando aportaciones legítimas sobre intercambios de estrellas.
**Cierre:** índices externos mantenibles y verificación documentada, no cantidad indiscriminada.

### D7 — Biblioteca funcional ampliada (50–100 h; evolución inicial)
- [ ] Antes de crear más fichas, cerrar los UDT/FB existentes de mayor utilidad: ruta analógica, motor/válvula y alarmas.
- [ ] Desarrollar y revisar nuevas fichas `fb-estado-maquina`, `fb-secuenciador-pasos` y `fb-control-pid` con contratos correctos, fuentes y pruebas reales si se priorizan.
- [ ] Mantener test negativo, límites, fallos, casos de integración con DB/UDT y evidencia de importación para cada recurso.
- [ ] Evaluar si HMI Comfort y Unified requieren artefactos distintos; no atribuir compatibilidad sin validación.
- [ ] No redistribuir lógica Safety ni ejemplos de riesgo como aptos para producción.
**Cierre:** cada nuevo recurso aporta código independiente y reproducible; publicar solo los efectivamente cerrados.

### D8 — Comunidad, distribución y sostenibilidad (12–24 h; evolución)
- [ ] Crear contribuciones de baja barrera: corrección de traducciones, documentación, tests y enlaces validados.
- [ ] Generar demos reales con ejemplos mínimos, capturas auténticas y resultados verificables.
- [ ] Establecer inglés mínimo para el descubrimiento sin perder la documentación española.
- [ ] Participar en listas/comunidades relevantes con contribuciones reales y enlaces contextuales.
- [ ] Preparar mantenimiento recurrente de enlaces, licencias, versiones y issues; medir visitas con datos disponibles y consentimiento.
**Cierre:** mecanismos de adquisición y contribución ética operativos, métricas trazables sin manipulación.

### D9 — Informe final de valoración integral (4–8 h; al terminar el programa)
- [ ] Rehacer la auditoría de cero sobre el commit final local y el estado público, si se publicó.
- [ ] Evaluar cada criterio y cada recurso de interés con evidencias y puntuaciones justificadas.
- [ ] Comparar línea base vs final, objetivos cumplidos, capacidad de mantenimiento y coste futuro.
- [ ] Enumerar riesgos abiertos y próximos hitos sin declarar producción segura.
**Cierre:** evaluación reproducible y comparativa, con datos medidos y ausencias explícitas.

**Total programa ampliado estimado: 118–233 h** (v0.2.0 + evolución inicial D6–D9). No equivale al esfuerzo de completar las 25 fichas pendientes; esa ambición exige estimaciones específicas.

## 5. Orden de trabajo y decisiones de alcance

1. No fusionar ni publicar el commit de investigación sin revisar su calidad y el tamaño de los datos.
2. Resolver antes la contradicción pública y los controles de seguridad que añadir nuevas plantillas.
3. Priorizar la reimportación limpia de los dos bloques ya probados sobre aumentar el número de "verified".
4. No desarrollar el PID propio hasta contrastar si cubre una necesidad no cubierta por instrucciones Siemens y definir `Ts` y semántica.
5. Diferenciar **v0.2.0 publicable** de evolución de biblioteca a medio plazo; evitar una versión interminable.
6. No crear ramas o worktrees automáticamente: elegir en cada fase según procesos concurrentes y riesgo de colisión.
7. Antes de cualquier trabajo con TIA/PLCSIM: verificar fixture, sesión, proyecto y destino virtual; prohibida descarga a CPU real sin orden explícita.

## 6. Puertas de calidad y evidencias por fase

Para declarar una fase cerrada se requiere: **alcance comprobado + pruebas relevantes + diff revisado + ninguna inconsistencia crítica + pendientes identificados**. Clasificar hallazgos como `VERIFICADO`, `REPORTADO`, `INFERIDO`, `SUPUESTO` o `RECOMENDADO`.

Métricas mínimas registrables:
- Inventario: número de recursos por estado, fuente, XML, compilación, reimportación y simulación.
- Fiabilidad: fallos críticos, antigüedad, enlaces internos/externos comprobados, secretos/CI, cobertura de validadores.
- Técnica: comportamiento esperado y observado, versión de TIA, CPU/PLCSIM y resultados de pruebas de borde.
- Documentación: rutas falsas, duplicación, tutoriales reproducibles, claridad de los procedimientos, idioma.
- Licencias: autoría, permisos, atribución y modificaciones para cada material incorporado.
- Comunidad: stars, forks, contributors únicos externos, PR externos, issues atendidos y referencias útiles; tráfico solo si se dispone de datos fiables.
- Mantenimiento: tiempo de revisión, caducidad de enlaces e incidencias, versiones publicadas y deuda abierta.

## 7. Informe de valoración final — rúbrica con pesos (100 puntos)

La puntuación solo se concederá con evidencia; un criterio `NO EVALUADO` se muestra aparte, nunca se presume cero ni se rellena arbitrariamente.

| Característica evaluable | Peso |
|---|---:|
| Completitud funcional y utilidad real de la biblioteca | 18 |
| Calidad y corrección de ingeniería PLC/HMI | 14 |
| Evidencia de compilación, importación y pruebas reproducibles | 14 |
| Seguridad industrial, límites y manejo de fallos | 10 |
| Compatibilidad real por TIA/CPU/HMI | 7 |
| Documentación, onboarding y experiencia web | 10 |
| CI, validadores, seguridad informática y calidad automática | 9 |
| Licencias, procedencia y atribuciones | 5 |
| Mantenibilidad y arquitectura del catálogo | 5 |
| Comunidad y facilidad de contribuir | 4 |
| Descubribilidad e interoperabilidad con el ecosistema | 2 |
| Gobernanza, releases y trazabilidad Git | 2 |
| **TOTAL** | **100** |

Por cada característica: **nota 0–100**, peso efectivo, evidencia/ruta, nivel de confianza, defectos graves, recomendación y evolución respecto a línea base. Mantener además una evaluación **por recurso** (interfaz, código, importación, compilación, test, seguridad, compatibilidad, documentación, licencia) independiente de la nota global. No permitir que abundancia de documentación o estrellas compense riesgos técnicos críticos.

## 8. Estado actual y próxima ejecución

- D0: **inspección parcial hecha**, contrato y matriz aún pendientes.
- D1: **pendiente**; fallos GitHub Actions y contradicciones confirmados.
- D2: **pendiente de reproducir** en TIA V20/PLCSIM; evidencias históricas existentes.
- D3–D9: **planificados**, no ejecutados por este documento.
- **Publicación:** ninguna autorizada en esta fase.
- Antes de ejecutar fases posteriores, contrastar siempre el HEAD real, trabajo de otros agentes y el último estado GitHub.

**Regla de cierre:** el informe de valoración final será una auditoría de la versión realmente terminada, no una estimación optimista del proyecto previsto.
