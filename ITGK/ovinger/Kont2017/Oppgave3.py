def show_display(content):
    pass

def enter_line(prompt, lenght):
    while True:
        line = input(str(prompt))
        if len(line) == lenght:
            print('NOICE')
            return line
        print('This text mus be', lenght, 'characters log')


def ajust_string(text, length):
    if len(text) > length:
        print(text[:30])
        return text[:30]
    if len(text) == 30:
        print('Noice')
        return text
    l = (length - len(text))//2
    blank = ' ' * l
    s = blank + text + blank
    if len(s) != 10:
        s += ' '
    return s

ajust_string('123', 10)

def enter_line_smart(prompt, length):
    text = input(prompt)
    if len(text) == length
    text = enter_line_smart(prompt, length)
