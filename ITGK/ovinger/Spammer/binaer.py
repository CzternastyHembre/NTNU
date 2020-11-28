def convert_to_bin(num):
    i = 0
    ex = 2**i
    while num//ex:
        i += 1
        ex = 2**i
    i -= 1
    ex = 2**i

    bin = ''
    for j in range(i):
        ex = 2**(i-j)
        if num//ex > 0:
            bin += '1'
            num//ex
        else:
            bin += '0'
        num %= ex
    return bin

def convert_from_bin(bin):
    tall = 0
    l = len(bin)
    for i in range(l):
        if bin[i] == '1':
            tall += 2**(l-i)
    return tall


print(convert_to_bin(convert_from_bin(convert_to_bin(convert_from_bin(convert_to_bin(convert_from_bin(convert_to_bin(convert_from_bin(convert_to_bin(convert_from_bin(convert_to_bin(convert_from_bin(convert_to_bin(convert_from_bin(convert_to_bin(convert_from_bin('1000')))))))))))))))))