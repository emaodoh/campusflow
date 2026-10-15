"""Assignment, status workflow and work queue (Engineer B)."""

from .storage import save_ticket, load_ticket

# Allowed moves: current status -> list of statuses it may move to.
VALID_TRANSITIONS = {
    "open": ["in_progress"],
    "in_progress": ["resolved"],
    "resolved": ["open"],
    "reopen": ["reopen"],  # reopen
}

# Lower number = more urgent.
PRIORITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}


def find_ticket(ticket_id):
    tickets = load_ticket()
    """Return the ticket dict with this ID, or raise ValueError."""
    ticket_id = str(ticket_id).strip().upper()
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket
    raise ValueError(f"Ticket {ticket_id} not found")


def assign_ticket( ticket_id, staff_name):
    """Assign a ticket to a staff member and return the updated ticket."""
    ticket_list = load_ticket()

    # Check everything first, change data last.
    name = str(staff_name).strip()
    if name == "":
        raise ValueError("Staff name cannot be blank")

    ticket = find_ticket(ticket_id)

    if ticket["status"] == "resolved":
        raise ValueError(
            f"Ticket {ticket['id']} is resolved; reopen it before assigning"
        )
    if not ticket["assigned_to"] or ticket["assigned_to"] == "None":
        ticket["assigned_to"] = name
    else:
        raise ValueError(
            f"Ticket {ticket['id']} is assigned to {ticket["assigned_to"]}"
        )


    ticket_list = [t for t in ticket_list if t["id"] != ticket_id]
    ticket["status"] = "in_progress"
    
    ticket_list.append(ticket)
    save_ticket(ticket_list)

    return ticket

VALID_TRANSITIONS = {
    "open": ["in_progress"],
    "in_progress": ["resolved"],
    "resolved": ["open"],
    "reopen": ["reopen"],  # reopen
}

def change_status(ticket_id, new_status):
    """Move a ticket to a new status and return the updated ticket."""
    new_status = str(new_status).strip().lower()
    
    # 1. Always fetch fresh data to avoid sync issues
    ticket_list = load_ticket()
    ticket = find_ticket(ticket_id)
    current = ticket["status"].lower()

    # 2. Check if the target status is even a real state
    if new_status not in VALID_TRANSITIONS:
        raise ValueError(f"Unknown status: '{new_status}'")

    # 3. Guard: Enforce strict step-by-step lifecycle paths
    if new_status not in VALID_TRANSITIONS[current]:
        raise ValueError(
            f"Invalid transition: Cannot move ticket {ticket['id']} from '{current}' to '{new_status}'"
        )

    # 4. Guard: Cannot manually move to in_progress without an assignee
    if new_status == "in_progress" and not ticket.get("assigned_to"):
        raise ValueError(
            f"Ticket {ticket['id']} must be assigned to a staff member before it can be 'in_progress'"
        )

    # 5. Rule: If a ticket is being reopened (resolved -> open), clear the assignee
    if current == "resolved" and new_status == "open":
        ticket["assigned_to"] = None

    # 6. Apply status change and save_ticket safely
    ticket["status"] = new_status
    
    updated_list = [t for t in ticket_list if t["id"] != ticket["id"]]
    updated_list.append(ticket)
    save_ticket(updated_list)

    return ticket


def get_queue():
    tickets = load_ticket()
    """Return open tickets sorted by priority, then by numeric ID."""
    # Map priorities to a numeric order (lower number = higher priority)
    priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    
    return sorted(
        [t for t in tickets if t["status"] == "open"],
        key=lambda t: (priority_order.get(t["priority"].lower(), 4), t["id"])
    )