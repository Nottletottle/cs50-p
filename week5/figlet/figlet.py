from pyfiglet import Figlet
import sys


def main():
    f = Figlet()
    available_fonts = f.getFonts()
    options = ["-f", "--font"]
    textfont = "slant"
    if len(sys.argv) not in [1, 3]:
        print("Usage: python figlet.py -f/--font <font name>")
        sys.exit(1)
    if len(sys.argv) == 3:
        if sys.argv[1] not in options:
            print("Invalid Option")
            sys.exit(1)
        if sys.argv[2] not in available_fonts:
            print("Invalid font")
            sys.exit(1)
    textfont = sys.argv[2]
    f = Figlet(font=textfont)
    print(f.renderText(input("Input: ")))


main()
