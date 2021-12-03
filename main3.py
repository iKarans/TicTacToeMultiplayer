import pygame
import sys
import numpy as np
import threading
import socket

HOST = "localhost"
PORT = 9090
FORMAT = "utf-8"

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
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.board = np.zeros((3, 3))
        self.turn = 1
        self.you = "X"
        self.opponent = "O"
        self.winner = None
        self.game_over = False
        self.counter = 0

        multiplayer_thread = threading.Thread(target=self.handle_multiplayer)
        multiplayer_thread.start()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.setup_pygame()
        self.run_pygame()

    def handle_multiplayer(self):
        while True:
            print("hi")
            if self.turn == 1:
                move = self.sock.recv(1024).decode(FORMAT)
                print(move)
                movex = int(move.split(",")[0])
                movey = int(move.split(",")[1])
                self.mark_square(movex, movey, self.turn)
                self.turn = 2
                self.draw_shape()

    def run_pygame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    if self.turn == 2:
                        if self.is_valid_square(int(event.pos[1] // 200), int(event.pos[0] // 200)):
                            self.mark_square(int(event.pos[1] // 200), int(event.pos[0] // 200), self.turn)
                            self.turn = 1
                            self.sock.send(f"{int(event.pos[1] // 200)},{int(event.pos[0] // 200)}".encode(FORMAT))
                            print(1)
                            print(self.board)
                            self.draw_shape()
            pygame.display.update()

    def setup_pygame(self):
        pygame.display.set_caption("Tic-Tac-Toe")
        self.screen.fill(BG_COLOR)
        pygame.draw.line(self.screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
        pygame.draw.line(self.screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

    def draw_shape(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 1:
                    pygame.draw.circle(self.screen, Y_COLOR, (col * 200 + 100, row * 200 + 100), CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif self.board[row][col] == 2:
                    pygame.draw.circle(self.screen, X_COLOR, (col * 200 + 100, row * 200 + 100), CIRCLE_RADIUS, CIRCLE_WIDTH)

    def is_valid_square(self, row, col):
        return self.board[row][col] == 0

    def mark_square(self, row, col, player):
        self.board[row][col] = player

    def check_if_won(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                self.winner = self.board[row][0]
                self.game_over = True
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                self.winner = self.board[0][col]
                self.game_over = True
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            self.winner = self.board[0][0]
            self.game_over = True
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            self.winner = self.board[0][0]
            self.game_over = True
            return True
        return False




ticTacToe = TicTacToe(HOST, PORT)