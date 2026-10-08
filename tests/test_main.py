from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "Online"

def test_defect_density_excellent():
    payload = {"lines_of_code": 5000, "defects_found": 2}
    response = client.post("/api/v1/metrics/density", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["defect_density"] == 0.4
    assert data["quality_level"] == "EXCELENTE"

def test_defect_density_critical():
    payload = {"lines_of_code": 1000, "defects_found": 5}
    response = client.post("/api/v1/metrics/density", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["defect_density"] == 5.0
    assert data["quality_level"] == "CRITICO"