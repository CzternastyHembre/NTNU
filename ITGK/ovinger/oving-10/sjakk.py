pieces = {
    'P' :'♟',
    'p' :'♙',

    'R' :'♜',
    'r' :'♖',

    'B' :'♝',
    'b' :'♗',

    'K' :'♞',
    'k':'♘',

    'Q' :'♛',
    'q' :'♕',

    'KING':'♚',
    'king':'♔',

    'empty':''
}
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numbers = [i for i in range(8, 0, -1)]

box = ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜']
box2 = ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛']

turn = 'white'
orientation = {'white':1,'black':-1}

def makeBoard():
    chessBoard = [
        ['empty' for i in range(8)] for i in range(8)
    ]
    chessBoard[1] = ['p' for i in range(8)]
    chessBoard[6] = ['P' for i in range(8)]
    chessBoard[5][4] = 'B'
    order = ['R', 'K', 'B', 'Q', 'KING', 'B', 'K', 'R']

    for i in range(8):
        chessBoard[0][i] = order[i].lower()
        chessBoard[7][i] = order[i].upper()
    return chessBoard

def printBoard(board):



  #  for i in range(8):
#        print(letters[i].ljust(3), end='')
 #   print()
    for i in range(8):
        print(numbers[i], end=' ')
        for j in range(8):
            print(format(pieces[board[i][j]]).rjust(3), end='')
        #print(str(numbers[i]), end='')
        print()
    for i in range(8):
        print('', letters[i].rjust(3), end='')

def movePiece():
    global turn
    while True:
        move = input(str(turn)+' to move: ')
        if checkRecognisable(move):

            moveFromX = letters.index(move[0].upper())
            moveFromY = len(board) - int(move[1])

            moveToX = letters.index(move[-2].upper())
            moveToY = len(board) - int(move[-1])

            if legalMove(moveFromY, moveFromX, moveToY, moveToX):
                if turn == 'white':
                    turn = 'black'
                else:
                    turn = 'white'
                break

    board[moveToY][moveToX] = board[moveFromY][moveFromX]
    board[moveFromY][moveFromX] = 'empty'



def checkRecognisable(move):
    if len(move) >= 4:
        if move[1].isdigit() and move[-1].isdigit():
            if 1 <= int(move[1]) <= 8 and 1 <= int(move[-1]) <= 8 and move[:2] != move[-2:]:
                if move[0].upper() in letters and move[-2].upper() in letters:
                    return True
    print(move, 'is not a recognisable move')
    return False

def legalMove(y1, x1, y2, x2):
    if board[y1][x1].upper() == 'P': #Pawn
        if board[y2][x2] == 'empty':
            if y1-y2 == orientation[turn] and x1 == x2:
                return True
            if y1-y2 == 2*orientation[turn] and x1 == x2 and y1 - 2.5*orientation[turn] == 3.5:
                return True
        if y1-y2 == orientation[turn] and board[y2][x2] != 'empty':
            if board[y2][x2].isupper() ^ board[y1][x1].isupper():
                return True

    if bool(orientation[turn]+1) == board[y1][x1].isupper(): # Check your turn
        oppostite = board[y2][x2].isupper() ^ board[y1][x1].isupper() # XOR
        if oppostite or board[y2][x2] == 'empty': # Check if y2x2 is not same colored

            if board[y1][x1].upper() == 'K':  # Knight
                if abs(y2-y1) + abs(x2-x1) == 3:
                    if abs(y2-y1) != 3 and abs(x2-x1) != 3:
                        return True

            if board[y1][x1].upper() == 'B':  # Bishop
                if legalBishop(y1,x1,y2,x2):
                    return True

            if board[y1][x1].upper() == 'R':  # Rook
                if legalRook(y1, x1, y2, x2):
                    return True

            if board[y1][x1].upper() == 'Q':  # Queen
                if legalBishop(y1, x1, y2, x2) or legalRook(y1, x1, y2, x2):
                    return True

            if board[y1][x1].upper() == 'KING':  # King
                pass

    print('Not a legal move')
    return False

def legalBishop(y1,x1,y2,x2):
    if abs(x2 - x1) == abs(y2 - y1):
        yIncline = int(abs(y2 - y1) / (y2 - y1))
        xIncline = int(abs(x2 - x1) / (x2 - x1))
        for i in range(1, abs(x2 - x1)):
            if board[y1 + yIncline * i][x1 + xIncline * i] != 'empty':
                return False
        return True
    return False

def legalRook(y1, x1, y2, x2):
    if (x1 == x2) ^ (y1 == y2):
        if x1==x2:
            yIncline = int(abs(y2 - y1) / (y2 - y1))
            for i in range(1, abs(y2 - y1)):
                if board[y1 + yIncline * i][x1] != 'empty':
                    return False
        else:
            xIncline = int(abs(x2 - x1) / (x2 - x1))
            for i in range(1, abs(x2 - x1)):
                if board[y1][x1 + xIncline * i] != 'empty':
                    return False
        return True

    return False


board = makeBoard()

for i in range(100):
    printBoard(board)
    print()
    movePiece()

