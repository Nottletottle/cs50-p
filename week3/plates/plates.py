def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6 or not s.isalnum():
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    digit_positions = [i for i, char in enumerate(s) if char.isdigit()]
    if len(digit_positions) == 0:
        return True
    if s[digit_positions[0]] == '0' or digit_positions[-1] != len(s) - 1:
        return False
    if any(digit_positions[i] + 1 != digit_positions[i + 1] for i in range(len(digit_positions) - 1)):
        return False
    return True


main()