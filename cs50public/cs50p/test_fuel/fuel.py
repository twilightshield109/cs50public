def main():
    percentage = convert(input("Fraction:")).strip()
    print(gauge(percentage))


def convert(fraction):
    while True:
        try:
            x,y = fraction.split("/")
            x,y = int(x), int(y)
            fuel_output = x/y

            if fuel_output <= 1:
                percentage = round(fuel_output * 100)
                return percentage

            else:
                fraction = input("Fraction:")
                pass

        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage >= 99:
        return("F")

    elif percentage <= 1:
        return("E")

    else:
        return(str(percentage) + "%")


if __name__ == "__main__":
    main()
