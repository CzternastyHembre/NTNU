from random import randint

def dice():
    tall = [randint(1,6) for i in range(5)]
    return tall
#print(dice())

def antall(n,liste):
    x = 0
    for i in liste:
        if i == n:
            x+=1
    return x
    #return liste.count(n) #Mye raksere

terning = dice()
print(terning)
print(antall(6, terning))