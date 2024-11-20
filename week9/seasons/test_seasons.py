import pytest
from datetime import date
from seasons import calculate_age_in_minutes, number_to_words, main


def test_calculate_age_in_minutes():
    # Testing with a date exactly one year ago
    birth_date = date.today().replace(year=date.today().year - 1)
    expected_minutes = 527040
    assert calculate_age_in_minutes(birth_date) == expected_minutes

    # Testing with a date exactly two years ago
    birth_date = date.today().replace(year=date.today().year - 2)
    expected_minutes = 1052640
    assert calculate_age_in_minutes(birth_date) == expected_minutes


def test_number_to_words():
    assert number_to_words(0) == "zero"
    assert number_to_words(525600) == "five hundred twenty-five thousand, six hundred"
    assert number_to_words(1051200) == "one million, fifty-one thousand, two hundred"
    assert number_to_words(527040) == "five hundred twenty-seven thousand forty"


def test_invalid_date_format(monkeypatch):
    # Mock input to simulate an invalid date
    monkeypatch.setattr("builtins.input", lambda _: "invalid-date")
    with pytest.raises(SystemExit):  # Expecting the program to exit
        main()
