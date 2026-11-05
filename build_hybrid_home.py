import os

repo_dir = r"F:\Development\OfflineRepos\3d\3DeditosSlicer"
b64_file = os.path.join(repo_dir, "logo_b64.txt")
with open(b64_file, "r") as f:
    logo_b64 = f.read().strip()

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <base href="/web/flutter_web/">

  <meta charset="UTF-8">
  <meta content="IE=Edge" http-equiv="X-UA-Compatible">
  <meta name="description" content="3DeditosSlicer // Snapmaker U1 Suite">
  <meta http-equiv="Permissions-Policy" content="local-files-write=*">
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black">
  <meta name="apple-mobile-web-app-title" content="3DeditosSlicer">
  <link rel="apple-touch-icon" href="icons/Icon-192.png">
  <link rel="icon" type="image/png" href="favicon.png"/>

  <title>3DeditosSlicer // Suite Oficial</title>
  <link rel="manifest" href="manifest.json">
  <script src="posthog-array.0930d984aecf936d75a80e534e55d1eb.js"></script>

  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <meta name="theme-color" content="#161b22">
  <style>
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    html, body {{
      overflow: hidden;
      height: 100%;
      width: 100%;
      background: #0d1117;
      color: #e6edf3;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }}

    /* Top Tab Bar */
    #top-tab-bar {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 48px;
      background: #161b22;
      border-bottom: 1px solid #30363d;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 18px;
      z-index: 2147483647;
      user-select: none;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
    }}

    .brand-group {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .brand-logo-mini {{
      width: 28px;
      height: 28px;
      border-radius: 50%;
      border: 1.5px solid #00C1AE;
      object-fit: cover;
      background: #000;
    }}

    .brand-title {{
      font-size: 14px;
      font-weight: 800;
      letter-spacing: 1.5px;
      color: #ffffff;
      text-transform: uppercase;
    }}

    .brand-title span {{
      color: #00ffea;
    }}

    .tab-pills {{
      display: flex;
      gap: 8px;
      background: #0d1117;
      padding: 4px;
      border-radius: 24px;
      border: 1px solid #30363d;
    }}

    .tab-pill {{
      cursor: pointer;
      font-size: 13px;
      font-weight: 700;
      padding: 6px 18px;
      border-radius: 18px;
      border: none;
      background: transparent;
      color: #8b949e;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .tab-pill:hover {{
      color: #ffffff;
      background: rgba(255, 255, 255, 0.05);
    }}

    .tab-pill.active {{
      background: linear-gradient(135deg, #00C1AE 0%, #007A6E 100%);
      color: #002220;
      box-shadow: 0 2px 10px rgba(0, 193, 174, 0.35);
    }}

    .badge-info {{
      font-size: 11px;
      font-weight: 600;
      color: #7ee787;
      display: flex;
      align-items: center;
      gap: 6px;
      background: rgba(126, 231, 135, 0.1);
      padding: 4px 10px;
      border-radius: 12px;
      border: 1px solid rgba(126, 231, 135, 0.2);
    }}

    .badge-dot {{
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #7ee787;
      box-shadow: 0 0 6px #7ee787;
    }}

    /* 3DEDITOS Suite Dashboard */
    #panel-3deditos {{
      position: fixed;
      top: 48px;
      left: 0;
      right: 0;
      bottom: 0;
      background: radial-gradient(circle at 50% 20%, #161b22 0%, #0d1117 70%);
      overflow-y: auto;
      z-index: 2147483646;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      padding: 36px 20px 48px 20px;
    }}

    .hero-container {{
      max-width: 920px;
      width: 100%;
      background: linear-gradient(180deg, rgba(22, 27, 34, 0.95) 0%, rgba(13, 17, 23, 0.95) 100%);
      border: 1px solid #30363d;
      border-radius: 16px;
      padding: 36px 32px;
      box-shadow: 0 16px 48px rgba(0, 0, 0, 0.7);
      text-align: center;
      backdrop-filter: blur(8px);
    }}

    .logo-img {{
      width: 140px;
      height: 140px;
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
      gap: 16px;
      justify-content: center;
      margin-bottom: 30px;
    }}

    .btn {{
      cursor: pointer;
      font-weight: 700;
      font-size: 14px;
      padding: 13px 30px;
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
      margin-bottom: 26px;
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

    /* Flutter Web positioning below top tab bar */
    #flutter-loading, #flutter-error, flt-glass-pane, flutter-view {{
      top: 48px !important;
      height: calc(100% - 48px) !important;
      z-index: 2147483640 !important;
    }}
  </style>
  <link rel="preload" href="main.dart.js" as="script">
</head>
<body>
  <!-- Top Navigation Bar for Home View -->
  <div id="top-tab-bar">
    <div class="brand-group">
      <img src="data:image/png;base64,{logo_b64}" alt="3Deditos Logo" class="brand-logo-mini" />
      <div class="brand-title">3DEDITOS <span>SLICER</span></div>
    </div>

    <div class="tab-pills">
      <button id="btn-tab-3deditos" class="tab-pill active" onclick="switchTab('3deditos')">
        🚀 3Deditos Suite
      </button>
      <button id="btn-tab-catalog" class="tab-pill" onclick="switchTab('catalog')">
        🌐 Catálogo Snapmaker
      </button>
    </div>

    <div class="badge-info">
      <span class="badge-dot"></span> Snapmaker U1 &bull; 0.2 mm
    </div>
  </div>

  <!-- 3DEDITOS Suite Content Panel -->
  <div id="panel-3deditos">
    <div class="hero-container">
      <img src="data:image/png;base64,{logo_b64}" alt="3Deditos Logo" class="logo-img" />
      
      <h1>3DEDITOS <span>SLICER</span></h1>
      <div class="subtitle">
        Suite de Slicing Oficial para <strong>Snapmaker U1</strong> (Quad-Toolhead CoreXY) &bull; Tolerancias a 0.2 mm
      </div>

      <div class="action-row">
        <button class="btn btn-primary" onclick="triggerNewProject()">
          🚀 Nuevo Proyecto (Ir a Preparar)
        </button>
        <button class="btn btn-secondary" onclick="triggerOpenProject()">
          📂 Abrir Modelo (STL / STEP / 3MF)
        </button>
        <button class="btn btn-secondary" onclick="switchTab('catalog')">
          🌐 Explorar Catálogo Snapmaker
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
  </div>

  <script>
    // Tab switching logic
    function switchTab(target) {{
      var btn3d = document.getElementById('btn-tab-3deditos');
      var btnCat = document.getElementById('btn-tab-catalog');
      var panel3d = document.getElementById('panel-3deditos');

      if (target === '3deditos') {{
        btn3d.classList.add('active');
        btnCat.classList.remove('active');
        panel3d.style.display = 'flex';
      }} else {{
        btnCat.classList.add('active');
        btn3d.classList.remove('active');
        panel3d.style.display = 'none';
      }}
    }}

    // Native IPC integration matching Snapmaker Orca specification
    window.sendMessage = function (message) {{
      window.wx && window.wx.postMessage(message);
      if (!window.wx) {{
        console.log('window.wx not found, logging IPC packet:', message);
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
    }}

    function triggerNewProject() {{
      sendCommand('homepage_newproject');
    }}

    function triggerOpenProject() {{
      sendCommand('homepage_openproject');
    }}
  </script>

  <!-- Native Flutter Web bootstrap for Snapmaker Catalog -->
  <script src="flutter_overlay.js"></script>
  <script src="flutter_bootstrap.js" async></script>
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

print(f"Generated optimized hybrid index.html (size: {len(html_content)})")
