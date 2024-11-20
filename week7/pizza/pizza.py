import sys
import os
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    filename = sys.argv[1]

    if not os.path.isfile(filename):
        print("File does not exist")
        sys.exit(1)
    if not ".csv" in filename:
        print("Not a csv file")
        sys.exit(1)

    menu = []

    with open(filename) as file:
        first_row = file.readline().strip().split(",")

        # Create DictReader with the field names from the first row
        reader = csv.DictReader(file, fieldnames=first_row)

        # Add the header row as a dictionary to the menu
        menu.append(dict(zip(first_row, first_row)))
        for line in reader:
            menu.append(line)

    print(tabulate(menu, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
