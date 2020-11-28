

pieces = {
    'P': '♟',
    'p': '♟',

    'R': '♜',
    'r': '♜',

    'B': '♝',
    'b': '♝',

    'K': '♞',
    'k': '♞',

    'Q': '♛',
    'q': '♛',

    'KING': '♚',
    'king': '♚',

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
mate = False
moves = []
takenPieces = []
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '', '']
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


def movePiece(move):
    global turn
    global mate
    if checkRecognisable(move):
        y1 = len(board) - int(move[1])
        x1 = letters.index(move[0].upper())

        y2 = len(board) - int(move[-1])
        x2 = letters.index(move[-2].upper())

        if legalMove(y1, x1, y2, x2, turn):
            moveP(y1, x1, y2, x2)
        else:
            return
    else:
        return

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
    print(move.strip(), 'is not a recognisable move')
    return False


def legalMove(y1, x1, y2, x2, chkTurn, test = False):
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

"""
board = makeBoard()

def game():
    printBoard(board)
    print()


import pygame
import sys



def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((chessboardsize, chessboardsize))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()



print(pygame.font.get_fonts())
"""

board = makeBoard()
def game(move):
    movePiece(move)
    printBoard(board)
    print()


import pygame as pg

BLACK = (120, 80, 60)
WHITE = (0, 0, 0)
chessboardsize = 600
fontsize = chessboardsize//14

widthto = 70
pg.init()
screen = pg.display.set_mode((chessboardsize, chessboardsize))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 50)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                movePiece(self.text)
                self.text = ''
            elif event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            # Re-render the text.
            self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(widthto, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        global FONT
        FONT = pg.font.Font(None, 32)

        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)




def main():
    global SCREEN, board
    SCREEN = pg.display.set_mode((chessboardsize, chessboardsize))
    SCREEN.fill(BLACK)

    clock = pg.time.Clock()
    input_box = InputBox(chessboardsize/2-widthto/2, chessboardsize-32-5, 0, 32)
    done = False

    while not done:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            input_box.handle_event(event)
        input_box.update()

        screen.fill(BLACK)
        drawGrid()
        input_box.draw(screen)

        pg.display.flip()
        clock.tick(30)
letters2 = ['','A','B','C','D','E','F','G','H','']
numbers2 = ['','1','2','3','4','5','6','7','8','']
numbers2 = numbers2[::-1]
def drawGrid():
    global FONT
    block_amount = 10 #Set the size of the grid block
    blockSize = chessboardsize / block_amount
    FONT = pg.font.SysFont('segoeuisymbol', fontsize)
    img = FONT.render('', True, (10, 10, 10))
    for x in range(10):
        for y in range(10):
            if 0 < x < 9 and 0 < y < 9:
                rect = pg.Rect(x*blockSize, y*blockSize,blockSize, blockSize)
                pg.draw.rect(SCREEN, WHITE, rect, 1)
                if board[y-1][x-1] != 'empty':
                    if board[y-1][x-1].islower():
                        img = FONT.render(pieces[board[y-1][x-1]], True, (10, 10, 10))
                    elif board[y-1][x-1].isupper():
                        img = FONT.render(pieces[board[y-1][x-1]], True, (245, 245, 245))
                else:
                    img = FONT.render('', True, (10, 10, 10))
            elif (y == 0 or y == 9) and x != 10:
                img = FONT.render(letters2[x], True, (10, 10, 10))
            elif (x == 0 or x == 9):
                img = FONT.render(numbers2[y], True, (10, 10, 10))


            SCREEN.blit(img,(x*blockSize+chessboardsize//80, y*blockSize))

if __name__ == '__main__':
    main()
    pg.quit()


