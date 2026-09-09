"""
Interactive UI Dashboard for Cognitive Agent Evaluator.
100% self-contained CSS styling with a modern light "blanco grisáceo" theme (Stripe/Notion style).
"""

HTML_DASHBOARD = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cognitive Agent Evaluator • Fabio Torres</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      background-color: #f1f5f9; /* Blanco grisáceo moderno */
      color: #0f172a;
      line-height: 1.5;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }
    
    /* Layout Navbar */
    .navbar {
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid #e2e8f0;
      position: sticky;
      top: 0;
      z-index: 50;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
    }
    .nav-container {
      max-width: 1100px;
      margin: 0 auto;
      padding: 12px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .brand-group {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .brand-icon {
      width: 38px;
      height: 38px;
      background: linear-gradient(135deg, #0284c7, #2563eb);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      box-shadow: 0 4px 10px rgba(2, 132, 199, 0.25);
    }
    .brand-title {
      font-size: 17px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .badge-live {
      font-size: 11px;
      font-weight: 700;
      background: #e0f2fe;
      color: #0284c7;
      padding: 2px 8px;
      border-radius: 9999px;
      border: 1px solid #bae6fd;
    }
    .brand-sub {
      font-size: 12px;
      color: #64748b;
    }
    .brand-sub a {
      color: #0284c7;
      text-decoration: none;
      font-weight: 600;
    }
    .nav-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .btn-swagger {
      font-size: 12px;
      font-weight: 600;
      padding: 7px 14px;
      border-radius: 8px;
      background: #ffffff;
      color: #334155;
      text-decoration: none;
      border: 1px solid #cbd5e1;
      transition: all 0.2s;
    }
    .btn-swagger:hover { background: #f8fafc; color: #0f172a; border-color: #94a3b8; }
    .btn-github {
      font-size: 12px;
      font-weight: 600;
      padding: 7px 14px;
      border-radius: 8px;
      background: #0f172a;
      color: #ffffff;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
      box-shadow: 0 2px 6px rgba(15, 23, 42, 0.2);
    }
    .btn-github:hover { background: #1e293b; }
    .btn-github svg {
      width: 16px !important;
      height: 16px !important;
      max-width: 16px !important;
      max-height: 16px !important;
      fill: currentColor;
    }

    /* Main Container */
    .main-content {
      max-width: 1100px;
      margin: 0 auto;
      padding: 28px 20px;
      flex: 1;
      width: 100%;
    }

    /* Purpose Section */
    .purpose-box {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 16px;
      padding: 24px;
      margin-bottom: 28px;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
    }
    .purpose-header {
      text-align: center;
      max-width: 720px;
      margin: 0 auto 20px;
    }
    .purpose-header h2 {
      font-size: 23px;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .purpose-header p {
      font-size: 13.5px;
      color: #475569;
      margin-top: 6px;
    }
    .purpose-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
    }
    .purpose-card {
      padding: 16px;
      border-radius: 12px;
      font-size: 13px;
    }
    .purpose-card-1 {
      background: #fff1f2;
      border: 1px solid #fecdd3;
    }
    .purpose-card-1 h3 { color: #e11d48; font-size: 14px; font-weight: 700; margin-bottom: 6px; }
    .purpose-card-2 {
      background: #f0f9ff;
      border: 1px solid #bae6fd;
    }
    .purpose-card-2 h3 { color: #0284c7; font-size: 14px; font-weight: 700; margin-bottom: 6px; }
    .purpose-card-3 {
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
    }
    .purpose-card-3 h3 { color: #16a34a; font-size: 14px; font-weight: 700; margin-bottom: 6px; }
    .purpose-card p { color: #334155; line-height: 1.45; }

    /* Playground Grid */
    .playground-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
    }
    @media (max-width: 860px) {
      .playground-grid { grid-template-columns: 1fr; }
    }

    .panel {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 16px;
      padding: 22px;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
    }
    .panel-title {
      font-size: 16px;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    /* Samples Buttons */
    .samples-label {
      font-size: 11px;
      font-weight: 700;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 8px;
      display: block;
    }
    .samples-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin-bottom: 16px;
    }
    .btn-sample {
      text-align: left;
      padding: 10px 12px;
      border-radius: 10px;
      font-size: 12px;
      cursor: pointer;
      transition: all 0.2s;
      line-height: 1.35;
    }
    .btn-sample-1 {
      background: #fff1f2;
      border: 1px solid #fecdd3;
      color: #9f1239;
    }
    .btn-sample-1:hover { background: #ffe4e6; border-color: #fda4af; }
    .btn-sample-2 {
      background: #fffbeb;
      border: 1px solid #fde68a;
      color: #92400e;
    }
    .btn-sample-2:hover { background: #fef3c7; border-color: #fcd34d; }
    .btn-sample-3 {
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      color: #1e40af;
    }
    .btn-sample-3:hover { background: #dbeafe; border-color: #93c5fd; }
    .btn-sample-4 {
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      color: #166534;
    }
    .btn-sample-4:hover { background: #dcfce7; border-color: #86efac; }
    .btn-sample b { display: block; font-size: 12px; margin-bottom: 2px; }
    .btn-sample span { font-size: 11px; opacity: 0.9; }

    /* Textarea & Controls */
    .textarea-label {
      font-size: 11px;
      font-weight: 700;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 6px;
      display: block;
    }
    .text-input {
      width: 100%;
      height: 120px;
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-radius: 12px;
      padding: 12px;
      color: #0f172a;
      font-size: 13.5px;
      resize: vertical;
      outline: none;
      transition: all 0.2s;
    }
    .text-input:focus {
      background: #ffffff;
      border-color: #0284c7;
      box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.15);
    }

    .author-selector {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin: 12px 0 16px;
      font-size: 12px;
      color: #64748b;
    }
    .author-options {
      display: flex;
      gap: 14px;
    }
    .author-options label {
      display: flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      color: #334155;
      font-weight: 500;
    }

    .btn-run {
      width: 100%;
      padding: 13px;
      border-radius: 12px;
      border: none;
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #fff;
      font-weight: 800;
      font-size: 14px;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.25);
      transition: all 0.2s;
    }
    .btn-run:hover { opacity: 0.95; transform: translateY(-1px); box-shadow: 0 6px 18px rgba(2, 132, 199, 0.35); }
    .btn-run:active { transform: translateY(0); }

    /* Results States */
    .empty-state {
      text-align: center;
      padding: 50px 20px;
      color: #64748b;
    }
    .empty-icon { font-size: 40px; margin-bottom: 12px; }
    .empty-state h4 { font-size: 16px; font-weight: 700; color: #0f172a; margin-bottom: 6px; }
    .empty-state p { font-size: 13px; max-width: 320px; margin: 0 auto; color: #64748b; }

    .loading-state {
      text-align: center;
      padding: 60px 20px;
      display: none;
    }
    .spinner {
      width: 42px;
      height: 42px;
      border: 4px solid rgba(2, 132, 199, 0.15);
      border-top-color: #0284c7;
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
      margin: 0 auto 16px;
    }
    @keyframes spin { to { transform: rotate(360deg); } }

    /* Output Cards */
    .result-content { display: none; }
    .result-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 14px;
      border-bottom: 1px solid #e2e8f0;
      margin-bottom: 16px;
    }
    .risk-badge {
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      padding: 5px 14px;
      border-radius: 9999px;
    }
    .risk-nominal { background: #dcfce7; color: #15803d; border: 1px solid #86efac; }
    .risk-moderate { background: #fef3c7; color: #b45309; border: 1px solid #fde68a; }
    .risk-critical { background: #fee2e2; color: #b91c1c; border: 1px solid #fca5a5; }

    .latency-badge {
      font-size: 12px;
      font-family: monospace;
      color: #0284c7;
      font-weight: 700;
    }

    .metrics-title {
      font-size: 11px;
      font-weight: 700;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 10px;
    }
    .metrics-grid {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 10px;
      margin-bottom: 18px;
    }
    .metric-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 12px;
      text-align: center;
    }
    .metric-name { font-size: 11px; color: #64748b; font-weight: 600; }
    .metric-value { font-size: 18px; font-weight: 800; color: #0f172a; margin: 2px 0; }
    .metric-sub { font-size: 10.5px; color: #475569; }

    .biases-section { margin-bottom: 18px; }
    .bias-item {
      padding: 12px;
      border-radius: 12px;
      margin-bottom: 8px;
      font-size: 12.5px;
    }
    .bias-item-high {
      background: #fff1f2;
      border: 1px solid #fecdd3;
    }
    .bias-item-medium {
      background: #fffbeb;
      border: 1px solid #fde68a;
    }
    .bias-item-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-weight: 800;
      margin-bottom: 4px;
    }
    .bias-name { color: #0f172a; font-size: 13.5px; }
    .bias-pill {
      font-size: 10px;
      padding: 2px 8px;
      border-radius: 9999px;
      font-weight: 800;
      text-transform: uppercase;
    }
    .pill-high { background: #fee2e2; color: #991b1b; }
    .pill-medium { background: #fef3c7; color: #92400e; }
    .bias-desc { color: #334155; font-size: 11.5px; line-height: 1.4; margin-bottom: 6px; }
    .bias-triggers { font-size: 11px; color: #64748b; }
    .trigger-tag {
      background: #e2e8f0;
      color: #0369a1;
      padding: 2px 6px;
      border-radius: 4px;
      font-family: monospace;
      font-size: 10.5px;
      margin-right: 4px;
    }

    .mitigation-box {
      background: #f5f3ff;
      border: 1px solid #ddd6fe;
      border-radius: 12px;
      padding: 16px;
    }
    .mitigation-box h4 {
      font-size: 12px;
      font-weight: 800;
      color: #6d28d9;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .mitigation-box ul {
      padding-left: 18px;
      font-size: 12px;
      color: #312e81;
      line-height: 1.5;
    }
    .counterfactual-text {
      margin-top: 10px;
      padding-top: 10px;
      border-top: 1px solid #ddd6fe;
      font-size: 11.5px;
      color: #4338ca;
      font-style: italic;
    }

    /* Footer */
    .footer {
      border-top: 1px solid #e2e8f0;
      background: #ffffff;
      padding: 20px;
      font-size: 12px;
      color: #64748b;
      text-align: center;
    }
    .footer a { color: #0284c7; text-decoration: none; margin: 0 8px; font-weight: 500; }
    .footer a:hover { text-decoration: underline; }
  </style>
</head>
<body>

  <!-- Navbar -->
  <header class="navbar">
    <div class="nav-container">
      <div class="brand-group">
        <div class="brand-icon">🧠</div>
        <div>
          <div class="brand-title">
            Cognitive Agent Evaluator
            <span class="badge-live">v1.0 Live</span>
          </div>
          <div class="brand-sub">Por <a href="https://github.com/neurodeveloper11" target="_blank">Fabio Torres</a> • Psicología Conductual + Inteligencia Artificial</div>
        </div>
      </div>
      <div class="nav-actions">
        <a href="/docs" target="_blank" class="btn-swagger">⚡ API Swagger</a>
        <a href="https://github.com/neurodeveloper11/cognitive-agent-evaluator" target="_blank" class="btn-github">
          <svg viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
          <span>GitHub</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Main Container -->
  <main class="main-content">

    <!-- Purpose Cards -->
    <section class="purpose-box">
      <div class="purpose-header">
        <h2>¿Para qué sirve este Agente de Inteligencia Artificial?</h2>
        <p>Diseñado para resolver un problema crítico en la tecnología moderna: <b>las trampas lógicas e inconscientes</b> en las que caen tanto los humanos como las IAs al tomar decisiones.</p>
      </div>
      <div class="purpose-grid">
        <div class="purpose-card purpose-card-1">
          <h3>🚨 1. El Problema Oculto</h3>
          <p>Las IAs actuales filtran insultos, pero cometen <b>sesgos cognitivos graves</b>: rechazan pruebas contrarias o defienden proyectos fallidos porque "ya se gastó mucho dinero".</p>
        </div>
        <div class="purpose-card purpose-card-2">
          <h3>🧠 2. La Solución de Fabio</h3>
          <p>Unimos <b>10+ años de Psicología</b> con <b>Ingeniería de Software</b> para auditar en milisegundos qué tan pesado, emocional y coherente es el razonamiento.</p>
        </div>
        <div class="purpose-card purpose-card-3">
          <h3>✅ 3. El Resultado Práctico</h3>
          <p>El agente diagnostica las falacias y le entrega a la persona o al modelo una <b>receta de corrección</b> clara para pensar de forma objetiva y racional.</p>
        </div>
      </div>
    </section>

    <!-- Playground -->
    <section class="playground-grid">
      
      <!-- Input Panel -->
      <div class="panel">
        <div class="panel-title"><span>✍️</span> Prueba en Vivo el Evaluador</div>
        
        <label class="samples-label">Prueba un ejemplo rápido con 1 clic:</label>
        <div class="samples-grid">
          <button type="button" onclick="setSample(1)" class="btn-sample btn-sample-1">
            <b>🔴 Sesgo Confirmación</b>
            <span>"Es obvio y descarto pruebas..."</span>
          </button>
          <button type="button" onclick="setSample(2)" class="btn-sample btn-sample-2">
            <b>🟠 Costo Hundido</b>
            <span>"Ya invertí mucho para parar..."</span>
          </button>
          <button type="button" onclick="setSample(3)" class="btn-sample btn-sample-3">
            <b>🔵 Sesgo de Anclaje</b>
            <span>"El precio inicial dicta la oferta..."</span>
          </button>
          <button type="button" onclick="setSample(4)" class="btn-sample btn-sample-4">
            <b>🟢 Racional / Científico</b>
            <span>"Evidencia empírica validada..."</span>
          </button>
        </div>

        <label for="inputText" class="textarea-label">O escribe tu propio texto / argumento:</label>
        <textarea id="inputText" class="text-input" placeholder="Escribe aquí cualquier argumento, idea o razonamiento de prueba (en español o inglés)..."></textarea>

        <div class="author-selector">
          <span>Origen del texto:</span>
          <div class="author-options">
            <label><input type="radio" name="author_type" value="human" checked> Persona</label>
            <label><input type="radio" name="author_type" value="llm"> Modelo de IA</label>
          </div>
        </div>

        <button type="button" id="btnEval" onclick="runEvaluation()" class="btn-run">
          ⚡ Evaluar Texto con el Agente de IA
        </button>
      </div>

      <!-- Output Panel -->
      <div class="panel">
        <div id="emptyState" class="empty-state">
          <div class="empty-icon">🔍</div>
          <h4>Esperando texto para auditar</h4>
          <p>Haz clic en cualquiera de los 4 botones de ejemplo de la izquierda o escribe una frase para ver el diagnóstico en vivo.</p>
        </div>

        <div id="loadingState" class="loading-state">
          <div class="spinner"></div>
          <p style="color: #0284c7; font-weight: 700;">Analizando heurísticas y psicometría...</p>
        </div>

        <div id="resultContent" class="result-content">
          <div class="result-header">
            <div id="riskBadge" class="risk-badge"></div>
            <div class="latency-badge">⚡ <span id="latencyText">0.9 ms</span></div>
          </div>

          <div class="metrics-title">Métricas Psicométricas del Razonamiento</div>
          <div class="metrics-grid">
            <div class="metric-card">
              <div class="metric-name">Carga Cognitiva</div>
              <div id="valCognitiveLoad" class="metric-value">0</div>
              <div id="descCognitiveLoad" class="metric-sub">Ligero</div>
            </div>
            <div class="metric-card">
              <div class="metric-name">Valencia Emocional</div>
              <div id="valValence" class="metric-value" style="color: #0284c7;">0.0</div>
              <div id="descValence" class="metric-sub">Neutro</div>
            </div>
            <div class="metric-card">
              <div class="metric-name">Coherencia Lógica</div>
              <div id="valConsistency" class="metric-value" style="color: #16a34a;">0%</div>
              <div id="descConsistency" class="metric-sub">Alta</div>
            </div>
          </div>

          <div class="metrics-title">Sesgos Cognitivos Detectados</div>
          <div id="biasesList" class="biases-section"></div>

          <div class="mitigation-box">
            <h4><span>💡</span> Receta Psicológica de Mitigación (AI Alignment)</h4>
            <ul id="mitigationList"></ul>
            <div id="counterfactualBox" class="counterfactual-text"></div>
          </div>
        </div>
      </div>

    </section>
  </main>

  <footer class="footer">
    <div>© 2026 <b>Fabio Ignacio Torres Benítez</b> • Cali / Buenaventura, Colombia</div>
    <div style="margin-top: 6px;">
      <a href="https://github.com/neurodeveloper11" target="_blank">GitHub</a> |
      <a href="https://www.linkedin.com/in/fabio-torres-39364b258" target="_blank">LinkedIn</a> |
      <a href="mailto:psicologofabiotorres@gmail.com">Contacto</a>
    </div>
  </footer>

  <script>
    const SAMPLES = {
      1: "Esta estrategia es obviamente verdadera y todos en la industria lo saben. Debemos descartar cualquier prueba contraria porque esto confirma lo que ya sabía desde el principio.",
      2: "Ya invertí demasiado dinero y tiempo en este software para parar ahora. Sería una pérdida total dejarlo, así que no podemos parar ahora y debemos seguir gastando.",
      3: "Dado que el precio inicial que nos pidieron en la primera propuesta fue de 80,000 dólares, nuestra oferta debe estar cerca de esa primera cifra.",
      4: "El análisis empírico y sistemático demuestra una solución óptima y rigurosa, con evidencia validada y resultados altamente consistentes en todas las pruebas."
    };

    function setSample(id) {
      document.getElementById('inputText').value = SAMPLES[id];
      runEvaluation();
    }

    async function runEvaluation() {
      const text = document.getElementById('inputText').value.trim();
      if (!text) {
        alert("Por favor escribe una frase o selecciona un ejemplo de prueba.");
        return;
      }

      const authorType = document.querySelector('input[name="author_type"]:checked').value;
      const emptyState = document.getElementById('emptyState');
      const loadingState = document.getElementById('loadingState');
      const resultContent = document.getElementById('resultContent');

      emptyState.style.display = 'none';
      resultContent.style.display = 'none';
      loadingState.style.display = 'block';

      try {
        const res = await fetch('/api/v1/evaluate', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ text, author_type: authorType })
        });

        if (!res.ok) throw new Error("Error en la respuesta del servidor");
        const data = await res.json();
        renderResults(data);
      } catch (err) {
        alert("Error al evaluar: " + err.message);
        emptyState.style.display = 'block';
      } finally {
        loadingState.style.display = 'none';
      }
    }

    function renderResults(data) {
      const resultContent = document.getElementById('resultContent');
      resultContent.style.display = 'block';

      document.getElementById('latencyText').innerText = data.execution_latency_ms + " ms";

      const risk = data.mitigation.alignment_risk_level;
      const riskBadge = document.getElementById('riskBadge');
      if (risk === 'critical') {
        riskBadge.className = "risk-badge risk-critical";
        riskBadge.innerHTML = "🚨 Riesgo Crítico de Sesgo";
      } else if (risk === 'moderate') {
        riskBadge.className = "risk-badge risk-moderate";
        riskBadge.innerHTML = "⚠️ Riesgo Moderado de Sesgo";
      } else {
        riskBadge.className = "risk-badge risk-nominal";
        riskBadge.innerHTML = "✅ Razonamiento Equilibrado";
      }

      const p = data.psychometrics;
      document.getElementById('valCognitiveLoad').innerText = p.cognitive_load_index + "/100";
      document.getElementById('descCognitiveLoad').innerText = p.cognitive_load_index > 70 ? "Alta complejidad" : (p.cognitive_load_index > 40 ? "Moderado" : "Fácil lectura");

      document.getElementById('valValence').innerText = (p.emotional_valence > 0 ? "+" : "") + p.emotional_valence;
      document.getElementById('descValence').innerText = p.emotional_valence > 0.1 ? "Constructivo" : (p.emotional_valence < -0.1 ? "Negativo / Reactivo" : "Neutral");

      document.getElementById('valConsistency').innerText = Math.round(p.logical_consistency_score * 100) + "%";
      document.getElementById('descConsistency').innerText = p.logical_consistency_score > 0.75 ? "Sólida" : (p.logical_consistency_score > 0.5 ? "Aceptable" : "Baja");

      const biasesList = document.getElementById('biasesList');
      biasesList.innerHTML = "";

      if (!data.biases_detected || data.biases_detected.length === 0) {
        biasesList.innerHTML = `
          <div style="padding: 12px; border-radius: 10px; background: #f0fdf4; border: 1px solid #bbf7d0; color: #166534; font-size: 12px;">
            🎉 <b>No se detectaron sesgos evidentes.</b> El argumento se mantiene objetivo y basado en datos.
          </div>
        `;
      } else {
        data.biases_detected.forEach(b => {
          const itemClass = b.severity === 'high' ? 'bias-item-high' : 'bias-item-medium';
          const pillClass = b.severity === 'high' ? 'pill-high' : 'pill-medium';
          
          biasesList.innerHTML += `
            <div class="bias-item ${itemClass}">
              <div class="bias-item-header">
                <span class="bias-name">🎯 ${b.bias_name}</span>
                <span class="bias-pill ${pillClass}">Severidad: ${b.severity} (${Math.round(b.confidence_score * 100)}% certeza)</span>
              </div>
              <div class="bias-desc">${b.explanation}</div>
              ${b.matched_patterns && b.matched_patterns.length > 0 ? `
                <div class="bias-triggers">
                  <b>Frases delatadas:</b>
                  ${b.matched_patterns.map(pat => `<span class="trigger-tag">"${pat}"</span>`).join('')}
                </div>
              ` : ''}
            </div>
          `;
        });
      }

      const mitList = document.getElementById('mitigationList');
      mitList.innerHTML = "";
      data.mitigation.recommended_interventions.forEach(rec => {
        mitList.innerHTML += `<li>${rec}</li>`;
      });

      const cfBox = document.getElementById('counterfactualBox');
      if (data.mitigation.counterfactual_prompt) {
        cfBox.style.display = 'block';
        cfBox.innerHTML = `<b>Ejercicio de Refutación Sugerido:</b> "${data.mitigation.counterfactual_prompt}"`;
      } else {
        cfBox.style.display = 'none';
      }
    }
  </script>
</body>
</html>
"""
