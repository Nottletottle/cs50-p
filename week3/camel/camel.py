def camelcase(camelCase):
    result = []

    for index, char in enumerate(camelCase):
        if char.isupper() and index != 0:
            result.append('_')
        result.append(char.lower())
    return ''.join(result)

def main():
    camelCase = input('camelCase: ')
    snake_case = camelcase(camelCase)
    print(snake_case)

if __name__ == "__main__":
    main()



# camelCase = list(camelCase)
#     indices = []
#     for x in camelCase:
#         if x.isupper():
#             indices.append(camelCase.index(x))
#     for index in indices:
#         camelCase.insert(index+indices.index(index), '_')
#     camelCase = ''.join(camelCase)
#     print(camelCase.lower())