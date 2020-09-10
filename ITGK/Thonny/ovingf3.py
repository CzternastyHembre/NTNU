# x = float(input('Skriv tall: '))

# if int(x) == float(x):
#     x = int(x)
#     print(str(abs(x)) + ' er absolutt dit tall')

#Boolean er enten True eller False, (1,0)

# a = int(input('a: 0/1 '))
# b = int(input('b: 0/1 '))
# if a and b:
#     print('Begge er sanne')
# if a or b:
#     print('Minst 1 er sann')
# if not a and not b:
#     print('Ingen er sanne')
# if not(a and b):
#     print('Minst 1 er ikke sann')
# if a is b:
#     print('a og b er like')
# if a is not b:
#     print('a og b er ikke like')
#
#
#
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
# if a + b == c:
#     print(a,'+',b,'=',c)
# else:
#     print(a,'+',b,'!=',c)

# a = int(input('a: '))
# if a%2 == 0:
#     print(str(a)+' er et partall')
# else:
#     print(str(a)+' er et oddetall')

# x = False
# while not x:
#     a = (input('skriv inn passord: '))
#     passord = 'Indøk er gay'
#     if a == passord:
#         print('Riktig passord!')
#         x = True
#     else:
#         print('Feil passord, (hint: indøks legning)')


#Måter å formatere i print()
navn = 'Mattis'

print('Hei ' + navn + "  --> print('Hei ' + navn)")

print('Hei', navn, " --> print('Hei', navn)")

print('Hei {}'.format(navn)," --> 'Hei {}'.format(navn)")

print(f'Hei {navn}', " --> print(f'Hei {navn}')")

print('Hei %s' % navn, " --> print('Hei %s' % navn)")









input('enter for å avslutte ')
