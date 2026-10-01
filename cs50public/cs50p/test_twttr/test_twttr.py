from twttr import shorten

def main():
    test_twttr()


def test_twttr():
    assert shorten("hello") == "hll"
    assert shorten("HELLO, WORLD") == "HLL, WRLD"
    assert shorten("HERE 1S PYTH0N") == "HR 1S PYTH0N"
    assert shorten("12345") == "12345"

if __name__ == "__main__":
    main()
