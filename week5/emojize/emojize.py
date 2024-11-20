from emoji import emojize


# defining a function
def emoji():
    print(f'Output: {emojize(input('Input: '), language = "alias")}')


emoji()
