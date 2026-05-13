# 🔧 Troubleshooting y FAQ

Guía de solución de problemas y preguntas frecuentes para IA + TIA Portal.

---

## 📑 Tabla de contenido

- [Errores comunes](#errores-comunes)
- [Permisos de Openness](#permisos-de-openness)
- [Problemas de conexión](#problemas-de-conexión)
- [Errores de compilación](#errores-de-compilación)
- [FAQ](#faq)

---

## ❌ Errores comunes

### Error: "No se puede conectar a TIA Portal"

**Síntoma:**
```
Error: No se puede conectar a TIA Portal
```

**Causas:**
1. TIA Portal no está abierto
2. API de Openness no está habilitada
3. Proyecto no está abierto
4. Permisos insuficientes

**Soluciones:**

1. **Abrir TIA Portal**
   ```
   1. Abre TIA Portal
   2. Abre el proyecto
   3. Verifica que el proyecto está activo
   ```

2. **Habilitar API de Openness**
   ```
   1. Ve a Opciones → Openness
   2. Habilita "Permitir acceso a Openness"
   3. Reinicia TIA Portal
   ```

3. **Verificar permisos**
   ```
   1. Ejecuta TIA Portal como administrador
   2. Verifica permisos de lectura/escritura
   3. Verifica permisos de red
   ```

---

### Error: "Timeout de compilación"

**Síntoma:**
```
Error: Timeout de compilación
```

**Causas:**
1. Proyecto demasiado grande
2. Recursos insuficientes
3. Bloques con errores
4. Dependencias circulares

**Soluciones:**

1. **Compilar bloques individualmente**
   ```
   1. Identifica bloques con errores
   2. Compila bloques uno por uno
   3. Corrige errores antes de compilar todo
   ```

2. **Aumentar timeout**
   ```powershell
   # Aumentar timeout de compilación
   tia-portal compile -timeout 600
   ```

3. **Optimizar proyecto**
   ```
   1. Eliminar bloques no usados
   2. Reducir complejidad de bloques
   3. Eliminar dependencias circulares
   ```

---

### Error: "Bloque no encontrado"

**Síntoma:**
```
Error: Bloque no encontrado
```

**Causas:**
1. Nombre de bloque incorrecto
2. Bloque no existe
3. Bloque en otra carpeta
4. Bloque no compilado

**Soluciones:**

1. **Verificar nombre de bloque**
   ```
   1. Verifica ortografía del nombre
   2. Verifica mayúsculas/minúsculas
   3. Verifica prefijos/sufijos
   ```

2. **Listar bloques disponibles**
   ```powershell
   # Listar todos los bloques
   tia-portal list-blocks
   ```

3. **Verificar ubicación del bloque**
   ```
   1. Busca bloque en TIA Portal
   2. Verifica carpeta del bloque
   3. Verifica que el bloque está compilado
   ```

---

### Error: "Error de sintaxis"

**Síntoma:**
```
Error: Error de sintaxis en línea X
```

**Causas:**
1. Sintaxis incorrecta
2. Falta de punto y coma
3. Paréntesis no cerrados
4. Variables no declaradas

**Soluciones:**

1. **Verificar sintaxis**
   ```
   1. Revisa línea indicada
   2. Verifica punto y coma
   3. Verifica paréntesis
   4. Verifica variables declaradas
   ```

2. **Usar validador de sintaxis**
   ```powershell
   # Validar sintaxis
   tia-portal validate-syntax -file "block.scl"
   ```

3. **Pedir a IA que corrija**
   ```
   Corrige este error de sintaxis.

   ERROR: [pegar error]
   CÓDIGO: [pegar código]

   Por favor, genera el código corregido.
   ```

---

### Error: "Error de compilación"

**Síntoma:**
```
Error: Error de compilación en bloque X
```

**Causas:**
1. Variables no declaradas
2. Tipos incorrectos
3. Bloques no encontrados
4. Dependencias faltantes

**Soluciones:**

1. **Verificar variables**
   ```
   1. Verifica que todas las variables están declaradas
   2. Verifica tipos de variables
   3. Verifica nombres de variables
   ```

2. **Verificar dependencias**
   ```
   1. Verifica que todos los bloques existen
   2. Verifica que los bloques están compilados
   3. Verifica que los bloques están en el proyecto
   ```

3. **Pedir a IA que corrija**
   ```
   Corrige este error de compilación.

   ERROR: [pegar error]
   CÓDIGO: [pegar código]

   Por favor, genera el código corregido.
   ```

---

### Error: "Error de ejecución"

**Síntoma:**
```
Error: Error de ejecución en bloque X
```

**Causas:**
1. División por cero
2. Overflow/underflow
3. Acceso a memoria inválido
4. Condiciones de carrera

**Soluciones:**

1. **Verificar división por cero**
   ```
   1. Verifica que el divisor no es cero
   2. Añade validación antes de dividir
   3. Maneja el caso de divisor cero
   ```

2. **Verificar overflow/underflow**
   ```
   1. Verifica rangos de variables
   2. Añade validación de rangos
   3. Usa tipos apropiados
   ```

3. **Pedir a IA que corrija**
   ```
   Corrige este error de ejecución.

   ERROR: [pegar error]
   CÓDIGO: [pegar código]

   Por favor, genera el código corregido.
   ```

---

## 🔑 Permisos de Openness

### Error: "Permisos insuficientes"

**Síntoma:**
```
Error: Permisos insuficientes para acceder a Openness
```

**Causas:**
1. TIA Portal no ejecutado como administrador
2. API de Openness no habilitada
3. Firewall bloqueando conexión
4. Antivirus bloqueando conexión

**Soluciones:**

1. **Ejecutar como administrador**
   ```
   1. Cierra TIA Portal
   2. Haz clic derecho en TIA Portal
   3. Selecciona "Ejecutar como administrador"
   4. Abre el proyecto
   ```

2. **Habilitar API de Openness**
   ```
   1. Ve a Opciones → Openness
   2. Habilita "Permitir acceso a Openness"
   3. Reinicia TIA Portal
   ```

3. **Configurar firewall**
   ```
   1. Abre firewall de Windows
   2. Añade excepción para TIA Portal
   3. Añade excepción para Openness
   4. Reinicia firewall
   ```

4. **Configurar antivirus**
   ```
   1. Abre antivirus
   2. Añade excepción para TIA Portal
   3. Añade excepción para Openness
   4. Reinicia antivirus
   ```

---

### Error: "API de Openness no disponible"

**Síntoma:**
```
Error: API de Openness no disponible
```

**Causas:**
1. Openness no instalado
2. Versión de Openness incompatible
3. Licencia de Openness no válida
4. Openness no habilitado

**Soluciones:**

1. **Instalar Openness**
   ```
   1. Descarga Openness desde Siemens
   2. Ejecuta instalador
   3. Reinicia TIA Portal
   ```

2. **Verificar versión**
   ```
   1. Verifica versión de TIA Portal
   2. Verifica versión de Openness
   3. Asegura compatibilidad
   ```

3. **Verificar licencia**
   ```
   1. Verifica licencia de Openness
   2. Verifica que la licencia es válida
   3. Renueva licencia si es necesario
   ```

4. **Habilitar Openness**
   ```
   1. Ve a Opciones → Openness
   2. Habilita "Permitir acceso a Openness"
   3. Reinicia TIA Portal
   ```

---

## 🔌 Problemas de conexión

### Error: "No se puede conectar al servidor MCP"

**Síntoma:**
```
Error: No se puede conectar al servidor MCP
```

**Causas:**
1. Servidor MCP no iniciado
2. Puerto incorrecto
3. Firewall bloqueando conexión
4. Dirección incorrecta

**Soluciones:**

1. **Iniciar servidor MCP**
   ```bash
   # Iniciar servidor MCP
   node /path/to/tiaportal-mcp/dist/index.js
   ```

2. **Verificar puerto**
   ```
   1. Verifica puerto en configuración
   2. Verifica que el puerto no está en uso
   3. Cambia puerto si es necesario
   ```

3. **Configurar firewall**
   ```
   1. Abre firewall de Windows
   2. Añade excepción para puerto MCP
   3. Reinicia firewall
   ```

4. **Verificar dirección**
   ```
   1. Verifica dirección en configuración
   2. Verifica que la dirección es correcta
   3. Prueba con localhost
   ```

---

### Error: "Timeout de conexión"

**Síntoma:**
```
Error: Timeout de conexión al servidor MCP
```

**Causas:**
1. Servidor MCP lento
2. Red lenta
3. Firewall bloqueando conexión
4. Servidor MCP no iniciado

**Soluciones:**

1. **Aumentar timeout**
   ```json
   {
     "mcpServers": {
       "tiaportal-mcp": {
         "timeout": 60000
       }
     }
   }
   ```

2. **Verificar servidor MCP**
   ```
   1. Verifica que el servidor MCP está iniciado
   2. Verifica logs del servidor MCP
   3. Reinicia servidor MCP si es necesario
   ```

3. **Verificar red**
   ```
   1. Verifica conexión de red
   2. Verifica velocidad de red
   3. Prueba con otra red
   ```

4. **Configurar firewall**
   ```
   1. Abre firewall de Windows
   2. Añade excepción para servidor MCP
   3. Reinicia firewall
   ```

---

## 🔨 Errores de compilación

### Error: "Bloque no compilado"

**Síntoma:**
```
Error: Bloque no compilado
```

**Causas:**
1. Bloque con errores
2. Bloque no guardado
3. Bloque no validado
4. Bloque con dependencias faltantes

**Soluciones:**

1. **Compilar bloque**
   ```
   1. Abre bloque en TIA Portal
   2. Compila bloque
   3. Corrige errores si hay
   4. Guarda bloque
   ```

2. **Validar bloque**
   ```
   1. Abre bloque en TIA Portal
   2. Valida bloque
   3. Corrige errores si hay
   4. Guarda bloque
   ```

3. **Verificar dependencias**
   ```
   1. Verifica que todas las dependencias existen
   2. Verifica que las dependencias están compiladas
   3. Verifica que las dependencias están en el proyecto
   ```

---

### Error: "Error de compilación en bloque X"

**Síntoma:**
```
Error: Error de compilación en bloque X
```

**Causas:**
1. Variables no declaradas
2. Tipos incorrectos
3. Bloques no encontrados
4. Dependencias faltantes

**Soluciones:**

1. **Verificar variables**
   ```
   1. Verifica que todas las variables están declaradas
   2. Verifica tipos de variables
   3. Verifica nombres de variables
   ```

2. **Verificar dependencias**
   ```
   1. Verifica que todos los bloques existen
   2. Verifica que los bloques están compilados
   3. Verifica que los bloques están en el proyecto
   ```

3. **Pedir a IA que corrija**
   ```
   Corrige este error de compilación.

   ERROR: [pegar error]
   CÓDIGO: [pegar código]

   Por favor, genera el código corregido.
   ```

---

## ❓ FAQ

### P: ¿Cómo empiezo a usar IA + TIA Portal?

**R:**
1. Instala un servidor MCP (tiaportal-mcp, tia-portal-openness-mcpserver, etc.)
2. Configura el servidor MCP en tu cliente de IA
3. Abre TIA Portal y habilita la API de Openness
4. Empieza a generar bloques con IA

Ver [Tutorial: Primeros pasos con MCP](../tutoriales/01-primeros-pasos-mcp.md) para más detalles.

---

### P: ¿Qué servidores MCP están disponibles?

**R:**
- **tiaportal-mcp** — Servidor MCP para TIA Portal (Node.js)
- **tia-portal-openness-mcpserver** — Servidor MCP para TIA Portal Openness (Python)
- **totally-integrated-claude** — Integración de Claude con TIA Portal
- **multiverse-sdlc** — Integración de IA con TIA Portal para SDLC

Ver [Comparativas de MCP Servers](../comparativas/README.md) para más detalles.

---

### P: ¿Cómo genero un bloque con IA?

**R:**
1. Crea un prompt detallado con requisitos
2. Envía el prompt a tu cliente de IA
3. Revisa el código generado
4. Valida el código en TIA Portal
5. Prueba en simulación

Ver [Tutorial: Generar bloque SCL](../tutoriales/02-generar-bloque-scl.md) para más detalles.

---

### P: ¿Cómo valido código generado por IA?

**R:**
1. Compila el bloque en TIA Portal
2. Verifica que no hay errores
3. Revisa la lógica manualmente
4. Prueba en simulación
5. Revisa con pares si es crítico

Ver [Best practices: Validación de código](../best-practices/README.md#validación-de-código-generado-por-ia) para más detalles.

---

### P: ¿Es seguro usar código generado por IA?

**R:**
Sí, si sigues las mejores prácticas:
1. Siempre revisa el código manualmente
2. Valida el código en TIA Portal
3. Prueba en simulación antes de producción
4. Revisa con pares si es crítico
5. Ten un plan de rollback

Ver [Best practices: Seguridad industrial](../best-practices/README.md#seguridad-industrial) para más detalles.

---

### P: ¿Cómo soluciono errores de compilación?

**R:**
1. Lee el mensaje de error
2. Identifica la causa
3. Corrige el error manualmente
4. Vuelve a compilar
5. Si no puedes solucionarlo, pide a IA que corrija

Ver [Errores de compilación](#errores-de-compilación) para más detalles.

---

### P: ¿Cómo soluciono problemas de conexión?

**R:**
1. Verifica que TIA Portal está abierto
2. Verifica que la API de Openness está habilitada
3. Verifica que el servidor MCP está iniciado
4. Verifica que el firewall no está bloqueando
5. Verifica que la dirección y puerto son correctos

Ver [Problemas de conexión](#problemas-de-conexión) para más detalles.

---

### P: ¿Cómo genero prompts efectivos?

**R:**
1. Sé específico y detallado
2. Define claramente la interfaz
3. Especifica el comportamiento
4. Incluye ejemplos
5. Especifica restricciones

Ver [Guía de prompts](../prompts/README.md) para más detalles.

---

### P: ¿Cómo automatizo tareas con IA?

**R:**
1. Identifica tareas repetitivas
2. Crea scripts de automatización
3. Integra con IA para generación de código
4. Automatiza compilación y pruebas
5. Automatiza despliegue

Ver [Integraciones con otras herramientas](../integraciones/README.md) para más detalles.

---

### P: ¿Cómo documento bloques generados por IA?

**R:**
1. Pide a IA que genere documentación
2. Revisa la documentación
3. Añade detalles específicos
4. Guarda en formato Markdown
5. Publica en Confluence o similar

Ver [Tutorial: Documentación automática](../tutoriales/03-documentacion-automatica.md) para más detalles.

---

### P: ¿Cómo pruebo bloques generados por IA?

**R:**
1. Compila el bloque en TIA Portal
2. Crea casos de prueba
3. Ejecuta pruebas en simulación
4. Verifica resultados
5. Corrige errores si hay

Ver [Tutorial: Testing automatizado](../tutoriales/05-testing-automatizado.md) para más detalles.

---

### P: ¿Cómo migro un proyecto a IA + TIA Portal?

**R:**
1. Analiza el proyecto existente
2. Identifica bloques que pueden ser generados por IA
3. Genera bloques con IA
4. Valida bloques en TIA Portal
5. Migra gradualmente

Ver [Tutorial: Migración de proyecto](../tutoriales/04-migracion-proyecto.md) para más detalles.

---

### P: ¿Cómo refactorizo bloques con IA?

**R:**
1. Identifica bloques que necesitan refactorización
2. Pide a IA que refactorice el bloque
3. Revisa el código refactorizado
4. Valida en TIA Portal
5. Prueba en simulación

Ver [Tutorial: Refactorización inteligente](../tutoriales/06-refactorizacion-inteligente.md) para más detalles.

---

### P: ¿Cómo integro IA con otras herramientas?

**R:**
1. Identifica herramientas a integrar
2. Configura integraciones
3. Automatiza flujos de trabajo
4. Monitorea resultados
5. Optimiza continuamente

Ver [Integraciones con otras herramientas](../integraciones/README.md) para más detalles.

---

### P: ¿Cómo creo dashboards con IA?

**R:**
1. Exporta datos de TIA Portal
2. Importa en Power BI
3. Pide a IA que genere medidas DAX
4. Crea visualizaciones
5. Publica en Power BI Service

Ver [Integración con Power BI](../integraciones/README.md#integración-con-power-bi) para más detalles.

---

### P: ¿Cómo envío notificaciones con IA?

**R:**
1. Configura webhook de Teams
2. Detecta eventos en TIA Portal
3. Pide a IA que genere mensajes
4. Envía notificaciones a Teams
5. Monitorea respuestas

Ver [Integración con Microsoft Teams](../integraciones/README.md#integración-con-microsoft-teams) para más detalles.

---

### P: ¿Cómo controlo versiones con IA?

**R:**
1. Configura Git
2. Exporta bloques como XML
3. Commit en Git
4. Pide a IA que genere mensajes de commit
5. Push a repositorio remoto

Ver [Integración con Git](../integraciones/README.md#integración-con-git) para más detalles.

---

### P: ¿Cómo gestiono tareas con IA?

**R:**
1. Configura Jira
2. Crea issues para cambios
3. Pide a IA que genere descripciones
4. Actualiza issues con progreso
5. Cierra issues cuando completado

Ver [Integración con Jira](../integraciones/README.md#integración-con-jira) para más detalles.

---

### P: ¿Cómo creo documentación con IA?

**R:**
1. Configura Confluence
2. Pide a IA que genere documentación
3. Formatea contenido
4. Añade diagramas y tablas
5. Publica en Confluence

Ver [Integración con Confluence](../integraciones/README.md#integración-con-confluence) para más detalles.

---

## 📊 Resumen de troubleshooting

| Categoría | Errores | Soluciones |
|-----------|---------|------------|
| **Errores comunes** | 5 | 5 |
| **Permisos de Openness** | 2 | 4 |
| **Problemas de conexión** | 2 | 4 |
| **Errores de compilación** | 2 | 3 |
| **FAQ** | 20 | 20 |

---

## 💡 Consejos finales

1. **Lee el mensaje de error** — Identifica la causa
2. **Verifica la configuración** — Asegura que todo está correcto
3. **Prueba en simulación** — Antes de producción
4. **Pide ayuda a IA** — Si no puedes solucionar
5. **Documenta soluciones** — Para futuras referencias

---

## 📚 Recursos adicionales

- [Tutoriales](../tutoriales/) — Aprende a usar IA + TIA Portal
- [Casos de uso](../casos-de-uso/) — Ejemplos reales
- [Guía de prompts](../prompts/) — Prompts efectivos
- [Best practices](../best-practices/) — Mejores prácticas
