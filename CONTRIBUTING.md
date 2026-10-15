# Cómo contribuir a Awesome TIA Portal

Gracias por querer compartir tu conocimiento. Esta guía está diseñada para que cualquier programador de PLC pueda aportar, aunque nunca haya usado GitHub.

---

## 📖 Diccionario GitHub para Programadores de PLC

Si no vienes del mundo del software, GitHub puede sonar raro. Aquí tienes una traducción:

| Término GitHub | Traducción al mundo PLC | ¿Qué significa? |
|---|---|---|
| **Repository (Repo)** | Proyecto / Librería | Es la carpeta principal que contiene todos los archivos. |
| **Fork** | "Guardar como..." | Creas una copia exacta del proyecto en tu propia cuenta para hacer pruebas. |
| **Branch (Rama)** | Variante de proyecto | Una línea de trabajo separada (como cuando haces una copia de un proyecto para probar una modificación sin romper el original). |
| **Commit** | Guardar cambios | Es como darle al botón de guardar, pero con un comentario de qué has cambiado. |
| **Pull Request (PR)** | Propuesta de cambios | Nos pides que revisemos tus cambios para "unirlos" a la librería principal. |
| **Issue** | Aviso / Ticket | Un mensaje para avisar de un error, hacer una pregunta o proponer una idea. |

---

## 🛤️ El camino fácil: ¿Qué quieres hacer?

### A. Tengo un recurso (Bloque, UDT...) y quiero compartirlo
Sigue los pasos de la **Guía Completa** más abajo.

### B. He visto un error o tengo una duda
Abre una [issue](https://github.com/iagorobo24-hub/awesome-tia-portal/issues/new). Es como escribir un post en un foro. No necesitas instalar nada.

### C. Quiero mejorar una explicación (README)
Puedes hacerlo directamente desde la web de GitHub pulsando el icono del lápiz ✏️ en el archivo que quieras cambiar.

---

## 🚀 Guía Completa para añadir un recurso nuevo

### 1. Prepara tu recurso
1. Asegúrate de que el código es tuyo o tienes autorización para publicarlo. Elimina nombres de cliente, máquina, producto, direcciones IP, rutas locales y secretos.
2. Incluye un archivo fuente `.scl` o una exportación del objeto individual cuando exista. No subas un `.ap20` de cliente ni un paquete Siemens propietario.
3. Indica versión de TIA, tipo de CPU/HMI, dependencias, estado de compilación y si existe una prueba de comportamiento en PLCSIM o Runtime. Si no lo has probado, dilo.

### 2. Haz un Fork
Pulsa el botón **Fork** arriba a la derecha. Ahora tienes una copia del repo en tu cuenta.

### 3. Crea una Rama (Branch)
En tu copia, crea una rama con un nombre corto, por ejemplo: `feat/mi-nuevo-bloque`.

### 4. Sube tus archivos
Entra en la carpeta correspondiente (`bloques-de-funcion/`, `tipos-de-datos/`, etc.):
1. Crea una subcarpeta para tu recurso (usa nombres en minúsculas y con guiones).
2. Sube la fuente o exportación que realmente hayas probado; si solo aportas un diseño, indica que todavía no hay bloque importable.
3. Crea un archivo README.md usando la [plantilla de recursos](./_plantillas/README-recurso.md).

### 5. Abre la Pull Request
Vuelve a la página principal de tu repo y verás un botón que dice **"Compare & pull request"**. Pulsa, escribe un pequeño resumen de lo que aportas y listo.

---

## 📏 Reglas de Oro para que aceptemos tu aporte
- **Documentación**: el `README.md` debe explicar el problema, la interfaz, el uso, las dependencias, la versión probada y los límites.
- **Evidencia**: distingue claramente fuente disponible, compilación, guardado y prueba funcional. Una captura sin contexto no demuestra funcionamiento.
- **Limpieza**: no subas proyectos de cliente ni archivos masivos; comparte solo los archivos necesarios para el recurso.
- **Seguridad**: no incluyas bloques F/Safety, contraseñas ni instrucciones de descarga a hardware sin una revisión específica.
- **Formato**: Usa nombres de carpeta claros (ej: `escalado-analogico` en vez de `Bloque_1`).

---

¿Aún tienes dudas? Abre un **Issue** y te ayudaremos paso a paso. ¡No hay aportación pequeña!

Las imágenes generadas deben identificarse como ilustraciones. Las capturas reales necesitan indicar proyecto de demostración, versión de TIA y qué acción muestran.
