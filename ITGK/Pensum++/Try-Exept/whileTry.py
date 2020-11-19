tall = 0
while True:
    try:
        tall = int(input('Skriv inn nert tall '))
    except:
        print('Du må skrive inn et tall!')
    else:
        break
print(tall)