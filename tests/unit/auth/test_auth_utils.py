import auth.utils
import models.users as users_model


def test_login_user():
    session = {}
    user = users_model.User(
        id=0,
        email="foo@bar.com",
        password_hash="foo",
        password_salt="bar",
        is_active=True,
        is_admin=False,
    )
    auth.utils.login_user(session, user)
    assert "user_id" in session
    assert "email" in session


def test_logout_user():
    session = {"user_id": 1, "email": "foo@bar.com"}
    auth.utils.logout_user(session)
    assert "user_id" not in session
    assert "email" not in session


def test_get_current_user():
    pass


def test_is_authenticated():
    session = {"user_id": 1, "email": "foo@bar.com"}
    assert auth.utils.is_authenticated(session)

    session = {}
    assert not auth.utils.is_authenticated(session)


def test_is_active():
    pass


def test_is_admin():
    pass
