import pygame.display

from Stage import *


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.stage = Stage()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.screen.fill((0,  0,  0))
            self.stage.draw(self.screen)
            pygame.display.update()
