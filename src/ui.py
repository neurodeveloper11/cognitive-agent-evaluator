"""
Interactive UI Dashboard for Cognitive Agent Evaluator.
Modern, accessible, and intuitive interface with live evaluation and real-time visualization.
"""

HTML_DASHBOARD = """<!DOCTYPE html>
<html lang="es" class="h-full bg-slate-950 text-slate-100">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cognitive Agent Evaluator • Fabio Torres</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Plus Jakarta Sans', sans-serif; }
    code, pre { font-family: 'JetBrains Mono', monospace; }
    .gradient-glow {
      background: radial-gradient(circle at 50% 0%, rgba(56, 189, 248, 0.15), transparent 70%);
    }
  </style>
</head>
<body class="min-h-full gradient-glow flex flex-col antialiased selection:bg-cyan-500 selection:text-white">

  <!-- Navbar -->
  <header class="border-b border-slate-800/80 backdrop-blur-md sticky top-0 z-50 bg-slate-950/70">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 py-3.5 flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 to-indigo-600 flex items-center justify-center shadow-lg shadow-cyan-500/20 font-bold text-lg text-white">
          🧠
        </div>
        <div>
          <h1 class="font-extrabold text-base sm:text-lg text-white tracking-tight flex items-center gap-2">
            Cognitive Agent Evaluator
            <span class="text-xs font-semibold px-2 py-0.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">v1.0 Live</span>
          </h1>
          <p class="text-xs text-slate-400">Por <a href="https://github.com/neurodeveloper11" target="_blank" class="text-cyan-400 hover:underline font-medium">Fabio Torres</a> • Psicología Conductual + Inteligencia Artificial</p>
        </div>
      </div>
      <div class="flex items-center space-x-3">
        <a href="/docs" target="_blank" class="text-xs font-semibold px-3 py-1.5 rounded-lg border border-slate-700 bg-slate-900 hover:bg-slate-800 text-slate-300 transition flex items-center gap-1.5">
          <span>⚡ API Swagger</span>
        </a>
        <a href="https://github.com/neurodeveloper11/cognitive-agent-evaluator" target="_blank" class="text-xs font-semibold px-3.5 py-1.5 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white shadow-md shadow-cyan-600/20 transition flex items-center gap-1.5">
          <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
          <span>GitHub</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Main Container -->
  <main class="max-w-6xl mx-auto px-4 sm:px-6 py-8 flex-1 w-full space-y-8">

    <!-- Purpose Explanation Cards (¿Para qué sirve?) -->
    <section class="rounded-2xl border border-slate-800 bg-slate-900/50 p-6 shadow-xl backdrop-blur-sm">
      <div class="text-center max-w-3xl mx-auto mb-6">
        <h2 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
          ¿Para qué sirve este Agente de Inteligencia Artificial?
        </h2>
        <p class="text-sm sm:text-base text-slate-400 mt-2">
          Diseñado para resolver un problema crítico en la tecnología moderna: <strong class="text-slate-200">las trampas lógicas e inconscientes</strong> en las que caen tanto los humanos como las IAs al tomar decisiones.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div class="p-4 rounded-xl border border-rose-500/20 bg-rose-950/10">
          <div class="text-2xl mb-2">🚨</div>
          <h3 class="font-bold text-rose-300 text-sm sm:text-base">1. El Problema Oculto</h3>
          <p class="text-xs sm:text-sm text-slate-300 mt-1 leading-relaxed">
            Las IAs actuales filtran insultos, pero cometen <strong>sesgos cognitivos graves</strong>: rechazan pruebas contrarias o defienden proyectos fallidos porque "ya se gastó mucho dinero".
          </p>
        </div>

        <div class="p-4 rounded-xl border border-cyan-500/20 bg-cyan-950/10">
          <div class="text-2xl mb-2">🧠</div>
          <h3 class="font-bold text-cyan-300 text-sm sm:text-base">2. La Solución de Fabio</h3>
          <p class="text-xs sm:text-sm text-slate-300 mt-1 leading-relaxed">
            Unimos <strong>10+ años de Psicología</strong> con <strong>Ingeniería de Software</strong> para auditar en milisegundos qué tan pesado, emocional y coherente es el razonamiento.
          </p>
        </div>

        <div class="p-4 rounded-xl border border-emerald-500/20 bg-emerald-950/10">
          <div class="text-2xl mb-2">✅</div>
          <h3 class="font-bold text-emerald-300 text-sm sm:text-base">3. El Resultado Práctico</h3>
          <p class="text-xs sm:text-sm text-slate-300 mt-1 leading-relaxed">
            El agente diagnostica las falacias y le entrega a la persona o al modelo una <strong>receta de corrección</strong> clara para pensar de forma objetiva y racional.
          </p>
        </div>
      </div>
    </section>

    <!-- Testing Playground -->
    <section class="grid grid-cols-1 lg:grid-cols-12 gap-8">
      
      <!-- Input Panel -->
      <div class="lg:col-span-6 space-y-4">
        <div class="rounded-2xl border border-slate-800 bg-slate-900/70 p-6 shadow-xl space-y-4">
          <div class="flex items-center justify-between">
            <h3 class="font-bold text-lg text-white flex items-center gap-2">
              <span>✍️</span> Prueba en Vivo el Evaluador
            </h3>
            <span class="text-xs font-medium text-slate-400">Español & English</span>
          </div>

          <!-- Example Buttons -->
          <div>
            <label class="block text-xs font-semibold text-slate-400 mb-2 uppercase tracking-wider">
              Prueba un ejemplo rápido con 1 clic:
            </label>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
              <button onclick="setSample(1)" class="text-left text-xs font-medium p-2.5 rounded-lg border border-rose-500/30 bg-rose-500/10 hover:bg-rose-500/20 text-rose-300 transition">
                🔴 <b>Sesgo de Confirmación</b><br><span class="text-[11px] opacity-80">"Es obvio y descarto pruebas contrarias..."</span>
              </button>
              <button onclick="setSample(2)" class="text-left text-xs font-medium p-2.5 rounded-lg border border-amber-500/30 bg-amber-500/10 hover:bg-amber-500/20 text-amber-300 transition">
                🟠 <b>Falacia del Costo Hundido</b><br><span class="text-[11px] opacity-80">"Ya invertí demasiado para parar ahora..."</span>
              </button>
              <button onclick="setSample(3)" class="text-left text-xs font-medium p-2.5 rounded-lg border border-blue-500/30 bg-blue-500/10 hover:bg-blue-500/20 text-blue-300 transition">
                🔵 <b>Sesgo de Anclaje</b><br><span class="text-[11px] opacity-80">"El precio inicial dicta nuestra oferta..."</span>
              </button>
              <button onclick="setSample(4)" class="text-left text-xs font-medium p-2.5 rounded-lg border border-emerald-500/30 bg-emerald-500/10 hover:bg-emerald-500/20 text-emerald-300 transition">
                🟢 <b>Razonamiento Científico</b><br><span class="text-[11px] opacity-80">"La evidencia empírica muestra precisión..."</span>
              </button>
            </div>
          </div>

          <!-- Text Area -->
          <div>
            <label for="inputText" class="block text-xs font-semibold text-slate-400 mb-1.5 uppercase tracking-wider">
              O escribe tu propio texto / argumento:
            </label>
            <textarea id="inputText" rows="5" placeholder="Escribe aquí cualquier argumento, idea o razonamiento de prueba..." class="w-full rounded-xl border border-slate-700 bg-slate-950 p-3.5 text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 transition"></textarea>
          </div>

          <!-- Author Type -->
          <div class="flex items-center justify-between text-xs text-slate-400">
            <span>Origen del texto:</span>
            <div class="flex items-center gap-3">
              <label class="flex items-center gap-1.5 cursor-pointer">
                <input type="radio" name="author_type" value="human" checked class="text-cyan-500 focus:ring-cyan-500 bg-slate-900 border-slate-700">
                <span>Persona</span>
              </label>
              <label class="flex items-center gap-1.5 cursor-pointer">
                <input type="radio" name="author_type" value="llm" class="text-cyan-500 focus:ring-cyan-500 bg-slate-900 border-slate-700">
                <span>Modelo de IA</span>
              </label>
            </div>
          </div>

          <!-- Submit Button -->
          <button id="btnEval" onclick="runEvaluation()" class="w-full py-3.5 px-4 rounded-xl bg-gradient-to-r from-cyan-500 via-blue-600 to-indigo-600 hover:from-cyan-400 hover:to-indigo-500 text-white font-bold text-sm tracking-wide shadow-lg shadow-cyan-500/25 transition transform active:scale-[0.99] flex items-center justify-center gap-2">
            <span>⚡ Evaluar Texto con el Agente de IA</span>
          </button>
        </div>
      </div>

      <!-- Output Results Panel -->
      <div class="lg:col-span-6 space-y-4">
        <div id="resultsContainer" class="rounded-2xl border border-slate-800 bg-slate-900/70 p-6 shadow-xl min-h-[440px] flex flex-col justify-center">
          
          <!-- Empty State -->
          <div id="emptyState" class="text-center py-12 space-y-3">
            <div class="w-16 h-16 mx-auto rounded-2xl bg-slate-800/60 border border-slate-700 flex items-center justify-center text-3xl">
              🔍
            </div>
            <h4 class="font-bold text-slate-200 text-base">Esperando texto para auditar</h4>
            <p class="text-xs text-slate-400 max-w-sm mx-auto">
              Haz clic en cualquiera de los 4 botones de ejemplo de la izquierda o escribe una frase para ver el diagnóstico psicológico en vivo.
            </p>
          </div>

          <!-- Loading State -->
          <div id="loadingState" class="hidden text-center py-16 space-y-4">
            <div class="w-12 h-12 border-4 border-cyan-500/20 border-t-cyan-500 rounded-full animate-spin mx-auto"></div>
            <p class="text-sm font-semibold text-cyan-400">Analizando heurísticas y psicometría...</p>
          </div>

          <!-- Real Results State -->
          <div id="resultContent" class="hidden space-y-5">
            
            <!-- Top Status Bar -->
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
              <div id="riskBadge" class="px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider flex items-center gap-1.5">
                <!-- Injected via JS -->
              </div>
              <div class="text-xs font-mono text-cyan-400 flex items-center gap-1">
                <span>⚡</span>
                <span id="latencyText">0.9 ms</span>
              </div>
            </div>

            <!-- Psychometrics Gauges -->
            <div>
              <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-3">Métricas Psicométricas del Razonamiento</h4>
              <div class="grid grid-cols-3 gap-2.5 text-center">
                
                <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800">
                  <div class="text-[11px] text-slate-400 font-medium">Carga Cognitiva</div>
                  <div id="valCognitiveLoad" class="text-lg font-black text-white mt-0.5">0</div>
                  <div id="descCognitiveLoad" class="text-[10px] text-slate-400 mt-0.5">Ligero</div>
                </div>

                <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800">
                  <div class="text-[11px] text-slate-400 font-medium">Valencia Emocional</div>
                  <div id="valValence" class="text-lg font-black text-cyan-400 mt-0.5">0.0</div>
                  <div id="descValence" class="text-[10px] text-slate-400 mt-0.5">Neutro</div>
                </div>

                <div class="p-3 rounded-xl bg-slate-950/80 border border-slate-800">
                  <div class="text-[11px] text-slate-400 font-medium">Coherencia Lógica</div>
                  <div id="valConsistency" class="text-lg font-black text-emerald-400 mt-0.5">0%</div>
                  <div id="descConsistency" class="text-[10px] text-slate-400 mt-0.5">Alta</div>
                </div>

              </div>
            </div>

            <!-- Detected Biases List -->
            <div>
              <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">Sesgos Cognitivos Detectados</h4>
              <div id="biasesList" class="space-y-2">
                <!-- Injected via JS -->
              </div>
            </div>

            <!-- Mitigation Recipe -->
            <div class="p-4 rounded-xl border border-indigo-500/30 bg-indigo-950/20 space-y-2">
              <h4 class="text-xs font-bold text-indigo-300 uppercase tracking-wider flex items-center gap-1.5">
                <span>💡</span> Receta Psicológica de Mitigación (AI Alignment)
              </h4>
              <ul id="mitigationList" class="text-xs text-slate-200 space-y-1.5 list-disc list-inside">
                <!-- Injected via JS -->
              </ul>
              <div id="counterfactualBox" class="mt-2.5 pt-2 border-t border-indigo-500/20 text-[11px] text-indigo-200/90 italic">
                <!-- Injected via JS -->
              </div>
            </div>

          </div>

        </div>
      </div>

    </section>

  </main>

  <!-- Footer -->
  <footer class="border-t border-slate-800/80 bg-slate-950/50 py-6 text-center text-xs text-slate-500">
    <div class="max-w-6xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2">
      <p>© 2026 <b>Fabio Ignacio Torres Benítez</b> • Cali / Buenaventura, Colombia</p>
      <div class="flex items-center space-x-4">
        <a href="https://github.com/neurodeveloper11" target="_blank" class="hover:text-cyan-400 transition">GitHub</a>
        <a href="https://www.linkedin.com/in/fabio-torres-39364b258" target="_blank" class="hover:text-cyan-400 transition">LinkedIn</a>
        <a href="mailto:psicologofabiotorres@gmail.com" class="hover:text-cyan-400 transition">Contacto</a>
      </div>
    </div>
  </footer>

  <!-- Interactive Logic -->
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

      emptyState.classList.add('hidden');
      resultContent.classList.add('hidden');
      loadingState.classList.remove('hidden');

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
        emptyState.classList.remove('hidden');
      } finally {
        loadingState.classList.add('hidden');
      }
    }

    function renderResults(data) {
      const resultContent = document.getElementById('resultContent');
      resultContent.classList.remove('hidden');

      // 1. Latency
      document.getElementById('latencyText').innerText = data.execution_latency_ms + " ms";

      // 2. Risk Badge
      const risk = data.mitigation.alignment_risk_level;
      const riskBadge = document.getElementById('riskBadge');
      if (risk === 'critical') {
        riskBadge.className = "px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider bg-rose-500/20 text-rose-300 border border-rose-500/30";
        riskBadge.innerHTML = "🚨 Riesgo Crítico de Sesgo";
      } else if (risk === 'moderate') {
        riskBadge.className = "px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider bg-amber-500/20 text-amber-300 border border-amber-500/30";
        riskBadge.innerHTML = "⚠️ Riesgo Moderado de Sesgo";
      } else {
        riskBadge.className = "px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider bg-emerald-500/20 text-emerald-300 border border-emerald-500/30";
        riskBadge.innerHTML = "✅ Razonamiento Equilibrado y Limpio";
      }

      // 3. Psychometrics
      const p = data.psychometrics;
      document.getElementById('valCognitiveLoad').innerText = p.cognitive_load_index + "/100";
      document.getElementById('descCognitiveLoad').innerText = p.cognitive_load_index > 70 ? "Alta complejidad" : (p.cognitive_load_index > 40 ? "Moderado" : "Fácil lectura");

      document.getElementById('valValence').innerText = p.emotional_valence > 0 ? "+" + p.emotional_valence : p.emotional_valence;
      document.getElementById('descValence').innerText = p.emotional_valence > 0.1 ? "Constructivo" : (p.emotional_valence < -0.1 ? "Reactivo / Negativo" : "Neutral");

      document.getElementById('valConsistency').innerText = Math.round(p.logical_consistency_score * 100) + "%";
      document.getElementById('descConsistency').innerText = p.logical_consistency_score > 0.75 ? "Sólida" : (p.logical_consistency_score > 0.5 ? "Aceptable" : "Débil");

      // 4. Biases
      const biasesList = document.getElementById('biasesList');
      biasesList.innerHTML = "";

      if (!data.biases_detected || data.biases_detected.length === 0) {
        biasesList.innerHTML = `
          <div class="p-3 rounded-lg border border-emerald-500/20 bg-emerald-950/20 text-xs text-emerald-300 flex items-center gap-2">
            <span>🎉</span>
            <span>No se detectaron sesgos cognitivos evidentes en esta muestra. El texto es objetivo.</span>
          </div>
        `;
      } else {
        data.biases_detected.forEach(b => {
          const colorClass = b.severity === 'high' ? 'border-rose-500/30 bg-rose-950/20 text-rose-200' : 'border-amber-500/30 bg-amber-950/20 text-amber-200';
          const badgeClass = b.severity === 'high' ? 'bg-rose-500/30 text-rose-300' : 'bg-amber-500/30 text-amber-300';
          
          biasesList.innerHTML += `
            <div class="p-3 rounded-xl border ${colorClass} text-xs space-y-1">
              <div class="flex items-center justify-between font-bold">
                <span class="text-sm text-white flex items-center gap-1.5"><span>🎯</span> ${b.bias_name}</span>
                <span class="px-2 py-0.5 rounded text-[10px] uppercase font-extrabold ${badgeClass}">Severidad: ${b.severity} (${Math.round(b.confidence_score * 100)}% certeza)</span>
              </div>
              <p class="text-slate-300 text-[11px] leading-relaxed">${b.explanation}</p>
              ${b.matched_patterns && b.matched_patterns.length > 0 ? `
                <div class="pt-1 flex items-center gap-1 flex-wrap text-[10px] text-slate-400">
                  <span class="font-semibold">Frases que lo delataron:</span>
                  ${b.matched_patterns.map(pat => `<span class="px-1.5 py-0.5 rounded bg-slate-800 text-cyan-300 font-mono">"${pat}"</span>`).join('')}
                </div>
              ` : ''}
            </div>
          `;
        });
      }

      // 5. Mitigations
      const mitList = document.getElementById('mitigationList');
      mitList.innerHTML = "";
      data.mitigation.recommended_interventions.forEach(rec => {
        mitList.innerHTML += `<li>${rec}</li>`;
      });

      const cfBox = document.getElementById('counterfactualBox');
      if (data.mitigation.counterfactual_prompt) {
        cfBox.classList.remove('hidden');
        cfBox.innerHTML = `<b>Ejercicio de Refutación:</b> "${data.mitigation.counterfactual_prompt}"`;
      } else {
        cfBox.classList.add('hidden');
      }
    }
  </script>
</body>
</html>
"""
