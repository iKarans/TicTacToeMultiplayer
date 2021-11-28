import pygame
import sys
import numpy as np

pygame.init()

WIDTH = 650
HEIGHT = 650

BG_COLOR = (42, 157, 143)
LINE_COLOR = (38, 70, 83)
LINE_WIDTH = 15
X_COLOR = (233, 196, 106)
Y_COLOR = (244, 162, 97)

CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(BG_COLOR)

#board
board = np.zeros((3, 3))

#Lines
pygame.draw.line(screen, LINE_COLOR, (10, 210), (640, 210), LINE_WIDTH)
pygame.draw.line(screen, LINE_COLOR, (10, 425), (640, 425), LINE_WIDTH)
pygame.draw.line(screen, LINE_COLOR, (210, 10), (210, 640), LINE_WIDTH)
pygame.draw.line(screen, LINE_COLOR, (425, 10), (425, 640), LINE_WIDTH)

# player
player = 1

def draw_shapes():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 2:
                pygame.draw.circle(screen, Y_COLOR, (j * 200 + 100, i * 200 + 100), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[i][j] == 1:
                pygame.draw.circle(screen, X_COLOR, (j * 200 + 100, i * 200 + 100), CIRCLE_RADIUS, CIRCLE_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player

def is_valid_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if is_valid_square(int(event.pos[1] // 200), int(event.pos[0] // 200)):
                if player == 1:
                    mark_square(int(event.pos[1] // 200), int(event.pos[0] // 200), player)
                    player = 2
                elif player == 2:
                    mark_square(int(event.pos[1] // 200), int(event.pos[0] // 200), player)
                    player = 1
                draw_shapes()
                print(board)
    pygame.display.update()