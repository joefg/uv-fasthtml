
from sqlmodel import Session

from app.models import users as users_model


def make_session_factory(test_engine):
    def _factory():
        return Session(test_engine)

    return _factory


def test_get_user_by_id_found(sample_user, test_engine):
    factory = make_session_factory(test_engine)
    result = users_model.get_user_by_id(12345, session_factory=factory)
    assert result is not None
    assert result.id == 12345
    assert result.gh_login == "testuser"


def test_get_user_by_id_not_found(test_engine):
    factory = make_session_factory(test_engine)
    result = users_model.get_user_by_id(99999, session_factory=factory)
    assert result is None


def test_register_user(sample_user_data, test_engine):
    factory = make_session_factory(test_engine)
    user_data = sample_user_data.copy()
    user_data["created_at"] = "2024-01-15T10:30:00Z"
    users_model.register_user(user_data, session_factory=factory)
    result = users_model.get_user_by_id(12345, session_factory=factory)
    assert result is not None
    assert result.gh_login == "testuser"
    assert result.is_active is True
    assert result.is_admin is False


def test_search_users(sample_user, test_engine):
    factory = make_session_factory(test_engine)
    results = users_model.search_users("test", session_factory=factory)
    assert len(results) == 1
    assert results[0].gh_login == "testuser"


def test_search_users_no_results(sample_user, test_engine):
    factory = make_session_factory(test_engine)
    results = users_model.search_users("nonexistent", session_factory=factory)
    assert len(results) == 0


def test_set_user_admin(sample_user, test_engine):
    factory = make_session_factory(test_engine)
    assert sample_user.is_admin is False
    users_model.set_user_admin(12345, True, session_factory=factory)
    result = users_model.get_user_by_id(12345, session_factory=factory)
    assert result.is_admin is True


def test_set_user_active(sample_user, test_engine):
    factory = make_session_factory(test_engine)
    assert sample_user.is_active is True
    users_model.set_user_active(12345, False, session_factory=factory)
    result = users_model.get_user_by_id(12345, session_factory=factory)
    assert result.is_active is False


def test_authenticate_user_active(sample_user, test_engine):
    factory = make_session_factory(test_engine)
    result = users_model.authenticate_user(12345, session_factory=factory)
    assert result is True


def test_authenticate_user_inactive(sample_user, test_engine):
    factory = make_session_factory(test_engine)
    users_model.set_user_active(12345, False, session_factory=factory)
    result = users_model.authenticate_user(12345, session_factory=factory)
    assert result is False


def test_update_user(sample_user, test_engine):
    factory = make_session_factory(test_engine)
    updated_info = {
        "id": 12345,
        "login": "updateduser",
        "node_id": "xyz789",
        "avatar_url": "https://example.com/new_avatar.png",
        "type": "User",
    }
    users_model.update_user(updated_info, session_factory=factory)
    result = users_model.get_user_by_id(12345, session_factory=factory)
    assert result.gh_login == "updateduser"
    assert result.gh_node_id == "xyz789"


def test_delete_user(sample_user, test_engine):
    factory = make_session_factory(test_engine)
    users_model.delete_user(12345, session_factory=factory)
    result = users_model.get_user_by_id(12345, session_factory=factory)
    assert result is None
