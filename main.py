from campusflow import storage, tickets, workflow, reports

# Load initial data (if needed globally, though you reload in operations 5 & 6)
ticket_list = storage.load()

def main():
    while True:
        # 1. Print Menu inside the loop so it reappears after an operation completes
        print("\n1. Create Ticket\n2. List/View\n3. Assign\n4. Workflow\n5. Work Queue\n6. Reports\n7. Exit")
        operation = input("Enter operation number: ").strip()

        # 2. Validate input safely
        try:
            operation = int(operation)
            if not (1 <= operation <= 7):
                print("\nPlease enter a number between 1 - 7")
                continue
        except ValueError:
            print("\nEnter a valid number")
            continue

        # 3. Handle operations
        if operation == 1:
            title = input("Enter title: ")
            category = input("Enter category: ")
            urgency = input("Urgency: ")
            affected_users = input("Affected Users: ")
            # Uses the imported 'tickets' module
            print(tickets.create_ticket(title, category, urgency, affected_users, status="Open", assigned_to="None"))

        elif operation == 2:
            ticket_id = input("Enter ticket ID: ").strip()
            print(workflow.find_ticket(ticket_list, ticket_id))

        elif operation == 3:
            ticket_id = input("Enter ticket ID: ").strip()
            staff_name = input("Enter staff name: ").strip()
            print(workflow.assign_ticket(ticket_list, ticket_id, staff_name))
        
        elif operation == 4:
            print("Workflow option selected (Not yet implemented).")
            pass

        elif operation == 5:
            
            loaded_tickets = storage.load()
            print(workflow.get_queue(loaded_tickets))

        elif operation == 6:
        
            loaded_tickets = storage.load()
            report = reports.build_report(loaded_tickets)
            print(report)

        elif operation == 7:
            print("Exiting CampusFlow. Goodbye!")
            break  # Successfully breaks the main loop and exits the program

if __name__ == "__main__":
    main()
