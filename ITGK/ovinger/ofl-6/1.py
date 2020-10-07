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
print(liste,'\n'+str(indeks))