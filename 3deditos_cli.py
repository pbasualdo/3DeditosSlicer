#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
3DeditosSlicer // CLI & Automation Suite for Snapmaker U1
Especialista: 3DEDITOS (3D CAD & Additive Manufacturing Specialist)
===============================================================================
Automatización, validación geométrica, empaquetado de proyectos 3MF multimaterial
y lanzamiento del motor oficial Snapmaker Orca V2.4.1.
"""

import sys
import os
import argparse
import subprocess
import json
import struct
from pathlib import Path

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent
ENGINE_DIR = BASE_DIR / "Snapmaker_Orca_Windows_V2.4.1_portable"
ENGINE_EXE = ENGINE_DIR / "snapmaker-orca.exe"
PROFILES_DIR = ENGINE_DIR / "resources" / "profiles" / "Snapmaker"

def banner():
    print(r"""
  ==================================================================
   3 D E D I T O S   S L I C E R  //  S N A P M A K E R   U 1
   Engineering & DfAM Slicing Automation Suite
  ==================================================================
    """)

def check_engine():
    if not ENGINE_EXE.exists():
        print(f"[ERROR] No se encontró el binario del motor en: {ENGINE_EXE}")
        sys.exit(1)

def inspect_stl(stl_path):
    """Inspecciona un archivo STL binario o ASCII para obtener dimensiones y facetas."""
    p = Path(stl_path)
    if not p.exists():
        print(f"[ERROR] Archivo no encontrado: {stl_path}")
        return None

    # Invocar el motor Orca con --info para inspección geométrica de alta precisión
    check_engine()
    res = subprocess.run([str(ENGINE_EXE), "--info", str(p)], capture_output=True, text=True)
    out = res.stdout.strip()
    
    # Filtrar solo el bloque de información del STL
    lines = out.splitlines()
    info_lines = []
    capture = False
    for line in lines:
        if line.startswith(f"[{p.name}]"):
            capture = True
        if capture:
            info_lines.append(line)
            
    if info_lines:
        print("\n" + "\n".join(info_lines))
    else:
        print(out)
    return res.returncode == 0

def list_presets():
    """Lista todos los perfiles de proceso 3DEDITOS registrados."""
    process_dir = PROFILES_DIR / "process"
    if not process_dir.exists():
        print(f"[WARN] No se encontró el directorio de perfiles: {process_dir}")
        return

    print("\n📦 PERFILES DE PROCESO OFICIALES '3DEDITOS' DISPONIBLES:")
    print("=" * 75)
    for f in sorted(process_dir.glob("*3Deditos*.json")):
        try:
            with open(f, "r", encoding="utf-8") as jf:
                data = json.load(jf)
                name = data.get("name", f.stem)
                desc = data.get("description", "Sin descripción")
                print(f" • {name}")
                print(f"   Desc: {desc}")
                print("-" * 75)
        except Exception as e:
            print(f" • {f.name} (Error al leer JSON: {e})")

def launch_gui(file_path=None):
    """Lanza la interfaz gráfica de 3DeditosSlicer con el archivo cargado."""
    check_engine()
    cmd = [str(ENGINE_EXE)]
    if file_path:
        p = Path(file_path).resolve()
        if p.exists():
            cmd.append(str(p))
            print(f"[3DEDITOS] Abriendo en entorno visual: {p.name}")
        else:
            print(f"[WARN] Archivo no encontrado: {file_path}. Abriendo lienzo vacío...")
    else:
        print("[3DEDITOS] Abriendo entorno visual de 3DeditosSlicer...")

    # Lanzar desacoplado en Windows
    subprocess.Popen(cmd, cwd=str(ENGINE_DIR))
    print("[3DEDITOS] Slicer iniciado exitosamente.")

def main():
    banner()
    parser = argparse.ArgumentParser(
        description="3DeditosSlicer // Herramienta de automatización y slicing para Snapmaker U1."
    )
    parser.add_argument("input", nargs="?", help="Ruta a modelo STL, 3MF o ensamblado")
    parser.add_argument("--info", action="store_true", help="Inspeccionar geometría, volumen y facetas del modelo")
    parser.add_argument("--gui", action="store_true", help="Abrir en el entorno gráfico Snapmaker Orca")
    parser.add_argument("--presets", action="store_true", help="Listar los perfiles de proceso de ingeniería 3DEDITOS")

    args = parser.parse_args()

    if args.presets:
        list_presets()
        return

    if args.info:
        if not args.input:
            print("[ERROR] Debe especificar un archivo STL o 3MF para inspeccionar.")
            sys.exit(1)
        inspect_stl(args.input)
        return

    if args.gui or args.input:
        launch_gui(args.input)
        return

    # Si no se pasan argumentos, mostrar ayuda y perfiles
    parser.print_help()
    list_presets()

if __name__ == "__main__":
    main()
