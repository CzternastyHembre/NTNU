spm = ["hvor gammel er mattis","hvor gammel er karan",'Hva er hovedstaten i Norge?']
fasit = ['18','19','Oslo']
selv = str(input('vil du skrive inn spm selv? y/n: '))
if selv.lower() == 'y':
    x = True
    spm = []
    fasit = []
    while x == True:
        s = input("Skriv spm: ")
        spm.append(s)
        f = input("Skriv fasit: ")
        fasit.append(f)
        ferdig = input('Ferdig? y/n: ')
        if ferdig == 'y':
            x = False
# print(spm)
# print(fasit)
i=0
poeng = 0
while i < len(spm):
    print(spm[i])
    svar = (input("Svar: "))
    if fasit[i].lower()==svar.lower():
        poeng+= 1
        print("riktig svar")
    else:
        print("feil svar")
    i+= 1

prosent = str(int(round(poeng/i * 100,0)))+'%'
print('totale poeng:', poeng,'av', i,'|', prosent)

input("Enter to exit")
