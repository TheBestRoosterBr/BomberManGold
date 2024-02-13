import pygame.display

import Configuration
import Stage
from Enemy import Koopa
from Player import Player
import Stage


class Game:
    def __init__(self, screen, enemies=None):
        if enemies is None:
            enemies = []
        self.config = Configuration.Configuration.get_config()
        self.screen = screen
        self.stage = Stage.stage
        self.player = Player(1, 1)
        self.is_running = True
        self.frames = 0
        self.clock = pygame.time.Clock()
        self.enemies = enemies
        self.game_result = 0 # 0 for win, 1 to lose, 2 for draw

    def update(self, lucky_block_position=(0, 0)):
        #Simplesmente um if que n serve pra nada. TODO: um timer pra não ficar rápido
        self.frames += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                pygame.quit()
            if not self.player.is_morrendo or self.player.is_invincible:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_j:
                        self.player.put_bomb()
                    elif event.key == pygame.K_k:
                        if self.player.bomb_type == 'relogio':
                            for i in self.player.bombs:
                                if i.current_type == 'relogio':
                                    i.bomb_types['relogio']['enable'](i)
                                    break

        if not self.player.is_morrendo or self.player.is_invincible:
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

        if not self.player.isAlive:
            self.is_running = False
            self.game_result = 1
            return
        return self.draw(lucky_block_position)

    def draw(self, lucky_block_position=(0, 0)):
        self.screen.fill((0, 0, 0))
        self.stage.draw(self.screen, lucky_block_position)
        result = self.player.update(self.screen, self.frames)
        pos = self.player.position
        for i in range(len(self.enemies)):
            self.enemies[i].update(self.screen, Stage.screen_pos_to_matrix(pos[0], pos[1]))
        pygame.display.update()
        self.clock.tick(self.config.game_fps)
        return result

    def run(self, lucky_block_position=(0, 0)):
        while self.is_running:
            self.game_result = self.update(lucky_block_position)
            if self.game_result:
                return True
            if not self.player.isAlive:
                return False
        return False


