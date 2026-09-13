"""
Pydantic v2 Schemas for Cognitive Evaluation & Behavioral Telemetry.
"""

from datetime import datetime, timezone
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


def utc_now():
    return datetime.now(timezone.utc)


class EvaluationRequest(BaseModel):
    """Payload for submitting text/transcript for cognitive evaluation."""
    text: str = Field(..., min_length=5, description="Transcript or reasoning chain to evaluate")
    context: Optional[str] = Field(default=None, description="Surrounding conversational context or task description")
    author_type: str = Field(default="llm", description="Source: 'llm', 'human', or 'hybrid'")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Arbitrary execution metadata")


class BiasDetection(BaseModel):
    """Quantified instance of an identified cognitive bias."""
    bias_name: str = Field(..., description="E.g., Confirmation Bias, Anchoring, Sunk Cost")
    severity: str = Field(..., description="'low', 'medium', or 'high'")
    confidence_score: float = Field(..., ge=0.0, le=1.0, description="Model confidence in bias detection")
    explanation: str = Field(..., description="Cognitive explanation of why this bias was identified")
    matched_patterns: List[str] = Field(default_factory=list, description="Specific triggers or phrases matched")


class PsychometricMetrics(BaseModel):
    """Psychometric & behavioral telemetry dimensions."""
    cognitive_load_index: float = Field(..., ge=0.0, le=100.0, description="Estimated cognitive processing load (0-100)")
    emotional_valence: float = Field(..., ge=-1.0, le=1.0, description="Valence spectrum (-1.0 negative to +1.0 positive)")
    logical_consistency_score: float = Field(..., ge=0.0, le=1.0, description="Coherence and argument validity ratio")
    ambiguity_ratio: float = Field(..., ge=0.0, le=1.0, description="Proportion of vague or hedging phrases")
    burnout_risk_index: float = Field(default=0.0, ge=0.0, le=100.0, description="Occupational burnout & cognitive fatigue risk score (0-100)")
    psychological_safety_score: float = Field(default=100.0, ge=0.0, le=100.0, description="Psychological safety index in reasoning (0-100)")


class MitigationGuidance(BaseModel):
    """Actionable recommendations for AI alignment and human debiasing."""
    alignment_risk_level: str = Field(..., description="'nominal', 'moderate', or 'critical'")
    recommended_interventions: List[str] = Field(default_factory=list)
    counterfactual_prompt: Optional[str] = Field(default=None, description="Suggested reframing prompt")
    red_teaming_directive: Optional[str] = Field(default=None, description="Ready-to-use prompt directive for ChatGPT/Claude debiasing")


class EvaluationResult(BaseModel):
    """Complete evaluation report issued by the cognitive agent."""
    evaluation_id: str
    timestamp: datetime = Field(default_factory=utc_now)
    author_type: str
    biases_detected: List[BiasDetection]
    psychometrics: PsychometricMetrics
    mitigation: MitigationGuidance
    execution_latency_ms: float
