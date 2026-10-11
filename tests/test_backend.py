import sys
from pathlib import Path

from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.main import app

client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_diagnose_endpoint() -> None:
    response = client.post("/api/diagnose", json={"target": "google.com"})
    assert response.status_code == 200
    payload = response.json()
    assert "summary" in payload
    assert "recommendations" in payload
    assert isinstance(payload["recommendations"], list)
