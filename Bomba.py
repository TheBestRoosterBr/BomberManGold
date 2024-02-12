import pygame
import Stage
from Configuration import Configuration


class Bomba:
    def __init__(self, bomb_power, x, y):
        self.power = bomb_power
        self.timer = 0
        self.max_timer = Configuration.get_config().game_fps * 3 # 3 Seconds
        self.position = (x, y)
        self.sprite = pygame.image.load("Assets/bomba.png")
        self.explosion_sprite = pygame.image.load("Assets/explosao.png")
        self.explosion_index = [0, 0]
        self.explosion_timer = 0
        self.frames = 0
        self.frame_size = 16
        self.frame_index = 0
        self.is_exploded = False

    def update(self, screen):
        self.frames += 1
        if self.frames > self.max_timer:
            self.explode(screen)
        else:
            if self.frames % (Configuration.get_config().game_fps / 5) == 0:
                self.frame_index += 1
                if self.frame_index > 2:
                    self.frame_index = 0
            self.draw(screen)

    def explode(self, screen):
        if self.frames % (Configuration.get_config().game_fps/10) == 0:
            self.explosion_index[1] += 1
        if self.explosion_index[1] >= 3:
            self.is_exploded = True
            return
        # Center
        actual_frame = self.explosion_sprite.subsurface((0, self.explosion_index[1] * self.frame_size,
                                                         self.frame_size, self.frame_size))
        actual_frame = pygame.transform.scale(actual_frame, Configuration.get_config().cell_size)
        screen.blit(actual_frame, Stage.matrix_to_screen_pos(self.position[0], self.position[1]))
        # Up
        for i in range(1, self.power):
            position = self.position[0] - i
            index = 2 if i == self.power - 1 else 1
            spr = self.explosion_sprite.subsurface((index * self.frame_size, self.explosion_index[1] * self.frame_size,
                                                    self.frame_size, self.frame_size))
            rotated_spr = pygame.transform.rotate(spr, 90)
            rotated_spr = pygame.transform.scale(rotated_spr, Configuration.get_config().cell_size)
            screen.blit(rotated_spr, Stage.matrix_to_screen_pos(position, self.position[1]))
        # Down
        for i in range(1, self.power):
            position = self.position[0] + i
            index = 2 if i == self.power - 1 else 1
            spr = self.explosion_sprite.subsurface((index * self.frame_size, self.explosion_index[1] * self.frame_size,
                                                    self.frame_size, self.frame_size))
            rotated_spr = pygame.transform.rotate(spr, -90)
            rotated_spr = pygame.transform.scale(rotated_spr, Configuration.get_config().cell_size)
            screen.blit(rotated_spr, Stage.matrix_to_screen_pos(position, self.position[1]))

        # Right
        for i in range(1, self.power):
            position = self.position[1] - i
            index = 2 if i == self.power - 1 else 1
            spr = self.explosion_sprite.subsurface((index * self.frame_size, self.explosion_index[1] * self.frame_size,
                                                    self.frame_size, self.frame_size))

            spr = pygame.transform.scale(spr, Configuration.get_config().cell_size)
            screen.blit(spr, Stage.matrix_to_screen_pos(self.position[0], position))

        # Left
        for i in range(1, self.power):
            position = self.position[1] + i
            index = 2 if i == self.power - 1 else 1
            spr = self.explosion_sprite.subsurface((index * self.frame_size, self.explosion_index[1] * self.frame_size,
                                                    self.frame_size, self.frame_size))
            rotated_spr = pygame.transform.rotate(spr, -180)
            rotated_spr = pygame.transform.scale(rotated_spr, Configuration.get_config().cell_size)
            screen.blit(rotated_spr, Stage.matrix_to_screen_pos(self.position[0], position))

    def draw(self, screen):
        frame = self.sprite.subsurface((self.frame_index * self.frame_size, 0, self.frame_size, self.frame_size))
        frame = pygame.transform.scale(frame, Configuration.get_config().cell_size)
        screen.blit(frame, Stage.matrix_to_screen_pos(self.position[0], self.position[1]))

