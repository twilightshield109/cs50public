from bank import value

def main():
    test_bank_1()
    test_bank_2()
    test_bank_3()

def test_bank_1():
    assert value("hello") == 0
    assert value("HELLO, WORLD") == 0

def test_bank_2():
    assert value("hey") == 20
    assert value("Hohoho") == 20

def test_bank_3():
    assert value("12345") == 100
    assert value("!@#$%") == 100
    assert value("bonjour") == 100

if __name__ == "__main__":
    main()
