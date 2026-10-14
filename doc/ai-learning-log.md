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






## Name: Angel (Engineer B)

---

### Interaction #1 — Functions that reject bad input (`raise`, `try/except`, finding an item in a list)

**Problem:** I needed to write `assign_ticket`, which must reject a blank staff name and an unknown ticket ID without changing any ticket, and I did not know how to signal an error from a function.

**My initial understanding:** TODO (write in your own words what you understood before, for example "I knew loops but not `raise`").

**Prompt to AI:** I asked for a plan for my Engineer B work and how to start coding the assign feature, and asked to be taught step by step. The AI did not give me the project code first. It gave me a small unrelated example about lending library books.

**Useful AI guidance:** A function receives the list and the values as inputs. It checks for problems first, then changes the data last. It uses `.strip()` to clean a name, a `for` loop to find the matching item, and `raise ValueError(...)` to reject bad input. The caller uses `try/except` to catch the error.

**My independent experiment/test:** I ran the library example in a scratch file (`scratch.py`). Output I observed:

```
{'id': 'B2', 'title': 'Git Guide', 'lent_to': 'Ada'}
[{'id': 'B1', 'title': 'Python Basics', 'lent_to': None}, {'id': 'B2', 'title': 'Git Guide', 'lent_to': 'Ada'}]
Error: Book B9 not found
```

My prediction before running: TODO (write what you expected, or write honestly that you did not predict first).

**Verification source or result:** The output showed the name was cleaned (`Ada` without spaces), the list itself was changed, and the unknown ID raised an error that `except` caught. Later, my project tests for assign all passed when I ran `python3 -m unittest discover -s tests -v`.

**Decision:** Accepted the approach. Because of limited time, I then asked the AI to provide the full code for my files, so `campusflow/workflow.py` and `tests/test_workflow.py` came from the AI rather than being written by me. I ran the 14 tests (all `ok`). TODO: add what you read and checked in the code before committing.

**Related file/commit:** `campusflow/workflow.py` (`assign_ticket`), `tests/test_workflow.py` (`TestAssign`), commit SHA: TODO

**What I can now explain without AI:** TODO (for example: why the blank-name check comes before changing the ticket, and why the list changes without putting the item back).

---

### Interaction #2 — Sorting with a `key` function and `lambda` (the work queue)

**Problem:** I did not understand this line in my queue: `key=lambda t: (PRIORITY_ORDER[t["priority"]], int(t["id"][1:]))`.

**My initial understanding:** TODO.

**Prompt to AI:** I asked the AI to explain that line.

**Useful AI guidance:** `lambda` is a small unnamed function. `PRIORITY_ORDER` turns the priority word into a number so critical sorts first. `int(t["id"][1:])` removes the `T` and turns the rest into a number, so `T20` comes before `T100` (sorting the text would put `T100` first). A pair of values `(a, b)` sorts by `a` first, then `b` for ties.

**My independent experiment/test:** TODO. Suggested experiment: run this in a scratch file and write your prediction before running:

```python
print(sorted(["T100", "T20"]))
print(sorted([100, 20]))
print(int("T012"[1:]))
```

Prediction: TODO. Observed result: TODO.

**Verification source or result:** My tests `test_sorted_by_priority_then_numeric_id` and `test_numeric_id_tiebreak_not_text` passed. TODO: add the official Python docs page for `sorted()` if you checked it.

**Decision:** TODO (accepted, improved, or rejected, and why).

**Related file/commit:** `campusflow/workflow.py` (`get_queue`), `tests/test_workflow.py` (`TestQueue`), commit SHA: TODO

**What I can now explain without AI:** TODO.

---

### Interaction #3 — Checking Engineer A's code against the shared data format (critical evaluation)

**Problem:** My queue, status rules and report depend on the ticket format from the brief. I needed to know whether Engineer A's `create_ticket` produces tickets my code can use.

**My initial understanding:** TODO.

**Prompt to AI:** I pasted Engineer A's `create_ticket` and asked the AI to explain it.

**Useful AI guidance:** The AI pointed out possible mismatches with the brief and with my code: the ID format (`F-XXXXXX` instead of `T001`), `status="Open"` with a capital O instead of `"open"`, `assigned_to="None"` as text instead of the real `None`, errors returned as text instead of raised, and `load()`/`save()` called inside the function.

**My independent experiment/test:** TODO. You must check these claims yourself and not trust the AI. For example, create one ticket with A's real function, print it, and record what the `id`, `status` and `assigned_to` values actually are. Then run my `get_queue` on it and record what happens.

**Verification source or result:** TODO (the real output you got).

**Decision:** TODO. Write honestly what happened. Examples of valid outcomes: the AI was right and I raised it in my PR review; one claim was wrong because A had already fixed it; I changed my code to accept A's format.

**Related file/commit:** TODO (PR review comment link or commit SHA)

**What I can now explain without AI:** TODO (for example: why two parts of a program must agree on exact values such as `"open"`).

---

## Notes

- Correction I received during planning: I first thought the code could get the live ticket list by calling the `save` function. The AI explained that `load` reads the file and `save` writes it, and that my functions should receive the list from the menu and not read the file themselves, so they can be tested. TODO: confirm in your own words whether you accepted this and what you told Engineer A.
- Time limits meant some code was AI-provided. I am reading it, running its tests, and checking it against the brief so I can explain it in the technical defence.
