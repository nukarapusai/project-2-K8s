from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home_returns_success_response() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Project 2 CI/CD working 🚀"}
