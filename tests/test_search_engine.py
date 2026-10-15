from unittest.mock import patch

import pytest

# Change "campusflow.search" if your module file has a different name.
from campusflow.search_engine import search, search_title

MODULE = "campusflow.search_engine"


@pytest.fixture
def tickets():
    return [
        {"id": "T1", "title": "Wifi down in library", "category": "network",
         "status": "Open", "priority": "High"},
        {"id": "T2", "title": "Projector broken", "category": "hardware",
         "status": "Open", "priority": "Low"},
        {"id": "T3", "title": "WIFI slow in dorm", "category": "Network",
         "status": "Closed", "priority": "High"},
        {"id": "T4", "title": "Password reset", "category": "accounts",
         "status": "open", "priority": "medium"},
    ]


@pytest.fixture
def mock_load(tickets):
    with patch(f"{MODULE}.load_ticket", return_value=tickets) as m:
        yield m


# ---------- search(category, status, priority) ----------

def test_search_returns_matching_tickets(mock_load):
    results = search("network", "open", "high")
    assert [t["id"] for t in results] == ["T1"]
    mock_load.assert_called_once()


def test_search_is_case_insensitive(mock_load):
    results = search("NETWORK", "OPEN", "HIGH")
    assert [t["id"] for t in results] == ["T1"]


def test_search_matches_stored_values_with_different_case(mock_load):
    # T3 is stored as "Network" / "Closed" / "High"
    results = search("network", "closed", "high")
    assert [t["id"] for t in results] == ["T3"]


def test_search_requires_all_three_filters(mock_load):
    # category + status match T1, but priority does not
    assert search("network", "open", "low") == []


def test_search_no_match_returns_empty_list(mock_load):
    assert search("furniture", "open", "high") == []


def test_search_empty_database(mock_load):
    mock_load.return_value = []
    assert search("network", "open", "high") == []


# ---------- search_title(title) ----------

def test_search_title_partial_match(mock_load):
    results = search_title("projector")
    assert [t["id"] for t in results] == ["T2"]


def test_search_title_is_case_insensitive_and_returns_all_matches(mock_load):
    results = search_title("WiFi")
    assert [t["id"] for t in results] == ["T1", "T3"]


def test_search_title_no_match_returns_empty_list(mock_load):
    assert search_title("printer") == []


def test_search_title_empty_string_matches_everything(mock_load, tickets):
    # "" is a substring of every title, so every ticket is returned
    assert search_title("") == tickets


def test_search_title_empty_database(mock_load):
    mock_load.return_value = []
    assert search_title("wifi") == []