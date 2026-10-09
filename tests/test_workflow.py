import unittest

from campusflow.workflow import assign_ticket, change_status, get_queue
from campusflow.reports import build_report


def make_ticket(ticket_id, priority="low", status="open", assigned_to=None):
    return {
        "id": ticket_id,
        "title": "Test ticket",
        "category": "Other",
        "urgency": "low",
        "affected_users": 1,
        "priority": priority,
        "status": status,
        "assigned_to": assigned_to,
    }


class TestAssign(unittest.TestCase):
    def test_assign_sets_name_and_returns_ticket(self):
        tickets = [make_ticket("T001")]
        result = assign_ticket(tickets, "T001", "  Ada  ")
        self.assertEqual(result["assigned_to"], "Ada")
        self.assertEqual(tickets[0]["assigned_to"], "Ada")

    def test_blank_name_rejected_and_ticket_unchanged(self):
        tickets = [make_ticket("T001")]
        with self.assertRaises(ValueError):
            assign_ticket(tickets, "T001", "   ")
        self.assertIsNone(tickets[0]["assigned_to"])

    def test_unknown_id_rejected(self):
        tickets = [make_ticket("T001")]
        with self.assertRaises(ValueError):
            assign_ticket(tickets, "T999", "Ada")

    def test_resolved_ticket_cannot_be_assigned(self):
        tickets = [make_ticket("T001", status="resolved", assigned_to="Ada")]
        with self.assertRaises(ValueError):
            assign_ticket(tickets, "T001", "Ben")
        self.assertEqual(tickets[0]["assigned_to"], "Ada")


class TestWorkflow(unittest.TestCase):
    def test_unassigned_cannot_move_to_in_progress(self):
        tickets = [make_ticket("T001")]
        with self.assertRaises(ValueError):
            change_status(tickets, "T001", "in_progress")
        self.assertEqual(tickets[0]["status"], "open")

    def test_assigned_ticket_full_lifecycle(self):
        tickets = [make_ticket("T001", assigned_to="Ada")]
        change_status(tickets, "T001", "in_progress")
        self.assertEqual(tickets[0]["status"], "in_progress")
        change_status(tickets, "T001", "resolved")
        self.assertEqual(tickets[0]["status"], "resolved")

    def test_invalid_transition_rejected(self):
        tickets = [make_ticket("T001", assigned_to="Ada")]
        with self.assertRaises(ValueError):
            change_status(tickets, "T001", "resolved")  # open -> resolved
        self.assertEqual(tickets[0]["status"], "open")

    def test_reopen_resolved_ticket(self):
        tickets = [make_ticket("T001", status="resolved", assigned_to="Ada")]
        change_status(tickets, "T001", "open")
        self.assertEqual(tickets[0]["status"], "open")

    def test_unknown_status_rejected(self):
        tickets = [make_ticket("T001", assigned_to="Ada")]
        with self.assertRaises(ValueError):
            change_status(tickets, "T001", "done")


class TestQueue(unittest.TestCase):
    def test_sorted_by_priority_then_numeric_id(self):
        tickets = [
            make_ticket("T010", priority="low"),
            make_ticket("T002", priority="high"),
            make_ticket("T009", priority="critical"),
            make_ticket("T003", priority="high"),
        ]
        ids = [t["id"] for t in get_queue(tickets)]
        self.assertEqual(ids, ["T009", "T002", "T003", "T010"])

    def test_numeric_id_tiebreak_not_text(self):
        tickets = [
            make_ticket("T100", priority="low"),
            make_ticket("T020", priority="low"),
        ]
        ids = [t["id"] for t in get_queue(tickets)]
        self.assertEqual(ids, ["T020", "T100"])

    def test_queue_excludes_non_open_tickets(self):
        tickets = [
            make_ticket("T001", status="open"),
            make_ticket("T002", status="in_progress", assigned_to="Ada"),
            make_ticket("T003", status="resolved", assigned_to="Ada"),
        ]
        ids = [t["id"] for t in get_queue(tickets)]
        self.assertEqual(ids, ["T001"])


class TestReport(unittest.TestCase):
    def test_empty_report(self):
        report = build_report([])
        self.assertEqual(report["total"], 0)
        self.assertEqual(sum(report["by_status"].values()), 0)
        self.assertEqual(sum(report["by_priority"].values()), 0)

    def test_report_counts(self):
        tickets = [
            make_ticket("T001", priority="critical", status="open"),
            make_ticket("T002", priority="critical", status="resolved"),
            make_ticket("T003", priority="low", status="open"),
        ]
        report = build_report(tickets)
        self.assertEqual(report["total"], 3)
        self.assertEqual(report["by_status"]["open"], 2)
        self.assertEqual(report["by_status"]["resolved"], 1)
        self.assertEqual(report["by_priority"]["critical"], 2)
        self.assertEqual(report["by_priority"]["low"], 1)


if __name__ == "__main__":
    unittest.main()