import sys
import csv
import tabulate

import sys
import os
import csv
from tabulate import tabulate

pizzas = []

if len(sys.argv) == 2:
    if sys.argv[1] == "regular.csv":
        with open("regular.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                pizzas.append({"Regular Pizza": row["Regular Pizza"], "Small": row["Small"], "Large": row["Large"]})

        print(tabulate(pizzas, headers = "keys", tablefmt = "grid"))

    elif sys.argv[1] == "sicilian.csv":
        with open("sicilian.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                pizzas.append({"Sicilian Pizza": row["Sicilian Pizza"], "Small": row["Small"], "Large": row["Large"]})

            print(tabulate(pizzas, headers = "keys", tablefmt = "grid"))

    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    elif not os.path.exists(sys.argv[1]) and sys.argv[1].endswith("csv"):
        sys.exit("File does not exist")
        raise FileNotFoundError

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")


