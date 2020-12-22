import random
def car_registation():
    letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    r_letter = letters[random.randint(0,len(letters)-1)]
    r_letter += letters[random.randint(0,len(letters)-1)]
    r_number = str(random.randint(10000,99999))
    return r_letter+r_number

#print(car_registation())

def prepare(bin):
    for ch in bin:
        if ch in range(2):
            return 'Det er ikke et binært tall.'
    remainder = (3 - len(bin)) % 3
    return '0' * remainder + bin

print(prepare('01'))

def list_to_disk(lstlst, filename):
    try:
        with open(filename, 'w') as f:
            for lst in lstlst:
                string = str(lst[0]) + ';' + str(lst[1])
                f.write(string + '\n')
    except:
        print('Could not write to file')

list_to_disk([[1,2],[3,4],[5,6]], 'test.txt')