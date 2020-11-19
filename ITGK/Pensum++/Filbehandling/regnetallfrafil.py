filnavn = input('Skriv inn filnavn: ')

with open(filnavn, 'r') as file:
    for line in file.readlines():
        line = line.strip()
        if line.isnumeric():
            print(int(line)**3)
