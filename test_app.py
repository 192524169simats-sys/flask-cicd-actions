
from app import app

def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert "message" in response.get_json()

def test_health():
    response = app.test_client().get("/health")
    assert response.get_json()["status"] == "UP"
