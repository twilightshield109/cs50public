from plates import is_valid

def main():
    test_plates_valid()
    test_plates_invalid()

def test_plates_valid():
    assert is_valid("CS50") == True
    assert is_valid("XYZ") == True
    assert is_valid("AB413") == True
    assert is_valid("EFG234") == True

def test_plates_invalid():
    assert is_valid("1234") == False
    assert is_valid("CS05") == False
    assert is_valid("AAA2AA") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False



