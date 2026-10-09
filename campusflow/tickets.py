from services import  priority, check_categories, check_urgency, check_affected_users
from storage import load, save
import uuid

def create_ticket(title, category, urgency, affected_users, status="Open", assigned_to="None"):
    tickets = load()
    if not title.strip():
        return "Title must not be blank."
    priority_level = priority(urgency, affected_users)
    
    category = check_categories(category)

    urgency = check_urgency(urgency)

    if not urgency:
        return "urgency provided is not allowed\naccepted options: low, medium, high"

    affected_users = check_affected_users(affected_users)

    if not affected_users:
        return "Please enter a valid number of affected user"

    
    ticket_data = {
        "id": f"F-{uuid.uuid4().hex[:6].upper()}",
        "title": title,
        "category": category,
        "urgency": urgency,
        "affected_users":affected_users,
        "priority": priority_level,
        "status": status,
        "assigned_to": assigned_to,
    }


    tickets.append(ticket_data)

    save(tickets)

