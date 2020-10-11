liste = [[[],[],[]],
         [[],[],[]],
         [[],[],[]],
         ]
l = [[] for i in range(3)]
print(l)
for i in range(3):
    for j in range(3):
        liste[i][j] = (j+1)*2*(2**i)
    print(liste[i])



print([i for i in range(20)])




input('d')