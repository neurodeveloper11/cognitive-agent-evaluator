"""
Autonomous Cognitive Evaluation Agent.
Implements a deterministic state machine workflow for behavioral auditing and alignment.
"""

import time
import uuid
from typing import Dict, Any, List
from src.schemas import (
    EvaluationRequest,
    EvaluationResult,
    BiasDetection,
    PsychometricMetrics,
    MitigationGuidance
)
from src.biases import analyze_biases
from src.psychometrics import calculate_psychometrics


class CognitiveEvaluationAgent:
    """
    State Graph Agent for evaluating cognitive bias, emotional valence,
    and psychometric telemetry in human and LLM reasoning traces.
    """

    def __init__(self):
        self.agent_name = "CognitiveAgent-v1"

    async def evaluate(self, request: EvaluationRequest) -> EvaluationResult:
        """
        Executes the multi-stage evaluation pipeline.
        """
        start_time = time.perf_counter()
        eval_id = f"eval_{uuid.uuid4().hex[:12]}"

        # Node 1: Parse & Preprocess
        clean_text = request.text.strip()

        # Node 2: Cognitive Bias Audit
        biases = analyze_biases(clean_text)

        # Node 3: Psychometric Telemetry Modeling
        metrics = calculate_psychometrics(clean_text)

        # Node 4: Mitigation & Alignment Synthesis
        mitigation = self._synthesize_mitigation(biases, metrics)

        # Node 5: Package Telemetry Result
        duration_ms = round((time.perf_counter() - start_time) * 1000, 2)

        return EvaluationResult(
            evaluation_id=eval_id,
            author_type=request.author_type,
            biases_detected=biases,
            psychometrics=metrics,
            mitigation=mitigation,
            execution_latency_ms=duration_ms
        )

    def _synthesize_mitigation(
        self,
        biases: List[BiasDetection],
        metrics: PsychometricMetrics
    ) -> MitigationGuidance:
        """
        Synthesizes alignment actions and counterfactual prompts based on detected distortions.
        """
        interventions: List[str] = []
        high_severity_count = sum(1 for b in biases if b.severity == "high")

        # Risk stratification
        if high_severity_count >= 2:
            risk = "critical"
        elif len(biases) > 0 or metrics.logical_consistency_score < 0.5:
            risk = "moderate"
        else:
            risk = "nominal"

        # Formulate interventions
        for b in biases:
            if b.bias_name == "Confirmation Bias":
                interventions.append(
                    "Require red-teaming: Generate 3 disconfirming hypotheses before finalizing decision."
                )
            elif b.bias_name == "Sunk Cost Fallacy":
                interventions.append(
                    "Decouple forward-looking utility from past expenditures. Audit prospective ROI."
                )
            elif b.bias_name == "Anchoring Bias":
                interventions.append(
                    "Re-estimate core quantities using zero-base estimation independent of initial anchor."
                )
            elif b.bias_name == "Availability Heuristic":
                interventions.append(
                    "Gather systematic base-rate statistical data rather than relying on recent anecdotes."
                )
            elif b.bias_name == "Framing Effect":
                interventions.append(
                    "Reframe the decision matrix symmetrically (present both gain and loss scenarios concurrently)."
                )

        if metrics.cognitive_load_index > 75.0:
            interventions.append(
                "High cognitive load detected: Decompose complex sentences into modular premises."
            )

        if not interventions:
            interventions.append("Reasoning trace appears balanced and within nominal alignment parameters.")

        counterfactual = (
            f"Please reconsider this argument from a null hypothesis perspective: assume the opposite conclusion is true "
            f"and list what concrete empirical evidence would be required to validate it."
        ) if biases else None

        return MitigationGuidance(
            alignment_risk_level=risk,
            recommended_interventions=interventions,
            counterfactual_prompt=counterfactual
        )
