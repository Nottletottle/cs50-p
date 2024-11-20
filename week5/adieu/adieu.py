def main():
    import sys

    names = []
    try:
        while True:
            name = input("Enter names one per line (Press Control-D to end): ")
            names.append(name)
    except EOFError:
        pass

    if len(names) > 1:
        formatted_names = ", ".join(names[:-1]) + ", and " + names[-1]
        print(f"Adieu, adieu, to {formatted_names}")
    elif len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")


if __name__ == "__main__":
    main()
