# lister
liste = []
indeks = []
x = 10
for i in range(x):
    liste.append(' '+str(i))
    indeks.append(''+str(-x+i))

# print(liste[2:4]) # fra og med, til(men ikke med)
# print(liste[::-1])
# print(liste[::2])

# liste.append
# lsite.sort
# liste.reverse
# liste.remove
# liste.insert
# del liste[indeks]
# a = min(liste)
# liste = [1] * 4 ; [1,1,1,1]
# liste = list('Mattis') ;['M','a','t','t','i','s']
# liste = [i for i in range(100)] ; [1,2,3,...,99]
print(liste,'\n'+str(indeks))