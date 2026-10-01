def main():
    clock = input("What time is it?")
    clock = convert(clock)
    if 7 <= clock <= 8:
        print("breakfast time")
    elif 13 <= clock <= 14:
        print("lunch time")
    elif 18 <= clock <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)/60
    time = hours + minutes
    return float(time)

if __name__ == "__main__":
        main()
