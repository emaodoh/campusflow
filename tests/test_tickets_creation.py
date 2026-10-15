from unittest.mock import patch

import pytest

from campusflow.tickets_creation import create_ticket


@pytest.fixture
def mocks():
    """Patch storage and ID generators where tickets_creation looks them up."""
    with patch("campusflow.tickets_creation.load_ticket") as mock_load, \
         patch("campusflow.tickets_creation.save_ticket") as mock_save, \
         patch("campusflow.tickets_creation.generate_ticket_id", return_value="T1"), \
         patch("campusflow.tickets_creation.generate_note_id", return_value="N1"):
        mock_load.return_value = []
        yield mock_load, mock_save


def test_ticket_creation_success(mocks):
    _, mock_save = mocks

    result = create_ticket(
        title="school",
        category="other",
        urgency="high",
        affected_users=15,
        author="John",
        message="still working on it",
    )

    assert result == "Ticket created successfully!"
    mock_save.assert_called_once()

    saved_tickets = mock_save.call_args[0][0]
    ticket = saved_tickets[-1]
    assert ticket["id"] == "T1"
    assert ticket["title"] == "school"
    assert ticket["status"] == "Open"
    assert ticket["assigned_to"] == "None"
    assert ticket["notes"][0]["author"] == "John"
    assert ticket["notes"][0]["message"] == "still working on it"


def test_ticket_creation_invalid_affected_users(mocks):
    _, mock_save = mocks

    result = create_ticket(
        title="school",
        category="other",
        urgency="high",
        affected_users="lklk",
        author="John",
        message="still working on it",
    )

    assert result == "Please enter a valid number of affected user"
    mock_save.assert_not_called()


@pytest.mark.parametrize("bad_urgency", ["", "extreme"])
def test_ticket_creation_invalid_urgency(mocks, bad_urgency):
    _, mock_save = mocks

    result = create_ticket(
        title="school",
        category="other",
        urgency=bad_urgency,
        affected_users=12,
        author="John",
        message="still working on it",
    )

    assert result == "urgency provided is not allowed\naccepted options: low, medium, high"
    mock_save.assert_not_called()


def test_ticket_creation_blank_title(mocks):
    _, mock_save = mocks

    result = create_ticket(
        title="   ",
        category="other",
        urgency="high",
        affected_users=12,
        author="John",
        message="still working on it",
    )

    assert result == "Title must not be blank."
    mock_save.assert_not_called()