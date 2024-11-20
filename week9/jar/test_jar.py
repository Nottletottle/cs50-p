import pytest
from jar import Jar


class TestJar:
    def test_initialization(self):
        jar = Jar()
        assert jar.capacity == 12
        assert jar.size == 0

    def test_initialization_with_custom_capacity(self):
        jar = Jar(10)
        assert jar.capacity == 10
        assert jar.size == 0

    def test_initialization_invalid_capacity(self):
        with pytest.raises(
            ValueError, match="Capacity must be a non-negative integer."
        ):
            Jar(-1)
        with pytest.raises(
            ValueError, match="Capacity must be a non-negative integer."
        ):
            Jar("a")
        with pytest.raises(
            ValueError, match="Capacity must be a non-negative integer."
        ):
            Jar(3.5)

    def test_str(self):
        jar = Jar(5)
        assert str(jar) == ""
        jar.deposit(3)
        assert str(jar) == "🍪🍪🍪"
        jar.withdraw(1)
        assert str(jar) == "🍪🍪"

    def test_deposit(self):
        jar = Jar(5)
        jar.deposit(5)
        assert jar.size == 5
        with pytest.raises(ValueError, match="Exceeding capacity."):
            jar.deposit(1)

    def test_deposit_negative(self):
        jar = Jar(5)
        with pytest.raises(
            ValueError, match="Cannot deposit a negative number of cookies."
        ):
            jar.deposit(-1)

    def test_withdraw(self):
        jar = Jar(5)
        jar.deposit(3)
        jar.withdraw(2)
        assert jar.size == 1
        with pytest.raises(ValueError, match="Not enough cookies to withdraw."):
            jar.withdraw(3)

    def test_withdraw_negative(self):
        jar = Jar(5)
        with pytest.raises(
            ValueError, match="Cannot withdraw a negative number of cookies."
        ):
            jar.withdraw(-1)

    def test_capacity_property(self):
        jar = Jar(10)
        assert jar.capacity == 10

    def test_capacity_setter_invalid_values(self):
        jar = Jar()
        with pytest.raises(
            ValueError, match="Capacity must be a non-negative integer."
        ):
            jar.capacity = -5
        with pytest.raises(
            ValueError, match="Capacity must be a non-negative integer."
        ):
            jar.capacity = "invalid"
        with pytest.raises(
            ValueError, match="Capacity must be a non-negative integer."
        ):
            jar.capacity = 2.5

    def test_capacity_setter_valid_value(self):
        jar = Jar()
        jar.capacity = 15
        assert jar.capacity == 15

    def test_initial_size(self):
        jar = Jar()
        assert jar.size == 0

    def test_full_capacity_after_deposit(self):
        jar = Jar(3)
        jar.deposit(3)
        assert jar.size == 3
        assert str(jar) == "🍪🍪🍪"

    def test_empty_capacity_after_withdraw(self):
        jar = Jar(3)
        jar.deposit(3)
        jar.withdraw(3)
        assert jar.size == 0
        assert str(jar) == ""
