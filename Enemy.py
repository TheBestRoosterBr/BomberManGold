import pygame

from Configuration import Configuration
import PathFinder
import Stage


class Enemy:
    def __init__(self, health=100, damage=1, speed=1):
        self.health = health
        self.damage = damage
        self.speed = speed

    def update(self, screen, player_board_position):
        pass

    def draw(self, screen):
        pass


class Koopa(Enemy):
    def __init__(self, x, y):
        super().__init__()
        self.sprite = pygame.image.load('Assets\Koopa.png')
        self.index = 0
        self.frames = 0
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
