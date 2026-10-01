from project import get_timed_input, calculate_wpm, chara_accuracy, colour_words
from faker import Faker

Faker.seed(4321)

def main():
    test_get_timed_input()
    test_chara_accuracy()
    test_calculate_wpm()

def test_get_timed_input(monkeypatch):
    user_inputs = (Faker().text()).replace(".", "")
    monkeypatch.setattr("builtins.input", lambda _: (user_inputs))
    mock_time = iter([100.0, 105.0])
    monkeypatch.setattr("time.time", lambda: next(mock_time))
    user_input, time_taken = get_timed_input()

    assert user_input == "Imagine as computer half Take only main\nDiscuss prevent stock knowledge color according mother just World personal decision front politics Little fast then go hope attention friend peace"
    assert time_taken == 5.0

def test_chara_accuracy():
    assert chara_accuracy("abcd", "abcd") == (100.0, 1, 0, 1)
    assert chara_accuracy("Sheep sheep", "sheep shep") == (0.0, 0, 2, 2)

def test_calculate_wpm():
    assert calculate_wpm("abcd",3) == (20.0, 0.05)
    assert calculate_wpm("Sheep sheep sheep", 6) == (30.0,0.1)

if __name__ == "__main__":
    main()
