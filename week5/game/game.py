import sys
from random import randint


def main():
    while True:
        try:
            level = input("Level: ")
            if not level.isdigit():
                raise ValueError
            answer = randint(1, int(level))
            break
        except ValueError:
            pass

    while True:
        try:
            guess = input("Guess: ")
            if int(guess) > answer:
                print('Too large!')
            elif int(guess) < answer:
                print('Too small!')
            else:
                print('Just right!')
                break
            if int(level) < int(guess) < 1 or not guess.isdigit():
                raise ValueError
        except ValueError:
            pass
        

        


main()
