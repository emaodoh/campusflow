from .storage import load_ticket, save_ticket
from .workflow import find_ticket 
from .services import generate_note_id
from .validate import validate_note_entry

def add_note(ticket_id, author, message):

    try:
        err = validate_note_entry(author, message)

    except ValueError as error:

        return f"\nError: {error}"

    tickets = load_ticket()
    ticket = find_ticket(ticket_id)

    if ticket["status"] == "resolved":
        print("Cannot add a note to a resolved ticket. Reopen the ticket first.")
        return
    
    notes = ticket["notes"]

    note_id = generate_note_id()

    
    notes.append({
        "note_id": note_id,
        "author": author,
        "message": message
        
    })
    

    tickets = [t for t in tickets if t["id"] != ticket_id]

    tickets.append(ticket)

    save_ticket(tickets)

    return "Note added successfully! "


def note_display(ticket_id):

    ticket = find_ticket(ticket_id)

    return ticket