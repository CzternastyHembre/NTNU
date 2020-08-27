print("hei")
spm = ["hvor gammel er mattis","hvor gammel er karan"]
fasit = [18,19]
i=0
poeng = 0
def nyttSpm():
    print(spm[i])
    svar = int(input("Svar: "))
    if fasit[i]==svar:
        poeng+= 1
        print("riktig svar")
    else:
        print("feil svar")


nyttSpm()




input("Enter to exit")
