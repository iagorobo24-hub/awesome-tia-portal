# Tutorial 1: Tu primer proyecto con IA + TIA Portal

> **⏱️ Tiempo estimado**: 45 minutos
> **🎯 Dificultad**: ⭐ (Principiante)
> **📋 Prerrequisitos**: Ninguno

---

## 🎯 Objetivo

Configurar tu entorno y generar tu primer bloque PLC con Inteligencia Artificial. Al final de este tutorial tendrás:

- ✅ Un MCP Server configurado y funcionando
- ✅ Claude Desktop o VS Code Copilot conectado
- ✅ Un FC de escalado generado por IA
- ✅ El bloque importado y compilado en TIA Portal

---

## 📋 Prerrequisitos

Antes de empezar, asegúrate de tener:

- **Windows 10/11** — TIA Portal solo funciona en Windows
- **Siemens TIA Portal V17+** instalado
- **Usuario en grupo `Siemens TIA Openness`**
- **Claude Desktop** o **VS Code con GitHub Copilot**

---

## 🚀 Paso 1: Elegir tu herramienta

### Opción A: Claude Desktop (recomendado para principiantes)

**Ventajas:**
- ✅ Interfaz de chat simple
- ✅ No requiere VS Code
- ✅ Ideal para probar rápidamente

### Opción B: VS Code + GitHub Copilot

**Ventajas:**
- ✅ Integración con tu editor de código
- ✅ Mejor para desarrollo continuo
- ✅ Más opciones de configuración

> **En este tutorial usaremos Claude Desktop** por su simplicidad. Si prefieres VS Code, consulta el [Tutorial 1B](./01-primeros-pasos-vscode.md).

---

## 🔧 Paso 2: Instalar el MCP Server

### Descargar tiaportal-mcp

1. Ve al repositorio: [heilingbrunner/tiaportal-mcp](https://github.com/heilingbrunner/tiaportal-mcp)
2. Descarga la última release desde la sección [Releases](https://github.com/heilingbrunner/tiaportal-mcp/releases)
3. Descomprime el archivo en una carpeta, por ejemplo: `C:\TIA-MCP\`

### Verificar instalación

Abre una terminal y ejecuta:

```powershell
cd C:\TIA-MCP
.\TiaMcpServer.exe --help
```

Deberías ver la ayuda del programa.

---

## ⚙️ Paso 3: Configurar Claude Desktop

### 3.1 Crear el archivo de configuración

1. Abre el explorador de archivos
2. Navega a: `C:\Users\<tu-usuario>\AppData\Roaming\Claude\`
3. Si no existe, crea la carpeta `Claude`
4. Crea un archivo llamado `claude_desktop_config.json`

### 3.2 Añadir la configuración del MCP Server

Edita `claude_desktop_config.json` y añade:

```json
{
  "mcpServers": {
    "tia-portal": {
      "command": "C:\\TIA-MCP\\TiaMcpServer.exe",
      "args": [],
      "env": {}
    }
  }
}
```

> **Nota**: Ajusta la ruta `C:\\TIA-MCP\\TiaMcpServer.exe` a donde hayas descomprimido el archivo.

### 3.3 Reiniciar Claude Desktop

Cierra y vuelve a abrir Claude Desktop para que cargue la nueva configuración.

---

## 🧪 Paso 4: Verificar la conexión

### 4.1 Abrir TIA Portal

1. Abre TIA Portal
2. Crea un nuevo proyecto o abre uno existente
3. Asegúrate de que el proyecto está guardado

### 4.2 Probar la conexión en Claude Desktop

En Claude Desktop, escribe:

```
¿Qué proyectos de TIA Portal tengo abiertos?
```

Claude debería responder con información sobre tu proyecto. Si ves un error, revisa la sección [Troubleshooting](#troubleshooting).

---

## 🎨 Paso 5: Generar tu primer bloque

### 5.1 Pedir a Claude que genere un FC

En Claude Desktop, escribe:

```
Genera un FC de escalado lineal con las siguientes características:

- Nombre: FC_Escalado_Temperatura
- Descripción: Escala una entrada analógica de temperatura
- Entrada: Raw (INT, 0-27648)
- Salida: Temperatura (REAL, -50.0 a 150.0 °C)
- Lenguaje: SCL

El FC debe:
1. Recibir el valor raw de la entrada analógica
2. Escalarlo linealmente al rango de temperatura
3. Devolver el valor escalado
4. Manejar valores fuera de rango (clipping)
```

### 5.2 Revisar el código generado

Claude generará código SCL. Revisa que:

- ✅ El nombre del bloque es correcto
- ✅ Las variables tienen nombres descriptivos
- ✅ La lógica de escalado es correcta
- ✅ Hay manejo de errores

Si algo no te gusta, pide a Claude que lo modifique:

```
El código está bien, pero añade comentarios explicativos en cada paso
```

---

## 📥 Paso 6: Importar el bloque en TIA Portal

### 6.1 Copiar el código

1. Copia el código SCL generado por Claude
2. Guárdalo en un archivo temporal, por ejemplo: `FC_Escalado_Temperatura.scl`

### 6.2 Importar en TIA Portal

1. En TIA Portal, ve a tu PLC
2. Haz clic derecho en "Bloques de programa"
3. Selecciona "Añadir nuevo bloque"
4. Elige "FC" (Function)
5. Nombre: `FC_Escalado_Temperatura`
6. Lenguaje: SCL
7. Clic en "Añadir"

### 6.3 Pegar el código

1. Abre el bloque recién creado
2. Borra el código por defecto
3. Pega el código generado por Claude
4. Guarda el bloque (Ctrl+S)

---

## ✅ Paso 7: Compilar y verificar

### 7.1 Compilar el bloque

1. Haz clic derecho en el bloque
2. Selecciona "Compilar"
3. Verifica que no haya errores

### 7.2 Probar el bloque

1. Crea una tabla de variables para probar
2. Añade una variable de entrada (raw) y una de salida (temperatura)
3. Simula diferentes valores de entrada
4. Verifica que la salida es correcta

**Ejemplo de prueba:**

| Raw (INT) | Temperatura esperada (°C) |
|-----------|---------------------------|
| 0         | -50.0                     |
| 13824     | 50.0                      |
| 27648     | 150.0                     |

---

## 🎉 ¡Felicidades!

Has generado tu primer bloque PLC con IA. Ahora puedes:

- ✅ Usar este bloque en tu proyecto
- ✅ Modificarlo según tus necesidades
- ✅ Generar más bloques con IA
- ✅ Continuar con el [Tutorial 2](./02-generar-bloque-scl.md)

---

## 📚 Qué has aprendido

En este tutorial has aprendido:

1. ✅ Cómo instalar y configurar un MCP Server
2. ✅ Cómo conectar Claude Desktop con TIA Portal
3. ✅ Cómo generar código PLC con IA
4. ✅ Cómo importar y compilar bloques en TIA Portal
5. ✅ Cómo probar bloques generados por IA

---

## 🔄 Próximos pasos

Ahora que ya has generado tu primer bloque, puedes:

- **Tutorial 2**: Generar un FB de control complejo
- **Tutorial 3**: Documentar tu proyecto con IA
- **Guía de prompts**: Aprender a escribir mejores prompts
- **Casos de uso**: Ver ejemplos reales de aplicación

---

## 🆘 Troubleshooting

### Error: "No se puede conectar a TIA Portal"

**Causa**: TIA Portal no está abierto o el proyecto no está guardado.

**Solución**:
1. Abre TIA Portal
2. Abre o crea un proyecto
3. Guarda el proyecto
4. Vuelve a intentar la conexión

### Error: "Usuario no en grupo TIA Openness"

**Causa**: Tu usuario de Windows no tiene permisos para usar la API Openness.

**Solución**:
1. Abre "Usuarios y grupos locales"
2. Busca el grupo "Siemens TIA Openness"
3. Añade tu usuario al grupo
4. Reinicia el equipo

### Error: "No se encuentra TiaMcpServer.exe"

**Causa**: La ruta en el archivo de configuración es incorrecta.

**Solución**:
1. Verifica que el archivo existe en la ruta especificada
2. Ajusta la ruta en `claude_desktop_config.json`
3. Reinicia Claude Desktop

### El código generado tiene errores de compilación

**Causa**: El código generado por IA puede tener errores.

**Solución**:
1. Revisa los errores de compilación
2. Pide a Claude que corrija el código
3. Modifica manualmente si es necesario

---

## 💡 Consejos adicionales

1. **Sé específico en tus prompts** — Cuanto más detallado sea tu prompt, mejor será el código generado
2. **Revisa siempre el código** — La IA puede cometer errores, siempre verifica
3. **Itera si es necesario** — Si el código no es perfecto, pide mejoras
4. **Guarda tus prompts** — Crea una librería de prompts útiles para reutilizar

---

## 📖 Recursos adicionales

- [Guía de prompts efectivos](../prompts/prompts-generacion-bloques.md)
- [Troubleshooting completo](../troubleshooting/errores-comunes.md)
- [FAQ](../troubleshooting/faq.md)

---

## 🏆 Badge de completado

¡Has completado el Tutorial 1! 🥉

**Badge obtenido**: 🥉 **Principiante en IA + TIA Portal**

Continúa con el [Tutorial 2: Generar un FB de control](./02-generar-bloque-scl.md) para obtener el badge de Intermedio.
