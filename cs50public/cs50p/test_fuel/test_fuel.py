from fuel import convert, gauge
import pytest

def main():
    test_conversion()
    test_gauge()
    test_errors()

def test_conversion():
    assert convert("5/9") == 56
    assert convert("2/3") == 67
    assert convert("1/90") == 1

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(66) == "66%"

def test_errors():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("cat/rat")
