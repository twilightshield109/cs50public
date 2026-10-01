inputdict = {}

while True:
    try:
        item = input().upper()
        if item in inputdict:
            inputdict[item] += 1
        else:
            inputdict[item] = 1

    except EOFError:
        print()
        break

for item in sorted(inputdict.keys()):
    print(inputdict[item], item)
