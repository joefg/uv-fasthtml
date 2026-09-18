import json
import lxml.html as lx
import pytest
from starlette.testclient import TestClient

from app.main import app

from utils import mock_auth, set_test_user_admin

def extract_hx_hdr(html: str):
    html_tag = lx.fromstring(html).xpath('/html')[0]
    assert 'hx-headers' in html_tag.attrib
    hx_hdr = html_tag.xpath('/html')[0].attrib['hx-headers']
    return json.loads(hx_hdr)


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

def test_authenticated_admins_can_search():
    client = TestClient(app)
    authenticated_client = mock_auth(client)
    admin_page = authenticated_client.get("/admin")
    hx_headers = extract_hx_hdr(admin_page.text)
    request = authenticated_client.post("/admin/users", data={'query': 'foo'}, headers=hx_headers)
    assert request.status_code == 200

def test_authenticated_non_admins_cant_search():
    client = TestClient(app)
    authenticated_client = mock_auth(client)
    set_test_user_admin(False)
    authenticated_client.get("/admin")
    request = authenticated_client.post("/admin/users", data={'query': 'foo'})
    assert request.status_code == 401

def test_authenticated_admins_can_see_user():
    client = TestClient(app)
    authenticated_client = mock_auth(client)
    authenticated_client.get("/admin")
    admin_page = authenticated_client.get("/admin")
    hx_headers = extract_hx_hdr(admin_page.text)
    request = authenticated_client.get("/admin/user/459", headers=hx_headers)
    assert request.status_code == 200

def test_authenticated_non_admins_cant_see_user():
    client = TestClient(app)
    authenticated_client = mock_auth(client)
    set_test_user_admin(False)
    authenticated_client.get("/admin")
    request = authenticated_client.get("/admin/user/459")
    assert request.status_code == 401
