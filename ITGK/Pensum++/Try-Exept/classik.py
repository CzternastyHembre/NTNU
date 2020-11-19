try:
    tall = input('Skriv inn et tall: ')
    tall = int(tall)
    print(100/tall,'100/'+str(tall))
    with open(tall, 'r') as lol:
        print(lol.readlines())


except Exception as err:
    print('Feilmeldig!\n'+str(err))
