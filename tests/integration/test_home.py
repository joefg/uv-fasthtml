from unittest import mock

from starlette.testclient import TestClient

from app.main import app

class TestHome:
    def test_home_returns_ok(self):
        client = TestClient(app)
        request = client.get("/")
        assert request.status_code == 200
