import json
import os
from typing import List, Dict, Any

def load() -> List[Dict[str, Any]]:
    file_path = "tickets.json"
    """
    Loads a list of dictionaries from a JSON file.
    If the file does not exist or is empty, creates a new file with an empty list.
    """
    # Edge Case: File does not exist -> Create it with an empty list []
    if not os.path.exists(file_path):
        save(file_path)
        return []

    # Edge Case: File exists but is completely empty (0 bytes)
    if os.path.getsize(file_path) == 0:
        save_to_json(file_path, [])
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Ensure the root data structure is a list
            return data if isinstance(data, list) else [data]
            
    except json.JSONDecodeError:
        # Edge Case: File contains invalid/corrupted JSON -> Reset it to safely continue
        print(f"Warning: '{file_path}' contained invalid JSON. Resetting to an empty list.")
        save_to_json(file_path, [])
        return []


def save( data: List[Dict[str, Any]]) -> None:
    file_path = "tickets.json"
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
