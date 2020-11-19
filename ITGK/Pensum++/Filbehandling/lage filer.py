def skrivFil(filnavn):
    with open(filnavn, 'w') as file:
        print('Skriv teksen inn')
        text = input('> ')
        while text != '':
            file.write(text + '\n')
            text = input('> ')
    print('teksten har blir lagret i '+ filnavn)

def skrivFilFraListe(filnavn):
    with open(filnavn, 'w') as file:
        print('Skriv teksen inn')
        liste = []
        text = '_'
        while text != '':
            text = input('> ')
            liste.append(text+'\n')
        file.writelines(liste)

skrivFilFraListe('tallfil')