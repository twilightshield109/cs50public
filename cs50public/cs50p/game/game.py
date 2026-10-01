import random

while True:
    try:
        n = int(input("Level:"))
        p = random.randint(1,n)
        break
    except ValueError:
        continue

while True:
    try:
        guess = int(input("Guess:"))
    except ValueError:
        continue
    else:
        if guess > p:
            print("Too large!")
        elif guess < p:
            print("Too small!")
        else:
            print("Just right!")
            break
