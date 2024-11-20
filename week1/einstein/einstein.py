def einstein(mass):
    c = 300000000
    energy = int(mass) * c**2
    print(f'E: {energy}')

einstein(input("m: "))