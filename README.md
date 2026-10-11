# CampusFlow — Campus Helpdesk Ticket Management System

## 1. Project Overview

CampusFlow is a Python-based command-line helpdesk application designed to help campus IT support teams manage technical issues efficiently.

The system allows users to create support tickets, calculate priorities, assign tickets to staff, track progress, generate reports, and save ticket records using JSON.

The project also demonstrates AI-assisted learning, automated testing, and collaborative software development using Git and GitHub.

## 2. Objectives

- Create and manage support tickets.
- Validate ticket information and generate unique ticket IDs.
- Calculate ticket priorities using predefined rules.
- Assign tickets to support staff.
- Track ticket status from open to resolved.
- Display unresolved tickets in priority order.
- Generate ticket statistics and reports.
- Store and retrieve tickets using JSON.
- Apply automated testing and professional Git workflows.
- Use AI responsibly for learning, debugging, and code improvement.

## 3. Technologies Used

- **Python 3:** Application development.
- **JSON:** Data storage and persistence.
- **unittest:** Automated testing.
- **Git:** Version control.
- **GitHub:** Repository management and code reviews.
- **AI Assistant:** Learning, debugging, and technical guidance.

## 4. Core Features

1. **Ticket Creation:** Creates tickets with validated information and unique IDs.
2. **Priority Calculation:** Automatically determines ticket priority.
3. **Ticket Management:** Lists all tickets and displays individual details.
4. **Ticket Assignment:** Assigns tickets to support staff.
6. **Work Queue:** Displays unresolved tickets by priority.
7. **Reports:** Shows ticket totals and breakdowns by status and priority.
8. **JSON Persistence:** Saves tickets and restores them when the application restarts.

## 5. Priority Rules

Ticket priority is calculated using the following rules in order:

| Condition | Priority |
|---|---|
| High urgency AND at least 10 affected users | Critical |
| High urgency OR at least 10 affected users | High |
| Medium urgency OR at least 3 affected users | Medium |
| All other valid tickets | Low |

Valid urgency levels are `low`, `medium`, and `high`.

Valid ticket categories are `Network`, `Hardware`, `Software`, and `Other`.

Ticket titles must not be blank, and the number of affected users must be a positive integer.

## 6. Project Structure

campusflow/ ├── README.md ├── .gitignore ├── main.py ├── campusflow/ │ ├── services.py ├── tickets.py │ ├── workflow.py │ ├── storage.py │ └── reports.py ├── tests/ │ ├── test_tickets.py │ ├── test_workflow.py │ └── test_services.py ├── docs/ │ ├── design-decisions.md │ └── ai-learning-log.md └──  tickets.json


## 7. Installation and Usage

### Prerequisites

Install Python 3 on your computer.

### Clone the Repository

git clone <https://github.com/emaodoh/campusflow.git> cd campusflow


### Run the Application

python3 main.py


Follow the command-line menu to create tickets, assign staff, update statuses, view the work queue, and generate reports.

### Run Automated Tests

python -m pytest tests



The test suite should cover ticket creation, priority calculation, validation, workflow rules, and data persistence.

## 8. Data Storage

CampusFlow uses JSON to store ticket records in `tickets.json`.

- Existing tickets are loaded when the application starts.
- New and updated tickets are saved to preserve data between sessions.
- Missing data files allow a fresh start.
- Malformed JSON should produce a clear error rather than silently erase existing data.
- Ticket IDs must remain unique after reloading saved records.

The runtime data file should be excluded from Git using `.gitignore`.

## 9. Team Contributions

The project is developed by two fellows.

- **Engineer A:** Ticket creation, input validation, priority calculation,menu operation and related tests.
- **Engineer B:** Ticket assignment, status management, work queue, reporting, and related tests.
- **Both Engineers:** JSON persistence, integration, code reviews, AI learning documentation, and final demonstration.


## 10. Testing and Quality Assurance

The application must be tested for:

- Correct priority calculations.
- Invalid and missing input.
- Unique ticket ID generation.
- Assignment and status transitions.
- Work queue ordering.
- Report accuracy.
- JSON saving and loading.
- ID continuity after application restarts.


## 12. Development Workflow

The team follows a collaborative GitHub workflow:

1. Create GitHub Issues for development tasks.
2. Develop features on separate branches.
3. Write and run automated tests.
4. Commit changes using descriptive messages.
5. Open pull requests against `main`.
6. Review each other's code and request corrections when necessary.
7. Obtain approval before merging.
8. Run the complete test suite after integration.

## 13. Future Improvements

Potential future enhancements include:

- User authentication and role management.
- Database integration.
- A graphical or web interface.
- Ticket search and filtering.
- Email notifications.
- Ticket history and audit logs.


## 14. Project Deliverables

- Working Python command-line application.
- Automated test suite.
- JSON-based data persistence.
- GitHub repository with meaningful commits.
- Two reviewed and approved pull requests.
- Completed `docs/design-decisions.md`.
- Completed `docs/ai-learning-log.md`.
- Project demonstration and individual technical explanations.

## 15. Team Information

**Project Name:** CampusFlow

**Engineer A:** [Odoh Emmanuel]

**Engineer B:** [Gabriel Oche]

**GitHub Repository:** [https://github.com/emaodoh/campusflow.git]

## 16. Conclusion

CampusFlow provides a simple and structured way to manage campus IT support requests. It combines ticket management, rule-based prioritization, workflow control, reporting, and persistent storage in a Python command-line application.

The project also promotes responsible AI usage, automated testing, version control, and collaborative code review.

