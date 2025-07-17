from unittest.mock import patch, Mock

import app.models.logbook as logbook_model

def test_get_all_logs():
    with patch('sqlite3.connect') as mock_connect:
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [
            logbook_model.Log(0, 'Test', 'A date')
        ]

        # GIVEN that we want all logs
        # THEN we get all logs
        result = logbook_model.get_all_logs()
        assert result == [
            logbook_model.Log(0, 'Test', 'A date')
        ]

def test_add_log():
    with patch('sqlite3.connect') as mock_connect:
        mock_conn = Mock()
        mock_cursor = Mock()

        # GIVEN we have a valid log (had text)
        good_log = logbook_model.Log(0, 'Test', 'A date')
        # WHEN we add it
        result = logbook_model.add_log(good_log)
        # THEN it should return True
        assert result == True

        # GIVEN an invalid log (no text)
        bad_log = logbook_model.Log(0, None, 'A date')
        # WHEN we add it
        result = logbook_model.add_log(bad_log)
        # THEN it should return false
        assert result == False
