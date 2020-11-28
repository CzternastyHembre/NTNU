import pygame as pg
import sjakkdup as chess
pieces = chess.pieces
board = chess.makeBoard()
width = 400
height = width
widthto = 70
pg.init()
screen = pg.display.set_mode((width, height))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)


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
                chess.movePiece(self.text)
                chess.game()
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


BLACK = (50, 30, 30)
WHITE = (0, 0, 0)
chessboardsize = 400


def main():
    global SCREEN, board
    SCREEN = pg.display.set_mode((chessboardsize, chessboardsize))
    SCREEN.fill(BLACK)

    clock = pg.time.Clock()
    input_box = InputBox(width/2-widthto/2, height-32-10, 0, 32)
    done = False

    while not done:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            input_box.handle_event(event)
        input_box.update()


        drawGrid()
        input_box.draw(screen)

        pg.display.flip()
        clock.tick(30)

def drawGrid():
    global FONT
    block_amount = 8 #Set the size of the grid block
    blockSize = chessboardsize / block_amount
    FONT = pg.font.SysFont('segoeuisymbol', 38)
    for x in range(8):
        for y in range(8):
            rect = pg.Rect(x*blockSize, y*blockSize,blockSize, blockSize)
            pg.draw.rect(SCREEN, WHITE, rect, 1)
            if board[y][x] != 'empty':
                if board[y][x].islower():
                    img = FONT.render(pieces[board[y][x]], True, (10, 10, 10))
                else:
                    img = FONT.render(pieces[board[y][x]], True, (150, 150, 150))

                SCREEN.blit(img,(x*blockSize+6, y*blockSize))

if __name__ == '__main__':
    main()
    pg.quit()


