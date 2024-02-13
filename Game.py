import pygame.display

import Configuration
import Stage
from Player import Player
import Stage


class Game:
    def __init__(self, screen):
        self.config = Configuration.Configuration.get_config()
        self.screen = screen
        self.stage = Stage.stage
        self.player = Player()
        self.is_running = True
        self.frames = 0
        self.clock = pygame.time.Clock()

    def update(self):
        #Simplesmente um if que n serve pra nada. TODO: um timer pra não ficar rápido
        self.frames += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    self.player.put_bomb()

        if not self.player.is_morrendo:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a]:
                self.player.move_left(self.frames,self.stage.board)
            elif keys[pygame.K_d]:
                self.player.move_right(self.frames, self.stage.board)
            elif keys[pygame.K_s]:
                self.player.move_down(self.frames, self.stage.board)
            elif keys[pygame.K_w]:
                self.player.move_up(self.frames, self.stage.board)
            else:
                self.player.stop()

        self.draw()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.stage.draw(self.screen)
        self.player.update(self.screen)
        pygame.display.update()
        self.clock.tick(self.config.game_fps)

    def run(self):
        while self.is_running:
            self.update()


