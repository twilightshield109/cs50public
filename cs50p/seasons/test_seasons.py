from seasons import calculate_date
import pytest


def main():
    test_good()
    test_bad()

def test_good():
    assert calculate_date("2025-01-01") == 288000

def test_bad():
    with pytest.raises(ValueError):
        calculate_date("1-1-2025")

if __name__ == "__main__":
    main()



