import random


def black_jack():
    mulige_kort = [i for i in range(2, 12)]
    mulige_kort[10:] = [10] * 3
    mulige_kort = mulige_kort * 4
    random.shuffle(mulige_kort)
    i = 0

    print('Dealers cards are ' + str(mulige_kort[i]) + ' and ?')
    dealer = mulige_kort[i] + mulige_kort[i + 1]
    i += 2
    spiller = mulige_kort[i]

    draw = True
    while draw:
        i += 1
        spiller += mulige_kort[i]

        if spiller >= 21:
            print('You got', spiller)
            break

        print('Your score is', spiller)

        while True:
            new_card = input('Do you want another card? (J/N) ').lower()
            if new_card == 'n' or new_card == 'j':
                break
            print('Du må skrive inn J eller N')

        if new_card == 'n':
            draw = False
        if spiller >= 22 and mulige_kort[i] == 11:
            spiller = spiller - 11 + 1

    if spiller >= 22:
        spiller = -1
    else:
        print('Dealers score is:', dealer)

    if spiller > dealer:
        print('You won!')
    else:
        print('You lost')


black_jack()
