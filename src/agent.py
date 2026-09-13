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
        self.agent_name = "CognitiveAgent-v2"

    async def evaluate(self, request: EvaluationRequest) -> EvaluationResult:
        """
        Executes the multi-stage evaluation pipeline.
        """
        start_time = time.perf_counter()
        eval_id = f"eval_{uuid.uuid4().hex[:12]}"

        # Node 1: Parse & Preprocess
        clean_text = request.text.strip()

        # Node 2: Cognitive Bias Audit (10-axis engine)
        biases = analyze_biases(clean_text)

        # Node 3: Psychometric & Occupational Telemetry Modeling
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
        if high_severity_count >= 2 or metrics.burnout_risk_index > 75.0 or metrics.psychological_safety_score < 30.0:
            risk = "critical"
        elif len(biases) > 0 or metrics.logical_consistency_score < 0.5 or metrics.burnout_risk_index > 45.0:
            risk = "moderate"
        else:
            risk = "nominal"

        # Formulate interventions across all 10 biases
        for b in biases:
            if b.bias_name == "Confirmation Bias":
                interventions.append(
                    "Require red-teaming: Generate 3 disconfirming hypotheses before finalizing decision."
                )
            elif b.bias_name == "Sunk Cost Fallacy":
                interventions.append(
                    "Decouple forward-looking utility from past expenditures. Audit prospective ROI independently."
                )
            elif b.bias_name == "Anchoring Bias":
                interventions.append(
                    "Re-estimate core quantities using zero-base estimation independent of initial anchor values."
                )
            elif b.bias_name == "Availability Heuristic":
                interventions.append(
                    "Gather systematic base-rate statistical distributions rather than relying on salient recent anecdotes."
                )
            elif b.bias_name == "Framing Effect":
                interventions.append(
                    "Reframe decision matrix symmetrically: present gain scenarios and loss scenarios side by side."
                )
            elif b.bias_name == "Catastrophizing":
                interventions.append(
                    "Apply cognitive de-catastrophizing: Quantify true probability (P<5%) and establish bounded containment plans."
                )
            elif b.bias_name == "All-or-Nothing Thinking":
                interventions.append(
                    "Introduce continuum thinking: Replace binary dichotomies with iterative milestone metrics (0-100%)."
                )
            elif b.bias_name == "Overconfidence Bias":
                interventions.append(
                    "Implement pre-mortem audit: Assume project failure in 6 months and document exact failure modes."
                )
            elif b.bias_name == "Fundamental Attribution Bias":
                interventions.append(
                    "Shift focus to blameless root-cause analysis (Ishikawa/5-Whys): Examine system architecture and tooling."
                )
            elif b.bias_name == "Outcome Bias":
                interventions.append(
                    "Separate process quality from stochastic noise: Audit expected value (EV) at time of decision."
                )

        if metrics.burnout_risk_index > 65.0:
            interventions.append(
                "High occupational fatigue & urgency detected: Enforce asynchronous cooldown and reduce message velocity."
            )

        if metrics.psychological_safety_score < 45.0:
            interventions.append(
                "Low psychological safety profile: Reframe critique into collaborative inquiry and remove personal attribution."
            )

        if metrics.cognitive_load_index > 75.0:
            interventions.append(
                "High cognitive load detected: Decompose complex compound arguments into modular bullet premises."
            )

        if not interventions:
            interventions.append("Reasoning trace appears balanced, resilient, and within nominal cognitive parameters.")

        counterfactual = (
            f"Please reconsider this argument from a null hypothesis perspective: assume the opposite conclusion is true "
            f"and list what concrete empirical evidence would be required to validate it."
        ) if biases else None

        # Synthesize ready-to-use LLM debiasing directive
        bias_names = [b.bias_name for b in biases]
        if bias_names:
            red_teaming = (
                f"[SYSTEM DIRECTIVE: REASONING ALIGNMENT & DEBIASING]\n"
                f"The following reasoning trace exhibited tendencies toward: {', '.join(bias_names)}.\n"
                f"Instructions: Re-evaluate this conclusion by strictly adopting a neutral, adversary perspective.\n"
                f"1. Identify and state 3 factual counter-arguments that disprove the primary premise.\n"
                f"2. Separate past non-recoverable costs from prospective marginal utility.\n"
                f"3. Frame the scenario with symmetric gain/loss matrices and state expected value (EV) with explicit uncertainty intervals."
            )
        else:
            red_teaming = "[SYSTEM DIRECTIVE] No critical biases identified. Maintain structured, evidence-based reasoning."

        return MitigationGuidance(
            alignment_risk_level=risk,
            recommended_interventions=interventions,
            counterfactual_prompt=counterfactual,
            red_teaming_directive=red_teaming
        )
