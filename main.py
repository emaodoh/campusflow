from campusflow import tickets_creation, workflow, reports

# Load initial data (if needed globally, though you reload in operations 5 & 6)


def main():
    while True:
        # 1. Print Menu inside the loop so it reappears after an operation completes
        print("\n1. Create Ticket\n2. List/View\n3. Assign\n4. Change status\n5. Work Queue\n6. Reports\n7. Exit")
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
            print(tickets_creation.create_ticket(title, category, urgency, affected_users, status="Open", assigned_to="None"))

        elif operation == 2:
            ticket_id = input("Enter ticket ID: ").strip()
            ticket = workflow.find_ticket(ticket_id)

            print(f"\nID: {ticket["id"]}\nTitle: {ticket["title"]}\nCategory: {ticket["category"]}\nUrgency: {ticket["urgency"]}\nAffected Users:  {ticket["affected_users"]}\nPriority: {ticket["priority"]}\nStatus: {ticket["status"]}\nAssigned to: {ticket["assigned_to"]}")

        elif operation == 3:
            ticket_id = input("Enter ticket ID: ").strip()
            staff_name = input("Enter staff name: ").strip()
            print(workflow.assign_ticket( ticket_id, staff_name))
        
        elif operation == 4:
            ticket_id = input("Enter ticket id: ").lower()
            ticket_status = input("Enter ticket status: ").lower()
        
            print(workflow.change_status(ticket_id, ticket_status))
            

        elif operation == 5:
            
            tickets = workflow.get_queue()

            for ticket in tickets:
                print(f"Ticket_ID: {ticket["id"]} <  Title: {ticket["title"]} >   < Category: {ticket["category"]}  >   < Affected Users: {ticket["affected_users"]} >  <  Priority: {ticket["priority"]}  > ")



        elif operation == 6:
        
            
            report = reports.build_report()
            print(f"\nTotal ticket: {report["total"]}\nTickets Open: {report["by_status"]["open"]}\nTickets in progress: {report["by_status"]["in_progress"]}\nTickets resolved: {report["by_status"]["resolved"]}\n")
            print(f"Priority:  << Critical: {report["by_priority"]["critical"]} >>   << High: {report["by_priority"]["high"]} >>   << Medium: {report["by_priority"]["medium"]} >>  << Low: {report["by_priority"]["low"]}  >>")

        elif operation == 7:
            print("Exiting CampusFlow. Goodbye!")
            break  # Successfully breaks the main loop and exits the program

if __name__ == "__main__":
    main()
