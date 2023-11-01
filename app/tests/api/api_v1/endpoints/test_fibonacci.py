from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_fibonacci():
    response = client.get("/api/v1/10")
    assert response.status_code == 200
    assert response.json() == {"result": 55}


def test_read_fibonacci_invalid_input():
    response = client.get("/api/v1/-5")
    assert response.status_code == 422


def test_read_fibonacci_edge_case():
    response = client.get("/api/v1/1")
    assert response.status_code == 200
    assert response.json() == {"result": 1}
