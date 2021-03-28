import xlrd
import time

import datetime
my_date = datetime.date.today() # if date is 01/01/2018
year, week_num, day_of_week = my_date.isocalendar()

print(my_date.isocalendar())

wished_week = 9;

diffWeek = week_num - wished_week;

timeInterval = []
#timeInterval[0] =

loc = "Skytterdagbok-Kopi.xls"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)



def dateConverter(t):
    stringTime = str(xlrd.xldate.xldate_as_datetime(t, wb.datemode))
    stringTime = stringTime.split(' ')[0]
    stringTime = stringTime.split('-')

    year, month, day = int(stringTime[0]), int(stringTime[1]), int(stringTime[2])
    return year, month, day


x = []
i = 0
start = 6
endDay = 3

while i < 100:
    x.append([])
    for cell in sheet.row(start + i)[7:21]:
        try:
            x[i].append(int(cell.value))
        except:
            x[i].append(cell.value)
    year, month, day = dateConverter(x[i][0])
    print(month)
    print(x[i])
    print(dateConverter(x[i][0]))
    i += 1
    if day == endDay:
        break




