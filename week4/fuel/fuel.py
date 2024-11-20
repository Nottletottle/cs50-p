def main():
    f = fuel()
    print(f"{f}%") if f in range(2, 99) else fullorempty(f)


def fuel():
    while True:
        try:
            fraction = input("Fraction: ")
            numerator, denominator = fraction.split("/")
            numerator = int(numerator)
            denominator = int(denominator)
            if denominator == 0:
                raise ZeroDivisionError
            result = round((numerator / denominator) * 100)
            if result < 0 or result > 100:
                continue
            return result
        except (ZeroDivisionError, ValueError):
            pass


def fullorempty(f):
    print("F") if f >= 99 else print("E")


main()
