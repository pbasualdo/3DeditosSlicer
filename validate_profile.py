#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
3DeditosSlicer // Automated Profile Safety Validator
Especialista: 3DEDITOS (3D CAD & Additive Manufacturing Specialist)
===============================================================================
Valida sintaxis JSON, compatibilidad con Snapmaker U1 y límites estrictos
de seguridad física de hardware antes de integrar perfiles a la suite.
"""

import sys
import json
from pathlib import Path

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

MAX_NOZZLE_TEMP = 300.0
MAX_BED_TEMP = 100.0

def validate_profile_file(filepath):
    p = Path(filepath)
    if not p.exists():
        print(f"[FAIL] Archivo no encontrado: {filepath}")
        return False

    print(f"🔍 Validando perfil: {p.name} ...")
    try:
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"[FAIL] Error de sintaxis JSON: {e}")
        return False

    errors = []
    warnings = []

    # 1. Campos requeridos
    req_fields = ["type", "name", "inherits", "setting_id"]
    for field in req_fields:
        if field not in data:
            errors.append(f"Falta el campo obligatorio: '{field}'")

    prof_type = data.get("type", "")
    if prof_type not in ["process", "filament", "machine"]:
        errors.append(f"Tipo de perfil no reconocido: '{prof_type}'. Debe ser process, filament o machine.")

    # 2. Validación de Impresora Compatible
    compat = data.get("compatible_printers", [])
    if isinstance(compat, list) and len(compat) > 0:
        is_u1 = any("Snapmaker U1" in printer for printer in compat)
        if not is_u1:
            warnings.append("El perfil no declara compatibilidad explícita con 'Snapmaker U1'.")

    # 3. Límites Térmicos de Seguridad
    for key, val in data.items():
        if "temperature" in key:
            try:
                # Si es lista o escalar
                temps = val if isinstance(val, list) else [val]
                for t in temps:
                    t_float = float(t)
                    if "bed" in key and t_float > MAX_BED_TEMP:
                        errors.append(f"Temperatura de cama insegura ({t_float} °C > {MAX_BED_TEMP} °C en '{key}')")
                    elif "nozzle" in key and t_float > MAX_NOZZLE_TEMP:
                        errors.append(f"Temperatura de boquilla insegura ({t_float} °C > {MAX_NOZZLE_TEMP} °C en '{key}')")
            except (ValueError, TypeError):
                pass

    # 4. Reglas específicas para TPU
    name_lower = data.get("name", "").lower()
    if "tpu" in name_lower:
        if "0.2 nozzle" in name_lower or "(0.2 nozzle)" in name_lower:
            errors.append("Regla de Oro violada: Prohibido usar TPU con boquilla de 0.2 mm (riesgo crítico de atasco).")
        for printer in compat:
            if "0.2 nozzle" in printer.lower():
                errors.append("Regla de Oro violada: Perfil de TPU asignado a variante de boquilla de 0.2 mm.")

    # Resultado
    if errors:
        print("\n❌ ERRORES DE SEGURIDAD DETECTADOS:")
        for err in errors:
            print(f"  • {err}")
        return False

    if warnings:
        print("\n⚠️ ADVERTENCIAS:")
        for w in warnings:
            print(f"  • {w}")

    print("✅ Perfil 100% válido y seguro para la Snapmaker U1.")
    return True

def main():
    if len(sys.argv) < 2:
        print("Uso: python validate_profile.py <ruta_al_perfil.json> [<perfil2.json> ...]")
        # Validar por defecto los perfiles locales de 3DEDITOS
        base = Path(__file__).resolve().parent / "profiles" / "process"
        files = list(base.glob("*.json"))
        if files:
            print(f"\nAuditando {len(files)} perfiles oficiales locales:")
            all_ok = True
            for f in files:
                ok = validate_profile_file(f)
                if not ok:
                    all_ok = False
            sys.exit(0 if all_ok else 1)
        sys.exit(1)

    all_ok = True
    for arg in sys.argv[1:]:
        ok = validate_profile_file(arg)
        if not ok:
            all_ok = False

    sys.exit(0 if all_ok else 1)

if __name__ == "__main__":
    main()
