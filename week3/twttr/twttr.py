def shorten(input):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for vowel in vowels:
        if vowel in input:
            input = input.replace(vowel, "")
    return input


def main():
    inp = input("Input: ")
    output = shorten(inp)
    print(f"Output: {output}")


if __name__ == "__main__":
    main()
