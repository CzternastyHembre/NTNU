def input_string():
    strings = []
    for i in range(4):
        str1 = input('Skriv inn en streng: ')
        strings.append(str1)
    return strings


def acronym():
    strings = input_string()
    acr = ''
    for i in range(len(strings)):
        acr += strings[i][0].upper()
    print(acr)

acronym()