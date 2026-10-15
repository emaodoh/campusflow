def validate_note_entry(author, message):
    if not author or not message:
        raise ValueError("Author or message cannot be empty.")

    if len(message) < 5 or len(massage) > 200:
        raise ValueError("Message can not be above 200")


def validate_answer(user_answer):
    if user_answer.lower() not in ("a", "b", "c", "d"):
        raise ValueError(f"{user_answer} is invalid. Choose A, B, C, or D.")