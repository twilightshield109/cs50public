import sys
import csv

students = []

if len(sys.argv) == 3 and sys.argv[1].endswith(".csv"):
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            with open(sys.argv[2], "w") as other_file:
                writer = csv.DictWriter(other_file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                     row["first"] = row.pop("name")
                     last_name, first_name = row["first"].split(", ")
                     row["first"], row["last"] = first_name, last_name
                     writer.writerow(row)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
