def home_draw_away(lst):
    hda = [0 for i in range(3)]
    for game in lst:
        if game.upper() == 'H':
            hda[0] += 1
        elif game.upper() == 'U':
            hda[1] += 1
        elif game.upper() == 'B':
            hda[2] += 1
    return hda

match = ('h','u','b','H','H','B')

#  print(home_draw_away(match))

def pos_vocals(txt):
    vocals = ['a','e','i','o','å','ø','æ','y','u']
    pos = []
    for i in range(len(txt)):
        if txt[i].lower() in vocals:
            pos.append(i)
    return pos

#  print(pos_vocals('AÆdaopekfe'))


def uniqe(textstr):
    nytxtstr = ''
    for ch in textstr:
        if ch.isalpha() or ch == ' ' or ch.isdigit():
            nytxtstr += ch
    txt = list(set(nytxtstr[::].lower().split()))
    return txt

print(uniqe('sfef erfe efe 2 we we WE we! efe'))

def calculate():
    expression = input('Enter calculation: ')
    expression = expression.replace(',', '.')
    expression = expression.replace(' ', '')

    expression = expression.split('+')
    totalsummen = 0

    for part in expression:
        summen = 0
        part = part.split('-')
        summen += float(part[0])

        for i in range(1, len(part)):
            summen -= float(part[i])
        totalsummen += summen

    print('Result:', totalsummen)


calculate()




