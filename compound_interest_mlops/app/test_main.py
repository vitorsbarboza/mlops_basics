import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_calculate_compound_interest_basic():
    payload = {
        "principal": 1000,
        "rate": 12,
        "time": 2,
        "n": 1
    }
    response = client.post("/calculate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["final_amount"] == pytest.approx(1254.4, 0.1)
    assert data["interest_earned"] == pytest.approx(254.4, 0.1)

def test_calculate_zero_interest():
    payload = {
        "principal": 1000,
        "rate": 0,
        "time": 5,
        "n": 1
    }
    response = client.post("/calculate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["final_amount"] == 1000.0
    assert data["interest_earned"] == 0.0

def test_calculate_monthly_compounding():
    payload = {
        "principal": 1000,
        "rate": 12,
        "time": 1,
        "n": 12
    }
    response = client.post("/calculate", json=payload)
    assert response.status_code == 200
    data = response.json()
    # Valor esperado: 1000 * (1 + 0.01)^12
    assert data["final_amount"] == pytest.approx(1126.8, 0.1)
    assert data["interest_earned"] == pytest.approx(126.8, 0.1)

def test_welcome_route():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "mensagem" in data
    assert "como_usar" in data
    assert "exemplo_json" in data
    assert "exemplo_curl" in data
