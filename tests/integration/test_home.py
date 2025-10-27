from starlette.testclient import TestClient

from app.main import app

def test_home_returns_ok():
    client = TestClient(app)
    request = client.get("/")
    assert request.status_code == 200
