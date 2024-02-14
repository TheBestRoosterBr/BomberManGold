import math
import random
import pygame
from Configuration import Configuration
from BlockStatus import BlockStatus
from PowerUp import PowerUp


def create_clear_board():
    ROW = 19
    COL = 15
    # Create an empty board filled with clear blocks
    board = [[0 for _ in range(COL)] for _ in range(ROW)]
    return board


def preencher_board(board):
    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[j][i] == BlockStatus.CLEAR:
                if random.randint(1, 20) < 19:
                    board[j][i] = BlockStatus.DESTRUCTIBLE_WALL
            elif board[j][i] == 3:
                board[j][i] = BlockStatus.CLEAR
    return board


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

    return preencher_board(board)


def screen_pos_to_matrix(screen_x, screen_y):
    config = Configuration.get_config()
    cell_size = config.cell_size[0]
    offset_x = config.offset_x
    offset_y = config.offset_y

    i = (screen_y - offset_y) / cell_size
    j = (screen_x - offset_x) / cell_size

    i = round(i)
    j = round(j)

    return i, j


def screen_pos_to_matrix_movimentation(screen_x, screen_y, current_position, direction):
        config = Configuration.get_config()
        cell_size = config.cell_size[0]
        offset_x = config.offset_x
        offset_y = config.offset_y

        screen_x = screen_x + (direction[0] * cell_size / 2)
        screen_y = screen_y + (direction[1] * cell_size / 2)

        i = (screen_y - offset_y) / cell_size
        j = (screen_x - offset_x) / cell_size

        i = round(i)
        j = round(j)

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
        self.sprite_parede_destrutiva = pygame.transform.scale(pygame.image.load("Assets/ParedeDestrutiva.png"),
                                                               self.config.cell_size)
        self.bloco_explodindo = pygame.image.load("Assets/blocoQueimando.png")
        self.spr_porta_fechada = pygame.transform.scale(pygame.image.load("Assets/porta.png"), self.config.cell_size)
        self.spr_porta_aberta = pygame.transform.scale(pygame.image.load("Assets/portaAbrida.png"),
                                                       self.config.cell_size)
        self.spr_lucky_block = pygame.transform.scale(pygame.image.load("Assets/brickBlockFase2.png"),
                                                      self.config.cell_size)
        self.spr_chave = pygame.transform.scale(pygame.image.load("Assets/chave.png"),
                                                      self.config.cell_size)
        self.bloco_explodindo_index = [
            0b1000000,
            0b1100000,
            0b1110000,
            0b1111000,
            0b1111100,
            0b1111110,
        ]
        self.power_up_sprite = pygame.image.load("Assets/power_up_queimando.png")
        self.power_up_explodindo_index = [
            0b10000001000000,
            0b11000001000000,
            0b11100001000000,
            0b11110001000000,
            0b11111001000000,
            0b11111101000000,
        ]

        self.bombas = []
        self.frames = 0
        self.power_ups = []
        self.background_color = (0, 100, 0)

    def draw(self, screen, lucky_block_position=(0, 0)):

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                position = (self.config.cell_size[1] * j + self.config.offset_x, self.config.cell_size[0] * i + self.config.offset_y)
                if (i, j) == lucky_block_position and self.board[i][j] == BlockStatus.LUCKY_BLOCK:
                    screen.blit(self.spr_lucky_block, position)
                elif self.board[i][j] == BlockStatus.CLEAR or self.board[i][j] == BlockStatus.BOMBA or self.board[i][j] == BlockStatus.FIRE:
                    pygame.draw.rect(screen, self.background_color, pygame.Rect(position, self.config.cell_size), 0)
                elif self.board[i][j] == BlockStatus.PORTAL_FECHADO:
                    pygame.draw.rect(screen, self.background_color, pygame.Rect(position, self.config.cell_size), 0)
                    screen.blit(self.spr_porta_fechada, position)
                elif self.board[i][j] == BlockStatus.PORTAL_ABERTO:
                    pygame.draw.rect(screen, self.background_color, pygame.Rect(position, self.config.cell_size), 0)
                    screen.blit(self.spr_porta_aberta, position)
                elif self.board[i][j] == BlockStatus.CHAVE:
                    pygame.draw.rect(screen, self.background_color, pygame.Rect(position, self.config.cell_size), 0)
                    screen.blit(self.spr_chave, position)
                elif self.board[i][j] == BlockStatus.WALL:
                    screen.blit(self.sprite_parede, position)
                elif self.board[i][j] == BlockStatus.DESTRUCTIBLE_WALL:
                    screen.blit(self.sprite_parede_destrutiva, position)
                elif self.board[i][j] & 0b10000001000000 == 0b1000000:
                    index = self.bloco_explodindo_index.index(self.board[i][j])
                    frame = self.bloco_explodindo.subsurface(index * 16, 0, 16, 16)
                    frame = pygame.transform.scale(frame, Configuration.get_config().cell_size)
                    pygame.draw.rect(screen, self.background_color, pygame.Rect(position, self.config.cell_size), 0)
                    screen.blit(frame, matrix_to_screen_pos(i, j))
                elif self.board[i][j] & 0b10000001000000 == 0b10000001000000:
                    index = self.power_up_explodindo_index.index(self.board[i][j])
                    frame = self.power_up_sprite.subsurface(index * 16, 0, 16, 16)
                    frame = pygame.transform.scale(frame, Configuration.get_config().cell_size)
                    pygame.draw.rect(screen, self.background_color, pygame.Rect(position, self.config.cell_size), 0)
                    screen.blit(frame, matrix_to_screen_pos(i, j))

        for i in self.power_ups:
            i.draw(screen)

        self.update(lucky_block_position)

    def update(self, lucky_block_position=(0, 0)):

        self.frames += 1
        if self.frames >= 6:
            self.frames = 0

            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] & 0b10000001000000 == 0b1000000:
                        index = self.bloco_explodindo_index.index(self.board[i][j])
                        if index == len(self.bloco_explodindo_index) - 1:
                            if random.randint(0, 1) == 1:
                                if (i, j) != lucky_block_position and random.randint(0, 1) == 1:
                                    self.board[i][j] = BlockStatus.POWER_UP
                                    power_up = PowerUp(i, j)
                                    self.board[i][j] += power_up.num
                                    self.power_ups.append(power_up)
                                else:
                                    if lucky_block_position == (i, j):
                                        self.board[i][j] = BlockStatus.CHAVE
                                    else:
                                        self.board[i][j] = BlockStatus.CLEAR
                        else:
                            self.board[i][j] = self.bloco_explodindo_index[index + 1]

                    elif self.board[i][j] & 0b10000001000000 == 0b10000001000000:
                        index = self.power_up_explodindo_index.index(self.board[i][j])
                        if index == len(self.power_up_explodindo_index) - 1:
                            self.board[i][j] = BlockStatus.CLEAR
                        else:
                            self.board[i][j] = self.power_up_explodindo_index[index + 1]


stage = Stage()
