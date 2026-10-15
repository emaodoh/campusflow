import json
import os
from typing import List, Dict, Any


def load_ticket() -> List[Dict[str, Any]]:
    """
    Loads tickets from the ticket JSON file.
    """
    file_path = "data/tickets.json"

    if not os.path.exists(file_path):
        save_ticket([])
        return []

    if os.path.getsize(file_path) == 0:
        save_ticket([])
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

            if isinstance(data, list):
                return data

            return []

    except json.JSONDecodeError:
        print(f"Warning: '{file_path}' contained invalid JSON. Resetting.")
        save_ticket([])
        return []


def save_ticket( data: List[Dict[str, Any]]) -> None:
    file_path = "data/tickets.json"
    """
    Saves a list of dictionaries to a JSON file.
    Creates any missing parent directories automatically.
    """
    # Edge Case: Ensure the directory exists before writing
    dir_name = os.path.dirname(file_path)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        # indent=4 makes the file human-readable; ensure_ascii=False supports non-English characters
        json.dump(data, f, indent=4, ensure_ascii=False)
# A sample list of dictionaries




def save_question_bank( data: List[Dict[str, Any]]) -> None:
    file_path = "data/tickets.json"
    """
    Saves a list of dictionaries to a JSON file.
    Creates any missing parent directories automatically.
    """
    # Edge Case: Ensure the directory exists before writing
    dir_name = os.path.dirname(file_path)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        # indent=4 makes the file human-readable; ensure_ascii=False supports non-English characters
        json.dump(data, f, indent=4, ensure_ascii=False)
# A sample list of dictionaries



def load_question_bank() -> List[Dict[str, Any]]:
    """
    Loads questions from the question bank JSON file.
    """
    file_path = "data/question_bank.json"

    if not os.path.exists(file_path):
        save_question_bank([])
        return []

    if os.path.getsize(file_path) == 0:
        save_question_bank([])
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

            if isinstance(data, list):
                return data

            return []

    except json.JSONDecodeError:
        print(f"Warning: '{file_path}' contains invalid JSON. Resetting.")
        save_question_bank([])
        return []
