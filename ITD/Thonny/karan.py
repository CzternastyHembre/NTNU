print("hei")
spm = ["hvor gammel er mattis","hvor gammel er karan",'Hva er hovedstaten i Norge?']
fasit = ['18','19','Oslo']
i=0
poeng = 0
while i < len(spm):
    print(spm[i])
    svar = (input("Svar: "))
    if fasit[i]==svar:
        poeng+= 1
        print("riktig svar")
    else:
        print("feil svar")
    i+= 1


print('totale poeng:', poeng,'av', i)

input("Enter to exit")
