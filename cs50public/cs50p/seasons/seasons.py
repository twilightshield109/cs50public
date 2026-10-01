import datetime
from datetime import datetime, date
import sys
import inflect

p = inflect.engine()

def main():
    try:
        a = calculate_date(input("Date of Birth:"))
        b = p.number_to_words(a, andword = "")
        c = str(b).capitalize()
        print(f"{c} minutes")
    except ValueError:
        sys.exit("Invalid Date")

def calculate_date(str_birth_date):
    birth_date = date.fromisoformat(str_birth_date)
    current_time = date.today()
    time_diff = current_time - birth_date
    minutes = int(time_diff.total_seconds() // 60)
    return minutes

if __name__ == "__main__":
    main()
