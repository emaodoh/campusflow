from .services import  priority, check_categories, check_urgency, check_affected_users, generate_ticket_id
from .storage import load_ticket, save_ticket


def create_ticket(title, category, urgency, affected_users, status="Open", assigned_to="None"):
    
    tickets = load_ticket()
    if not title.strip():
        return "Title must not be blank."

    
    
    category = check_categories(category)

    urgency = check_urgency(urgency)

    if not urgency:
        return "urgency provided is not allowed\naccepted options: low, medium, high"

    affected_users = check_affected_users(affected_users)


    if not affected_users:
        return "Please enter a valid number of affected user"

    priority_level = priority(urgency, affected_users)

    ticket_id = generate_ticket_id()
    ticket_data = {
        "id": ticket_id,
        "title": title,
        "category": category,
        "urgency": urgency,
        "affected_users":affected_users,
        "priority": priority_level,
        "status": status,
        "assigned_to": assigned_to,
        "notes": [
            {
                "note_id": "",
                "author": "",
                "message": ""
            }
        ]
    }
    


    tickets.append(ticket_data)

    save_ticket(tickets)

    return "Ticket created successfully!"

