def makeBoard():
    board = [[i for i in range(1,10)] for i in range(9)]
    return board

board = makeBoard()


"""
borad[0][0-3] board[1][0-3] board[2][0-3]
borad[0][3-6]
borad[0][6-9]

borad[1][0-3]"""
for i in range(0,9,3):
    print(i, i+1, i+2)
    x,y,z = '','', ''
    for j in range(3):
        x += str(board[i][j])
        y += str(board[i+1][j])
        z += str(board[i+2][j])
    for j in range(3,6):
        x += str(board[i][j])
        y += str(board[i+1][j])
        z += str(board[i+2][j])
    for j in range(6,9):
        x += str(board[i][j])
        y += str(board[i+1][j])
        z += str(board[i+2][j])
    print(x,y,z)
