from starlette.testclient import TestClient

from app.main import app


def mock_auth(client):
   client.get("/auth/oauth-redirect?code=mock-code-123")
   return client


class TestAuth:
    def test_login_unauthenticated_returns_ok(self):
        client = TestClient(app)
        request = client.get("/auth/login")
        assert request.status_code == 200

    def test_oauth_register_user(self):
        client = TestClient(app)
        args = "code=mock-code-123"
        request = client.get("/auth/oauth-redirect?" + args)
        assert request.status_code == 200

    def test_oauth_redirect_inactive_user(self):
        pass

    def test_logout_authenticated_user(self):
        client = TestClient(app)
        authenticated_client = mock_auth(client)
        request = authenticated_client.get("/auth/logout")
        assert request.status_code == 200
