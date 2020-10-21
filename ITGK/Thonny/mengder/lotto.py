import random as r

like_tall = set()
vinner_tall = [i for i in range(35)]
r.shuffle(vinner_tall)
vinner_tall = set(vinner_tall[:7])
n = 0
while len(like_tall) < 7:
    n+= 1
    mine_tall = [i for i in range(35)]
    r.shuffle(mine_tall)
    mine_tall = set(mine_tall[:7])
    like_tall = mine_tall.intersection(vinner_tall)

print('koden kjørte',n,'ganger')
print(vinner_tall)
print(mine_tall)
print(like_tall)
print(len(like_tall),'like tall')

