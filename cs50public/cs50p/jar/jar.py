class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if self._size > self._capacity:
            raise ValueError("Deposit exceeds capacity of jar")
        elif n < 0:
            raise ValueError("Number is too small")
        else:
            self.size += n


    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Withdrawal exceeds capacity of jar")
        elif n < 0:
            raise ValueError("Number is too small")
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not 0 <= value <= self.capacity:
            raise ValueError("Size is outside of range")
        self._size = value

def main():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(4)

if __name__ == "__main__":
    main()
