from re import L
import pygame  # used for the display

pygame.init()
screen = pygame.display.set_mode((1000, 1000))  # create 1000px x 1000px window


pygame.display.set_caption("Sudoku solver")

# sudoku grid is 9x9 0 can be used as placeholder since it isn't used in game
grid = [[0 for _ in range(9)] for x in range(9)]

step = 1000/9

font1 = pygame.font.SysFont("Ariel", 60)


def createChallengeGrid():  # create a predifined sudoku table
    grid[0] = [9, 8, 5, 4, 0, 1, 0, 0, 0]
    grid[1] = [0, 0, 0, 0, 3, 0, 0, 0, 0]
    grid[2] = [1, 0, 6, 0, 0, 0, 0, 0, 0]
    grid[3] = [0, 0, 0, 5, 0, 0, 0, 0, 0]
    grid[4] = [4, 0, 2, 0, 0, 9, 0, 0, 3]
    grid[5] = [0, 9, 0, 0, 6, 3, 4, 0, 0]
    grid[6] = [0, 6, 0, 0, 1, 0, 0, 0, 0]
    grid[7] = [0, 0, 0, 3, 0, 6, 0, 0, 5]
    grid[8] = [2, 0, 0, 0, 8, 0, 0, 0, 1]


def drawGrid():  # this isn't a pure function but oh well
    screen.fill((255, 255, 255))
    for i in range(9)[1:]:
        if i % 3 == 0:
            pygame.draw.line(screen, (0, 0, 0), (i*step, 0), (i*step, 1000), 3)
        else:
            pygame.draw.line(screen, (0, 0, 0), (i*step, 0), (i*step, 1000), 1)
    for i in range(9)[1:]:
        if i % 3 == 0:
            pygame.draw.line(screen, (0, 0, 0), (0, i*step), (1000, i*step), 3)
        else:
            pygame.draw.line(screen, (0, 0, 0), (0, i*step), (1000, i*step), 1)


def populateGrid():  # this isn't a pure function too
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != 0:
                cellVal = font1.render(str(cell), 1, (0, 0, 0))
                screen.blit(cellVal, ((i+0.5)*step, (j+0.5)*step))
            print(cell, end=' ')
        print('')


def solve():
    # rules of sudoku:
    # 1. There can't be two same numbers in each 3x3 square
    # 2. There can't be two same numbers in a row
    # 3. There can't be two same numbers in a collumn
    empty = findEmpty()
    if not empty:
        return True
    x, y = empty
    for guess in range(1, 10):
        if validate(x, y, guess):
            grid[y][x] = guess
            if solve():
                return True

        grid[y][x] = 0
    return False


def findEmpty():  # needed for the backtracking algorithm
    for x in range(9):
        for y in range(9):
            if grid[y][x] == 0:
                return (x, y)
    return False


def validate(x, y, val):
    # check if the given inputs are suitable
    # returns true if inputs are suitable
    for i in range(9):
        if grid[y][i] == val:
            return False
    for i in range(9):
        if grid[i][x] == val:
            return False
    for i in range(9):
        pass
    qx = x//3*3  # qx and qy are the coords of the top left corner of the small square containing x and y
    qy = y//3*3
    for i in range(3):
        for j in range(3):
            if val == grid[qy + j][qx + i]:
                return False
    return True


createChallengeGrid()
drawGrid()
populateGrid()
pygame.display.update()

while True:
    pass
