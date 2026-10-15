from campusflow import tickets_creation, workflow, reports, notes, search_engine, quiz

# Load initial data (if needed globally, though you reload in operations 5 & 6)


def main():
    while True:
        # 1. Print Menu inside the loop so it reappears after an operation completes
        print("\n1. Create Ticket\n2. List/View\n3. Assign\n4. Change status\n5. Work Queue\n6. Reports\n7. Notes\n8. Search/Filter\n9. Quiz\n10. Exit")
        operation = input("Enter operation number: ").strip()

        # 2. Validate input safely
        try:
            operation = int(operation)
            if not (1 <= operation <= 10):
                print("\nPlease enter a number between 1 - 7")
                continue
        except ValueError:
            print("\nEnter a valid number")
            continue

        # 3. Handle operations
        if operation == 1:
            title = input("Enter title: ")
            category = input("Enter category (Network, Hardware, Software or Other): ")
            urgency = input("Urgency: (low, medium or high)")
            affected_users = input("Affected Users: ")
            
            while True:

                note = input("Leave a note (y/n): ").lower().strip()
            
                if note == "y" or note == "n":
                    break

                print("Enter 'Y' to leave a note and 'N' to skip: ")

            author = ""
            message = ""

            if note == "y":
                
            
                author = input("Enter your name: ").strip()
                message = input("Enter a short note:  ")

            # Uses the imported 'tickets' module
            
            print(tickets_creation.create_ticket(title, category, urgency, affected_users, author, message ))

        elif operation == 2:
            ticket_id = input("Enter ticket ID: ").strip()

            try:
                ticket = workflow.find_ticket(ticket_id)
                print(f"\nID: {ticket["id"]}\nTitle: {ticket["title"]}\nCategory: {ticket["category"]}\nUrgency: {ticket["urgency"]}\nAffected Users:  {ticket["affected_users"]}\nPriority: {ticket["priority"]}\nStatus: {ticket["status"]}\nAssigned to: {ticket["assigned_to"]}")

            except ValueError as error:
                print(f"\nError: {error}")

            


        elif operation == 3:
            ticket_id = input("Enter ticket ID: ").strip()
            staff_name = input("Enter staff name: ").strip()
            try:
                result = workflow.assign_ticket( ticket_id, staff_name)
                print(result)

            except ValueError as error:
                print(f"Error: {error}")

        elif operation == 4:
            ticket_id = input("Enter ticket id: ").lower()
            ticket_status = input("Enter ticket status: ").lower()
            try:
                result = workflow.change_status(ticket_id, ticket_status)
                print(result)
            
            except ValueError as error:
                print(f"\nError: {error}")

        elif operation == 5:
            
            tickets = workflow.get_queue()

            for ticket in tickets:
                print(f"Ticket_ID: {ticket["id"]} <  Title: {ticket["title"]} >   < Category: {ticket["category"]}  >   < Affected Users: {ticket["affected_users"]} >  <  Priority: {ticket["priority"]}  > ")



        elif operation == 6:
            
            try:
                report = reports.build_report()
                print(f"\nTotal ticket: {report["total"]}\nTickets Open: {report["by_status"]["open"]}\nTickets in progress: {report["by_status"]["in_progress"]}\nTickets resolved: {report["by_status"]["resolved"]}\n")
                print(f"Priority:  << Critical: {report["by_priority"]["critical"]} >>   << High: {report["by_priority"]["high"]} >>   << Medium: {report["by_priority"]["medium"]} >>  << Low: {report["by_priority"]["low"]}  >>")


            except ValueError as error:
                print(f"\nError: {error}")

        elif operation == 7:
            print("\n1. Add note\n2. View Note:  ")

            while True:
                try:
                    option = int(input().strip())
                    if option > 0 and option <= 2:
                        break
                    else:
                        print("Enter a number between 1 and 2")

                except ValueError:
                    print("Enter a valid number")
            if option == 1:
                ticket_id = input("Enter ticket ID: ").strip()
                author = input("Enter your name: ").strip()
                message = input("Enter a short note:  ")
                message = notes.add_note(ticket_id, author, message)

                print(message)

            elif option == 2:
                ticket_id = input("Enter ticket ID: ").strip()

                try:
                    ticket = notes.note_display(ticket_id)

                    note = ticket["notes"]
                    
                    
                    print("\nNotes History:")
                    print("\nNotes:")

                    for index, note_item in enumerate(note, start=1):
                        print(f"{index}. {note_item['author'].title()}: {note_item['message']}")

                
                except ValueError as error:
                    print(f"\nError: {error}")
            
        
        elif operation == 8:
            while True:
                try:
                    print(f"1. search by title\n2. search by category, status and priority")

                    response = int(input(" ").strip())
                
                    

                    if response > 0 and response <= 2:
                        break
                    else:
                        print("Enter between 1 and 2")

                except ValueError:
                    print("Enter a valid number")
                
            if response == 1:
                title = input("Enter title:  ").strip().lower()

                found = search_engine.search_title(title)

                if found:
                            
                    for ticket in found:
                        print(
                            f"\nTicket Found\n"
                            f"ID: {ticket['id']}\n"
                            f"Title: {ticket['title']}\n"
                            f"Category: {ticket['category']}\n"
                            f"Urgency: {ticket['urgency']}\n"
                            f"Affected Users: {ticket['affected_users']}\n"
                            f"Priority: {ticket['priority']}\n"
                            f"Status: {ticket['status']}\n"
                            f"Assigned To: {ticket['assigned_to']}"
                        )
                else:
                    print("\nNo tickets matched this search.")


            if response == 2:       
                category = input("Enter category (Network, Hardware, Software or Other): ").strip().lower()
                priority = input("Priority: (low, medium, high or critical):  ").strip().lower()
                status = input("Status: (open, in_progress, resolved):  ").strip().lower()
                        
                found = search_engine.search( category, status, priority)
                
                if found:
                            
                    for ticket in found:
                        print(
                            f"Ticket Found\n"
                            f"ID: {ticket['id']}\n"
                            f"Title: {ticket['title']}\n"
                            f"Category: {ticket['category']}\n"
                            f"Urgency: {ticket['urgency']}\n"
                            f"Affected Users: {ticket['affected_users']}\n"
                            f"Priority: {ticket['priority']}\n"
                            f"Status: {ticket['status']}\n"
                            f"Assigned To: {ticket['assigned_to']}"
                        )
                else:
                    print("\nNo tickets matched this search.")

        elif operation == 9:
            try:
                score = quiz.quiz()
                print(f"\nScore: {score}")
            except ValueError as error:
                print(f"\nError: {error}\n")


        elif operation == 10:
            print("Exiting CampusFlow. Goodbye!")
            break  # Successfully breaks the main loop and exits the program

if __name__ == "__main__":
    main()
