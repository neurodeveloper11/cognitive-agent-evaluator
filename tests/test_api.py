"""
Integration tests for Cognitive Agent Evaluator FastAPI endpoints.
"""

import pytest
from fastapi.testclient import TestClient
from src.api import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client


def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Cognitive Agent Evaluator" in response.text
    assert "Fabio Torres" in response.text


def test_info_endpoint(client):
    response = client.get("/api/v1/info")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "operational"
    assert "Fabio Torres" in data["author"]


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "Confirmation Bias" in data["supported_biases"]


def test_taxonomy_endpoint(client):
    response = client.get("/api/v1/taxonomy/biases")
    assert response.status_code == 200
    data = response.json()
    assert "Sunk Cost Fallacy" in data
    assert data["Sunk Cost Fallacy"]["severity"] == "high"


def test_evaluate_endpoint(client):
    payload = {
        "text": "We cannot stop now because we already poured millions into this infrastructure and it would be wasted if we quit.",
        "author_type": "human"
    }
    response = client.post("/api/v1/evaluate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["author_type"] == "human"
    assert any(b["bias_name"] == "Sunk Cost Fallacy" for b in data["biases_detected"])
    assert "psychometrics" in data
    assert data["psychometrics"]["cognitive_load_index"] > 0


def test_batch_evaluate_endpoint(client):
    payload = [
        {"text": "We already invested too much to turn back now."},
        {"text": "The empirical findings show systematic accuracy across all trial groups."}
    ]
    response = client.post("/api/v1/benchmark/batch-eval", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
