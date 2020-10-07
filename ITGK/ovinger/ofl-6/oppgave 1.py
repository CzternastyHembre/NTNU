handleliste = ['Melk','Bananer','Brus', 'Rundstykker']
print(handleliste)

ind = (handleliste.index('Rundstykker'))
handleliste[ind] = 'Brød'

handleliste.append('a')
handleliste.append('a')
handleliste.append('a')
handleliste.append('a')
handleliste.append('a')
print(handleliste)

def firstHalf(liste):
    lengde = len(liste)//2
    return liste[:lengde]

print(firstHalf(handleliste))