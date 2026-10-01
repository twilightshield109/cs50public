# vending machines do not accept notes, only coins

amount_due = 50

# check amount due

while amount_due > 0:
    print("Amount Due:", amount_due)

# insert coins

    machine = int(input("Insert Coin:"))

    if machine in [25,10,5]:
        # SUBTRACT VALUE FROM AMOUNT_DUE
        amount_due -= machine

change = abs(amount_due)
print("Change Owed:", change)











