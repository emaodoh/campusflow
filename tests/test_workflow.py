import unittest
from unittest.mock import patch

from campusflow.workflow import find_ticket, assign_ticket, change_status, get_queue

# Patch where workflow.py looks the names up. If workflow.py does
# `from campusflow import storage` and calls `storage.load_ticket(...)`,
# change these to "campusflow.storage.load_ticket" / "campusflow.storage.save_ticket".
LOAD = "campusflow.workflow.load_ticket"
SAVE = "campusflow.workflow.save_ticket"


class TestTicketWorkflow(unittest.TestCase):

    def setUp(self):
        # Sample mock database state before each test
        self.mock_tickets = [
            {"id": "T1", "status": "open", "priority": "high", "assigned_to": None},
            {"id": "T2", "status": "in_progress", "priority": "critical", "assigned_to": "Alice"},
            {"id": "T3", "status": "resolved", "priority": "low", "assigned_to": "Bob"},
            {"id": "T4", "status": "open", "priority": "critical", "assigned_to": None},
        ]

    @patch(LOAD)
    def test_find_ticket_success(self, mock_load):
        mock_load.return_value = self.mock_tickets
        ticket = find_ticket("t1")  # Test case insensitivity
        self.assertEqual(ticket["id"], "T1")

    @patch(LOAD)
    def test_find_ticket_not_found(self, mock_load):
        mock_load.return_value = self.mock_tickets
        with self.assertRaises(ValueError):
            find_ticket("INVALID_ID")

    @patch(SAVE)
    @patch(LOAD)
    def test_assign_ticket_success(self, mock_load, mock_save):
        mock_load.return_value = self.mock_tickets
        updated_ticket = assign_ticket("T1", "Charlie")
        self.assertEqual(updated_ticket["assigned_to"], "Charlie")
        self.assertEqual(updated_ticket["status"], "in_progress")
        mock_save.assert_called_once()

    @patch(LOAD)
    def test_assign_ticket_already_assigned(self, mock_load):
        mock_load.return_value = self.mock_tickets
        with self.assertRaises(ValueError):
            assign_ticket("T2", "Charlie")

    @patch(SAVE)
    @patch(LOAD)
    def test_change_status_valid_transition(self, mock_load, mock_save):
        mock_load.return_value = self.mock_tickets
        updated_ticket = change_status("T2", "resolved")
        self.assertEqual(updated_ticket["status"], "resolved")
        mock_save.assert_called_once()

    @patch(LOAD)
    def test_change_status_invalid_transition(self, mock_load):
        mock_load.return_value = self.mock_tickets
        with self.assertRaises(ValueError):
            change_status("T1", "resolved")  # open -> resolved is invalid

    @patch(LOAD)
    def test_get_queue_sorting(self, mock_load):
        mock_load.return_value = self.mock_tickets
        queue = get_queue()
        # Only T4 and T1 are open. T4 is critical, T1 is high.
        # Critical (0) comes before High (1).
        self.assertEqual(len(queue), 2)
        self.assertEqual(queue[0]["id"], "T4")
        self.assertEqual(queue[1]["id"], "T1")


if __name__ == "__main__":
    unittest.main()