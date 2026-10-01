input1 = input("Greeting:")
input1 = input1.lower().strip()

if "hello" in input1:
    print("$0")
elif "h" in input1[0]:
    print("$20")
else:
    print("$100")
