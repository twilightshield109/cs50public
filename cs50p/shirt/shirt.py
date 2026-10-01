import sys, csv, os
from PIL import Image, ImageOps

images = []
extensions = [".jpg", ".jpeg", ".png"]
ex1 = os.path.splitext(sys.argv[1])
ex2 = os.path.splitext(sys.argv[2])


if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

else:

    if ex1[1] not in extensions:
        sys.exit("Invalid output")

    elif ex1[1] != ex2[1]:
        sys.exit("Input and output have different extensions")

    else:
        try:
            muppet = Image.open(sys.argv[1], "r")
        except FileNotFoundError:
            sys.exit("Input does not exist")

        shirt = Image.open("shirt.png")
        shirt_size = shirt.size
        muppet = ImageOps.fit(muppet, shirt_size)
        muppet.paste(shirt, shirt)
        muppet.save(sys.argv[2])








