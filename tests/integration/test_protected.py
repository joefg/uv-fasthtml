from starlette.testclient import TestClient

from app.main import app


def mock_auth(client):
   client.get("/auth/oauth-redirect?code=mock-code-123")
   return client


class TestProtected:
    def test_unauthenticated_protected_returns_404(self):
        client = TestClient(app)
        request = client.get("/protected/test.txt")
        assert request.status_code == 404

    def test_authenticated_protected_returns_200(self):
        client = TestClient(app)
        # log in using integration_test
        authenticated_client = mock_auth(client)
        # then get this resource
        request = authenticated_client.get("/protected/test.txt")
        assert request.status_code == 200
