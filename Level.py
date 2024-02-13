import pygame
import Stage
from Configuration import Configuration
from Enemy import *
from Game import Game


class Level:
    def __init__(self, num):
        self.enemies = []
        self.num = num

    def alter_stage(self):
        pass

    def run(self, screen):
        pass


class Level1World1(Level):
    def __init__(self):
        super().__init__(1)

    def alter_stage(self):
        Stage.stage.sprite_parede = pygame.transform.scale(pygame.image.load("Assets/marioBlock.png"),
                                                           Configuration.get_config().cell_size)
        Stage.stage.sprite_parede_destrutiva = pygame.transform.scale(
            pygame.image.load("Assets/marioBrickBlock.png"), Configuration.get_config().cell_size)

        Stage.stage.board = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1],
            [1, 3, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 0, 1, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 3, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 3, 1, 0, 1, 1, 0, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 3, 1, 0, 1, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 3, 1, 0, 1, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        Stage.stage.board = Stage.preencher_board(Stage.stage.board)

        koopa1 = Koopa(1, 16)
        koopa2 = Koopa(3, 13)
        self.enemies.append(koopa1)
        self.enemies.append(koopa2)

    def run(self, screen):
        self.alter_stage()
        game = Game(screen, enemies=self.enemies)
        game.run()


class Level1World1(Level):
    def __init__(self):
        super().__init__(1)

    def alter_stage(self):
        Stage.stage.sprite_parede = pygame.transform.scale(pygame.image.load("Assets/marioBlock.png"),
                                                           Configuration.get_config().cell_size)
        Stage.stage.sprite_parede_destrutiva = pygame.transform.scale(
            pygame.image.load("Assets/marioBrickBlock.png"), Configuration.get_config().cell_size)

        Stage.stage.board = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1],
            [1, 3, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 0, 1, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 3, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 3, 1, 0, 1, 1, 0, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 3, 1, 0, 1, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 3, 1, 0, 1, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        Stage.stage.board = Stage.preencher_board(Stage.stage.board)

        koopa1 = Koopa(1, 16)
        koopa2 = Koopa(3, 13)
        self.enemies.append(koopa1)
        self.enemies.append(koopa2)

    def run(self, screen):
        self.alter_stage()
        game = Game(screen, enemies=self.enemies)
        game.run()

class Level2World2(Level):
    def __init__(self):
        super().__init__(1)

    def alter_stage(self):
        Stage.stage.sprite_parede = pygame.transform.scale(pygame.image.load("Assets/marioBlock.png"),
                                                           Configuration.get_config().cell_size)
        Stage.stage.sprite_parede_destrutiva = pygame.transform.scale(
            pygame.image.load("Assets/marioBrickBlock.png"), Configuration.get_config().cell_size)

        Stage.stage.board = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1],
            [1, 3, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 0, 1, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 3, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 3, 1, 0, 1, 1, 0, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 3, 1, 0, 1, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 3, 1, 0, 1, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        Stage.stage.board = Stage.preencher_board(Stage.stage.board)

        koopa1 = Koopa(1, 16)
        koopa2 = Koopa(3, 13)
        self.enemies.append(koopa1)
        self.enemies.append(koopa2)

    def run(self, screen):
        self.alter_stage()
        game = Game(screen, enemies=self.enemies)
        game.run()