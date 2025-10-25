from starlette.testclient import TestClient

from app.main import app

class TestProtected:
    def test_unauthenticated_protected_returns_404(self):
        client = TestClient(app)
        request = client.get("/protected/.gitkeep")
        assert request.status_code == 404

    def test_authenticated_protected_returns_200(self):
        cookies = {"session_name" : "session_value"}
        client = TestClient(app, cookies=cookies)
        request = client.get("/protected/.gitkeep")
        assert request.status_code == 200
