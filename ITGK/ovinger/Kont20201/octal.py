def prepare(bin):
    for ch in bin:
        if ch not in range(2):
            print('Det er ikke et binært tall')
            return
    remainder = (3-len(bin)) % 3
    bin = '0' * remainder + bin
    return bin

#print(prepare('00101'))

def convert(string):
    l = len(string)
    sum = 0
    for i in range(1, min(l+1, 6)):
        sum += ord(string[-i])
    return chr(sum)



def conver_from_bin_to_oct(bin):
    bin = prepare(bin)
    oct = ''
    for i in range(0, len(bin),3)[::-1]:
        delsum = 0
        if bin[i] == '1':
            delsum += 1
        if bin[i-1] == '1':
            delsum += 2
        if bin[i-2] == '1':
            delsum += 4
        oct += str(delsum)
    return oct

print(conver_from_bin_to_oct('1000'))



print(convert(''))


