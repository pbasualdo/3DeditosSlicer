# 📐 3DEDITOS // Reglas de Ingeniería DfAM & Manual de Taller Validado
**Especialista:** 3DEDITOS (3D CAD & Additive Manufacturing Specialist)  
**Hardware de Referencia:** Snapmaker U1 (High-Flow Toolchanger & Enclosed Chamber)  
**Laminador Base:** Snapmaker Orca V2.4.1 Portable  

Este documento compila **exclusivamente el conocimiento técnico verificado por la física de polímeros y la ingeniería de fabricación aditiva**, descartando mitos, simplificaciones de redes sociales y malas prácticas de taller.

---

## 🧪 1. Adhesión Superficial y Limpieza de Láminas PEI

### ✅ La Regla Validada
* **El lavado profundo con surfactantes aniónicos es el único método que elimina lípidos:** Las grasas de la piel humana no se evaporan con alcohol. El jabón neutro disuelve y atrapa los aceites en micelas hidrosolubles que el chorro de agua tibia arrastra físicamente.
* **El alcohol isopropílico (IPA $\ge 99\%$) es solo para mantenimiento entre capas:** Sirve para quitar polvo estático y residuos ligeros de PLA, pero si la chapa ya tiene grasa acumulada, frotar con un paño solo redistribuye una fina película oleosa.

### ❌ Lo Descartado (Mitos y Errores)
* **Detergentes con loción hidratante o fragancias:** Detergentes comerciales con glicerina, aloe vera o protectores de piel dejan una película grasa sobre el PEI que anula la adhesión.
* **Tocar la superficie tras el secado:** El contacto con la yema de los dedos recontamina la chapa de inmediato.

> **Procedimiento Estándar:** Lavar con agua tibia y detergente concentrado básico neutro sin cremas. Secar al aire o con papel tissue limpio sin apoyar las manos.

---

## 📐 2. Hidrodinámica y Geometría de la Primera Capa

### ✅ La Regla Validada
* **Ancho de línea al 125%–135% del diámetro de boquilla:** En una boquilla estándar de 0.40 mm, forzar un ancho de extrusión de **0.50 mm a 0.52 mm** a una velocidad $\le 40$ mm/s.
* **Acción de espátula térmica:** El anillo exterior plano de la boquilla (*nozzle flat*) presiona hidrodinámicamente el polímero fundido contra los micro-valles del PEI texturado, maximizando el área de contacto íntimo.

### ❌ Lo Descartado
* **Superar el 150% del diámetro ($> 0.60$ mm en boquilla 0.4 mm):** Genera contrapresión excesiva en el extrusor, redondeo indeseado de esquinas vivas por *die-swell* descontrolado y acumulación de rebabas en el exterior del cabezal.

---

## ⚡ 3. Control Reológico: Límite por Flujo Volumétrico Real

### ✅ La Regla Validada
* **La velocidad lineal (mm/s) no manda; manda el caudal volumétrico ($mm^3/s$):**
  $$Q = v \cdot w \cdot h \le Q_{\text{máx}}$$
  El hotend tiene una potencia térmica finita de transferencia por conducción. Cada polímero debe tener configurado su techo reológico en el slicer para que las velocidades se calculen solas de forma segura.

### 📊 Techos de Flujo Volumétrico Calibrados para la Snapmaker U1
| Polímero | $Q_{\text{máx}}$ Seguro | Motivo Técnico |
| :--- | :---: | :--- |
| **TPU 90A / 95A** | **3.5 – 5.0 $mm^3/s$** | Evita pandeo del filamento en la garganta y atascos. |
| **PETG / PET-CF** | **11.0 – 14.0 $mm^3/s$** | Viscosidad media; previene delaminación por sub-fusión. |
| **PLA Estándar** | **14.0 – 16.0 $mm^3/s$** | Límite de transferencia de calor en bloque convencional. |
| **SnapSpeed / PLA High-Flow** | **24.0 – 30.0 $mm^3/s$** | Formulación de bajo peso molecular apta para hotend U1. |

---

## 🌲 4. Árbol de Decisión de Soportes: Cuándo Tree y Cuándo Rectilíneo

### ✅ La Regla Validada
* **Tree Supports (Orgánicos):** Mandatorio para figuras complejas, salientes puntuales y caras orgánicas. Ahorran un 40%–60% de material, reducen el tiempo y dejan puntos de contacto mínimos fáciles de remover.
* **Soporte Rectilíneo Tradicional con Interfaz Continua:** Mandatorio para **voladizos horizontales planos extensos** (techos de carcasas, montajes mecánicos, bridas). Proporciona un puente rígido que no oscila con la inercia del cabezal.

### ❌ Lo Descartado
* **"Usar Tree Supports para absolutamente todo":** En techos planos grandes, las ramas oscilan y flexionan, provocando que la primera capa del voladizo se descuelgue y quede rugosa.

---

## ✂️ 5. Costuras Invisibles: Requisitos del *Scarf Joint*

### ✅ La Regla Validada
* **Rampa en bisel gradual:** La unión en bisel (*Scarf Joint*) solapa el final de la capa en cuña descendente con el inicio en cuña ascendente, erradicando el típico bulto o zanja vertical.

### ❌ Lo Descartado
* **"Scarf Joint funciona mágicamente en cualquier impresora":** Si el filamento no está calibrado en **Pressure Advance (Linear Advance)** o tiene humedad residual, la rampa sufre sobre-extrusión o micro-burbujas en el solape, dejando una línea brillante o rugosa peor que la costura tradicional.

---

## 💧 6. Termodinámica de Polímeros: La Deshidratación Obligatoria

### ✅ La Regla Validada
* **Las bobinas selladas al vacío de fábrica vienen húmedas:** La extrusión industrial del filamento se enfría en piscinas de agua. La bolsita de gel de sílice solo seca el aire dentro de la bolsa, no extrae el agua ya absorbida en el interior molecular del plástico.
* **Hidrólisis térmica dentro del hotend:** En polímeros hidrófilos (**Nylon/PA, PETG, TPU**), el agua a más de 220°C produce microexplosiones (*popping* / *stringing*) y **rompe las cadenas poliméricas**, reduciendo la resistencia mecánica en el eje Z hasta un 50%.

> **Regla de Taller:** Secar térmicamente en deshidratador / secador activo antes de imprimir:
> * **TPU:** 55 °C durante 6 a 8 horas.
> * **PETG:** 65 °C durante 6 horas.
> * **PA / PA-CF:** 75–80 °C durante 10 a 12 horas.

---

## 🔬 7. Desgaste de Boquillas y Abrasivos Ocultos

### ✅ La Regla Validada
* **El PLA Matte contiene cargas minerales abrasivas:** Para eliminar el brillo especular, los fabricantes añaden **carbonato de calcio ($\text{CaCO}_3$) o talco** (dureza Mohs ~3.0, igual a la del latón).
* **Escala de Desgaste:**
  * Imprimir 1 o 2 carretes de PLA Matte en boquilla de latón produce un desgaste despreciable.
  * Imprimir más de 5 kg en granjas de producción desgasta y ensancha el orificio de latón de 0.40 mm a 0.45+ mm.
  * Los filamentos con **fibra de carbono, fibra de vidrio o partículas fosforescentes** destruyen una boquilla de latón en menos de 500 gramos.

> **Regla de Taller:** Para piezas continuas de PLA Matte o cualquier compuesto técnico, utilizar exclusivamente **boquillas de acero endurecido (*hardened steel*)**.

