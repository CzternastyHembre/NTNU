"""
name = input ('Enter a name: ')

if name == 'Joe':
    print('Name entered is :', name)
elif name == "Mama":
    print('Name entered is :', name)
elif name == "Mamma":
    print('Name entered is :', name)
elif name == "Mammma":
    print('Name entered is :', name)
else:
    print('Not a valid name')
"""
from random import randint
x = 0
i = 0
while x != 6:
    x = randint(1,6)
    i += 1
    print(x)
print ('i = ', i)

    