"""
Cognitive Agent Evaluator v2.0 - Interactive Hugging Face Space
Engineered by Fabio Torres (neurodeveloper11)
Bilingual Behavioral Telemetry, 10-Axis Cognitive Bias Audit & AI Alignment Mitigation Engine
"""

import asyncio
import json
import plotly.graph_objects as go
import gradio as gr

from src.schemas import EvaluationRequest
from src.agent import CognitiveEvaluationAgent
from src.biases import BIAS_DEFINITIONS

agent = CognitiveEvaluationAgent()

ALL_BIAS_NAMES = list(BIAS_DEFINITIONS.keys())

def create_radar_chart(detected_biases):
    """
    Creates a 10-axis Spider / Radar chart in Plotly visualizing the cognitive distortion profile.
    """
    scores = {}
    for name in ALL_BIAS_NAMES:
        scores[name] = 0.0
        
    for b in detected_biases:
        if b.bias_name in scores:
            weight = 1.0 if b.severity == "high" else 0.65
            scores[b.bias_name] = round(b.confidence_score * weight, 2)
            
    categories = [
        "Confirmation", "Anchoring", "Sunk Cost", "Availability", "Framing",
        "Catastrophizing", "All-or-Nothing", "Overconfidence", "Attribution", "Outcome Bias"
    ]
    values = [
        scores.get("Confirmation Bias", 0),
        scores.get("Anchoring Bias", 0),
        scores.get("Sunk Cost Fallacy", 0),
        scores.get("Availability Heuristic", 0),
        scores.get("Framing Effect", 0),
        scores.get("Catastrophizing", 0),
        scores.get("All-or-Nothing Thinking", 0),
        scores.get("Overconfidence Bias", 0),
        scores.get("Fundamental Attribution Bias", 0),
        scores.get("Outcome Bias", 0),
    ]
    # Close polygon
    categories_closed = categories + [categories[0]]
    values_closed = values + [values[0]]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values_closed,
        theta=categories_closed,
        fill='toself',
        name='Distortion Footprint',
        fillcolor='rgba(99, 102, 241, 0.35)',
        line=dict(color='#4f46e5', width=2.5),
        marker=dict(size=6, color='#4338ca')
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1.0],
                tickvals=[0.25, 0.50, 0.75, 1.0],
                ticktext=["25%", "50%", "75%", "100%"],
                linecolor="#cbd5e1",
                gridcolor="#e2e8f0"
            ),
            angularaxis=dict(
                linecolor="#cbd5e1",
                gridcolor="#e2e8f0"
            )
        ),
        showlegend=False,
        margin=dict(l=40, r=40, t=30, b=30),
        height=380,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    return fig

def evaluate_text_sync(text: str, author_type: str):
    """
    Synchronous wrapper for agent evaluation.
    """
    if not text or len(text.strip()) < 5:
        return (
            "⚠️ Por favor ingresa un texto con al menos 5 caracteres.",
            "N/A", "0.0", "0.0", "0.0", "0.0",
            create_radar_chart([]),
            "<p style='color:#64748b;'>Sin datos suficientes para evaluar.</p>",
            "Sin intervenciones requeridas.",
            "Sin directiva necesaria.",
            "{}"
        )

    author_code = "llm" if "LLM" in author_type else ("human" if "Human" in author_type else "hybrid")
    req = EvaluationRequest(text=text, author_type=author_code)
    result = asyncio.run(agent.evaluate(req))

    # Format KPI badges
    risk_color = "#10b981" if result.mitigation.alignment_risk_level == "nominal" else (
        "#f59e0b" if result.mitigation.alignment_risk_level == "moderate" else "#ef4444"
    )
    risk_html = f"<div style='font-size:22px; font-weight:800; color:{risk_color}; text-transform:uppercase;'>{result.mitigation.alignment_risk_level}</div>"

    cog_load = f"{result.psychometrics.cognitive_load_index} / 100"
    burnout = f"{result.psychometrics.burnout_risk_index} / 100"
    safety = f"{result.psychometrics.psychological_safety_score} / 100"
    valence = f"{result.psychometrics.emotional_valence:+.2f}"

    # Generate Radar Chart
    fig = create_radar_chart(result.biases_detected)

    # Detailed Biases HTML
    if not result.biases_detected:
        biases_html = """
        <div style='background:#f0fdf4; border:1px solid #bbf7d0; border-radius:8px; padding:16px; color:#166534;'>
            <strong>✅ No se detectaron distorsiones cognitivas críticas.</strong>
            <p style='margin-top:4px; font-size:14px;'>El texto muestra un razonamiento balanceado y dentro de parámetros nominales.</p>
        </div>
        """
    else:
        cards = []
        for b in result.biases_detected:
            sev_badge = f"<span style='background:{'#fee2e2' if b.severity=='high' else '#fef3c7'}; color:{'#991b1b' if b.severity=='high' else '#92400e'}; padding:2px 8px; border-radius:4px; font-weight:700; font-size:12px;'>Severidad: {b.severity.upper()}</span>"
            patterns_badges = "".join([f"<code style='background:#f1f5f9; color:#0f172a; padding:2px 6px; border-radius:4px; margin-right:4px; font-size:12px;'>\"{p}\"</code>" for p in b.matched_patterns])
            
            card = f"""
            <div style='background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid {'#ef4444' if b.severity=='high' else '#f59e0b'}; border-radius:8px; padding:14px; margin-bottom:12px;'>
                <div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;'>
                    <span style='font-weight:700; font-size:16px; color:#1e293b;'>🧠 {b.bias_name}</span>
                    <div>{sev_badge} <span style='font-size:12px; color:#64748b; margin-left:6px;'>Confianza: {int(b.confidence_score*100)}%</span></div>
                </div>
                <p style='color:#475569; font-size:14px; margin-bottom:8px;'>{b.explanation}</p>
                <div style='font-size:13px; color:#64748b;'><strong>Disparadores detectados:</strong> {patterns_badges}</div>
            </div>
            """
            cards.append(card)
        biases_html = "".join(cards)

    # Interventions list
    interventions_md = "\n".join([f"- **{i+1}.** {it}" for i, it in enumerate(result.mitigation.recommended_interventions)])
    if result.mitigation.counterfactual_prompt:
        interventions_md += f"\n\n**🔄 Ejercicio Contrafactual de Des-sesgo:**\n> *\"{result.mitigation.counterfactual_prompt}\"*"

    # Red Teaming Directive
    red_teaming = result.mitigation.red_teaming_directive or "No se requiere directiva de red-teaming."

    # Raw JSON
    json_output = json.dumps(result.model_dump(mode="json"), indent=2, ensure_ascii=False)

    return (
        risk_html,
        cog_load,
        burnout,
        safety,
        valence,
        fig,
        biases_html,
        interventions_md,
        red_teaming,
        json_output
    )

CUSTOM_CSS = """
.gradio-container { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important; }
.header-box { background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); color: white; padding: 24px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
.header-title { font-size: 26px; font-weight: 800; margin-bottom: 6px; color: #f8fafc; }
.header-sub { font-size: 14px; color: #cbd5e1; margin-bottom: 12px; }
.badge-link { display: inline-block; background: rgba(255,255,255,0.12); color: #93c5fd; padding: 4px 10px; border-radius: 6px; font-size: 12px; text-decoration: none; margin-right: 8px; font-weight: 600; }
.badge-link:hover { background: rgba(255,255,255,0.22); color: #ffffff; }
"""

with gr.Blocks(css=CUSTOM_CSS, theme=gr.themes.Soft(primary_hue="indigo", neutral_hue="slate")) as demo:
    gr.HTML("""
    <div class="header-box">
        <div class="header-title">🧠 Cognitive Agent Evaluator v2.0</div>
        <div class="header-sub">Autonomous Behavioral Telemetry • 10-Axis Cognitive Distortion Audit • AI Alignment & Debiasing Engine</div>
        <div>
            <a class="badge-link" href="https://www.linkedin.com/in/fabio-torres-39364b258/" target="_blank">👔 Fabio Torres | LinkedIn</a>
            <a class="badge-link" href="https://github.com/neurodeveloper11/cognitive-agent-evaluator" target="_blank">💻 GitHub Repository</a>
            <span class="badge-link" style="color:#a7f3d0;">🎓 M.Sc. Data Engineering & Cloud • 10+ Years Behavioral Science</span>
            <span class="badge-link" style="color:#fde68a;">🚀 Hugging Face v2.0 Live</span>
        </div>
    </div>
    """)

    with gr.Row():
        with gr.Column(scale=5):
            input_text = gr.Textbox(
                label="Texto o Traza de Razonamiento a Evaluar (Español o Inglés)",
                placeholder="Pega aquí el razonamiento de un modelo LLM, un correo laboral, una transcripción de reunión o una decisión de arquitectura...",
                lines=7
            )
            with gr.Row():
                author_type = gr.Dropdown(
                    choices=["LLM Reasoning Trace (Modelo de IA)", "Human Decision Maker (Humano)", "Team Channel / Meeting Transcript (Equipo)"],
                    value="LLM Reasoning Trace (Modelo de IA)",
                    label="Origen del Texto"
                )
                eval_btn = gr.Button("⚡ Auditar Sesgos & Telemetría", variant="primary", scale=1)

            gr.Markdown("### 📌 Casos de Estudio Reales (Prueba en 1 Clic):")
            example_1 = gr.Button("🚨 Caso 1: Incidente Crítico (Catastrofismo & Culpa)")
            example_2 = gr.Button("💼 Caso 2: Inversión Tecnológica (Costo Hundido & Anclaje)")
            example_3 = gr.Button("🤖 Caso 3: Salida LLM con Sobreconfianza & Confirmación")
            example_4 = gr.Button("🌱 Caso 4: Comunicación Resiliente (Control Nominal)")

        with gr.Column(scale=6):
            gr.Markdown("### 📊 Tablero de Telemetría Ejecutiva")
            with gr.Row():
                with gr.Column(scale=1):
                    gr.Markdown("**Riesgo de Alineación:**")
                    risk_output = gr.HTML("<div style='font-size:20px; font-weight:800; color:#10b981;'>NOMINAL</div>")
                with gr.Column(scale=1):
                    cog_output = gr.Textbox(label="Carga Cognitiva", value="0.0", interactive=False)
                with gr.Column(scale=1):
                    burnout_output = gr.Textbox(label="Riesgo Burnout", value="0.0", interactive=False)
                with gr.Column(scale=1):
                    safety_output = gr.Textbox(label="Seguridad Psicológica", value="100.0", interactive=False)
                with gr.Column(scale=1):
                    valence_output = gr.Textbox(label="Valencia Emocional", value="0.0", interactive=False)

            radar_plot = gr.Plot(label="Huella de Distorsión Cognitiva (10 Ejes)")

    with gr.Tabs():
        with gr.TabItem("🔍 Desglose de Sesgos Detectados"):
            biases_display = gr.HTML("<p style='color:#64748b;'>Presiona 'Auditar Sesgos' para ver el diagnóstico detallado.</p>")
        with gr.TabItem("🛡️ Directivas de Mitigación (Fabio Torres)"):
            mitigation_display = gr.Markdown("Las recomendaciones de des-sesgo aparecerán aquí.")
        with gr.TabItem("📋 Prompt de Red-Teaming (Listo para ChatGPT/Claude)"):
            red_teaming_display = gr.Textbox(label="Directiva de Re-prompting para Modelos de IA", lines=5, interactive=False)
        with gr.TabItem("💾 Telemetría JSON (API-Ready)"):
            json_display = gr.Code(label="Respuesta estructurada para consumo en producción", language="json")

    # Wire actions
    eval_btn.click(
        fn=evaluate_text_sync,
        inputs=[input_text, author_type],
        outputs=[
            risk_output, cog_output, burnout_output, safety_output, valence_output,
            radar_plot, biases_display, mitigation_display, red_teaming_display, json_display
        ]
    )

    # Wire Preset Buttons
    sample_1 = "This outage is a total disaster! Everything is broken and ruined, and we are completely doomed because the junior engineers are incompetent and it's entirely their fault! I am completely exhausted and this is urgent, fix it asap!"
    sample_2 = "We have already invested too much into this legacy architecture to turn back now. It would be wasted if we quit. Besides, the initial price estimate was $50,000, so our new budget must be close to that starting figure."
    sample_3 = "This algorithmic solution is 100% guaranteed and impossible to fail. It is obviously true and everyone knows it, so we can safely ignore opposing counterevidence because this confirms what I already knew."
    sample_4 = "The experimental data indicates a 12% improvement in latency under controlled load conditions. We will collaborate together as a team to support the rollout, learn from unexpected edge cases, and maintain transparent, constructive feedback."

    example_1.click(lambda: (sample_1, "Human Decision Maker (Humano)"), outputs=[input_text, author_type]).then(
        fn=evaluate_text_sync, inputs=[input_text, author_type],
        outputs=[risk_output, cog_output, burnout_output, safety_output, valence_output, radar_plot, biases_display, mitigation_display, red_teaming_display, json_display]
    )
    example_2.click(lambda: (sample_2, "Human Decision Maker (Humano)"), outputs=[input_text, author_type]).then(
        fn=evaluate_text_sync, inputs=[input_text, author_type],
        outputs=[risk_output, cog_output, burnout_output, safety_output, valence_output, radar_plot, biases_display, mitigation_display, red_teaming_display, json_display]
    )
    example_3.click(lambda: (sample_3, "LLM Reasoning Trace (Modelo de IA)"), outputs=[input_text, author_type]).then(
        fn=evaluate_text_sync, inputs=[input_text, author_type],
        outputs=[risk_output, cog_output, burnout_output, safety_output, valence_output, radar_plot, biases_display, mitigation_display, red_teaming_display, json_display]
    )
    example_4.click(lambda: (sample_4, "Team Channel / Meeting Transcript (Equipo)"), outputs=[input_text, author_type]).then(
        fn=evaluate_text_sync, inputs=[input_text, author_type],
        outputs=[risk_output, cog_output, burnout_output, safety_output, valence_output, radar_plot, biases_display, mitigation_display, red_teaming_display, json_display]
    )

if __name__ == "__main__":
    demo.launch()
