from random import randint


def dice():
    tall = [randint(1, 6) for i in range(5)]
    return tall


# print(dice())

def antall(n, liste):
    x = 0
    for i in liste:
        if i == n:
            x += 1
    return x
    # return liste.count(n) #Mye raksere


# terning = dice()
# print(terning)
# print(antall(6, terning))


def hoyeste_like(n, terninger=dice()):
    p = 0
    for i in range(1, 7):
        if antall(i, terninger) >= n:
            p = n * i
    print(terninger)
    return p


print(hoyeste_like(2))


def yatzy():
    p = 0
    for i in range(1, 7):
        kast = dice()
        tall = antall(i, kast)
        print(kast, tall, tall * i)
        p += tall * i
    print(p)

yatzy()

liste = [j for j in range(4)]
print(liste)