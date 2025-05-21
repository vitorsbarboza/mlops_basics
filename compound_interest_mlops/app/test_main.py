import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_calculate_compound_interest():
    payload = {
        "principal": 1000,
        "rate": 10,
        "time": 2,
        "n": 1
    }
    response = client.post("/calculate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["final_amount"] == 1210.0
    assert data["interest_earned"] == 210.0

def test_zero_interest():
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
