from jar import Jar
import pytest



def test_init():
    jar = Jar(3)
    assert jar.capacity == 3


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(12)
    assert jar.capacity == 12
    with pytest.raises(ValueError):
        jar.deposit(16)


def test_withdraw():
    jar = Jar(12)
    jar.deposit(11)
    jar.withdraw(5)
    assert jar.size == 6
    with pytest.raises(ValueError):
        jar.withdraw(11)


