import pytest
from working import convert


def test_valid_time_conversion():
    assert convert("8 AM to 5 PM") == "08:00 to 17:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("1:30 PM to 3:45 PM") == "13:30 to 15:45"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"


def test_invalid_time_format():
    with pytest.raises(ValueError):
        convert("8 AM 5 PM")  # Missing "to"

    with pytest.raises(ValueError):
        convert("13 PM to 2 PM")  # Hour out of range

    with pytest.raises(ValueError):
        convert("8:60 AM to 4:00 PM")  # Minute out of range

    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")  # Minute out of range


def test_edge_cases():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("1:01 PM to 2:02 PM") == "13:01 to 14:02"
    assert convert("12:59 AM to 1:00 AM") == "00:59 to 01:00"


if __name__ == "__main__":
    pytest.main()
