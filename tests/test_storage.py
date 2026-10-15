import json
import unittest
from unittest.mock import patch, mock_open

# Assuming your code is structured as a package module
from campusflow.storage import load_ticket, save_ticket, load_question_bank


class TestTicketManager(unittest.TestCase):

    # ==========================================
    # TESTS FOR load_ticket()
    # ==========================================

    @patch("os.path.exists", return_value=False)
    @patch("campusflow.storage.save_ticket")  # FIXED: Point to the accurate module reference
    def test_load_ticket_file_does_not_exist(self, mock_save, mock_exists):
        """Should initialize an empty list and call save if file doesn't exist."""
        result = load_ticket()
        self.assertEqual(result, [])
        mock_save.assert_called_once_with([])

    @patch("os.path.exists", return_value=True)
    @patch("os.path.getsize", return_value=0)
    @patch("campusflow.storage.save_ticket")  # FIXED
    def test_load_ticket_file_is_empty(self, mock_save, mock_getsize, mock_exists):
        """Should initialize an empty list and call save if file size is 0."""
        result = load_ticket()
        self.assertEqual(result, [])
        mock_save.assert_called_once_with([])

    @patch("os.path.exists", return_value=True)
    @patch("os.path.getsize", return_value=100)
    def test_load_ticket_success(self, mock_getsize, mock_exists):
        """Should successfully parse and return a list from valid JSON."""
        mock_data = [{"id": 1, "issue": "Login fail"}]
        mock_json_str = json.dumps(mock_data)

        # FIXED: "builtins.open" is the correct standard across Python 3 environments
        with patch("builtins.open", mock_open(read_data=mock_json_str)):
            result = load_ticket()
            self.assertEqual(result, mock_data)

    @patch("os.path.exists", return_value=True)
    @patch("os.path.getsize", return_value=100)
    @patch("campusflow.storage.save_ticket")  # FIXED
    def test_load_ticket_invalid_json(self, mock_save, mock_getsize, mock_exists):
        """Should handle JSONDecodeError, reset the file, and return an empty list."""
        with patch("builtins.open", mock_open(read_data="invalid json data")):
            result = load_ticket()
            self.assertEqual(result, [])
            mock_save.assert_called_once_with([])

    @patch("os.path.exists", return_value=True)
    @patch("os.path.getsize", return_value=100)
    def test_load_ticket_not_a_list(self, mock_getsize, mock_exists):
        """Should return empty list if valid JSON evaluates to a dict instead of a list."""
        mock_dict = {"status": "error"}  # Valid JSON, but a dict, not a list
        mock_json_str = json.dumps(mock_dict)

        with patch("builtins.open", mock_open(read_data=mock_json_str)):
            result = load_ticket()
            self.assertEqual(result, [])

    # ==========================================
    # TESTS FOR save_ticket()
    # ==========================================

    @patch("os.path.exists", return_value=False)
    @patch("os.makedirs")
    def test_save_ticket_creates_directory(self, mock_makedirs, mock_exists):
        """Should create the 'data' directory if it does not already exist."""
        test_data = [{"id": 2}]
        
        with patch("builtins.open", mock_open()) as mock_file:
            save_ticket(test_data)
            mock_makedirs.assert_called_once_with("data", exist_ok=True)
            mock_file.assert_called_once_with("data/tickets.json", "w", encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
