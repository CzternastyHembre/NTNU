tall = float(input('Gi inn et desimaltall: '))
y = int(input('Antall desimaler i avrunding: '))
tall = list(str(tall))
print(tall)
if y >= 0:
    y+= 1

avtall = int(tall[tall.index('.')+y])
if avtall == 5:
   tall[tall.index('.')+y-1] = str(int(tall[tall.index('.')+y-1])+1)
tall[tall.index('.')+y] = '0'

str1 = ''.join(tall)

print(float(str1))
