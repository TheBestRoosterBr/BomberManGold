import pygame

from Configuration import Configuration
import PathFinder
import Stage


class Enemy:
    def __init__(self, health=100, damage=3, speed=1):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.frames = 0

    def update(self, screen, player_board_position):
        pass

    def draw(self, screen):
        pass


class Koopa(Enemy):
    def __init__(self, x, y):
        super().__init__()
        self.sprite = pygame.image.load('Assets\Koopa.png')
        self.index = 0
        self.position = [x, y]

    def update(self, screen, player_board_position):
        # todo: deixar essa animacao lisa @Mota
        self.frames += 1
        if self.frames % 100 == 0:
            self.index = self.frames % 2
            pos = PathFinder.path_finder(player_board_position, self.position)
            self.position[0] += pos[0]
            self.position[1] += pos[1]
        self.draw(screen)

    def draw(self, screen):
        spr = self.sprite.subsurface(self.index * 16, 0, 16, 27)
        spr = pygame.transform.scale(spr, Configuration.get_config().cell_size)
        screen.blit(spr, Stage.matrix_to_screen_pos(self.position[0], self.position[1]))


class BillSpawner(Enemy):
    def __init__(self, x, y, is_left=False):
        super().__init__(health=20, damage=5, speed=1)
        sz = Configuration.get_config().cell_size
        self.sprite = pygame.transform.scale(pygame.image.load("Assets/billSpawner.png"), (sz[0], sz[1] * 2))
        self.pos = (x, y)
        self.is_left = is_left
        self.sprite_bill = pygame.transform.scale(pygame.image.load('Assets/bill.png'), sz)
        if self.is_left:
            self.sprite_bill = pygame.transform.scale(pygame.image.load("Assets/bill_left.png"), sz)
        self.is_atirando = True
        self.bill_init_pos = Stage.matrix_to_screen_pos(self.pos[0], self.pos[1])
        self.bill_pos = [self.bill_init_pos[0], self.bill_init_pos[1]]

    def update(self, screen, player_board_position):
        self.frames += 1
        if self.frames % (Configuration.get_config().game_fps * 5) == 0:
            if self.is_atirando:
                self.is_atirando = False
                self.bill_pos[0] = self.bill_init_pos[0]
                self.bill_pos[1] = self.bill_init_pos[1]
            else:
                self.is_atirando = True
        if self.is_atirando:
            self.bill_pos[0] += 3 if self.is_left else -3
        self.draw(screen)

    def draw(self, screen):
        if self.is_atirando:
            screen.blit(self.sprite_bill, self.bill_pos)
        screen.blit(self.sprite, Stage.matrix_to_screen_pos(self.pos[0], self.pos[1]))


class Fulor(Enemy):
    def __init__(self, x, y):
        super().__init__()
        self.sprite = pygame.image.load('Assets\Koopa.png')
        self.index = 0
        self.position = [x, y]

    def update(self, screen, player_board_position):
        # todo: deixar essa animacao lisa @Mota
        self.frames += 1
        if self.frames % 100 == 0:
            self.index = self.frames % 2
            pos = PathFinder.path_finder(player_board_position, self.position)
            self.position[0] += pos[0]
            self.position[1] += pos[1]
        self.draw(screen)

    def draw(self, screen):
        spr = self.sprite.subsurface(self.index * 16, 0, 16, 27)
        spr = pygame.transform.scale(spr, Configuration.get_config().cell_size)
        screen.blit(spr, Stage.matrix_to_screen_pos(self.position[0], self.position[1]))