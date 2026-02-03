from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_people_list():
    response = client.get("/people/", headers={
        "Authorization": "Bearer fake-token"
    })
    assert response.status_code in [200, 401]
