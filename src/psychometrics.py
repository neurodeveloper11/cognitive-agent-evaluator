"""
Psychometric Modeling & Behavioral Telemetry Calculations.
Applies cognitive science formulas to quantify textual reasoning dynamics.
"""

import re
from typing import Dict
from src.schemas import PsychometricMetrics

POSITIVE_LEXICON = {
    "effective", "optimal", "rigorous", "evidence", "proven", "benefit",
    "solution", "validated", "constructive", "systematic", "accurate", "resilient"
}

NEGATIVE_LEXICON = {
    "catastrophic", "failure", "hopeless", "impossible", "ruined", "disaster",
    "terrible", "toxic", "regret", "fault", "useless", "panic"
}

HEDGING_TOKENS = {
    "maybe", "perhaps", "possibly", "probably", "might", "could", "somewhat",
    "unclear", "guess", "suppose", "fairly", "seemingly"
}

LOGICAL_CONNECTIVES = {
    "therefore", "consequently", "because", "furthermore", "thus", "however",
    "nevertheless", "accordingly", "specifically", "in contrast"
}


def calculate_psychometrics(text: str) -> PsychometricMetrics:
    """
    Computes multidimensional psychometric metrics on the evaluated text.
    """
    words = re.findall(r"\b\w+\b", text.lower())
    total_words = max(len(words), 1)
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    total_sentences = max(len(sentences), 1)

    # 1. Cognitive Load Index (0 - 100)
    # Estimated through sentence length, complex word ratio (>6 chars), and density
    avg_sentence_len = total_words / total_sentences
    long_words = [w for w in words if len(w) > 6]
    complex_word_ratio = len(long_words) / total_words

    # Formula: normalized composite score
    raw_load = (avg_sentence_len * 2.0) + (complex_word_ratio * 70.0)
    cognitive_load_index = round(min(max(raw_load, 5.0), 100.0), 2)

    # 2. Emotional Valence (-1.0 to +1.0)
    pos_count = sum(1 for w in words if w in POSITIVE_LEXICON)
    neg_count = sum(1 for w in words if w in NEGATIVE_LEXICON)
    
    if pos_count == 0 and neg_count == 0:
        emotional_valence = 0.0
    else:
        emotional_valence = round((pos_count - neg_count) / (pos_count + neg_count + 1), 3)

    # 3. Ambiguity Ratio (0.0 to 1.0)
    hedge_count = sum(1 for w in words if w in HEDGING_TOKENS)
    ambiguity_ratio = round(min(hedge_count / total_words, 1.0), 3)

    # 4. Logical Consistency Score (0.0 to 1.0)
    connective_count = sum(1 for w in words if w in LOGICAL_CONNECTIVES)
    base_consistency = 0.65
    connective_boost = min(connective_count * 0.06, 0.30)
    ambiguity_penalty = ambiguity_ratio * 0.40
    logical_consistency_score = round(
        min(max(base_consistency + connective_boost - ambiguity_penalty, 0.1), 1.0),
        2
    )

    return PsychometricMetrics(
        cognitive_load_index=cognitive_load_index,
        emotional_valence=emotional_valence,
        logical_consistency_score=logical_consistency_score,
        ambiguity_ratio=ambiguity_ratio
    )
