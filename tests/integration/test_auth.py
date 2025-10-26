import pytest
from starlette.testclient import TestClient

from app.main import app
from utils import mock_auth, set_test_user_active


@pytest.fixture(autouse=True)
def setup():
    set_test_user_active(True)

def test_login_unauthenticated_returns_ok():
    client = TestClient(app)
    request = client.get("/auth/login")
    assert request.status_code == 200

def test_oauth_register_user():
    client = TestClient(app)
    args = "code=mock-code-123"
    request = client.get("/auth/oauth-redirect?" + args)
    assert request.status_code == 200

def test_oauth_redirect_inactive_user():
    set_test_user_active(False)
    client = TestClient(app)
    args = "code=mock-code-123"
    request = client.get("/auth/oauth-redirect?" + args)
    assert request.status_code == 200

def test_logout_authenticated_user():
    client = TestClient(app)
    authenticated_client = mock_auth(client)
    request = authenticated_client.get("/auth/logout")
    assert request.status_code == 200
