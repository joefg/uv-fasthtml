from starlette.testclient import TestClient

from app.main import app

class TestAuth:
    def test_login_unauthenticated_returns_ok(self):
        client = TestClient(app)
        request = client.get("/auth/login")
        assert request.status_code == 200

    def test_oauth_redirect_active_user(self):
        pass

    def test_oauth_redirect_inactive_user(self):
        pass

    def test_logout_authenticated_user(self):
        client = TestClient(app)
        request = client.get("/auth/logout")
        assert request.status_code == 200


