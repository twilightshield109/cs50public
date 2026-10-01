while True:
    fuel = input("Fraction:")

    try:

        x, y = fuel.split("/")
        x, y = int(x), int(y)

        fuel_output = x/y

    # break = exit loop
        if fuel_output <= 1:
            break

    except (ValueError, ZeroDivisionError):
        pass

fuel_output = fuel_output * 100
fuel_output = round(fuel_output)

if fuel_output >= 99:
    print("F")

elif fuel_output <= 1:
    print("E")

else:
    print(f"{fuel_output}%")


