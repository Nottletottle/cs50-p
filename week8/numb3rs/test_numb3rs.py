from numb3rs import validate
import pytest


def test_input():
    assert validate("125.555.555.555") == False
    assert validate("125.555.555.555.555") == False
    assert validate("123.123.123.123") == True
