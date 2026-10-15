from unittest.mock import patch

import pytest

from campusflow.quiz import quiz

MODULE = "campusflow.quiz"


@pytest.fixture
def question_bank():
    return [
        {
            "question": "What is 2 + 2?",
            "options": {"A": "3", "B": "4", "C": "5", "D": "22"},
            "answer": "B",
        },
        {
            "question": "Capital of France?",
            "options": {"A": "Paris", "B": "Rome", "C": "Madrid", "D": "Berlin"},
            "answer": "A",
        },
    ]


@pytest.fixture
def mock_validate():
    # Default: every answer is valid (validate_answer returns without raising)
    with patch(f"{MODULE}.validate_answer") as m:
        yield m


@pytest.fixture
def mock_bank(question_bank):
    with patch(f"{MODULE}.load_question_bank", return_value=question_bank) as m:
        yield m


def test_all_answers_correct(mock_bank, mock_validate):
    with patch("builtins.input", side_effect=["B", "A"]):
        assert quiz() == 2


def test_all_answers_wrong(mock_bank, mock_validate):
    with patch("builtins.input", side_effect=["A", "B"]):
        assert quiz() == 0


def test_partial_score(mock_bank, mock_validate):
    with patch("builtins.input", side_effect=["B", "D"]):
        assert quiz() == 1


def test_answers_are_case_insensitive(mock_bank, mock_validate):
    # quiz() upper-cases input, so lowercase answers should still score
    with patch("builtins.input", side_effect=["b", "a"]):
        assert quiz() == 2


def test_empty_question_bank_raiseValue_error(mock_bank, mock_validate):
    # Arrange: Setup the mock to return an empty bank
    mock_bank.return_value = []
    
    # Act & Assert: Verify that calling quiz() throws a ValueError
    with patch("builtins.input") as mock_input:
        with pytest.raises(ValueError):
            quiz()
            
    # Assert: Verify that input was never requested from the user
    mock_input.assert_not_called()


def test_prints_question_and_options(mock_bank, mock_validate, capsys):
    with patch("builtins.input", side_effect=["B", "A"]):
        quiz()

    output = capsys.readouterr().out
    assert "What is 2 + 2?" in output
    assert "B. 4" in output
    assert "Capital of France?" in output
    assert "A. Paris" in output


def test_invalid_answer_reprompts_until_valid(mock_bank, mock_validate, capsys):
    # Question 1: "X" is rejected, then "B" is accepted. Question 2: "A" accepted.
    mock_validate.side_effect = [ValueError("invalid option"), None, None]

    with patch("builtins.input", side_effect=["X", "B", "A"]) as mock_input:
        score = quiz()

    assert score == 2
    assert mock_input.call_count == 3
    assert "Error invalid option" in capsys.readouterr().out


def test_invalid_answer_is_not_scored(mock_bank, mock_validate):
    # The rejected "B" must not count; only the re-entered "C" is scored (wrong)
    mock_validate.side_effect = [ValueError("invalid"), None, None]

    with patch("builtins.input", side_effect=["B", "C", "A"]):
        # Q1: "B" rejected, "C" accepted but wrong. Q2: "A" correct.
        assert quiz() == 1


def test_validate_answer_receives_uppercased_input(mock_bank, mock_validate):
    with patch("builtins.input", side_effect=["b", "a"]):
        quiz()

    mock_validate.assert_any_call("B")
    mock_validate.assert_any_call("A")