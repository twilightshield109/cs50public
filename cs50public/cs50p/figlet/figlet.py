from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(fonts))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "-font") and sys.argv[2] in fonts:
    figlet.setFont(font = sys.argv[2])
else:
    sys.exit("Invalid usage")

#the input must be put after the if statements so it checks for length before asking for input
FIG = input("Input:").strip()

print(figlet.renderText(FIG))
