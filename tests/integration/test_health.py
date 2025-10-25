from unittest import mock

from starlette.testclient import TestClient

from app.main import app

class TestHealth:
    def test_health_returns_ok(self):
        client = TestClient(app)
        request = client.get("/health/")
        assert request.status_code == 200
        assert request.text == '{"database":"ok"}'
