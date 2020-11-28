def fakultet(tall):
    if tall==0:
        return 1
    else:
        return tall*fakultet(tall-1)

def teller(nummer=0):
    print("Nå har vi kommet til: ", nummer)
    if (nummer < 10):
        teller(nummer + 1)

def liste_sum(liste):
    if (len(liste) == 1):
        return liste[0]  # dersom listen kun har et element er summen vår bare det ene elementet
    else:
        return liste[0] + liste_sum(
            liste[1:])  # ellers tar vi det første elementet og legger til summen av resten av lista

def recursive_sum(n):
    if n == 1:
        return 1
    return (n + recursive_sum(n-1))

def f(n):
    if n == 0 : return 0
    if n == 1 : return 1
    return f(n-1) + f(n-2)

# prints x number of *
def recursion(x):
  if(x == 0): #base case
    print()
  else: #recursive case
    print("*", end='')
    recursion(x - 1)

