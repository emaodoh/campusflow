"""Assignment, status workflow and work queue (Engineer B)."""

# Allowed moves: current status -> list of statuses it may move to.
VALID_TRANSITIONS = {
    "open": ["in_progress"],
    "in_progress": ["resolved"],
    "resolved": ["open"],  # reopen
}

# Lower number = more urgent.
PRIORITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}


def _find_ticket(tickets, ticket_id):
    """Return the ticket dict with this ID, or raise ValueError."""
    ticket_id = str(ticket_id).strip().upper()
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket
    raise ValueError(f"Ticket {ticket_id} not found")


def assign_ticket(tickets, ticket_id, staff_name):
    """Assign a ticket to a staff member and return the updated ticket."""
    # Check everything first, change data last.
    name = str(staff_name).strip()
    if name == "":
        raise ValueError("Staff name cannot be blank")

    ticket = _find_ticket(tickets, ticket_id)

    if ticket["status"] == "resolved":
        raise ValueError(
            f"Ticket {ticket['id']} is resolved; reopen it before assigning"
        )

    ticket["assigned_to"] = name
    return ticket


def change_status(tickets, ticket_id, new_status):
    """Move a ticket to a new status and return the updated ticket."""
    new_status = str(new_status).strip().lower()
    if new_status not in VALID_TRANSITIONS:
        raise ValueError(f"Unknown status: {new_status}")

    ticket = _find_ticket(tickets, ticket_id)
    current = ticket["status"]

    if new_status not in VALID_TRANSITIONS[current]:
        raise ValueError(
            f"Cannot move ticket {ticket['id']} from {current} to {new_status}"
        )

    if new_status == "in_progress" and not ticket["assigned_to"]:
        raise ValueError(
            f"Ticket {ticket['id']} must be assigned before it can be in_progress"
        )

    ticket["status"] = new_status
    return ticket


def get_queue(tickets):
    """Return open tickets sorted by priority, then by numeric ID."""
    open_tickets = [t for t in tickets if t["status"] == "open"]
    return sorted(
        open_tickets,
        key=lambda t: (PRIORITY_ORDER[t["priority"]], int(t["id"][1:])),
    )