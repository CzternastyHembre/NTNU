handleliste = ['Melk','Bananer','Brus', 'Rundstykker',]
# print(handleliste)

ind = (handleliste.index('Rundstykker'))
handleliste[ind] = 'Brød'

# print(handleliste)

def firstHalf(liste):
    lengde = len(liste)//2
    return liste[:lengde]

# print(firstHalf(handleliste))

def exceptFor_last_and_first(liste):
    return liste[1:-1]

# print(exceptFor_last_and_first(handleliste))