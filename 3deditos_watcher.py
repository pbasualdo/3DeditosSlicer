#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
3DEDITOS // WATCHER & INTELLIGENCE RADAR (Snapmaker U1 & DfAM Ecosystem)
Especialista: 3DEDITOS (3D CAD & Additive Manufacturing Specialist)
===============================================================================
Monitorea continuamente en tiempo real:
1. Upstream de Software: GitHub Releases & Commits (Snapmaker/OrcaSlicer & OrcaSlicer)
2. Guías Técnicas y Trends: Feed de Novedades de 3D Printing Canada (3DPC)
3. Documentación Oficial: Snapmaker Wiki & Firmware Updates
4. Auditoría de Seguridad Local: Validador de Reglas de Oro de 3DeditosSlicer
5. Generación de Radar Ejecutivo en Markdown y JSON para toma de decisiones
"""

import sys
import os
import json
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "docs"
RADAR_MD_FILE = DOCS_DIR / "WATCHER_RADAR.md"
RADAR_JSON_FILE = DOCS_DIR / "watcher_state.json"
CURRENT_ORCA_VERSION = "v2.4.1"

def http_get(url, headers=None, timeout=12):
    """Realiza una petición HTTP GET con User-Agent seguro."""
    h = {"User-Agent": "3Deditos-Watcher/1.0 (Additive Manufacturing Radar)"}
    if headers:
        h.update(headers)
    token = os.environ.get("GITHUB_TOKEN")
    if token and "github.com" in url:
        h["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()
    except Exception as e:
        return 0, str(e).encode("utf-8")

def check_github_repo(repo_name):
    """Consulta último release y últimos commits de un repositorio en GitHub."""
    info = {
        "repo": repo_name,
        "latest_tag": "N/A",
        "release_name": "N/A",
        "published_at": "N/A",
        "recent_commits": [],
        "status": "ok"
    }

    # 1. Release
    rel_url = f"https://api.github.com/repos/{repo_name}/releases/latest"
    st, data = http_get(rel_url)
    if st == 200:
        try:
            j = json.loads(data.decode("utf-8"))
            info["latest_tag"] = j.get("tag_name", "N/A")
            info["release_name"] = j.get("name", info["latest_tag"])
            info["published_at"] = j.get("published_at", "N/A")[:10]
            info["html_url"] = j.get("html_url", "")
        except Exception:
            info["status"] = "parse_error"
    elif st == 403:
        info["status"] = "rate_limited"
    else:
        info["status"] = f"http_{st}"

    # 2. Commits recientes
    commits_url = f"https://api.github.com/repos/{repo_name}/commits?per_page=3"
    st_c, data_c = http_get(commits_url)
    if st_c == 200:
        try:
            jc = json.loads(data_c.decode("utf-8"))
            for c in jc:
                msg = c.get("commit", {}).get("message", "").splitlines()[0]
                date = c.get("commit", {}).get("author", {}).get("date", "")[:10]
                sha = c.get("sha", "")[:7]
                info["recent_commits"].append({"sha": sha, "date": date, "message": msg})
        except Exception:
            pass

    return info

def check_3dpc_trends():
    """Consulta el feed Atom oficial de 3D Printing Canada (guías y novedades)."""
    feed_url = "https://3dprintingcanada.com/blogs/news.atom"
    trends = []
    st, data = http_get(feed_url, timeout=10)
    if st == 200:
        try:
            root = ET.fromstring(data)
            ns = {"atom": "http://www.w3.org/2005/Atom"}
            for e in root.findall("atom:entry", ns)[:5]:
                title_elem = e.find("atom:title", ns)
                pub_elem = e.find("atom:published", ns)
                link_elem = e.find("atom:link", ns)
                title = title_elem.text if title_elem is not None else "Sin título"
                published = pub_elem.text[:10] if pub_elem is not None and pub_elem.text else "N/A"
                link = link_elem.attrib.get("href", "") if link_elem is not None else ""
                trends.append({"title": title, "date": published, "url": link})
        except Exception as e:
            trends.append({"title": f"Error al parsear Atom: {e}", "date": "N/A", "url": ""})
    else:
        trends.append({"title": f"Feed inalcanzable (HTTP {st})", "date": "N/A", "url": ""})

    return trends

def check_snapmaker_wiki():
    """Verifica estado y cabeceras de la Snapmaker Wiki."""
    wiki_url = "https://wiki.snapmaker.com/en/snapmaker_u1"
    st, data = http_get(wiki_url, timeout=10)
    return {
        "url": wiki_url,
        "online": (st == 200),
        "status_code": st
    }

def audit_local_profiles():
    """Verifica que todos los perfiles locales cumplan con las Reglas de Oro."""
    from validate_profile import validate_profile_file
    base = BASE_DIR / "profiles" / "process"
    files = sorted(base.glob("*.json"))
    passed = 0
    failed = 0
    results = []

    for f in files:
        # Redirigir stdout para captura limpia
        ok = validate_profile_file(f)
        results.append({"file": f.name, "valid": ok})
        if ok:
            passed += 1
        else:
            failed += 1

    return {
        "total": len(files),
        "passed": passed,
        "failed": failed,
        "profiles": results
    }

def build_radar_report(data):
    """Genera el informe ejecutivo en Markdown para documentación y alertas."""
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    snap_orca = data["repos"].get("Snapmaker/OrcaSlicer", {})
    main_orca = data["repos"].get("OrcaSlicer/OrcaSlicer", {})
    wiki = data["wiki"]
    trends = data["trends"]
    audit = data["local_audit"]

    md = f"""# 📡 3DEDITOS // Radar de Tendencias Técnicas & Watcher DfAM
> **Última Actualización Automática:** `{now_str}`  
> **Especialista:** 3DEDITOS  
> **Estado de la Suite Local:** **{'🟢 100% OPERATIVA' if audit['failed'] == 0 else '🔴 REGLA DE ORO VIOLADA'}**

Este reporte es generado de forma continua por el Watcher autónomo de `3DeditosSlicer` para mantener los perfiles y técnicas de corte sincronizados con el estado del arte mundial.

---

## 🔍 1. Monitor de Software & Upstream (Slicers)

### A. Snapmaker OrcaSlicer (Upstream Directo de Hardware)
* **Versión Local Desplegada:** `{CURRENT_ORCA_VERSION}`
* **Último Release Oficial en GitHub:** `{snap_orca.get('latest_tag', 'N/A')}` *(Publicado: {snap_orca.get('published_at', 'N/A')})*
* **Estado:** {'✅ Sincronizado al día' if snap_orca.get('latest_tag') == CURRENT_ORCA_VERSION else '🚨 Actualización disponible en upstream'}
* **Últimos Commits en Repositorio:**
"""
    for c in snap_orca.get("recent_commits", []):
        md += f"  * `{c['sha']}` ({c['date']}): {c['message']}\n"

    md += f"""
### B. Mainline OrcaSlicer (Vanguardia Global de Algoritmos)
* **Último Release Global:** `{main_orca.get('latest_tag', 'N/A')}` *(Publicado: {main_orca.get('published_at', 'N/A')})*
* **Últimos Commits de Innovación:**
"""
    for c in main_orca.get("recent_commits", []):
        md += f"  * `{c['sha']}` ({c['date']}): {c['message']}\n"

    md += f"""
---

## 📚 2. Radar de Artículos y Ensayos Técnicos (3D Printing Canada & Partners)

Últimas investigaciones y guías prácticas publicadas:
"""
    for t in trends:
        md += f"* **[{t['title']}]({t['url']})** (`{t['date']}`)\n"

    md += f"""
---

## 🌐 3. Estado de la Documentación Oficial (Snapmaker Wiki U1)
* **URL:** [{wiki['url']}]({wiki['url']})
* **Disponibilidad:** {'🟢 En Línea (HTTP 200)' if wiki['online'] else f'⚠️ Alerta de Red (HTTP {wiki["status_code"]})'}

---

## 🛡️ 4. Auditoría de Seguridad Física Local (Golden Safety Rules)
* **Total de Perfiles Auditados:** `{audit['total']}`
* **Perfiles Válidos y Seguros:** `{audit['passed']} / {audit['total']}`
"""
    for p in audit.get("profiles", []):
        icon = "✅" if p["valid"] else "❌"
        md += f"* {icon} `{p['file']}`\n"

    md += """
---
*Generado automáticamente por `3deditos_watcher.py`.*
"""

    with open(RADAR_MD_FILE, "w", encoding="utf-8") as f:
        f.write(md)

    with open(RADAR_JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def run_watcher(quiet=False):
    if not quiet:
        print("=" * 75)
        print("📡 3DEDITOS // WATCHER & INTELLIGENCE RADAR (Ejecución Activa)")
        print("=" * 75)

    data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "repos": {},
        "trends": [],
        "wiki": {},
        "local_audit": {}
    }

    # 1. Repos
    if not quiet:
        print("🔍 [1/4] Monitoreando repositorios de upstream en GitHub...")
    for repo in ["Snapmaker/OrcaSlicer", "OrcaSlicer/OrcaSlicer"]:
        info = check_github_repo(repo)
        data["repos"][repo] = info
        if not quiet:
            print(f"  • {repo:25} Tag: {info.get('latest_tag', 'N/A')} [{info.get('status')}]")

    # 2. Trends (3DPC Atom)
    if not quiet:
        print("\n📰 [2/4] Rastreador de guías técnicas en vivo (3D Printing Canada)...")
    trends = check_3dpc_trends()
    data["trends"] = trends
    if not quiet:
        for t in trends[:3]:
            print(f"  • [{t['date']}] {t['title'][:65]}")

    # 3. Wiki
    if not quiet:
        print("\n🌐 [3/4] Comprobando disponibilidad de Snapmaker Wiki...")
    wiki_info = check_snapmaker_wiki()
    data["wiki"] = wiki_info
    if not quiet:
        print(f"  • Wiki U1: {'En línea' if wiki_info['online'] else 'Fallo'}")

    # 4. Auditoría Local
    if not quiet:
        print("\n🛡️ [4/4] Ejecutando auditoría de perfiles locales...")
    audit = audit_local_profiles()
    data["local_audit"] = audit
    if not quiet:
        print(f"  • Perfiles aprobados: {audit['passed']}/{audit['total']}")

    # Guardar Radar
    build_radar_report(data)
    if not quiet:
        print(f"\n📝 Reporte Markdown generado en: {RADAR_MD_FILE}")
        print(f"💾 Estado JSON generado en:     {RADAR_JSON_FILE}")
        print("=" * 75)
        print("✅ WATCHER COMPLETADO EXITOSAMENTE.\n")

    return data

def main():
    quiet = "--quiet" in sys.argv
    run_watcher(quiet=quiet)

if __name__ == "__main__":
    main()
