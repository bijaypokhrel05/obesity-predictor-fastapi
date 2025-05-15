from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_obese():
    response = client.post("/predict", json={"height": 170, "weight": 90})
    assert response.status_code == 200
    assert "obese" in response.json()
