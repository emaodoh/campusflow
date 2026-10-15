def validate_note_entry(author, message):
    if not author or not message:
        raise ValueError("message or author can not be empty.")

    if len(message) < 5 or len(massage) > 200:
        raise ValueError("Message can not be above 200")