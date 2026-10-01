import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$"
    match = re.search(pattern,ip)

    if not match:
        return False
    for i in match.groups():
        if not(0 <= int(i) <= 255):
            return False
        elif i.startswith("0") and i != "0":
            return False
    return True

if __name__ == "__main__":
    main()
