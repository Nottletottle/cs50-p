import sys
import os
from PIL import Image as img, ImageOps as imgops


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python script.py inputfile outputfile")

    filename = sys.argv[1]
    outfilename = sys.argv[2]

    if not os.path.isfile(filename):
        print("File does not exist")
        sys.exit(1)

    fileextension = os.path.splitext(filename)[1].lower()
    if fileextension not in [".png", ".jpg", ".jpeg"]:
        print("Invalid input file extension")
        sys.exit(1)

    if not outfilename.endswith((".png", ".jpg", ".jpeg")):
        print("Output file must be a PNG, JPG, or JPEG")
        sys.exit(1)

    if fileextension != os.path.splitext(outfilename)[1].lower():
        print("Input and output must have the same file extension")
        sys.exit(1)

    try:
        shirt = img.open("shirt.png")
        muppet = img.open(filename)
    except FileNotFoundError:
        exit("Input does not exist")
    except Exception as exp:
        exit(exp)
    # get size of shirt.png
    size = shirt.size
    # crop muppet to fit shirt
    muppet = imgops.fit(muppet, size)
    # overlay shirt on mupper
    muppet.paste(shirt, shirt)
    # save image
    muppet.save(outfilename)


if __name__ == "__main__":
    main()
