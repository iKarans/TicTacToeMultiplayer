import pygame
import sys
import numpy as np
import threading
import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090
FORMAT = "utf-8"

WIDTH = 600
HEIGHT = 600

BG_COLOR = (69, 123, 157)
LINE_COLOR = (29, 53, 87)
LINE_WIDTH = 10
X_COLOR = (168, 218, 220)
O_COLOR = (230, 57, 70)
WIN_LINE_COLOR = (241, 250, 238)

CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15


class TicTacToe:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.board = np.zeros((3, 3))
        self.player = 1
        self.turn = 1
        self.game_over = 0
        self.counter = 0

        multiplayer_thread = threading.Thread(target=self.handle_multiplayer)
        multiplayer_thread.start()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.setup_pygame()
        self.run_pygame()

    def handle_multiplayer(self):
        while True:
            message = self.sock.recv(1024).decode(FORMAT)
            if message == "RESTART":
                self.restart()
            else:
                if self.turn != self.player:
                    moveX = int(message.split(",")[0])
                    moveY = int(message.split(",")[1])
                    self.game_over = int(message.split(",")[2])
                    self.mark_square(moveX, moveY, 2)
                    self.turn = self.player
                    self.draw_shape()

    def run_pygame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and self.game_over == 0 and not self.counter > 5:
                    if self.turn == self.player:
                        if self.is_valid_square(int(event.pos[1] // 200), int(event.pos[0] // 200)):
                            self.mark_square(int(event.pos[1] // 200), int(event.pos[0] // 200), self.player)
                            self.draw_shape()
                            self.counter += 1
                            self.check_if_won()
                            self.sock.send(f"{int(event.pos[1] // 200)},{int(event.pos[0] // 200)},{self.game_over}".encode(FORMAT))
                            self.turn = 2
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.sock.send("RESTART".encode(FORMAT))
                        self.restart()
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
                    pygame.draw.circle(self.screen, X_COLOR, (col * 200 + 100, row * 200 + 100), CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif self.board[row][col] == 2:
                    pygame.draw.circle(self.screen, O_COLOR, (col * 200 + 100, row * 200 + 100), CIRCLE_RADIUS, CIRCLE_WIDTH)

    def is_valid_square(self, row, col):
        return self.board[row][col] == 0

    def mark_square(self, row, col, player):
        self.board[row][col] = player

    def draw_vertical_win_line(self, col):
        posX = col * 200 + 100
        pygame.draw.line(self.screen, WIN_LINE_COLOR, (posX, 0), (posX, 600), LINE_WIDTH)

    def draw_horizontal_win_line(self, row):
        posY = row * 200 + 100
        pygame.draw.line(self.screen, WIN_LINE_COLOR, (0, posY), (600, posY), LINE_WIDTH)

    def draw_diagonal_up_line(self):
        pygame.draw.line(self.screen, WIN_LINE_COLOR, (600, 0), (0, 600), LINE_WIDTH)

    def draw_diagonal_down_line(self):
        pygame.draw.line(self.screen, WIN_LINE_COLOR, (0, 0), (600, 600), LINE_WIDTH)



    def check_if_won(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != 0:
                self.winner = self.board[row][0]
                self.game_over = 1
                self.draw_horizontal_win_line(row)
                return self.game_over
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != 0:
                self.winner = self.board[0][col]
                self.draw_vertical_win_line(col)
                self.game_over = 1
                return self.game_over
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            self.winner = self.board[0][0]
            self.draw_diagonal_down_line()
            self.game_over = 1
            return self.game_over
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            self.winner = self.board[0][0]
            self.draw_diagonal_up_line()
            self.game_over = 1
            return self.game_over
        return 0

    def restart(self):
        self.screen.fill(BG_COLOR)
        self.setup_pygame()
        self.board = np.zeros((3, 3))
        self.turn = 1
        self.game_over = 0
        self.counter = 0




ticTacToe = TicTacToe(HOST, PORT)