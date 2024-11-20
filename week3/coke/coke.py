def main():
    due = 50
    while True:
        while True:
            print(f"Amount Due: {due}")
            payment = int(input("Insert Coin: "))
            if payment in [25, 10, 5]:
                break
        due -= payment
        if due <= 0:
            break
    print(f"Change Owed: {abs(due)}")
main()


