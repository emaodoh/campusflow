class IDGenerator:
    def __init__(self, prefix: str = "F", start_num: int = 1):
        self.prefix = prefix
        self.counter = start_num

    def get_next_id(self) -> str:
        self.generated_id = f"{self.prefix}{self.counter:03d}"
        self.counter += 1
        return self.generated_id

# --- 2. GLOBAL SYSTEM INITIALIZATION ---
# This runs ONCE when the script starts. It lives in the background.
id_factory = IDGenerator(prefix="F", start_num=1)



def priority(urgency, affected_users):
    urgency = urgency.lower()
    if urgency == "high" and affected_users >= 10:
        return "critical"
    
    if urgency == "high" or affected_users >= 10:
        return "high"

    if urgency == "medium" or affected_users >= 3:
        return "medium"

    return "low"


def check_categories(category):
    if category.lower() in ["network", "hardware", "software", "other"]:
        return category.title()

    return "Other"

def check_urgency(urgency):
    if urgency  in ["low", "medium", "high"]:
        return urgency

    return None

def check_affected_users(affected_users):
    try:
        affected_users = int(affected_users)
        if affected_users > 0:
            return affected_users

    except ValueError:
        return None