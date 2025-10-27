from starlette.testclient import TestClient

from app.main import app

from utils import mock_auth

def test_unauthenticated_logbook_returns_ok():
    client = TestClient(app)
    request = client.get("/logbook")
    assert request.status_code == 200

def test_authenticated_logbook_returns_ok():
    client = TestClient(app)
    authenticated_client = mock_auth(client)
    request = authenticated_client.get("/logbook")
    assert request.status_code == 200

def test_unauthenticated_users_cannot_submit():
    client = TestClient(app)
    params = {
        "content": "hello world!"
    }
    request = client.post("/logbook/submit", data=params)
    assert request.status_code == 404

def test_authenticated_users_can_submit():
    client = TestClient(app)
    authenticated_client = mock_auth(client)
    params = {
        "content": "hello world!"
    }
    request = authenticated_client.post("/logbook/submit", data=params)
    assert request.status_code == 200
