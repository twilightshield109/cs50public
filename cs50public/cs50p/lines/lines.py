import sys
import os

if len(sys.argv) == 2:
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    elif not os.path.exists(sys.argv[1]):
        sys.exit("File does not exist")
        raise FileNotFoundError

    else:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
            line_count = 0
            for line in lines:
                strip_lines = line.strip()
                if line.isspace() or strip_lines.startswith("#"):
                    continue
                else:
                    line_count += 1
            print(line_count)

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
