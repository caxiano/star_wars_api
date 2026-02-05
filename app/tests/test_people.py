from fastapi.testclient import TestClient

from app.config import settings
from app.main import app

settings.TESTING = True


client = TestClient(app)


def test_people_unauthorized():
    response = client.get("/api/people/")
    assert response.status_code == 401


def test_people_with_valid_token():
    # Obter token de autenticação (ajuste o payload conforme necessário para seu endpoint de login)
    login = client.post("/auth/login", json={})
    assert login.status_code == 200
    token = login.json().get("access_token")
    assert token

    response = client.get(
        "/api/people/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
