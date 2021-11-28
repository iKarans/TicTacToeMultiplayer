import pygame
import sys

pygame.init()

WIDTH = 620
HEIGHT = 620

BG_COLOR = (42, 157, 143)
LINE_COLOR = (38, 70, 83)
LINE_WIDTH = 15
X_COLOR = (233, 196, 106)
Y_COLOR = (244, 162, 97)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(BG_COLOR)

pygame.draw.line(screen, LINE_COLOR, (10, 200), (610, 200), LINE_WIDTH)
pygame.draw.line(screen, LINE_COLOR, (10, 400), (610, 400), LINE_WIDTH)
pygame.draw.line(screen, LINE_COLOR, (210, 10), (210, 610), LINE_WIDTH)
pygame.draw.line(screen, LINE_COLOR, (410, 10), (410, 610), LINE_WIDTH)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()