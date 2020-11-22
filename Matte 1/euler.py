def f(x,y):
    return x+y

def euler(f,x0,y0,h,slutt):
    slutt = round((slutt-x0)/h)+1
    r = 7
    for i in range(1, slutt):
        y0 = y0 + h*f(x0,y0)
        x0 = x0+h
        print('i =',i,'| x =',round(x0,r),'| y =',round(y0,r))

euler(f,1,0,0.2,2)