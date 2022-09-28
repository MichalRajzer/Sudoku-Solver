import pygame  # used for the display

pygame.init()
screen = pygame.display.set_mode((1000, 1000))  # create 1000px x 1000px window


pygame.display.set_caption("Sudoku solver")

grid = [[0 for _ in range(9)] for x in range(9)]  # sudoku grid is 9x9

step = 1000/9

font1 = pygame.font.SysFont("Ariel", 60)

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

def populateGrid():
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            cellVal = font1.render(str(cell), 1, (0, 0, 0))
            screen.blit(cellVal, ((i+0.5)*step, (j+0.5)*step))
            print(cell, end=' ')
        print('')

drawGrid()
populateGrid()
pygame.display.update()


while True:
    pass