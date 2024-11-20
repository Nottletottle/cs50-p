import sys
import os
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    filename = sys.argv[1]
    outfilename = sys.argv[2]
    print(outfilename)

    if not os.path.isfile(filename):
        print("File does not exist")
        sys.exit(1)
    if not ".csv" in filename or not ".csv" in outfilename:
        print("Not a csv file")
        sys.exit(1)

    new_fieldnames = ["first", "last", "house"]
    data_to_write = []

    with open(filename) as file:
        first_row = file.readline().strip().split(",")
        reader = csv.DictReader(file, fieldnames=first_row)
        for line in reader:
            last, first = line["name"].split(",")
            reformatted_line = {
                "first": first.strip(),
                "last": last.strip(),
                "house": line["house"].strip(),
            }
            data_to_write.append(reformatted_line)

    with open(outfilename, mode="w", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=new_fieldnames)
        writer.writeheader()
        writer.writerows(data_to_write)


if __name__ == "__main__":
    main()
