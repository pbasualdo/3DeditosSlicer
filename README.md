# 🖨️ 3DeditosSlicer // Suite Oficial de Slicing para Snapmaker U1

> **Especialista:** **3DEDITOS** (Additive Manufacturing & Slicing Specialist)  
> **Motor Base:** [Snapmaker Orca V2.4.1 Portable](https://github.com/Snapmaker/OrcaSlicer) (Upstream OrcaSlicer / AGPLv3)  
> **Hardware Objetivo:** **Snapmaker U1** CoreXY Toolchanger (4 Cabezales Autónomos SnapSwap™).

---

## 🎯 ¿Qué es 3DeditosSlicer?

Es una suite personalizada de slicing y preparación de impresión para la **Snapmaker U1**, mantenida con el apoyo del agente de IA **3DEDITOS**.

> [!NOTE]
> **Alcance del Agente:** Por el momento, **3DEDITOS no modela ni diseña piezas 3D**. Vos traés tus propios modelos (diseñados en tu software CAD preferido o descargados de repositorios como Printables o MakerWorld) y 3DEDITOS se encarga de:
> * Auditar dimensiones, estanqueidad de malla (*manifold*) y volumen.
> * Calibrar tolerancias mecánicas de encastre (holgura predeterminada de `0.2 mm`).
> * Configurar soportes disímiles Zero-Gap (`Top Z = 0.0 mm`) entre **PLA y PETG**.
> * Optimizar la unión interfacial en sobremoldeados rígido + elástico (**PETG + TPU 95A/90A**).
> * Reforzar la estabilidad de la Prime Tower con costillas internas (`rib`).

---

## 🚀 Modos de Uso

### 1. Entorno Gráfico Completo (GUI)
Podés lanzar la interfaz visual completa de dos maneras:
* **Doble clic:** En [`3DeditosSlicer.bat`](3DeditosSlicer.bat).
* **Vía CLI pasando un modelo:**
  ```powershell
  python 3deditos_cli.py modelo.stl
  ```

---

### 2. Inspección Geométrica Headless por Consola
Para auditar dimensiones, volumen, manifold y cantidad de facetas antes de mandar a rebanar:
```powershell
python 3deditos_cli.py --info modelo.stl
```

**Salida instantánea del motor:**
```yaml
[modelo.stl]
size_x = 196.0 mm (Dentro del límite de 270 mm de la cama U1)
size_y = 126.0 mm
size_z = 45.0 mm
number_of_facets = 48
volume = 9,791.99 mm³
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
| **`0.20mm 3Deditos Mechanical`** | Piezas técnicas, carcasas y montajes funcionales. | 4 perímetros de pared, Infill Gyroid 30%, Costura alineada, Compensación de agujeros XY +0.1 mm, Compensación pata de elefante 0.15 mm. |
| **`0.20mm 3Deditos Dissimilar Support PLA+PETG`** | Voladizos críticos y geometrías con soporte que requieren acabado espejo. | Contacto directo Zero-Gap (`Top Z = 0.0 mm`), 3 capas de interfaz continua `Rectilinear Interlaced`, sin luz de despegue. |
| **`0.20mm 3Deditos Overmold PETG+TPU`** | Piezas híbridas rígido + flexible (sellos, juntas estancas, bumpers). | Temperatura de cama optimizada a 70°C, Prime Tower con costillas internas de anclaje, velocidad inicial a 40 mm/s. |
| **`0.20mm 3Deditos Kids Articulated 4Color`** | Juguetes articulados Print-in-Place y figuras multi-material. | Sin soportes en bisagras mecánicas, 6 capas de penetración de color en Z para erradicar sangrado de color (*color bleeding*). |

---

## 🛡️ Filosofía de Seguridad: Human-in-the-Loop (Mandatorio)

En **3DeditosSlicer**, ningún agente de IA tiene autorización para ordenar la extrusión física sin confirmación humana explícita:
1. **El Agente Audita y Calibra:** 3DEDITOS calcula trayectorias, evalúa tolerancias mecánicas (`0.2 mm`), verifica límites de volumen y optimiza la Prime Tower.
2. **El Humano Autoriza y Ejecuta:** Antes de encender los motores y calentar la cama, el operador humano confirma:
   * Cama libre de residuos de impresiones anteriores.
   * Chapa adecuada instalada (PEI texturado o liso con desmoldante).
   * Coincidencia física entre los carretes en las bahías y la asignación digital de cabezales (`T0`..`T3`).
   * Cierre seguro del cerramiento y ventilación despejada.

---

## 🛠️ Estructura del Repositorio

```
3DeditosSlicer/
├── 3DeditosSlicer.bat                         # Lanzador rápido de un clic
├── 3deditos_cli.py                            # Suite de automatización e inspección
├── bootstrap.py                               # Instalador rápido del runtime portable
├── validate_profile.py                        # Validador de perfiles y seguridad
├── sync_snapmaker_updates.py                  # Auditor semanal de novedades
├── CONTRIBUTING.md                            # Guía de contribución para la comunidad
├── README.md                                  # Este manual técnico
└── profiles/process/                          # Presets maestros versionados de 3DEDITOS
```
