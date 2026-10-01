tweet = input("Input:")
twt = ""
vowel = ["a","e","i","o","u"]

for i in tweet:
    if i.casefold() in vowel:
        pass
    else:
        twt += i

print(twt)







