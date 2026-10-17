from pyfiglet import Figlet
import random
import sys 

figlet = Figlet()

fonts_list = figlet.getFonts()
while True:
    try:
        if len(sys.argv) == 1:
            figlet.setFont(font=random.choice(fonts_list))
        elif sys.argv[1] in ("-f", "--font"):
            if len(sys.argv) != 3:
                raise IndexError
            figlet.setFont(font=sys.argv[2])
        else:
            raise ValueError
        break
    except (IndexError, ValueError):
        sys.exit("Usage: python figlet.py [-f FONT]")

text = input("Input: ")
print(figlet.renderText(text))
