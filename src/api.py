"""
FastAPI REST API for Cognitive Agent Evaluator.
"""

from typing import List, Dict, Any
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from src.schemas import EvaluationRequest, EvaluationResult
from src.agent import CognitiveEvaluationAgent
from src.biases import BIAS_DEFINITIONS

agent = CognitiveEvaluationAgent()

app = FastAPI(
    title="Cognitive Agent Evaluator & Behavioral Telemetry API",
    description="Autonomous Agent for evaluating cognitive biases, emotional valence, and psychometric alignment in human & LLM reasoning. Engineered by Fabio Torres (neurodeveloper11).",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["General"])
async def root():
    return {
        "project": "Cognitive Agent Evaluator & Behavioral Telemetry Engine",
        "author": "Fabio Torres (neurodeveloper11)",
        "docs": "/docs",
        "health": "/health",
        "status": "operational"
    }


@app.get("/health", tags=["Monitoring"])
async def health_check():
    return {
        "status": "healthy",
        "agent": agent.agent_name,
        "supported_biases": list(BIAS_DEFINITIONS.keys())
    }


@app.post(
    "/api/v1/evaluate",
    response_model=EvaluationResult,
    status_code=status.HTTP_200_OK,
    tags=["Agent Evaluation"]
)
async def evaluate_text(payload: EvaluationRequest):
    """
    Submits a text trace or LLM output for cognitive bias detection,
    psychometric telemetry scoring, and alignment mitigation.
    """
    try:
        return await agent.evaluate(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/v1/taxonomy/biases", tags=["Taxonomy"])
async def get_bias_taxonomy() -> Dict[str, Any]:
    """
    Returns the supported cognitive bias taxonomy, heuristics, and severity levels.
    """
    return {
        bias: {
            "severity": meta["severity"],
            "explanation": meta["explanation"]
        }
        for bias, meta in BIAS_DEFINITIONS.items()
    }


@app.post(
    "/api/v1/benchmark/batch-eval",
    response_model=List[EvaluationResult],
    tags=["Agent Evaluation"]
)
async def batch_evaluate(requests: List[EvaluationRequest]):
    """
    Batch processes multiple text traces for benchmark evaluation.
    """
    if len(requests) > 50:
        raise HTTPException(status_code=400, detail="Maximum batch size is 50 requests.")

    results: List[EvaluationResult] = []
    for req in requests:
        res = await agent.evaluate(req)
        results.append(res)
    return results
