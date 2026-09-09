"""
Unit tests for Cognitive Bias Detection Engine.
"""

from src.biases import analyze_biases


def test_confirmation_bias_detection():
    sample = "This is obviously true and everyone knows it. We can safely ignore opposing counterevidence because this confirms what I already knew."
    detections = analyze_biases(sample)
    bias_names = [d.bias_name for d in detections]
    assert "Confirmation Bias" in bias_names
    
    cb = next(d for d in detections if d.bias_name == "Confirmation Bias")
    assert cb.severity == "high"
    assert cb.confidence_score >= 0.60


def test_sunk_cost_detection():
    sample = "We have already invested too much into this project to turn back now. It would be wasted if we quit."
    detections = analyze_biases(sample)
    bias_names = [d.bias_name for d in detections]
    assert "Sunk Cost Fallacy" in bias_names


def test_clean_rational_text_no_biases():
    sample = "The experimental data indicates a 12% improvement in latency under controlled load conditions."
    detections = analyze_biases(sample)
    assert len(detections) == 0
