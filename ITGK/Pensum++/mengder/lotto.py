import random as r

# like_tall = set()
# vinner_tall = [i for i in range(35)]
# r.shuffle(vinner_tall)
# vinner_tall = set(vinner_tall[:7])
# n = 0
# while len(like_tall) < 7:
#     n+= 1
#     mine_tall = [i for i in range(35)]
#     r.shuffle(mine_tall)
#     mine_tall = set(mine_tall[:7])
#     like_tall = mine_tall.intersection(vinner_tall)
# 
# print('koden kjørte',n,'ganger')
# print(vinner_tall)
# print(mine_tall)
# print(like_tall)
# print(len(like_tall),'like tall')
# liste = [i for i in range(100)]
# 
# def sjekkIliste(lst,verdi):
#     for i in lst:
#         if i == verdi:
#             return True
#     return False


def f(n):
    if n == 0: return 1
    if n == 1: return 1
    return f(n-1)*n
print(f())

