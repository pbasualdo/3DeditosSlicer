import base64
import os

repo_dir = r"F:\Development\OfflineRepos\3d\3DeditosSlicer"
logo_path = os.path.join(repo_dir, "assets", "logo.png")

with open(logo_path, "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode("ascii")

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <base href="/web/flutter_web/">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>3DeditosSlicer // Suite Oficial</title>
  <style>
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
    }}
    body {{
      background: #0d1117;
      color: #e6edf3;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 24px;
      overflow-y: auto;
    }}
    .hero-container {{
      max-width: 920px;
      width: 100%;
      background: linear-gradient(180deg, #161b22 0%, #0d1117 100%);
      border: 1px solid #30363d;
      border-radius: 16px;
      padding: 36px 32px;
      box-shadow: 0 16px 48px rgba(0, 0, 0, 0.7);
      text-align: center;
      margin: auto;
    }}
    .logo-img {{
      width: 150px;
      height: 150px;
      border-radius: 50%;
      box-shadow: 0 0 30px rgba(0, 193, 174, 0.45), 0 8px 24px rgba(0,0,0,0.9);
      border: 3px solid #00C1AE;
      margin-bottom: 18px;
      background: #000;
      object-fit: cover;
    }}
    h1 {{
      font-size: 32px;
      font-weight: 800;
      letter-spacing: 2.5px;
      color: #ffffff;
      margin-bottom: 6px;
      text-transform: uppercase;
    }}
    h1 span {{
      color: #00ffea;
    }}
    .subtitle {{
      font-size: 14px;
      color: #8b949e;
      margin-bottom: 28px;
      letter-spacing: 0.5px;
    }}
    .action-row {{
      display: flex;
      gap: 18px;
      justify-content: center;
      margin-bottom: 32px;
    }}
    .btn {{
      cursor: pointer;
      font-weight: 700;
      font-size: 15px;
      padding: 14px 32px;
      border-radius: 10px;
      border: none;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .btn-primary {{
      background: linear-gradient(135deg, #00C1AE 0%, #007A6E 100%);
      color: #002220;
      box-shadow: 0 4px 18px rgba(0, 193, 174, 0.4);
    }}
    .btn-primary:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(0, 193, 174, 0.6);
      background: linear-gradient(135deg, #00ffea 0%, #009688 100%);
    }}
    .btn-secondary {{
      background: #21262d;
      color: #c9d1d9;
      border: 1px solid #30363d;
    }}
    .btn-secondary:hover {{
      background: #30363d;
      color: #ffffff;
      transform: translateY(-2px);
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 14px;
      margin-bottom: 28px;
      text-align: left;
    }}
    .card {{
      background: rgba(22, 27, 34, 0.85);
      border: 1px solid #30363d;
      border-radius: 10px;
      padding: 16px;
      transition: border-color 0.2s, transform 0.2s;
    }}
    .card:hover {{
      border-color: #00C1AE;
      transform: translateY(-2px);
    }}
    .card-title {{
      font-size: 13px;
      font-weight: 700;
      color: #f0f6fc;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .card-desc {{
      font-size: 12px;
      color: #8b949e;
      line-height: 1.45;
    }}
    .footer-banner {{
      background: rgba(245, 158, 11, 0.08);
      border: 1px solid rgba(245, 158, 11, 0.25);
      border-radius: 8px;
      padding: 14px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 12px;
      color: #fcd34d;
      text-align: left;
    }}
  </style>
</head>
<body>
  <div class="hero-container">
    <img src="data:image/png;base64,{logo_b64}" alt="3Deditos Logo" class="logo-img" />
    
    <h1>3DEDITOS <span>SLICER</span></h1>
    <div class="subtitle">
      Suite de Slicing Oficial para <strong>Snapmaker U1</strong> (Quad-Toolhead CoreXY) &bull; Tolerancias calibradas a 0.2 mm
    </div>

    <div class="action-row">
      <button class="btn btn-primary" onclick="triggerNewProject()">
        🚀 Nuevo Proyecto (Ir a Preparar)
      </button>
      <button class="btn btn-secondary" onclick="triggerOpenProject()">
        📂 Abrir Modelo (STL / STEP / 3MF)
      </button>
    </div>

    <div class="grid">
      <div class="card" style="border-left: 3px solid #00C1AE;">
        <div class="card-title">⚙️ Mechanical 0.20mm</div>
        <div class="card-desc">4 paredes, Gyroid 30%, costura alineada y compensación XY Hole (+0.1mm) para encastre exacto.</div>
      </div>
      <div class="card" style="border-left: 3px solid #38bdf8;">
        <div class="card-title">🧪 Dissimilar Support</div>
        <div class="card-desc">PLA + PETG Zero-Gap (Luz Z = 0.0mm) con interfaz sólida para desprendimiento limpio sin marcas.</div>
      </div>
      <div class="card" style="border-left: 3px solid #f59e0b;">
        <div class="card-title">🛡️ Overmold PETG+TPU</div>
        <div class="card-desc">Ensamble multi-material rígido + elastómero. Standby temp a -150°C para cero stringing en boquillas.</div>
      </div>
      <div class="card" style="border-left: 3px solid #ec4899;">
        <div class="card-title">🎨 Kids 4Color Articulated</div>
        <div class="card-desc">Purga reducida y torre de limpieza con costillas cónicas (Rib) para figuras articuladas de 4 colores.</div>
      </div>
    </div>

    <div class="footer-banner">
      <div>
        ⚠️ <strong>Protocolo Human-in-the-Loop Activo:</strong> Inspeccioná siempre las capas en la pestaña <em>Preparar / Previsualización</em> antes de enviar el archivo a la Snapmaker U1 por Moonraker/Klipper.
      </div>
      <div style="font-weight: 700; color: #00ffea; margin-left: 14px; white-space: nowrap;">
        Tolerancia: 0.2 mm
      </div>
    </div>
  </div>

  <script>
    window.sendMessage = function (message) {{
      if (window.wx && window.wx.postMessage) {{
        window.wx.postMessage(message);
      }}
      if (window.chrome && window.chrome.webview && window.chrome.webview.postMessage) {{
        window.chrome.webview.postMessage(message);
      }}
    }};

    function sendCommand(cmd, data) {{
      var packet = {{
        sequence_id: Math.round(Date.now() / 1000),
        command: cmd
      }};
      if (data) {{ packet.data = data; }}
      var str = JSON.stringify(packet);

      window.sendMessage(str);
      console.log('IPC message sent:', str);
    }}

    function triggerNewProject() {{
      sendCommand('homepage_newproject');
    }}

    function triggerOpenProject() {{
      sendCommand('homepage_openproject');
    }}
  </script>
</body>
</html>
"""

target_path = os.path.join(
    repo_dir,
    "Snapmaker_Orca_Windows_V2.4.1_portable",
    "resources",
    "web",
    "flutter_web",
    "index.html",
)

with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated {target_path} (length: {len(html_content)})")
