


A = [0,1,2,3,4,5,6]
print(A)
print(A[3:4])
A[3:4] = list('XXXXXXXXX')
print(A)
print(A[::-1].index('X'))
print(A.index('X'))
print(A[::2]) #annenhver

print(A[:2]) #første 2
print(A[-2:]) #siste 2

# print(min(A))
# print(max(A))

liste = []
for i in range(2,21,2):
    liste.append(i)
x=1
for i in range(1,len(liste),2):
    liste[i] = x*3
    x+=1
    print(i)

print(liste)

if 7 in liste:
    print('6 in liste')
else:
    print('6 not in liste')

# from random import randint
# print(randint(0, 10),'Randint')

j = 15
print(liste[::-1].index(j))
print(len(liste)-liste[::-1].index(j)-1)

input('Enter to exit ')
