#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

errors=0
documented=0
sources=0
exports=0

for category in bloques-de-funcion tipos-de-datos bloques-de-organizacion hmi plantillas-de-proyecto; do
  [[ -d "$category" ]] || continue
  while IFS= read -r -d '' folder; do
    if [[ ! -f "$folder/README.md" ]]; then
      echo "ERROR: falta README.md en $folder"
      errors=$((errors + 1))
      continue
    fi

    if compgen -G "$folder/*.xml" > /dev/null; then
      echo "EXPORTACION PRESENTE: $folder (requiere comprobar importación y compilación)"
      exports=$((exports + 1))
    elif compgen -G "$folder/*.scl" > /dev/null || compgen -G "$folder/*.s7dcl" > /dev/null; then
      echo "FUENTE DISPONIBLE: $folder (no implica XML ni prueba de runtime)"
      sources=$((sources + 1))
    else
      echo "SOLO DOCUMENTADO: $folder"
      documented=$((documented + 1))
    fi
  done < <(find "$category" -mindepth 1 -maxdepth 1 -type d -print0)
done

echo "Resumen: $exports con exportación, $sources con fuente, $documented solo documentados, $errors errores"
[[ "$errors" -eq 0 ]]
