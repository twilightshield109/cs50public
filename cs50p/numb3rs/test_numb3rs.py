from numb3rs import validate

def main():
    test_ip_true()
    test_ip_false()

def test_ip_true():
    assert validate("1.2.3.4") == True
    assert validate("100.43.12.97") == True
    assert validate("255.123.1.34") == True

def test_ip_false():
    assert validate("500.500.500.500") == False
    assert validate("256.1.2.3") == False
    assert validate("100.0001.43.23") == False
    assert validate("cat") == False

if __name__ == "__main__":
    main()
