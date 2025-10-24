import auth.utils


def test_login_user():
    session = {}
    user_id = 0
    auth.utils.login_user(session, user_id)
    assert "user_id" in session


def test_logout_user():
    session = {"user_id": 0}
    auth.utils.logout_user(session)
    assert "user_id" not in session

def test_is_authenticated():
    session = {"user_id": 0}
    assert auth.utils.is_authenticated(session)

    session = {}
    assert not auth.utils.is_authenticated(session)


def test_get_current_user():
    pass


def test_is_active():
    pass


def test_is_admin():
    pass
