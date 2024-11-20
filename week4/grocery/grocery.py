from collections import defaultdict
def grocery():
    items = defaultdict(int)
    while True:
        try:
            item = input('').strip()
            items[item] += 1
        except EOFError:
            print()
            for key, value in sorted(items.items()):
                print(value, key.upper())
            break

grocery()