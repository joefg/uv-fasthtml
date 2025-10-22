from unittest.mock import patch, Mock

import app.models.users as users_model


def test_get_all_users():
    with patch("sqlite3.connect") as mock_connect:
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [
            users_model.User(0, False, False, 'ghost', '000', 'none',
                             'test user', 'now', 'now', 'now')
        ]

        # GIVEN that we want all users
        # THEN we get all users
        result = users_model.get_all_users()
        assert result == [
            users_model.User(0, False, False, 'ghost', '000', 'none',
                             'test user', 'now', 'now', 'now')
        ]


def test_get_user_by_id():
    with patch("sqlite3.connect") as mock_connect:
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = \
            users_model.User(0, False, False, 'ghost', '000', 'none',
                             'test user', 'now', 'now', 'now'
                             )

        # GIVEN that we want a specific users
        # THEN we get that user
        result = users_model.get_user_by_id(0)
        assert result == \
            users_model.User(0, False, False, 'ghost', '000', 'none',
                             'test user', 'now', 'now', 'now'
                             )
