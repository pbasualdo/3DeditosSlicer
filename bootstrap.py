#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
3DeditosSlicer // Bootstrap & Environment Installer
Especialista: 3DEDITOS (3D CAD & Additive Manufacturing Specialist)
===============================================================================
Descarga el runtime portable oficial de Snapmaker Orca y sincroniza los
perfiles de ingeniería de 3DEDITOS.
"""

import sys
import os
import shutil
import urllib.request
import zipfile
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ENGINE_DIR = BASE_DIR / "Snapmaker_Orca_Windows_V2.4.1_portable"
PROFILES_SRC = BASE_DIR / "profiles" / "process"
PORTABLE_URL = "https://github.com/Snapmaker/OrcaSlicer/releases/download/v2.4.1/Snapmaker_Orca_Windows_V2.4.1_portable.zip"
ZIP_PATH = BASE_DIR / "Snapmaker_Orca_Windows_V2.4.1_portable.zip"

def download_engine():
    if ENGINE_DIR.exists() and (ENGINE_DIR / "snapmaker-orca.exe").exists():
        print("[3DEDITOS] Motor Snapmaker Orca ya instalado en:", ENGINE_DIR)
        return

    if not ZIP_PATH.exists():
        print(f"[3DEDITOS] Descargando motor portable desde:\n  {PORTABLE_URL}")
        urllib.request.urlretrieve(PORTABLE_URL, ZIP_PATH)
        print("[3DEDITOS] Descarga completada.")

    print(f"[3DEDITOS] Descomprimiendo en {BASE_DIR}...")
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(BASE_DIR)
    print("[3DEDITOS] Descompresión finalizada con éxito.")

def sync_profiles():
    target_process = ENGINE_DIR / "resources" / "profiles" / "Snapmaker" / "process"
    if not target_process.exists():
        print(f"[ERROR] No se encontró el directorio de perfiles destino: {target_process}")
        return

    print(f"[3DEDITOS] Sincronizando perfiles de ingeniería 3DEDITOS...")
    count = 0
    for profile in PROFILES_SRC.glob("*.json"):
        dest = target_process / profile.name
        shutil.copy2(profile, dest)
        print(f" • Instalado: {profile.name}")
        count += 1
    print(f"[3DEDITOS] Total perfiles inyectados: {count}")

def main():
    print("=" * 70)
    print("🚀 3DEDITOS // BOOTSTRAP SUITE SETUP")
    print("=" * 70)
    download_engine()
    sync_profiles()
    print("\n✅ Entorno de 3DeditosSlicer 100% operativo.")
    print("   Lanzá el entorno con: 3DeditosSlicer.bat")
    print("   O ejecutá la CLI con: python 3deditos_cli.py --help")
    print("=" * 70)

if __name__ == "__main__":
    main()
