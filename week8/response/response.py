import validators


def main():
    email = input("Please enter an email address: ")

    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
