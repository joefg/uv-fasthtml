from unittest.mock import patch, Mock

import app.models.logbook as logbook_model


def test_get_all_logs():
    with patch("sqlite3.connect") as mock_connect:
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [
            logbook_model.Log(0, "Test", "A date", "test_user")
        ]

        # GIVEN that we want all logs
        # THEN we get all logs
        result = logbook_model.get_all_logs()
        assert result == [logbook_model.Log(0, "Test", "A date", "test_user")]


def test_add_log():
    with patch("sqlite3.connect"):
        Mock()
        Mock()

        # GIVEN we have a valid log (has text)
        # WHEN we add it
        result = logbook_model.add_log("Test", user_id=1)
        # THEN it should return True
        assert result

        # GIVEN an invalid log (no text)
        # WHEN we add it
        result = logbook_model.add_log(None, user_id=1)
        # THEN it should return false
        assert not result

        # GIVEN trying to add a log without a user ID
        # THEN it should return false
        result = logbook_model.add_log("Test", user_id=None)
        assert not result
