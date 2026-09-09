"""
Cognitive Bias Detection Engine.
Rules, pattern matching, and psychometric heuristics for identifying cognitive distortions (EN/ES).
"""

import re
from typing import List
from src.schemas import BiasDetection

BIAS_DEFINITIONS = {
    "Confirmation Bias": {
        "spanish_name": "Sesgo de Confirmación",
        "patterns": [
            r"\b(obviously|unquestionably|no doubt|everyone knows|cannot be wrong)\b",
            r"\b(obviamente|es obvio|sin duda|todos saben|no hay duda|no puede estar mal)\b",
            r"\b(disregard|ignore|dismiss)\b.*\b(counterevidence|contradict|alternative|opposing)\b",
            r"\b(ignorar|descartar|rechazar|despreciar)\b.*\b(pruebas|evidencia|contraria|opuesta|alternativa)\b",
            r"\b(only proves|proves my point|confirms what i already knew)\b",
            r"\b(solo demuestra|prueba mi punto|confirma lo que ya sab[ií]a)\b",
            r"\b(no need to look further|needless to verify|no hay necesidad de verificar)\b"
        ],
        "explanation": "Selective overweighting of confirming evidence while ignoring or rejecting disconfirming data points (Sobrevaloración selectiva de evidencias que confirman la creencia previa, descartando pruebas en contra).",
        "severity": "high"
    },
    "Anchoring Bias": {
        "spanish_name": "Sesgo de Anclaje",
        "patterns": [
            r"\b(initial price|first number|starting figure|original estimate)\b.*\b(must be close to|dictates|anchors)\b",
            r"\b(precio inicial|primera cifra|n[uú]mero inicial|primer precio|estimaci[oó]n original)\b.*\b(debe estar cerca|dicta|ancla)\b",
            r"\b(since they asked for|started at)\b.*\b(we should offer around)\b",
            r"\b(como pidieron|empez[oó] en)\b.*\b(debemos ofrecer cerca)\b",
            r"\b(can't deviate much from the initial|no podemos alejarnos del inicial)\b"
        ],
        "explanation": "Disproportionate cognitive reliance on the first piece of information encountered when making subsequent estimates (Dependencia desmedida de la primera información o número recibido para juzgar estimaciones posteriores).",
        "severity": "medium"
    },
    "Sunk Cost Fallacy": {
        "spanish_name": "Falacia del Costo Hundido",
        "patterns": [
            r"\b(invested too much|spent so much time|already paid for|too late to turn back)\b",
            r"\b(ya invert[ií] demasiado|ya gast[eé] mucho|mucho tiempo invertido|demasiado dinero|muy tarde para volver atr[aá]s)\b",
            r"\b(can't stop now after|poured millions into|wasted if we quit)\b",
            r"\b(no podemos parar ahora|le metimos millones|ser[ií]a una p[eé]rdida dejarlo|desperdicio si lo dejamos)\b",
            r"\b(must keep going because of our past investment|debemos seguir por todo lo que ya pusimos)\b"
        ],
        "explanation": "Justifying continued resource allocation based on past non-recoverable expenditures rather than prospective future value (Justificar continuar un proyecto fallido solo por los recursos que ya se gastaron y no se recuperarán).",
        "severity": "high"
    },
    "Availability Heuristic": {
        "spanish_name": "Heurística de Disponibilidad",
        "patterns": [
            r"\b(i just saw|in the news yesterday|happened to my friend|comes to mind immediately)\b",
            r"\b(acabo de ver|sali[oó] en las noticias ayer|le pas[oó] a un amigo|se me viene a la mente|lo primero que pienso)\b",
            r"\b(everyone is talking about|so common nowadays because of this one case)\b",
            r"\b(todo el mundo habla de esto|es muy com[uú]n por este caso)\b",
            r"\b(first thing that pops into my head)\b"
        ],
        "explanation": "Overestimating the probability of an event based on the cognitive ease with which recent or emotional examples come to mind (Sobrestimar la probabilidad de un suceso solo porque es el primer ejemplo emocional o reciente que recordamos).",
        "severity": "medium"
    },
    "Framing Effect": {
        "spanish_name": "Efecto Encuadre",
        "patterns": [
            r"\b(only look at the downside|ignore the gain|framed solely as a loss)\b",
            r"\b(solo mira la p[eé]rdida|ignora la ganancia|presentado como p[eé]rdida)\b",
            r"\b(100% loss vs 0% gain|pure disaster|desastre total|pura p[eé]rdida)\b",
            r"\b(depending on how you word it, it changes completely|seg[uú]n como se diga cambia todo)\b"
        ],
        "explanation": "Drawing divergent conclusions from identical information depending entirely on whether it is presented as a gain or a loss (Tomar decisiones opuestas sobre la misma realidad según se presente como ganancia o como pérdida).",
        "severity": "medium"
    }
}


def analyze_biases(text: str) -> List[BiasDetection]:
    """
    Evaluates input text against known cognitive bias heuristics (bilingual EN/ES).
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
