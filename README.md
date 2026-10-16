# CampusFlow — Campus Helpdesk Ticket Management System

## 1. Project Overview

CampusFlow is a Python-based command-line helpdesk application designed to help campus IT support teams manage technical issues efficiently.

The system allows users to create support tickets, calculate priorities, assign tickets to staff, update ticket statuses, add notes, search tickets, generate reports, play a ticket knowledge quiz, and store application data using JSON files.

The project also demonstrates AI-assisted learning, automated testing, and collaborative software development using Git and GitHub.

---

## 2. Objectives

- Create and manage support tickets.
- Validate ticket information and generate unique ticket IDs.
- Calculate ticket priorities using predefined rules.
- Assign tickets to support staff.
- Update ticket statuses throughout the ticket lifecycle.
- Add and manage ticket notes.
- Search tickets using different search methods.
- Generate ticket statistics and reports.
- Store and retrieve application data using JSON.
- Build an interactive ticket knowledge quiz.
- Apply automated testing and professional Git workflows.
- Use AI responsibly for learning, debugging, and code improvement.

---

## 3. Technologies Used

- **Python 3:** Application development.
- **JSON:** Data storage and persistence.
- **pytest:** Automated testing.
- **Git:** Version control.
- **GitHub:** Repository management and code reviews.
- **AI Assistant:** Learning, debugging, and technical guidance.

---

## 4. Core Features

### 1. Ticket Creation

- Creates tickets with validated information and unique IDs.
- Automatically calculates ticket priority.
- Allows users to optionally add a note during ticket creation.
- If note creation fails because of invalid author or message input, the ticket will still be created without a note.
- Users can add notes later using the main note management feature.

### 2. Ticket Status Management

- Supports updating ticket status.
- Tracks ticket progress from creation to resolution.
- Maintains ticket workflow rules during status changes.

### 3. Priority Calculation

- Automatically determines ticket priority based on urgency and affected users.

### 4. Ticket Assignment

- Assigns tickets to support staff.

### 5. Note Management

- Allows users to add notes to existing tickets.
- Allows users to view ticket notes.
- Validates note author and message before saving.
- Prevents empty notes from being stored.

### 6. Search System

CampusFlow supports multiple search methods:

#### Title Search

- Searches tickets by title.
- Supports case-insensitive matching.
- Supports substring searching.

Example:
wifi
WIFI
WiFi

will match:



#### Filter Search

Supports combined filtering using:

- Category
- Priority
- Status

Filters are combined using **AND logic**, meaning a ticket must match all provided filters.

### 7. Reports

- Generates ticket summaries.
- Displays ticket totals.
- Shows breakdowns by status and priority.

### 8. Ticket Knowledge Quiz

- Includes an interactive quiz game.
- Uses a JSON-based question bank.
- Validates user answers.
- Calculates quiz scores.

### 9. JSON Persistence

- Saves and loads tickets and quiz questions using JSON files.
- Data files are stored separately inside the `data/` directory.

---

# 5. Priority Rules

Ticket priority is calculated using the following rules:

| Condition | Priority |
|---|---|
| High urgency AND at least 10 affected users | Critical |
| High urgency OR at least 10 affected users | High |
| Medium urgency OR at least 3 affected users | Medium |
| All other valid tickets | Low |

Valid urgency levels:
low
medium
high

Valid ticket categories:


Network
Hardware
Software
Other


Ticket titles must not be blank, and affected users must be a positive integer.

---

# 6. Project Structure
campusflow/
│
├── README.md
├── .gitignore
├── main.py
│
├── campusflow/
│   ├── services.py
│   ├── tickets.py
│   ├── workflow.py
│   ├── storage.py
│   ├── reports.py
│   ├── search_engine.py
│   ├── notes.py
│   ├── quiz.py
│   └── validate.py
│
├── data/
│   ├── tickets.json
│   └── question_bank.json
│
├── tests/
│   ├── test_tickets.py
│   ├── test_search.py
│   ├── test_notes.py
│   ├── test_quiz.py
│   └── test_storage.py
│
└── docs/
    ├── design-decisions.md
    └── ai-learning-log.md


---

# 7. Installation and Usage

## Prerequisites

Install Python 3 on your computer.

## Clone the Repository

```bash
git clone https://github.com/emaodoh/campusflow.git

cd campusflow


Run the Application


python3 main.py
```
The command-line menu allows users to:
- Create tickets.
- Add notes.
- View notes.
- Search tickets.
- Assign tickets.
- Update ticket status.
- Generate reports.
- Play the ticket knowledge quiz.

Run Automated Tests

python -m pytest tests

The test suite covers:
- Ticket creation.
- Validation.
- Search functionality.
- Notes management.
- Quiz functionality.
- Workflow rules.
- JSON persistence.

# 8. Data Storage
CampusFlow stores application data using JSON files inside the data/ directory.
Current data files:
data/
├── tickets.json
└── question_bank.json

Storage behavior:
- Each function that requires ticket information loads tickets independently.
- Ticket data is loaded only when required.
- Changes are saved back to JSON files.
- Missing data files allow the application to start with empty data.
- Corrupted JSON files are handled safely.
- Question bank data is separated from ticket data to prevent accidental overwriting.
- Runtime data files should be excluded from Git using .gitignore

# 9 Testing and Quality Assurance

The application is tested for:
- Correct priority calculations.
- Invalid and missing input handling.
- Unique ticket ID generation.
- Ticket status transitions.
- Note creation and viewing.
- Search functionality.
- Quiz scoring and validation.
- Report accuracy.
- JSON saving and loading.
- Recovery from missing or corrupted files.


# 10. Development Workflow
The team follows a collaborative GitHub workflow:
1. Create GitHub Issues for development tasks.
2. Develop features on separate branches.
3. Write and run automated tests.
4. Commit changes using descriptive messages.
5. Open pull requests against main.
6. Review each other's code.
7. Request corrections when necessary.
8. Obtain approval before merging.
9. Run the complete test suite after integration.


# 11. Future Improvements
Potential future enhancements include:
- User authentication and role management.
- Database integration.
- Graphical or web interface.
- Advanced analytics dashboard.
- Email notifications.
- Ticket history and audit logs.


# 12. Project Deliverables
- Working Python command-line application.
- Automated pytest test suite.
- JSON-based data persistence.
- GitHub repository with meaningful commits.
- Reviewed and approved pull requests.
- Completed docs/design-decisions.md.
- Completed docs/ai-learning-log.md.
- Project demonstration and individual technical explanations.

# 13. Team Information
Project Name: CampusFlow
Engineer A: Odoh Emmanuel
Engineer B: Gabriel Oche
GitHub Repository:
https://github.com/emaodoh/campusflow.git

# 14. Conclusion
CampusFlow provides a structured way to manage campus IT support requests through a Python command-line application.
The system combines ticket management, priority calculation, workflow control, status updates, note management, searching, reporting, quiz-based learning, validation, automated testing, and JSON-based persistent storage.
The project promotes clean software engineering practices through version control, testing, code reviews, and responsible AI-assisted development.