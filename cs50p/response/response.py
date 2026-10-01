import validators
# pyright: reportMissingImports=false


def main():
    print(validation(input("What's your email address?")))

def validation(email):
    if validators.email(email) == True:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()


