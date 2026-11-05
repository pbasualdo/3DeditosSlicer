import os

repo_dir = r"F:\Development\OfflineRepos\3d\3DeditosSlicer"
b64_file = os.path.join(repo_dir, "logo_b64.txt")
with open(b64_file, "r") as f:
    b64 = f.read().strip()

svg_logo_icon = f"""<svg width="32" height="32" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="circleClip">
      <circle cx="16" cy="16" r="15"/>
    </clipPath>
  </defs>
  <circle cx="16" cy="16" r="15.8" fill="#171717" stroke="#00C1AE" stroke-width="0.8"/>
  <image href="data:image/png;base64,{b64}" x="1" y="1" width="30" height="30" clip-path="url(#circleClip)"/>
</svg>"""

svg_snap_icon = f"""<svg width="140" height="24" viewBox="0 0 140 24" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="logoClip">
      <circle cx="12" cy="12" r="11"/>
    </clipPath>
  </defs>
  <circle cx="12" cy="12" r="11.5" fill="#171717" stroke="#00C1AE" stroke-width="0.8"/>
  <image href="data:image/png;base64,{b64}" x="1" y="1" width="22" height="22" clip-path="url(#logoClip)"/>
  <text x="28" y="16" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="900" fill="#FFFFFF" letter-spacing="1.2">3D<tspan fill="#00C1AE">EDITOS</tspan></text>
</svg>"""

base_dir = os.path.join(
    repo_dir,
    "Snapmaker_Orca_Windows_V2.4.1_portable",
    "resources",
    "web",
    "flutter_web",
    "assets",
    "assets",
    "svgs",
    "login",
)

with open(os.path.join(base_dir, "logo_icon.svg"), "w", encoding="utf-8") as f:
    f.write(svg_logo_icon)

with open(os.path.join(base_dir, "snap_icon.svg"), "w", encoding="utf-8") as f:
    f.write(svg_snap_icon)

print("Updated logo_icon.svg and snap_icon.svg successfully!")
