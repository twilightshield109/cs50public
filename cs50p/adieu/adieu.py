import inflect

p = inflect.engine()
NAME = []

#-1th term = last term
#EOFError can detect when ctrl-d is inputted

while True:
    try:
        ADIEU = input("Name:")
        NAME.append(ADIEU)

    except EOFError:
        print()
        break

print("Adieu, adieu, to " + p.join(NAME), sep = "\n")




