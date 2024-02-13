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
        self.sprite = pygame.image.load("Assets/billSpawner.png")
        self.sprite_bill = pygame.image.load('Assets/bill.png')
        self.pos = (x, y)
        self.is_left = is_left
        if self.is_left:
            self.sprite = pygame.transform.rotate(self.sprite, 180)
            self.sprite_bill = pygame.transform.rotate(self.sprite_bill, 180)
        self.is_atirando = False
        temp_pos_bill = Stage.matrix_to_screen_pos(self.pos[0], self.pos[1])
        self.bill_pos = [temp_pos_bill[0], temp_pos_bill[1]]

    def update(self, screen, player_board_position):
        self.frames += 1
        if self.frames % Configuration.get_config().game_fps * 5:
            self.is_atirando = True

        if self.is_atirando and self.frames % 5 == 0:
            self.bill_pos[0] += 1 if self.is_left else -1

    def draw(self, screen):
        if self.is_atirando:
            screen.blit(self.sprite_bill, self.bill_pos)

        screen.blit(self.sprite, Stage.matrix_to_screen_pos(self.pos[0], self.pos[1]))