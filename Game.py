import pygame.display

from Player import Player
from Stage import *


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.stage = Stage()
        self.player = Player()
        self.is_running = True
        self.frames = 0

    def update(self):
        self.frames += 1
        if self.frames <= 60:
            self.frames = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player.move_left(self.frames)
                elif event.key == pygame.K_d:
                    self.player.move_right(self.frames)
                elif event.key == pygame.K_s:
                    self.player.move_down(self.frames)
                elif event.key == pygame.K_w:
                    self.player.move_up(self.frames)
                else:
                    self.player.stop()
        self.draw()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.stage.draw(self.screen)
        self.player.draw(self.screen)

    def run(self):
        while self.is_running:
            self.update()


