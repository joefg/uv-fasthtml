import os
from pathlib import Path

import pytest
from starlette.testclient import TestClient

from app.main import app
from utils import mock_auth

@pytest.fixture(autouse=True)
def run_test():
    Path('./protected/test.txt').touch()
    yield
    os.remove('./protected/test.txt')

def test_unauthenticated_protected_returns_404():
    client = TestClient(app)
    request = client.get("./protected/test.txt")
    assert request.status_code == 404

def test_authenticated_protected_returns_200():
    client = TestClient(app)
    # log in using integration_test
    authenticated_client = mock_auth(client)
    # then get this resource
    request = authenticated_client.get("./protected/test.txt")
    assert request.status_code == 200
    assert request.text == ""
