#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
3DeditosSlicer // Sincronizador de Novedades Wiki & OrcaSlicer
Especialista: 3DEDITOS (3D CAD & Additive Manufacturing Specialist)
===============================================================================
Auditoría semanal automatizada de:
1. Nuevos releases en GitHub: https://github.com/Snapmaker/OrcaSlicer
2. Nuevas guías y perfiles en: https://wiki.snapmaker.com/en/snapmaker_u1
3. Generación de informe técnico consolidado para mantener al día 3DeditosSlicer.
"""

import sys
import os
import json
import urllib.request
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
REPORT_FILE = BASE_DIR / "sync_report.md"
CURRENT_VERSION = "v2.4.1"

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def fetch_latest_github_release():
    url = "https://api.github.com/repos/Snapmaker/OrcaSlicer/releases"
    headers = {"User-Agent": "3DeditosSlicer-WeeklySync/1.0"}
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if data and len(data) > 0:
                return data[0]
    except Exception as e:
        print(f"[ERROR] Error al consultar GitHub Releases: {e}")
    return None

def check_wiki_status():
    """Verifica accesibilidad y fecha de respuesta de la Wiki de Snapmaker."""
    wiki_url = "https://wiki.snapmaker.com/en/snapmaker_u1"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        req = urllib.request.Request(wiki_url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            status = resp.status
            last_modified = resp.headers.get("Last-Modified", "N/A")
            return {"status": status, "url": wiki_url, "last_modified": last_modified}
    except Exception as e:
        return {"status": "error", "error": str(e), "url": wiki_url}

def run_sync():
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("=" * 70)
    print(f"🔄 3DEDITOS // Sincronizador Semanal de Snapmaker U1 ({now_str})")
    print("=" * 70)

    # 1. Auditoría GitHub
    print("\n🔍 1. Consultando últimos releases de Snapmaker Orca...")
    rel = fetch_latest_github_release()
    latest_tag = CURRENT_VERSION
    published_at = "Desconocido"
    release_name = "N/A"
    body_snippet = ""
    is_newer = False

    if rel:
        latest_tag = rel.get("tag_name", CURRENT_VERSION)
        published_at = rel.get("published_at", "N/A")
        release_name = rel.get("name", latest_tag)
        body = rel.get("body", "")
        # Extraer primeras 10 líneas de novedades
        body_lines = [line.strip() for line in body.splitlines() if line.strip()][:12]
        body_snippet = "\n".join(body_lines)

        if latest_tag.lower().strip() != CURRENT_VERSION.lower().strip():
            is_newer = True
            print(f"🚨 ¡NUEVA VERSIÓN DETECTADA! Actual: {CURRENT_VERSION} -> Nueva: {latest_tag}")
        else:
            print(f"✅ Versión instalada ({CURRENT_VERSION}) coincide con el último release oficial ({latest_tag}).")
    else:
        print("⚠️ No se pudo obtener la información de releases de GitHub.")

    # 2. Auditoría Wiki
    print("\n🔍 2. Verificando conectividad con Snapmaker Wiki...")
    wiki_info = check_wiki_status()
    if wiki_info.get("status") == 200:
        print(f"✅ Wiki U1 en línea ({wiki_info['url']}). Código HTTP 200.")
    else:
        print(f"⚠️ Alerta en Wiki U1: {wiki_info}")

    # 3. Generar Informe Técnico Markdown
    report_content = f"""# 📋 3DeditosSlicer // Registro Semanal de Sincronización

> **Fecha de ejecución:** `{now_str}`  
> **Auditor:** [3DEDITOS](file:///f:/Development/OfflineRepos/.agents/skills/cad-3d-specialist/SKILL.md) (3D CAD & Additive Manufacturing Specialist)

---

## 🖨️ 1. Estado de Snapmaker Orca Slicer

* **Versión Local Instalada:** `{CURRENT_VERSION}`
* **Último Release en GitHub:** `{latest_tag}` ({release_name})
* **Fecha de Publicación:** `{published_at}`
* **Estado:** {"🚨 **Actualización requerida**" if is_newer else "🟢 **Al día (Up to Date)**"}
* **Enlace de Descarga:** [GitHub Releases](https://github.com/Snapmaker/OrcaSlicer/releases/latest)

### Resumen de Cambios del Release Oficial:
```text
{body_snippet}
```

---

## 📚 2. Estado de Documentación Oficial (Snapmaker Wiki)

* **URL U1:** [{wiki_info.get('url')}](https://wiki.snapmaker.com/en/snapmaker_u1)
* **Estado del portal:** `HTTP {wiki_info.get('status')}`
* **Última modificación detectada en cabecera:** `{wiki_info.get('last_modified', 'Dinámico')}`
* **Referencias locales integradas:**
  * [snapmaker_u1_cheatsheet.md](file:///f:/Development/OfflineRepos/.agents/skills/cad-3d-specialist/references/snapmaker_u1_cheatsheet.md)
  * [README.md de 3DeditosSlicer](file:///f:/Development/OfflineRepos/3d/3DeditosSlicer/README.md)

---

## 🎯 Acciones para 3DEDITOS:
{"1. Descargar nueva versión portable y migrar perfiles de proceso '3Deditos'." if is_newer else "1. Mantener los 4 perfiles de proceso 3DEDITOS vigentes en V2.4.1.\\n2. Validar periódicamente compatibilidad de G-code con Klipper."}
"""

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report_content)

    print(f"\n📝 Informe técnico actualizado en: {REPORT_FILE}")
    print("=" * 70)

if __name__ == "__main__":
    run_sync()
