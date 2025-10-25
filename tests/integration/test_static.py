from starlette.testclient import TestClient

from app.main import app

class TestStatic:
    def test_unauthenticated_static_returns_ok(self):
        client = TestClient(app)
        request = client.get("/static/styles.css")
        assert request.status_code == 200
