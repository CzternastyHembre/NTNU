def du_user_like(lst):
    array = []

    print('On a scale for 1 to 10 where 10 is the highest, how much do you like:')
    for i in lst:
        while True:
            svar = input(str(i)+'? ')
            if svar.isdigit():
                svar = int(svar)
                if 1 <= svar <= 10:
                    element = (i,svar)
                    array.append(element)
                    break
            print('You have to give avalue in the interval'
                  ' [1,10]. Try again')
    return array

#print(du_user_like(['dogs','cats']))

def get_prioritized_list(lst):
    new_lst = []
    lst.sort()

    while len(lst):
        maksIndex = 0
        for i in range(1,len(lst)):
            if lst[i][1] > lst[maksIndex][1]:
                maksIndex = i
        new_lst.append((lst[maksIndex][0],lst[maksIndex][1]))
        lst.pop(maksIndex)
    return new_lst

#print(get_prioritized_list(du_user_like(['dogs','cats','cbts','caas'])))


def what_user_likes_best(items, num):
    if num < 1 or num > len(items):
        print('Invalid number given')
        return
    streng = get_prioritized_list(du_user_like(items))

    top = 'top'
    if num == 1: top = 'number'
    print('Your',top,num,'are:')
    for i in range(num):
        print(str(i+1)+'.', streng[i][0])

what_user_likes_best(['dogs','cats','cbtsd','cagfdgts','cgbdfgts','cagdftgs','cgdfgbts','catoijois','Cbts','caas'],10)