vanlig_tall = int(input('Ditt tall: '))
binert = ''
if vanlig_tall >= 2**8:
    print('for stort tall')
y = False
for x in range(8):
    if vanlig_tall-2**(7-x) >= 0:
        binert += '1'
        vanlig_tall = vanlig_tall-2**(7-x)
        y = True
    elif y:
        binert += '0'
        
print(binert)
input('Enter to close')
