import pygame
import sys
import numpy as np

WIDTH = 600
HEIGHT = 600

BG_COLOR = (42, 157, 143)
LINE_COLOR = (38, 70, 83)
LINE_WIDTH = 10
X_COLOR = (233, 196, 106)
Y_COLOR = (244, 162, 97)

CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.turn = "X"
        self.you = "X"
        self.opponent = "O"
        self.winner = None
        self.playing = True
        self.counter = 0

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.setup_pygame()
        self.run_pygame()

    def run_pygame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()

    def setup_pygame(self):
        pygame.display.set_caption("Tic-Tac-Toe")
        self.screen.fill(BG_COLOR)
        pygame.draw.line(self.screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)




ticTacToe = TicTacToe()