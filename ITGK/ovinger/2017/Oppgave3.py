def file_to_table(filename):
    try:
        table = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                line = line.split(',')
                for i in range(len(line)):
                    if line[i].isdigit():
                        line[i] = int(line[i])
                table.append(line)
        return table
    except:
        print('Could not read file')

def time_diff(start, end):
    secs = diff_date(start, end)
    for i in range(1,4):
        secs += (end[-i] - start[-i])*60**(i-1)
    return secs

def diff_date(start,end):
    days = ((end[2] - start[2])+(end[1] - start[1])*30+(end[0] - start[0])*365)*24*60**2
    return days

def check_min_distance(car_table, diff):
    cars = []
    for i in range(len(car_table)-1):
        if time_diff(car_table[i][:-1],car_table[i+1][:-1]) < diff:
            cars.append(car_table[i+1][-1])
    return cars

def list_el_cars(car_table):
    total_el = 0
    el_reg = ['EL', 'EK', 'EV']
    for car_data in car_table:
        reg = car_data[-1]
        if reg[:2].upper() in el_reg:
            total_el += 1
    return total_el


import random as r
def generate_license_numbers(amount):
    reg_nrs = []
    reg_letters = ['BS', 'CV', 'EL', 'FY', 'KU', 'LE', 'NB', 'PC', 'SY', 'WC']
    for i in range(amount):
        while True:
            r_letters = r.choice(reg_letters)
            r_number = r.randint(10000,99999)
            reg_nr = r_letters+str(r_number)
            if reg_nr not in reg_nrs:
                reg_nrs.append(reg_nr)
                break
    return reg_nrs

def list_speeders(filename_a, filename_b, speed_limit, distanse):
    db = {}
    max_seconds = distanse/speed_limit*60*60
    table_a = file_to_table(filename_a)
    table_b = file_to_table(filename_b)

    for data in table_a:
        db[data[-1]] = [data[:-1]]
    for data in table_b:
        if data[-1] in db:
            db[data[-1]].append(data[:-1])
    speeders = []
    for key, value in db.items():
        if len(value) >= 2:
            for i in range(1, len(value)):
                time = time_diff(value[0], value[i])
                if time < max_seconds:
                    speeders.append(key)
                    break
    print(db)
    return speeders

print(list_speeders('box_a.txt','box_b.txt',60,10))
"""
if len(value) == 2:
    time = time_diff(value[0], value[-1])
    if time < max_seconds:
        speeders.append(key)
"""