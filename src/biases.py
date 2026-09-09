"""
Cognitive Bias Detection Engine.
Rules, pattern matching, and psychometric heuristics for identifying cognitive distortions.
"""

import re
from typing import List
from src.schemas import BiasDetection

BIAS_DEFINITIONS = {
    "Confirmation Bias": {
        "patterns": [
            r"\b(obviously|unquestionably|no doubt|everyone knows|cannot be wrong)\b",
            r"\b(disregard|ignore|dismiss)\b.*\b(counterevidence|contradict|alternative|opposing)\b",
            r"\b(only proves|proves my point|confirms what i already knew)\b",
            r"\b(no need to look further|needless to verify)\b"
        ],
        "explanation": "Selective overweighting of confirming evidence while ignoring or rejecting disconfirming data points.",
        "severity": "high"
    },
    "Anchoring Bias": {
        "patterns": [
            r"\b(initial price|first number|starting figure|original estimate)\b.*\b(must be close to|dictates|anchors)\b",
            r"\b(since they asked for|started at)\b.*\b(we should offer around)\b",
            r"\b(can't deviate much from the initial)\b"
        ],
        "explanation": "Disproportionate cognitive reliance on the first piece of information encountered when making subsequent estimates.",
        "severity": "medium"
    },
    "Sunk Cost Fallacy": {
        "patterns": [
            r"\b(invested too much|spent so much time|already paid for|too late to turn back)\b",
            r"\b(can't stop now after|poured millions into|wasted if we quit)\b",
            r"\b(must keep going because of our past investment)\b"
        ],
        "explanation": "Justifying continued resource allocation based on past non-recoverable expenditures rather than prospective future value.",
        "severity": "high"
    },
    "Availability Heuristic": {
        "patterns": [
            r"\b(i just saw|in the news yesterday|happened to my friend|comes to mind immediately)\b",
            r"\b(everyone is talking about|so common nowadays because of this one case)\b",
            r"\b(first thing that pops into my head)\b"
        ],
        "explanation": "Overestimating the probability of an event based on the cognitive ease with which recent or emotional examples come to mind.",
        "severity": "medium"
    },
    "Framing Effect": {
        "patterns": [
            r"\b(only look at the downside|ignore the gain|framed solely as a loss)\b",
            r"\b(100% loss vs 0% gain|pure disaster)\b",
            r"\b(depending on how you word it, it changes completely)\b"
        ],
        "explanation": "Drawing divergent conclusions from identical information depending entirely on whether it is presented as a gain or a loss.",
        "severity": "medium"
    }
}


def analyze_biases(text: str) -> List[BiasDetection]:
    """
    Evaluates input text against known cognitive bias heuristics.
    Returns structured detections with confidence scoring.
    """
    detections: List[BiasDetection] = []
    lower_text = text.lower()

    for bias_name, meta in BIAS_DEFINITIONS.items():
        matched_triggers: List[str] = []
        for pattern in meta["patterns"]:
            matches = re.findall(pattern, lower_text)
            if matches:
                if isinstance(matches[0], tuple):
                    matched_triggers.extend([m for m in matches[0] if m])
                else:
                    matched_triggers.extend(matches)

        if matched_triggers:
            # Confidence calculated by frequency and coverage
            confidence = min(0.60 + (len(matched_triggers) * 0.15), 0.98)
            detections.append(
                BiasDetection(
                    bias_name=bias_name,
                    severity=meta["severity"],
                    confidence_score=round(confidence, 2),
                    explanation=meta["explanation"],
                    matched_patterns=list(set(matched_triggers))
                )
            )

    return detections
