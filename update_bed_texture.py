import os

repo_dir = r"F:\Development\OfflineRepos\3d\3DeditosSlicer"
b64_file = os.path.join(repo_dir, "logo_b64.txt")
with open(b64_file, "r") as f:
    b64 = f.read().strip()

# Bed is 270 x 270 mm
# Center is (135, 135)
svg_bed = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="270px" height="270px" viewBox="0 0 270 270" version="1.1">
  <defs>
    <clipPath id="bedLogoClip">
      <circle cx="135" cy="135" r="40"/>
    </clipPath>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="60%" stop-color="#00C1AE" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#00C1AE" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Bed subtle border and origin indicator -->
  <rect x="1" y="1" width="268" height="268" rx="4" fill="none" stroke="#333842" stroke-width="0.8" stroke-dasharray="4,4"/>

  <!-- Center Circular 3DEDITOS Emblem -->
  <circle cx="135" cy="135" r="48" fill="url(#glow)"/>
  <circle cx="135" cy="135" r="42" fill="#12151B" stroke="#00C1AE" stroke-width="1.2"/>
  <image href="data:image/png;base64,{b64}" x="95" y="95" width="80" height="80" clip-path="url(#bedLogoClip)"/>

  <!-- Technical Branding & Tolerances -->
  <text x="135" y="195" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="7" font-weight="800" fill="#E6EDF3" letter-spacing="1.5" text-anchor="middle">3DEDITOS SLICER // SNAPMAKER U1</text>
  <text x="135" y="204" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="5" font-weight="600" fill="#00C1AE" letter-spacing="1" text-anchor="middle">PRECISION TOLERANCE: 0.20 MM &bull; QUAD TOOLHEAD</text>

  <!-- Axes Labels -->
  <text x="8" y="262" font-family="sans-serif" font-size="6" font-weight="bold" fill="#00C1AE">X</text>
  <text x="8" y="14" font-family="sans-serif" font-size="6" font-weight="bold" fill="#38BDF8">Y</text>
</svg>"""

profiles_dir = os.path.join(
    repo_dir,
    "Snapmaker_Orca_Windows_V2.4.1_portable",
    "resources",
    "profiles",
    "Snapmaker",
)

with open(os.path.join(profiles_dir, "Snapmaker U1_texture.svg"), "w", encoding="utf-8") as f:
    f.write(svg_bed)

with open(os.path.join(profiles_dir, "Snapmaker U1_bed.svg"), "w", encoding="utf-8") as f:
    f.write(svg_bed)

# Also check user app data roaming profiles just in case
roaming_profiles = r"C:\Users\p-e-b\AppData\Roaming\Snapmaker_Orca\resources\profiles\Snapmaker"
if os.path.exists(roaming_profiles):
    with open(os.path.join(roaming_profiles, "Snapmaker U1_texture.svg"), "w", encoding="utf-8") as f:
        f.write(svg_bed)
    with open(os.path.join(roaming_profiles, "Snapmaker U1_bed.svg"), "w", encoding="utf-8") as f:
        f.write(svg_bed)

print("Updated Snapmaker U1 bed textures successfully!")
