import pytest
from starlette.testclient import TestClient

from app.main import app

from utils import mock_auth, set_test_user_admin

@pytest.fixture(autouse=True)
def setup():
    set_test_user_admin(True)
    yield

def test_unauthenticated_users_cant_see_admin():
    client = TestClient(app)
    request = client.get("/admin")
    assert request.status_code == 404

def test_authenticated_users_no_admin_returns_401():
    client = TestClient(app)
    authenticated_client = mock_auth(client)
    set_test_user_admin(False)
    request = authenticated_client.get("/admin")
    assert request.status_code == 401

def test_authenticated_admins_returns_ok():
    client = TestClient(app)
    authenticated_client = mock_auth(client)
    request = authenticated_client.get("/admin")
    assert request.status_code == 200

def test_authenticated_admins_can_see_user():
    client = TestClient(app)
    authenticated_client = mock_auth(client)
    request = authenticated_client.get("/admin/user/459")
    assert request.status_code == 200

def test_authenticated_non_admins_cant_see_user():
    client = TestClient(app)
    authenticated_client = mock_auth(client)
    set_test_user_admin(False)
    request = authenticated_client.get("/admin/user/459")
    assert request.status_code == 401
