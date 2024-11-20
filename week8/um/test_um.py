import pytest
from um import count


def test_count_single_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1


def test_count_multiple_ums():
    assert count("Um, thanks, um...") == 2
    assert count("um um um um um") == 5


def test_count_no_um_in_word():
    assert count("summary") == 0
    assert count("bump") == 0
    assert count("humor") == 0


def test_count_mixed_case():
    assert count("Um um um") == 3
    assert count("UM!") == 1
    assert count("uM?") == 1


def test_count_no_um_sentences():
    assert count("Hello, how are you?") == 0
    assert count("") == 0


def test_count_edge_cases():
    assert count("  um ") == 1


if __name__ == "__main__":
    pytest.main()
