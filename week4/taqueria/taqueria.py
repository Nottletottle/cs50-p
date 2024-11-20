def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    lowercase_menu = {key.lower() : value for key, value in menu.items()}
    taqueria(lowercase_menu)

def taqueria(menu):
    total = 0.00
    while True:
        try:
            item_price = input('Item: ').lower()
            total = total+menu[item_price]
            print(f'Total: ${total:.2f}')
        except KeyError:
            pass
        except EOFError:
            break

main()