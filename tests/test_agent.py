"""
Unit tests for Cognitive Evaluation Agent State Machine.
"""

import asyncio
from src.agent import CognitiveEvaluationAgent
from src.schemas import EvaluationRequest, EvaluationResult


def test_agent_evaluation_workflow():
    agent = CognitiveEvaluationAgent()
    request = EvaluationRequest(
        text="It is obviously true that our first model cannot be wrong, so we disregard opposing counterevidence because this confirms what I already knew.",
        author_type="llm"
    )

    result = asyncio.run(agent.evaluate(request))
    assert isinstance(result, EvaluationResult)
    assert result.evaluation_id.startswith("eval_")
    assert len(result.biases_detected) >= 1
    assert result.mitigation.alignment_risk_level in ["moderate", "critical"]
    assert result.mitigation.counterfactual_prompt is not None
    assert result.execution_latency_ms >= 0
