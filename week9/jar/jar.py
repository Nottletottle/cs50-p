class Jar:
    def __init__(self, capacity=12):
        self._capacity = None
        self.capacity = capacity
        self._cookies = 0

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = value

    @property
    def size(self):
        return self._cookies

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies.")
        if self._cookies + n > self._capacity:
            raise ValueError("Exceeding capacity.")
        self._cookies += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies.")
        if n > self._cookies:
            raise ValueError("Not enough cookies to withdraw.")
        self._cookies -= n
