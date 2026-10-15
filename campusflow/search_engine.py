from .storage import load_ticket

def search(category, status, priority):

    if not result:
        return []

    tickets = load_ticket()
    results = []

    for ticket in tickets:
        
        if ticket["category"].lower() == category.lower() and ticket["status"].lower() == status.lower() and ticket["priority"].lower() == priority.lower():
            
            results.append(ticket)

    return results