from .storage import load_ticket

def generate_ticket_id(prefix="F"):
    tickets = load_ticket()

    if not tickets:
        return f"{prefix}001"

    existing_ids = []
    for ticket in tickets:
        id_str = ticket.get("id", "")
        if id_str.startswith(prefix):
            num_part = int(id_str.replace(prefix, ""))
            existing_ids.append(num_part)

        
    next_num = max(existing_ids) + 1 if existing_ids else 1

    return f"{prefix}{next_num:03d}"


def generate_note_id(prefix="T"):
    tickets = load_ticket()

    if not tickets:
        return f"{prefix}001"

    existing_ids = []

    for ticket in tickets:
        notes = ticket.get("notes", [])

        for note in notes:
            note_id = note.get("note_id", "")

            if note_id.startswith(prefix):
                num_part = int(note_id.replace(prefix, ""))
                existing_ids.append(num_part)

    next_num = max(existing_ids) + 1 if existing_ids else 1

    return f"{prefix}{next_num:03d}"


def priority(urgency, affected_users):
    urgency = urgency.lower()
    if urgency == "high" and affected_users >= 10:
        return "critical"
    
    if urgency == "high" or affected_users >= 10:
        return "high"

    if urgency == "medium" or affected_users >= 3:
        return "medium"

    return "low"


def check_categories(category):
    if category.lower() in ["network", "hardware", "software", "other"]:
        return category.title()

    return "Other"

def check_urgency(urgency):
    if urgency  in ["low", "medium", "high"]:
        return urgency

    return None

def check_affected_users(affected_users):
    try:
        affected_users = int(affected_users)
        if affected_users >= 0:
            return affected_users

    except ValueError:
        return None