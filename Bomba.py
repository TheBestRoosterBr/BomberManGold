import pygame
from Configuration import Configuration


class Bomba:
    def __init__(self, bomb_power, x, y):
        self.power = bomb_power
        self.timer = 0
        self.max_timer = Configuration.get_config().game_fps * 3 # 3 Seconds
        self.position = (x, y)
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass

