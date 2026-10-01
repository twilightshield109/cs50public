def playback(sentence):
    print(sentence, sep = "...")
sentence = input("What do you want to say?")
sentence = sentence.replace(" ", "...")
playback(sentence)

