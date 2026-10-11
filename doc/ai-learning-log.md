# Engineer A

**Name:** [Odoh Emmanuel]

## Interaction 1: Understanding GitHub Branching

**Problem:**  
I needed to understand how to create and use a separate Git branch to develop my CampusFlow features without directly modifying the main branch.

**Initial Understanding:**  
I knew GitHub was used to store code, but I was unsure how branches allowed team members to work independently.

**Prompt to AI:**  
"Explain Git branches using a simple example. Show me how to create a feature branch, make changes, commit them, and push the branch to GitHub."

**AI Guidance:**  
AI explained that branches allow developers to work on separate versions of a project. It also explained how to create a branch, commit changes, and push the branch to a remote repository.

**Independent Experiment:**  
I created a feature branch for my assigned CampusFlow task and checked my current branch using Git commands.

Commands used:

git switch main git pull origin main git switch -c feat/1-ticket-creation git status


After making changes, I committed and pushed my work:

git add . git commit -m "feat: implement ticket creation" git push -u origin feat/1-ticket-creation


**Verification:**  
I checked the current branch using `git status` and verified that my feature branch appeared in the GitHub repository.

**Decision:**  
I used the branch workflow to keep my development work separate from the main branch.

**What I Learned:**  
I learned how Git branches support independent development and help teams organize their work without directly changing the main branch.

---

## Interaction 2: Python Input Validation

**Problem:**  
I needed to understand how to validate user input and prevent invalid ticket information from being stored.

**Initial Understanding:**  
I understood that Python could check input values, but I was unsure how to handle invalid values consistently.

**Prompt to AI:**  
"Explain Python input validation and exception handling using a small example. Explain how to reject invalid numeric input."

**AI Guidance:**  
AI explained how conditional statements and exception handling can be used to validate input and display useful error messages.

**Independent Experiment:**  
I tested valid and invalid numeric inputs in a small Python program.

**Verification:**  
I compared the program's output with my expected results.

**Decision:**  
I used the concepts to guide validation in CampusFlow and checked that invalid inputs were rejected.

**What I Learned:**  
I learned how to validate user input and handle errors without allowing invalid values to proceed into the application.

