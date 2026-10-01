def main():
    tweet = input("Input:")
    print(shorten(tweet))


def shorten(word):
    twt = ""
    vowel = ["a","e","i","o","u"]

    for i in range(len(word)):
        if word[i].lower() in vowel:
            pass
        else:
            twt += word[i]
    return(twt)



if __name__ == "__main__":
    main()











