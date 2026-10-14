# Baseline Check

## Run Command

```bash
python3 main.py
```

## Test Results

- **Passing:** 3/3 manual test scenarios passed successfully.
- **Failing:** 0 failures.

## Inputs Tested

1. **Option 1 – Create Ticket:** Created a new ticket successfully to verify database insertion.
2. **Option 6 – Reports:** Generated the report to verify that summary information displayed correctly.
3. **Option 2 (List/View) / Option 3 (Assign):** Entered an invalid ticket ID (`dfsfdd`) and confirmed the application handled the invalid input gracefully without crashing.

## Audit Findings & Areas for Improvement

- **Peer-reported issues:** The audit reported that the **Reports** and **Work Queue** displays need improvement because their layout is difficult to read.
- **Verification:** I did **not** reproduce these layout issues as functional bugs during my testing, so they are recorded as peer-reported observations rather than confirmed defects. All tested functionality executed successfully without crashes.