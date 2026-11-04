# 🖨️ 3DeditosSlicer // Suite Oficial de Slicing para Snapmaker U1

> **Especialista:** [3DEDITOS](file:///f:/Development/OfflineRepos/.agents/skills/cad-3d-specialist/SKILL.md) (3D CAD & Additive Manufacturing Specialist)  
> **Motor Base:** [Snapmaker Orca V2.4.1 Portable](https://github.com/Snapmaker/OrcaSlicer) (Upstream OrcaSlicer / AGPLv3)  
> **Hardware Objetivo:** **Snapmaker U1** CoreXY Toolchanger (4 Cabezales Autónomos SnapSwap™).

---

## 🎯 ¿Qué es 3DeditosSlicer?

Es la suite personalizada e integrada de slicing del ecosistema **OfflineRepos**, optimizada específicamente para:
1. **Ajuste Mecánico Calibrado:** Tolerancias de diseño a código con holgura predeterminada de `0.2 mm`.
2. **Soportes Disímiles Zero-Gap:** Interfaz de contacto sin luz (`Top Z distance = 0.0 mm`) entre materiales incompatibles (**PLA + PETG**).
3. **Sobremoldeado Bimaterial:** Fusión química y enclavamiento mecánico interfacial (**PETG + TPU 95A/90A**).
4. **Juguetes Articulados Multi-Color:** Mecanismos *print-in-place* de 4 colores con torre de purga reforzada internamente con costillas (`rib`).
5. **Automatización e Inspección por CLI:** Integración directa con scripts generadores de código en Python/OpenSCAD.

---

## 🚀 Modos de Uso

### 1. Entorno Gráfico Completo (GUI)
Podés lanzar la interfaz visual completa de dos maneras:
* **Doble clic:** En [`3DeditosSlicer.bat`](file:///f:/Development/OfflineRepos/3d/3DeditosSlicer/3DeditosSlicer.bat).
* **Vía CLI pasando un modelo:**
  ```powershell
  python 3deditos_cli.py ..\citroen-c3-stereo-10\citroen_c3_stereo_10in_bezel.stl
  ```

---

### 2. Inspección Geométrica Headless por Consola
Para auditar dimensiones, volumen, manifold y cantidad de facetas antes de mandar a fabricar:
```powershell
python 3deditos_cli.py --info ..\citroen-c3-stereo-10\citroen_c3_stereo_10in_bezel.stl
```

**Salida instantánea del motor:**
```yaml
[citroen_c3_stereo_10in_bezel.stl]
size_x = 269.6 mm (Dentro del límite de 270 mm de la cama U1)
size_y = 134.0 mm
size_z = 176.26 mm
number_of_facets = 616
volume = 2,062,663 mm³
```

---

### 3. Listar Perfiles Oficiales 3DEDITOS
```powershell
python 3deditos_cli.py --presets
```

---

## 📦 Perfiles de Proceso de Ingeniería Precalibrados

Todos los perfiles están inyectados nativamente en el motor (`resources/profiles/Snapmaker/process/`):

| Perfil | Aplicación Principal | Parámetros Clave |
| :--- | :--- | :--- |
| **`0.20mm 3Deditos Mechanical`** | Piezas técnicas, carcasas automotrices y montajes funcionales. | 4 perímetros de pared, Infill Gyroid 30%, Costura alineada, Compensación de agujeros XY +0.1 mm, Compensación pata de elefante 0.15 mm. |
| **`0.20mm 3Deditos Dissimilar Support PLA+PETG`** | Voladizos críticos y geometrías con soporte que requieren acabado espejo. | Contacto directo Zero-Gap (`Top Z = 0.0 mm`), 3 capas de interfaz continua `Rectilinear Interlaced`, sin luz de despegue. |
| **`0.20mm 3Deditos Overmold PETG+TPU`** | Piezas híbridas rígido + flexible (sellos, juntas estancas, bumpers). | Temperatura de cama optimizada a 70°C, Prime Tower con costillas internas de anclaje, velocidad inicial a 40 mm/s. |
| **`0.20mm 3Deditos Kids Articulated 4Color`** | Juguetes articulados Print-in-Place y figuras multi-material. | Sin soportes en bisagras mecánicas, 6 capas de penetración de color en Z para erradicar sangrado de color (*color bleeding*). |

---

## 🛡️ Filosofía de Seguridad: Human-in-the-Loop (Mandatorio)

En **3DeditosSlicer**, ningún agente de IA tiene autorización para ordenar la extrusión física sin confirmación humana:
1. **El Agente Diseña, Audita y Calibra:** 3DEDITOS calcula trayectorias, evalúa tolerancias mecánicas (`0.2 mm`), verifica límites de volumen y optimiza la Prime Tower.
2. **El Humano Autoriza y Ejecuta:** Antes de encender los motores y calentar la cama, el operador humano confirma:
   * Cama libre de residuos de impresiones anteriores.
   * Chapa adecuada instalada (PEI texturado o liso con desmoldante).
   * Coincidencia física entre los carretes en las bahías y la asignación digital de cabezales (`T0`..`T3`).
   * Cierre seguro del cerramiento y ventilación despejada.

---

## 🛠️ Estructura del Directorio

```
f:\Development\OfflineRepos\3d\3DeditosSlicer\
├── 3DeditosSlicer.bat                         # Lanzador rápido de un clic
├── 3deditos_cli.py                            # Suite de automatización e inspección
├── README.md                                  # Este manual técnico
└── Snapmaker_Orca_Windows_V2.4.1_portable\    # Motor oficial Snapmaker Orca (Portable)
    ├── snapmaker-orca.exe                     # Binario ejecutable nativo
    └── resources\profiles\Snapmaker\          # Perfiles de impresora, filamentos y presets 3DEDITOS
```
