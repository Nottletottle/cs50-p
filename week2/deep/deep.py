def check_input(value):
    acceptable_values = ["42", "forty two", "forty-two"]

    if value in acceptable_values:
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    user_input = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
    print(check_input(user_input.lower().strip()))
