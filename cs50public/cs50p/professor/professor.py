import random

def main():
    level = get_level()
    point = 0
    attempts = 0

    for i in range(10):
        p, q = generate_integer(level), generate_integer(level)
        while attempts < 3:
            try:
                it = int(input((f"{p} + {q} = ")))
            except ValueError:
                print("EEE")
                attempts += 1
            else:
                if it == (p + q):
                    point += 1
                    attempts = 0
                    break
                else:
                    print("EEE")
                    attempts += 1
                    continue
        else:
            print(f"{p} + {q} = {p + q}")
            attempts = 0

    print(point)

def get_level():
    while True:
        try:
            level = int(input("Level:"))
        except ValueError:
            continue
        if level in [1, 2, 3]:
            return level
        continue

def generate_integer(level):
    if level == 3:
        answer = random.randint(100,999)
    elif level == 2:
        answer = random.randint(10,99)
    elif level == 1:
        answer = random.randint(0,9)
    else:
        raise ValueError
    return answer

if __name__ == "__main__":
    main()

