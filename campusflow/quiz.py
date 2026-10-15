from .storage import load_question_bank
from .validate import validate_answer

def quiz():
    question_bank = load_question_bank()
    score = 0

    for question in question_bank:
        print(question["question"])

        for key, value in question["options"].items():
            print(f"{key}. {value}")

        

        while True:
            user_answer = input("Answer: ").upper()
            try:
                check = validate_answer(user_answer)
                break

            except ValueError as error:
                print(f"Error {error}")

        if user_answer == question["answer"]:
            score += 1

    return score