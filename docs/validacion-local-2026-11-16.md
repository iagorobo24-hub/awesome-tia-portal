# Awesome TIA Portal — Validación local y conciliación pendiente

**Fecha:** 2026-11-16
**Alcance:** documentación, inventario, validadores y diagnóstico de CI; **sin abrir TIA Portal ni PLCSIM**.
**Estado:** avance local sin commit, sin merge y sin publicación.

## Identidad Git y reconciliación

- Worktree local: `feat/github-research-templates` @ `8c11821`.
- Referencia `origin/main`: `d5cefea` (publicación curada del 13/11/2026).
- Divergencia: 2 commits solo locales y 1 solo en `origin/main`. No hay integración entre ambas historias.
- `docs/plan-evolucion-v0.2.0.md` permanece sin seguimiento local y **difiere** del archivo existente en `origin/main`. Preservar ambas versiones antes de reconciliar.
- `docs/validacion-matriz-estado.md` sigue sin seguimiento local, pero su contenido coincide exactamente con `origin/main`.
- **Riesgo de regresión documental en un merge:** `docs/research/analisis.json` ocupa **4.348.345 bytes** en `HEAD` local y **43.328 bytes** en `origin/main`; la rama pública contiene una versión reducida. No reintroducir automáticamente los datos brutos descartados por la publicación.
- No se ha modificado el trabajo concurrente de los worktrees `T-IA-Portal` o CLI.

## Inventario comprobado

- 26 recursos distribuidos en 5 UDT, 11 FB/FC, 3 OB, 5 HMI y 2 plantillas.
- Frontmatter: **2 `verified`**, **24 `documented`**.
- `FB_AlarmLatch` y `FC_Escalado` tienen fuentes SCL, XML y evidencias previas de compilación V20 y ejecución PLCSIM; **no se ha repetido la reimportación desde cero** en esta sesión.
- Otros 24 recursos: fichas de diseño, no artefactos importables certificados.

## Comprobaciones locales ejecutadas

| Control | Resultado |
|---|---|
| `scripts/validate-resources.sh` | PASS; 2 carpetas con XML, 24 solo documentadas, 0 errores |
| `scripts/generate_catalog.py --check` | PASS |
| `scripts/check-local-links.py` | PASS; enlaces internos sin roturas |
| `scripts/validate-xml.py` | PASS; 3 XML y 4 SCL revisados estáticamente |
| `scripts/check-resource-index.py` | PASS; 26 recursos en README y matriz |
| Prueba negativa aislada del nuevo validador | PASS; recurso sintético omitido detectado en ambos índices, exit 1 |
| `docs/img/estados.svg` | XML válido |
| `git diff --check` | PASS |

Se corrigieron cifras y afirmaciones obsoletas en el README, FAQ, hoja de ruta, matriz, changelog y SVG de estados. Se añadió un validador de cobertura de índices y una nueva comprobación al workflow estructural, activable al cambiar README o matriz.

## CI pública, evidencias y bloqueos

- GitHub Actions [Validar Recursos #43703222265](https://github.com/iagorobo24-hub/awesome-tia-portal/actions/runs/43703222265), 15/11/2026: job **validate PASS**; job **secretos FAIL**.
- Se descargó y examinó **privadamente** el SARIF de ese run: **6 hallazgos** de regla `generic-api-key`, uno en `bloques-de-funcion/fb-alarm-latch/informe-ejecucion-2026-10-19.md` y cinco en `ia-tia-portal/plantillas/README.md`. No se copiaron valores detectados a este informe.
- **Clasificación completada con evidencia histórica:** cinco hallazgos en commit `3b1678c` corresponden al mismo valor sintético de ejemplo de las plantillas MCP; el sexto (commit `223f1e5`) corresponde a un literal de modo de acceso al simulador, no a una credencial. Son seis falsos positivos identificados; no se ha demostrado exposición de secretos reales en estos hallazgos.
- Se añadió `.gitleaksignore` con **seis fingerprints exactos** del log del run, sin desactivar `generic-api-key` ni ignorar rutas. Gitleaks **8.24.3** original, ZIP descargado y SHA-256 verificado: sobre el `main` publicado **6 hallazgos sin la exclusión (exit 2) y 0 con ella (exit 0)**. Auditoría ejecutada en clon local aislado; no equivale a CI remota.
- Workflow de enlaces externos del 15/11/2026: PASS.
- No se ejecutó CI remota sobre nuestros cambios locales, que siguen sin commit. Este hecho no invalida las pruebas locales, pero los hallazgos reales de seguridad deben resolverse.

## Seguimiento posterior de esta misma fecha

- Se creó el worktree de cierre `feat/awesome-v0.2.0-closure` a partir de `origin/main`, aplicando el parche selectivo sin perder el JSON reducido publicado; esta acta inicial sigue siendo evidencia de la reconciliación anterior.
- Se han importado y compilado ambos XML **desde cero en un proyecto TIA V20 nuevo** (0 errores/0 avisos), con [evidencia del 16/11](evidencias/validacion-importacion-tia-v20-2026-11-16.json). La afirmación anterior de «reimportación no repetida» describe solo el corte inicial de este documento.
- Se corrigieron 21 fallos reales de estilo del plan: `markdownlint-cli2` v0.23.2, 0 hallazgos. Dos nuevos falsos positivos producidos por literales documentales se corrigieron por redacción; en la candidata los escaneos Gitleaks histórico y `--no-git` pasaron con 0 hallazgos. [Acta candidata actualizada](aceptacion-v0.2.0-2026-11-16.md).

## Siguientes controles

1. Conservar la exclusión por huella exacta y revisar cualquier nuevo hallazgo de Gitleaks; la futura ejecución remota sigue sin comprobarse.
2. El candidato local aislado parte de `origin/main` (`d5cefea`) y aplica 10 archivos nuevos/modificados, preservando el plan público y `docs/research/analisis.json` reducido. Validar el parche reproducible antes de autorizar integración al Git real; la rama existente sigue intacta.
3. Reproducir importación limpia de los XML y casos de borde V20/PLCSIM en fixture aislado **solo cuando Siemens esté libre y el destino virtual se haya comprobado**.
4. Validar el parche reproducible contra `main`, conservar evidencias y revisar el diff final. No ejecutar merge, push ni publicación sin autorización.
