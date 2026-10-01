expression = input("Expression:")
x, y, z = expression.split(" ")
x_2 = float(x)
z_2 = float(z)

if y == "+":
    print(x_2 + z_2)
if y == "-":
    print(x_2 - z_2)
if y == "*":
    print(x_2 * z_2)
if y == "/":
    print(x_2 / z_2)


