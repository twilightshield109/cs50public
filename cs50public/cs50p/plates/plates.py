def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

    # Minimum 2 Letters and Maximum 6 letters
    # First two must be letters
    # First number cannot be 0
    # Number cannot be in the middle of a plate (check every number with for loop)
    # No punctuation allowed
    # No space allowed

def is_valid(s):
    if len(s) <= 6 and len(s) >= 2:
        if s.isalpha():
            return True

        elif s.isalnum() and s[0:2].isalpha():
            for char in s:
                if char.isdigit():
                    position = s.index(char)

                    if s[position:].isdigit() and int(char) != 0:
                        return True

                    else:
                        return False
main()
