import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"((?:[0-9]|1[0-2])(?:\:)?(?:[0-5][0-9])?\s(?:[AP]M)) to ((?:[0-9]|1[0-2])(?:\:)?(?:[0-5][0-9])?\s(?:[AP]M))"
    match = re.search(pattern, s)

    if match:
        start_24_hour = convert_24_hours(match.group(1))
        end_24_hour = convert_24_hours(match.group(2))

        return f"{start_24_hour} to {end_24_hour}"

    else:
        raise ValueError

def convert_24_hours(time_12_hour):
    time, meridian = time_12_hour.split()
    if ":" in time:
        hr, min = map(int, time.split(":"))
    else:
        hr, min = int(time), 0

    if meridian == "AM":
        if hr == 12:
            hr = 0
    elif meridian == "PM":
        if hr != 12:
            hr += 12

    return f"{hr:02}:{min:02}"

if __name__ == "__main__":
    main()


