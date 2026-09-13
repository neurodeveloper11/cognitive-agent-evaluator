"""
Unit tests for Psychometric Modeling Calculations.
"""

from src.psychometrics import calculate_psychometrics
from src.schemas import PsychometricMetrics


def test_psychometrics_calculation_positive():
    text = "The solution is validated, rigorous, highly optimal and constructive for the architecture."
    metrics = calculate_psychometrics(text)
    assert isinstance(metrics, PsychometricMetrics)
    assert metrics.emotional_valence > 0.0
    assert metrics.logical_consistency_score >= 0.50
    assert metrics.cognitive_load_index > 0.0


def test_psychometrics_calculation_hedging():
    text = "Maybe we might perhaps consider this, although it is somewhat unclear and probably not optimal."
    metrics = calculate_psychometrics(text)
    assert metrics.ambiguity_ratio > 0.15
    assert metrics.logical_consistency_score < 0.70


def test_burnout_and_safety_metrics():
    stressed_text = "I am completely exhausted and burned out! This is urgent, do it asap! Stop blaming everyone."
    metrics = calculate_psychometrics(stressed_text)
    assert metrics.burnout_risk_index >= 40.0
    assert metrics.psychological_safety_score <= 60.0

