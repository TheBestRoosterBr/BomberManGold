import random

import pygame

from Configuration import Configuration
from BlockStatus import BlockStatus


def create_board():
    board = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1],
        [1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 3, 1, 0, 1, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 3, 1, 0, 1, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 3, 1, 0, 1, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
        [1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[j][i] == BlockStatus.CLEAR:
                if random.randint(1, 20) < 19:
                    board[j][i] = BlockStatus.DESTRUCTIBLE_WALL
            elif board[j][i] == 3:
                board[j][i] = BlockStatus.CLEAR
    return board


def screen_pos_to_matrix(screen_x, screen_y):
    config = Configuration.get_config()
    cell_size = config.cell_size[0]
    offset_x = config.offset_x
    offset_y = config.offset_y

    i = (screen_y - offset_y) // cell_size
    j = (screen_x - offset_x) // cell_size

    return i, j


def matrix_to_screen_pos(i, j):
    screen_x = j * Configuration.get_config().cell_size[0] + Configuration.get_config().offset_x
    screen_y = i * Configuration.get_config().cell_size[0] + Configuration.get_config().offset_y
    return screen_x, screen_y


class Stage:
    def __init__(self):
        self.config = Configuration.get_config()
        self.board = create_board()
        self.sprite_parede = pygame.transform.scale(pygame.image.load("Assets/parede.png"), self.config.cell_size)
        self.sprite_parede_destrutiva = pygame.transform.scale(pygame.image.load("Assets/ParedeDestrutiva.png"), self.config.cell_size)

    def draw(self, screen):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                position = (self.config.cell_size[1] * j + self.config.offset_x, self.config.cell_size[0] * i + self.config.offset_y)
                if self.board[i][j] == BlockStatus.CLEAR:
                    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(position, self.config.cell_size), 0)
                elif self.board[i][j] == BlockStatus.WALL:
                    screen.blit(self.sprite_parede, position)
                elif self.board[i][j] == BlockStatus.DESTRUCTIBLE_WALL:
                    screen.blit(self.sprite_parede_destrutiva, position)
