from unittest.mock import patch, Mock

import app.models.users as users_model

def test_get_all_users():
    with patch('sqlite3.connect') as mock_connect:
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [
            users_model.User(0, 'test@test.com', 'password', 'password_hash', 0, 0)
        ]

        # GIVEN that we want all users
        # THEN we get all users
        result = users_model.get_all_users()
        assert result == [
            users_model.User(0, 'test@test.com', 'password', 'password_hash', 0, 0)
        ]

def test_get_user():
    with patch('sqlite3.connect') as mock_connect:
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = \
            users_model.User(0, 'test@test.com', 'password', 'password_hash', 0, 0)

        # GIVEN that we want a specific users
        # THEN we get that user
        result = users_model.get_user('test@test.com')
        assert result == \
            users_model.User(0, 'test@test.com', 'password', 'password_hash', 0, 0)

def test_get_user_by_id():
    with patch('sqlite3.connect') as mock_connect:
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = \
            users_model.User(0, 'test@test.com', 'password', 'password_hash', 0, 0)

        # GIVEN that we want a specific users
        # THEN we get that user
        result = users_model.get_user(0)
        assert result == \
            users_model.User(0, 'test@test.com', 'password', 'password_hash', 0, 0)
