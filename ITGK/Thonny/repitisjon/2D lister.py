tabell_10x10 = [
    [col for col in range(10)] for row in range(10)
    ]

# print(tabell_10x10)


def createTable(row,col):
    return [[None for i in range(row)]for i in range(col)]


# print(createTable(3,5))

def fillTable(Table):
#     print(Table)
    tall = 2
    for i in range(len(Table)):
        for j in range(len(Table[i])):
           Table[i][j] = tall
           tall += 2
    return Table
                       
# print(createTable(4,3))
#print(fillTable(createTable(5,6)))

def sumTable(tbl):
    summen = 0 
    for i in range(len(tbl)):
        summen += sum(tbl[i])
    #print(tbl)
    return summen

print(sumTable(fillTable(createTable(5000,6000))))