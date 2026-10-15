import pytest
from campusflow.services import (
    # IDGenerator,
    # id_factory,
    priority,
    check_categories,
    check_urgency,
    check_affected_users,
)

# # ==========================================
# # 1. Tests for IDGenerator Class & Factory
# # ==========================================

# def test_id_generator_increments_and_formats():
#     """Verify that IDGenerator pads numbers and increments accurately."""
#     generator = IDGenerator(prefix="T", start_num=9)
#     assert generator.get_next_id() == "T009"
#     assert generator.get_next_id() == "T010"

# def test_global_id_factory():
#     """Ensure the background id_factory is functioning and tracking state."""
#     # Since it's imported globally, we just make sure it yields the initial expected pattern
#     # Note: If other tests use this global factory, the starting number might vary.
#     current_id = id_factory.get_next_id()
#     assert current_id.startswith("F")
#     assert len(current_id) == 4


# ==========================================
# 2. Tests for priority()
# ==========================================

@pytest.mark.parametrize(
    "urgency, affected_users, expected_priority",
    [
        ("high", 15, "critical"),   # Both high urgency and >= 10 users
        ("high", 2, "high"),        # High urgency but fewer users
        ("low", 12, "high"),        # Low urgency but >= 10 users
        ("medium", 5, "medium"),    # Medium urgency and >= 3 users
        ("low", 4, "medium"),       # Low urgency but >= 3 users
        ("low", 1, "low"),          # Neither conditions met
    ]
)
def test_priority_logic(urgency, affected_users, expected_priority):
    assert priority(urgency, affected_users) == expected_priority

def test_priority_case_insensitivity():
    """Ensure priority functions properly regardless of casing."""
    assert priority("HIGH", 10) == "critical"
    assert priority("Medium", 3) == "medium"


# ==========================================
# 3. Tests for check_categories()
# ==========================================

@pytest.mark.parametrize(
    "input_category, expected_output",
    [
        ("network", "Network"),
        ("HARDWARE", "Hardware"),
        ("software", "Software"),
        ("other", "Other"),
        ("unknown_category", "Other"),
    ]
)
def test_check_categories(input_category, expected_output):
    assert check_categories(input_category) == expected_output


# ==========================================
# 4. Tests for check_urgency()
# ==========================================

@pytest.mark.parametrize(
    "input_urgency, expected_output",
    [
        ("low", "low"),
        ("medium", "medium"),
        ("high", "high"),
        ("critical", None),  # Invalid based on the function's strict match list
        ("LOW", None),       # Function does not call .lower(), so uppercase fails
    ]
)
def test_check_urgency(input_urgency, expected_output):
    assert check_urgency(input_urgency) == expected_output



if __name__ == "__main__":
    unittest.main()