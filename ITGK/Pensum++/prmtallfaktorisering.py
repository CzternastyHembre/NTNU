heltall = int(input('Skriv inn et positivt heltall: '))
tallrekke = []
teller = []

for i in range(heltall,1,-1):
    if heltall % i == 0:
        x = True
        for j in range(i-1,1,-1):
            if i % j == 0:
                x = False
                teller.append(j)
        if x:
            tallrekke.append(i)

for x in tallrekke:
    if heltall/x == int(heltall/x):
        tallrekke.append(x)
print(tallrekke)
print(teller)
input('Enter to exit ')
