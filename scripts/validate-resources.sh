#!/usr/bin/env bash
#
# Valida la estructura de las carpetas de recursos del repositorio.
#
# Reglas (idénticas a las del workflow de CI "Validar Recursos"):
#   - Cada subcarpeta de recurso DEBE tener un README.md (si falta -> error duro).
#   - El archivo .xml es opcional mientras el recurso está "documentado"
#     (pendiente de exportar desde TIA Portal) -> solo genera un aviso.
#
# Uso:
#   bash scripts/validate-resources.sh
#
# Salida:
#   0 -> estructura correcta (puede haber avisos por .xml pendientes)
#   1 -> falta algún README.md obligatorio
set -euo pipefail

# Ubica la raíz del repositorio a partir de la posición del script para poder
# ejecutarlo desde cualquier directorio.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

ERROR=0
MISSING_XML=0

# Carpetas a revisar (mismas rutas que vigila el workflow de CI).
DIRS="bloques-de-funcion tipos-de-datos bloques-de-organizacion hmi plantillas-de-proyecto"

for d in $DIRS; do
  if [ -d "$d" ]; then
    # Subcarpetas de primer nivel (cada una es un recurso).
    for sub in $(find "$d" -maxdepth 1 -mindepth 1 -type d | sort); do
      echo "Revisando recurso: $sub"

      # README.md es OBLIGATORIO. Si falta, error duro y no se evalúa el
      # resto del recurso.
      if [ ! -f "$sub/README.md" ]; then
        echo "❌ Error: Falta README.md en $sub"
        ERROR=1
      else
        # XML es opcional mientras el recurso está en estado "documentado".
        if ! ls "$sub"/*.xml >/dev/null 2>&1; then
          echo "⚠️  Aviso: $sub tiene README pero todavía no .xml (estado 'documentado')"
          MISSING_XML=$((MISSING_XML + 1))
        fi
      fi
    done
  fi
done

if [ "$ERROR" -eq 1 ]; then
  echo ""
  echo "La validación ha fallado. Asegúrate de incluir un README.md en la carpeta de tu recurso."
  exit 1
fi

echo ""
if [ "$MISSING_XML" -gt 0 ]; then
  echo "✅ Estructura correcta. $MISSING_XML recurso(s) sin .xml todavía (estado 'documentado')."
else
  echo "✅ ¡Estructura correcta y todos los recursos tienen .xml!"
fi
