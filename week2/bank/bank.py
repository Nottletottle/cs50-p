def bank(greeting):
    greeting = greeting.lower()
    if 'hello' in greeting:
        print('$0')
    elif 'h' in greeting[0]:
        print('$20')
    else:
        print('$100')

def main():
    greeting = input('Greeting: ')
    bank(greeting)

main()