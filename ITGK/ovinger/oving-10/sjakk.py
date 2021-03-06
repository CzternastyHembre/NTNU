pieces = {
    'P': '♟',
    'p': '♙',

    'R': '♜',
    'r': '♖',

    'B': '♝',
    'b': '♗',

    'K': '♞',
    'k': '♘',

    'Q': '♛',
    'q': '♕',

    'KING': '♚',
    'king': '♔',

    'empty': '⬛'
}
kingPos = {
    'WHITE': {
        'y': 7,
        'x': 4
    },
    'black': {
        'y': 0,
        'x': 4
    }
}
n= 0
mate = False
moves = []
takenPieces = []
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numbers = [i for i in range(8, 0, -1)]

box = ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜']
box2 = ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛']

turn = 'WHITE'

orientation = {'WHITE': 1,'black': -1}


def makeBoard():
    chessBoard = [
        ['empty' for i in range(8)] for i in range(8)
    ]
    chessBoard[1] = ['p' for i in range(8)]
    chessBoard[6] = ['P' for i in range(8)]

    order = ['R', 'K', 'B', 'Q', 'empty', 'B', 'K', 'R']

    for i in range(8):
        chessBoard[7][i] = order[i]
        chessBoard[0][i] = order[i].lower()

    chessBoard[kingPos['WHITE']['y']][kingPos['WHITE']['x']] = 'KING'
    chessBoard[kingPos['black']['y']][kingPos['black']['x']] = 'king'

    return chessBoard


def printBoard(board):

    # for i in range(8):
    # print(letters[i].ljust(3), end='')
    # print()
    for i in range(8):
        print(numbers[i], end=' ')
        for j in range(8):
            print(format(pieces[board[i][j]]).rjust(3), end='')
        # print(str(numbers[i]), end='')
        print()
    for i in range(8):
        print('', letters[i].rjust(3), end='')


def movePiece():
    global turn
    global mate
    while True:
        move = input(str(turn).lower()+' to move: ')
        if checkRecognisable(move):

            y1 = len(board) - int(move[1])
            x1 = letters.index(move[0].upper())

            y2 = len(board) - int(move[-1])
            x2 = letters.index(move[-2].upper())

            if legalMove(y1, x1, y2, x2, turn):
                break

    moveP(y1, x1, y2, x2)


    if checkChess(turn):
        print('Du er i sjakk mann')
        undoLastMove()
        return

    if checkMate(turn):
        printBoard(board)
        print('\nSjakk matt', turn, 'vant')
        mate = True
        return

    if turn == 'WHITE':
        turn = 'black'
    else:
        turn = 'WHITE'


def moveP(y1, x1, y2, x2):
    global n
    print(n ,'---N')
    n= 0
    takenPieces.append(board[y2][x2])
    moves.append([(y1, x1), (y2, x2)])

    board[y2][x2] = board[y1][x1]
    board[y1][x1] = 'empty'


def undoLastMove():
    y1 = moves[-1][0][0]
    x1 = moves[-1][0][-1]

    y2 = moves[-1][-1][0]
    x2 = moves[-1][-1][-1]

    board[y1][x1] = board[y2][x2]  # Moving the piece back
    board[y2][x2] = takenPieces[-1]  # putting back the taken piece

    takenPieces.pop(-1)
    moves.pop(-1)



def checkRecognisable(move):
    if len(move) >= 4:
        if move[1].isdigit() and move[-1].isdigit():
            if 1 <= int(move[1]) <= 8 and 1 <= int(move[-1]) <= 8 and move[:2] != move[-2:]:
                if move[0].upper() in letters and move[-2].upper() in letters:
                    return True
    print(move, 'is not a recognisable move')
    return False


def legalMove(y1, x1, y2, x2, chkTurn, test = False):
    global n
    n+= 1
    if board[y1][x1].upper() == 'P':  #Pawn
        if board[y2][x2] == 'empty':
            if y1-y2 == orientation[chkTurn] and x1 == x2:  # 1 forward
                return True
            if y1-y2 == 2*orientation[chkTurn] and x1 == x2 and y1 - 2.5*orientation[chkTurn] == 3.5:  # two forward
                return True
        if y1-y2 == orientation[chkTurn] and board[y2][x2] != 'empty' and (abs(x2 - x1) == 1):  # take
            if board[y2][x2].isupper() ^ board[y1][x1].isupper():
                return True

    if bool(orientation[chkTurn] + 1) == board[y1][x1].isupper():  # Check your turn
        oppostite = board[y2][x2].isupper() ^ board[y1][x1].isupper()  # XOR

        if oppostite or board[y2][x2] == 'empty':  # Check if y2x2 is not same colored

            if board[y1][x1].upper() == 'K':  # Knight
                if abs(y2-y1) + abs(x2-x1) == 3:
                    if abs(y2-y1) != 3 and abs(x2-x1) != 3:
                        return True

            if board[y1][x1].upper() == 'B':  # Bishop
                if legalBishop(y1 ,x1 ,y2 ,x2):
                    return True

            if board[y1][x1].upper() == 'R':  # Rook
                if legalRook(y1, x1, y2, x2):
                    return True

            if board[y1][x1].upper() == 'Q':  # Queen
                if legalBishop(y1, x1, y2, x2) or legalRook(y1, x1, y2, x2):
                    return True

            if board[y1][x1].upper() == 'KING':  # King
                if legalKing(y1, x1, y2, x2):
                    return True

    if not test:
        print('Not a legal move')
        pass
    return False


def legalBishop(y1 ,x1 ,y2 ,x2):
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
        if x1 == x2:
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


def legalKing(y1, x1, y2, x2, test = False):
    if abs(y2-y1) <= 1 and abs(x2-x1) <= 1 and not test:
        kingPos[turn]['y'] = y2
        kingPos[turn]['x'] = x2
        return True


def checkChess(turn):
    if turn == 'WHITE':
        chkTurn = 'black'
    else:
        chkTurn = 'WHITE'
    for i in range(8):
        for j in range(8):
            if legalMove(i, j, kingPos[turn]['y'], kingPos[turn]['x'], chkTurn, True):
                #   print(i, j, kingPos[turn]['y'], kingPos[turn]['x'], chkTurn)
                return True
    return False


def checkMate(turn):
    oldK = kingPos
    if turn == 'WHITE':
        chkTurn = 'black'
    else:
        chkTurn = 'WHITE'
    for i in range(8):
        for j in range(8):
            for k in range(8):
                for l in range(8):
                    if legalMove(i, j, k, l, chkTurn, True):
                        #   print(i,j,k,l,chkTurn,'lovlig')
                        piece = board[k][l]
                        board[k][l] = board[i][j]
                        board[i][j] = 'empty'
                        if checkChess(chkTurn):
                            pass
                            #  print('Sjakk')
                        else:
                            board[i][j] = board[k][l]
                            board[k][l] = piece
                            return False
                        board[i][j] = board[k][l]
                        board[k][l] = piece
    return True


board = makeBoard()

def game():
    while not mate:
        printBoard(board)
        print()
        movePiece()

game()