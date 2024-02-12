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
        #Simplesmente um if que n serve pra nada. TODO: um timer pra não ficar rápido
        self.frames += 1
        if self.frames <= 60:
            self.frames = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player.move_left(self.frames)
        elif keys[pygame.K_d]:
            self.player.move_right(self.frames)
        elif keys[pygame.K_s]:
            self.player.move_down(self.frames)
        elif keys[pygame.K_w]:
            self.player.move_up(self.frames)
        else:
            self.player.stop()

        self.draw()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.stage.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.update()

    def run(self):
        while self.is_running:
            self.update()


