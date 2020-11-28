def format_time(sec):
    hh = str(sec//60**2)
    mm = str(sec % (60**2)//60)
    ss = str(sec % 60)

    if int(ss) < 10:
        ss = '0'+ss
    if int(mm) < 10:
        mm = '0'+mm
    if int(hh) < 10:
        hh = '0'+hh

    mm += ':'
    hh += ':'

    time = str(hh)+str(mm)+str(ss)
    return time

def values_december():
    first_time = '03:18:00'
    hh, mm, ss = first_time.split(':')
    secons_since_mid = int(hh)*60**2 + int(mm)*60**1 + int(ss)*60**0

    hh, mm, ss = [12,25,12]
    period = int(hh)*60**2 + int(mm)*60**1 + int(ss)*60**0

    return secons_since_mid, period



def genTides():
    first, period = values_december()

    seconds_a_day = 24*60**2
    seconds_in_desember = 31*seconds_a_day

    tides = []

    last_period = first

    while last_period < seconds_in_desember:
        tides.append(last_period)
        last_period += period//2

    lows = tides[::2]
    highs = tides[1::2]
    return lows, highs


def genTidesStr(lst):
    tides = []
    seconds_a_day = 24*60**2
    for i in range(len(lst)):
        new_str = str(i) + ' ' + format_time(lst[i] % seconds_a_day)
        tides.append(new_str)
    return tides


def checkTides(dayInMonth):
    secs = [[],[]]
    clock = ([9,0,0],[13,0,0])
    for i in range(len(clock)):
        hh, mm, ss = clock[i]
        secs[i] = hh*60**2 + mm*60*1 + ss*60**0

    lows, highs = genTides()
    day_to_secs = dayInMonth*24*60**2
    secs[0] += day_to_secs
    secs[1] += day_to_secs

    is_tide = False
    for i in range(max(len(lows),len(highs))):
        if i < len(lows):
            if secs[0] <= lows[i] <= secs[1]:
                print('low tide at ' + format_time(lows[i] % (24 * 60 ** 2)))
                is_tide = True
        if i < len(highs):
            if secs[0] <= highs[i] <= secs[1]:
                print('high tide at ' + format_time(highs[i] % (24 * 60 ** 2)))
                is_tide = True
    if not is_tide:
        print('no tides')


def listTides():
    lows, highs = genTides()
    tides = lows
    days_in_dec = 31
    days_to_sec_const = 24*60**2
    tides_per_day = {}
    tides.sort()
    for i in range(1,days_in_dec+1):
        tides_per_day[str(i)] = []
        for tide in tides:
            if (i-1)*days_to_sec_const <= tide < i* days_to_sec_const:
                tides_per_day[str(i)].append(format_time(tide%days_to_sec_const))

    print('Key\tFirst\t\tSecond')
    for key, values in tides_per_day.items():
        line = key
        for value in values:
            line += '\t'+value
        print(line)

listTides()


