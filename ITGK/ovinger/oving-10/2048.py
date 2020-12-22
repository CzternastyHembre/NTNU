import pygame
import sys
import random as r
import copy

background = (100, 100, 100)
border = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = WINDOW_HEIGHT


def main():
    global SCREEN, CLOCK, grid
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()

    while True:
        SCREEN.fill(background)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == 119:
                    event.key = 3+1073741903
                if event.key == 115:
                    event.key = 2+1073741903
                if event.key == 100:
                    event.key = 0+1073741903
                if event.key == 97:
                    event.key = 1+1073741903
                if 1073741903 <= event.key <= 1073741906:
                    turn(event.key - 1073741903)
                if event.key == 114:
                    grid = make_grid()
        drawGrid()
        pygame.display.update()


def drawGrid():
    blocks = len(grid)
    blockSize = WINDOW_HEIGHT/blocks #Set the size of the grid block
    for x in range(blocks):
        for y in range(blocks):

            rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            pygame.draw.rect(SCREEN, border, rect, 10)


            FONT = pygame.font.SysFont(None, 50 + 50//(len(str(grid[y][x]))**2))
            img = FONT.render(' ', True, (10, 10, 10))
            if grid[y][x] > 0:
                img = FONT.render(str(grid[y][x]), True, (10, 10, 10))
            SCREEN.blit(img, (x * blockSize + blockSize//blocks -(len(str(grid[y][x]))-1)**2*2, y * blockSize + blockSize//blocks + (len(str(grid[y][x]))-1)**2*2))


def make_grid():
    grid = [[0 for i in range(4)] for i in range(4)]
    add_random(grid)
    add_random(grid)

    return grid


def print_grid(grid):
    for row in grid:
        for el in row:
            print(el, end=' ')
        print()

def move(dir):
    global grid
    oldgrid = copy.deepcopy(grid)

    if dir == 0:
        sort_right(grid)
    if dir == 1:
        sort_left(grid)
    if dir == 2:
        sort_down(grid)
    if dir == 3:
        sort_up(grid)

    change = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != oldgrid[i][j]:
                change = True

    if 0 <= dir <= 3:
        if change:
            add_random(grid)
            print()
            print_grid(grid)


def move_right(grid):
    for row in grid:
        for i in range(len(row)-1):
            if row[i+1] == 0 and row[i] != 0:
                row[i+1], row[i] = row[i], 0
def add_right(grid):
    for row in grid:
        for i in range(len(row)-1,0,-1):
            if row[i] == row[i-1]:
                row[i] *= 2
                row[i-1] = 0
def move_left(grid):
    for row in grid:
        for i in range(len(row)-1,0,-1):
            if row[i-1] == 0 and row[i] != 0:
                row[i-1], row[i] = row[i], 0
def add_left(grid):
    for row in grid:
        for i in range(len(row)-1):
            if row[i+1] == row[i]:
                row[i] *= 2
                row[i+1] = 0
def move_down(grid):
    for i in range(len(grid[0])):
        for j in range(len(grid)-1):
            if grid[j+1][i] == 0 and grid[j][i] != 0:
                grid[j+1][i], grid[j][i] = grid[j][i], 0
def add_down(grid):
    for i in range(len(grid[0])):
        for j in range(len(grid)-1,0,-1):
            if grid[j][i] == grid[j-1][i]:
                grid[j][i] *= 2
                grid[j-1][i] = 0
def move_up(grid):
    for i in range(len(grid[0])):
        for j in range(len(grid)-1,0,-1):
            if grid[j-1][i] == 0 and grid[j][i] != 0:
                grid[j-1][i], grid[j][i] = grid[j][i], 0
def add_up(grid):
    for i in range(len(grid[0])):
        for j in range(len(grid)-1):
            if grid[j+1][i] == grid[j][i]:
                grid[j][i] *= 2
                grid[j+1][i] = 0
def sort_right(grid):
    move_right(grid)
    move_right(grid)
    add_right(grid)
    move_right(grid)
    move_right(grid)
def sort_left(grid):
    move_left(grid)
    move_left(grid)
    add_left(grid)
    move_left(grid)
    move_left(grid)


def sort_down(grid):
    move_down(grid)
    move_down(grid)
    add_down(grid)
    move_down(grid)
    move_down(grid)


def sort_up(grid):
    move_up(grid)
    move_up(grid)
    add_up(grid)
    move_up(grid)
    move_up(grid)


def add_random(grid):
    loose = True
    for row in grid:
        for el in row:
            if not el:
                loose = False
    if loose:
        print('Du tapte man')
        return
    while True:
        rindex = (r.randint(0,len(grid)-1), r.randint(0,len(grid[0])-1))
        if grid[rindex[0]][rindex[1]] == 0:
            grid[rindex[0]][rindex[1]] = 2
            break

def turn(dir):
    global grid

    move(dir)

grid = make_grid()
print_grid(grid)

main()