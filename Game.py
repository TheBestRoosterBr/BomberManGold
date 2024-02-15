import pygame.display

import Configuration
import Enemy
import Options
import Stage
import pause
from Enemy import Koopa
from Options import Options
from Options import ImageButton
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
        self.game_result = 0 # 0 for win, 1 to lose, 2 for draw, 3 for resign
        self.pause = pause.Pause()
        self.lateral = pygame.image.load("Assets/back_lateral.png")
        sz_pause = 64
        self.pause_button = ImageButton(self.config.screen_width - self.lateral.get_width() + sz_pause, sz_pause,
                                                sz_pause, sz_pause, "Assets/pause.png")


    def update(self, lucky_block_position=(0, 0)):

        self.frames += 1
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                pygame.quit()
            if not self.player.is_morrendo or self.player.is_invincible:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.pause_button.is_clicked(pos):
                        op = self.pause.view_paused(self.screen)
                        if op == 1:
                            options = Options()
                            options.main_loop(self.screen)
                        elif op == 2:
                            self.is_running = False
                            self.game_result = 3
                            break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        op = self.pause.view_paused(self.screen)
                        if op == 1:
                            options = Options()
                            options.main_loop(self.screen)
                        elif op == 2:
                            self.is_running = False
                            self.game_result = 3
                            break

                    if event.key == pygame.K_j:
                        self.player.put_bomb()
                    elif event.key == pygame.K_k:
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

        for enemy in self.enemies:
            if enemy.is_morrendo:
                if enemy.dead:
                    self.enemies.remove(enemy)
            else:
                if isinstance(enemy, Enemy.BillSpawner):
                    if Stage.screen_pos_to_matrix(self.player.position[0], self.player.position[1]) == Stage.screen_pos_to_matrix(enemy.bill_pos[0], enemy.bill_pos[1]):
                        self.player.morrer()

                elif isinstance(enemy, Enemy.MuxeguSpawner):
                    for batman in enemy.muxegus:
                        if Stage.screen_pos_to_matrix(self.player.position[0], self.player.position[1]) == Stage.screen_pos_to_matrix(batman.position[0], batman.position[1]):
                            self.player.morrer()
                elif isinstance(enemy, Enemy.Camaleao):
                    for i in range(4):
                        if Stage.screen_pos_to_matrix(self.player.position[0], self.player.position[1]) == (enemy.position[0] + i, enemy.position[1]):
                            self.player.morrer()
                elif isinstance(enemy, Enemy.GhostSpawner):
                    for pantarma in enemy.ghosts:
                        if Stage.screen_pos_to_matrix(self.player.position[0], self.player.position[1]) == Stage.screen_pos_to_matrix(pantarma.position[0], pantarma.position[1]):
                            self.player.morrer()

                else:
                    if Stage.screen_pos_to_matrix(self.player.position[0], self.player.position[1]) == (enemy.position[0], enemy.position[1]):
                        self.player.morrer()

        self.draw(lucky_block_position)

    def draw(self, lucky_block_position=(0, 0)):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.lateral, (0, 0))
        self.screen.blit(self.lateral, (self.config.screen_width - self.lateral.get_width(), 0))
        self.stage.draw(self.screen, lucky_block_position)
        result = self.player.update(self.screen, self.frames)
        if result == 1:
            self.is_running = False
            self.game_result = 0
            return
        pos = self.player.position
        for i in range(len(self.enemies)):
            self.enemies[i].update(self.screen, Stage.screen_pos_to_matrix(pos[0], pos[1]))
        self.pause_button.is_clicked(pos)
        self.pause_button.draw(self.screen)
        pygame.display.update()
        self.clock.tick(self.config.game_fps)

    def run(self, lucky_block_position=(0, 0)):
        while self.is_running:
            self.update(lucky_block_position)
        return self.game_result


