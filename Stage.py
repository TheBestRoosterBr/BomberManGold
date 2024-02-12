import random

import pygame

import Configuration
from BlockStatus import BlockStatus


def create_board():
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    cannot_have_blocks = [
        (0, 0),
        (1, 0),
        (0, 1),
        (0, 12),
        (0, 11),
        (1, 12),
        (8, 0),
        (8, 1),
        (7, 0),
        (8, 12),
        (7, 12),
        (8, 11),
        (4, 6),
        (3, 6),
        (5, 6),
        (4, 5),
        (4, 7)
    ]

    for i in range(len(board[0])):
        for j in range(len(board)):
            if not cannot_have_blocks.__contains__((i, j)) and board[j][i] == BlockStatus.CLEAR:
                value = random.randint(1, 20)
                if value < 17:
                    board[j][i] = BlockStatus.DESTRUCTIBLE_WALL
    return board


class Stage:
    def __init__(self):
        self.board = create_board()
        self.blockSize = (48, 48)
        self.sprite_parede = pygame.transform.scale(pygame.image.load("Assets/parede.png"), self.blockSize)
        self.sprite_parede_destrutiva = pygame.transform.scale(pygame.image.load("Assets/ParedeDestrutiva.png"), self.blockSize)
        self.config = Configuration.Configuration()

    def draw(self, screen):
        offset_x = (self.config.screen_width - self.blockSize[0] * len(self.board[0])) / 2
        offset_y = (self.config.screen_height - self.blockSize[1] * len(self.board)) / 2
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                position = (self.blockSize[0] * j + offset_x, self.blockSize[1] * i + offset_y)
                if self.board[i][j] == BlockStatus.CLEAR:
                    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(position, self.blockSize), 0)
                elif self.board[i][j] == BlockStatus.WALL:
                    screen.blit(self.sprite_parede, position)
                elif self.board[i][j] == BlockStatus.DESTRUCTIBLE_WALL:
                    screen.blit(self.sprite_parede_destrutiva, position)
