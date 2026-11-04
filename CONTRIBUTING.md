# 🤝 Contributing to 3DeditosSlicer

Welcome to **3DeditosSlicer**! This project is an open-source, community-driven slicing and DfAM suite for the **Snapmaker U1** CoreXY Toolchanger, autonomously co-maintained by **3DEDITOS** (AI Additive Manufacturing Specialist) with final **Human-in-the-Loop** review by [@pbasualdo](https://github.com/pbasualdo).

We warmly welcome contributions from makers, engineers, and developers worldwide!

---

## 🤖 How Contributions Work (Agent + Human Review)

1. **You submit a Pull Request or Issue.**
2. **3DEDITOS conducts automated technical review:**
   * Validates JSON schema syntax and inheritance.
   * Runs safety checks (temperature limits, volumetric flow, nozzle constraints).
   * Verifies mechanical tolerance conventions ($0.2\text{ mm}$ fit).
3. **Human-in-the-Loop Approval:**
   * [@pbasualdo](https://github.com/pbasualdo) reviews the agent's findings and executes the final merge to `main`.

---

## 🎯 Contribution Areas

We actively seek community contributions in:

### 1. New Material & Filament Profiles
* Tested presets for popular third-party filaments (Polymaker, Sunlu, eSun, Overture, FormFutura, etc.).
* Novel multi-material combinations adhering to the chemical affinity matrix (`PETG + TPU`, `PLA + PETG` support, etc.).

### 2. Multi-Platform Support
* Extending [`3deditos_cli.py`](file:///f:/Development/OfflineRepos/3d/3DeditosSlicer/3deditos_cli.py) and bootstrap scripts to support **Linux (AppImage / Flatpak)** and **macOS (Universal DMG)**.

### 3. DfAM Heuristics & Automation
* Enhancing geometric inspection routines (e.g., minimum wall thickness detection, overhang classification, elephant-foot warnings).

### 4. Localization & Documentation
* Translating guides, tooltips, and presets into English, Spanish, German, French, and Chinese.

---

## 🛑 Inviolable Hardware Safety Guardrails (Zero-Tolerance)

To protect all physical 3D printers and prevent hardware damage, **every PR must respect these hard limits**:

1. **Zero Tampering with Machine Kinematics:**
   * Never modify toolhead parking coordinates, SnapSwap™ pickup sequences, or Klipper macros (`PRINT_START`, `SM_PRINT_CHECK_SWITCH_EXTRUDER`).
   * Machine profiles must inherit strictly from official Snapmaker U1 definitions.
2. **Firmware Temperature Caps:**
   * Maximum nozzle temperature: **`300 °C`**.
   * Maximum heated bed temperature: **`100 °C`**.
3. **Uniform Nozzle Rule:**
   * All 4 toolheads must assume identical nozzle diameters (e.g., all 0.4 mm). Mixed nozzle diameters are physically unsupported.
4. **TPU Safety Protocol:**
   * No TPU presets for 0.2 mm nozzles.
   * `Dynamic Flow Calibration` must be disabled for all TPU materials.

---

## 🧪 Testing Your Contribution Locally

Before submitting a Pull Request, validate your profile or script:

```powershell
# 1. Run profile validation
python validate_profile.py profiles/process/your_new_profile.json

# 2. Verify presets list
python 3deditos_cli.py --presets
```

---

## 📜 Pull Request Process

1. Fork the repository.
2. Create a feature branch: `git checkout -b feat/new-filament-profile`.
3. Commit your changes: `git commit -m "feat(profiles): add Polymaker PolyTerra PLA preset"`.
4. Push to your fork and submit a Pull Request targeting `main`.
5. 3DEDITOS and [@pbasualdo](https://github.com/pbasualdo) will review your contribution promptly!

Thank you for helping push the boundaries of multi-toolhead 3D printing! 🚀
