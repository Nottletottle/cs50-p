import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        a, b = generate_integer(level), generate_integer(level)
        expression = f"{a} + {b}"
        result = eval(expression)
        tries = 3
        while True:
            answer = input(f"{expression} = " )
            tries -= 1
            if not answer.isdigit() or int(answer) != result:
                print("EEE")
                if tries == 0:
                    print(f"Correct answer: {result}")
                    break
            elif int(answer) == result:
                score += 1
                break
    print(score)
    


def get_level():
    while True:
        try:
            l = input("Level: ")
            if not l.isdigit() or int(l) not in [1, 2, 3]:
                raise ValueError('Level should be 1, 2, or 3')
            return int(l)
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    return random.randrange(10**(level-1), 10**level)


if __name__ == "__main__":
    main()
