def check_across_div(num1, num2):
    num1 = str(num1)
    crossnum1 = 0
    for i in num1:
        crossnum1 += int(num1)
    if crossnum1 % num2 == 0:
        return True
    return False

def pick_num_string(txt):
    numbers = []
    for ch in txt:
        if ch.isdigit():
            numbers.append(int(ch))
    return list(set(numbers))


def read_game_file(filename):
    db = {}
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                line = line.split(';')
                if line[0] not in db:
                        db[line[0]] = line[1:]
                else:
                    for game in line[1:]:
                        db[line[0]].append(game)
    except:
        print('could not read file')
    return db

#print(read_game_file('gamefile.txt'))

def correct_date(date):
    date = date.split('.')
    for i in range(len(date)):
        if not date[i].isdigit():
            return False
        date[i] = int(date[i])
    days_in_month = [31,29,31,30,31,30,31,31,30,31,30,31]
    if not(0 < date[1] <= len(days_in_month)):
        return False

    if not(1 <= date[0] <= days_in_month[date[1]-1]):
        return False

    return True

def write_diary(filename):
    print('Press enter without text on date to quit!')
    data = []
    while True:
        date = input('Date [dd.mm.yyyy]: ')
        if not correct_date(date):
            if date == '' :
                break
            continue
        subject = input('Subject: ')
        details = input('Details: ')
        data.append((date, subject, details))
    if len(data):
        with open(filename, 'w') as f:
            for line in data:
                f.write(line[0] + '  ' + line[1] + '\n')
                f.write('='*18 + '\n')
                f.write(line[2] + '\n\n')


write_diary('d')


