# add underscore before all capital letters

camel_name = input("camelCase:")
snakeName = ""

for i in camel_name:
# convert uppercase to lowercase and add underscore.
    if (i.isupper()) == True:
        snakeName += "_" + i.lower()

    if(i.islower()) == True:
        snakeName += i

print(snakeName)















