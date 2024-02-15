import random

import pygame

import PowerUp
import Stage
from Bomba import Bomba
from BlockStatus import BlockStatus
from Configuration import Configuration


class Player:
    def __init__(self, x, y):
        self.score = 0
        self.lives = 1
        self.Name = "BomberManFodase"
        pos = Stage.matrix_to_screen_pos(x, y)
        self.position = [pos[0], pos[1]]
        self.power_ups = []
        self.sprite = pygame.image.load('Assets/player' + Configuration.get_config().player + '.png')
        self.frame_width = 16
        self.frame_height = 24
        self.frame_index = [0, 0]
        self.last_state = 0  # 0 for left, 1 for right, 2 for up, and 3 for down
        self.speed = 2
        self.max_bombs = 1
        self.active_bombs = 0
        self.bomb_power = 3
        self.bomb_type = 'normal'
        self.bombs = []
        self.isAlive = True
        self.vidas = 0
        self.is_morrendo = False
        self.frames_morrendo = 0
        self.morrendo_index = 0
        self.total_morrendo = 6
        self.sound_morrendo = pygame.mixer.Sound('Sounds/on-fire.ogg')

        self.morrendo_sprite = pygame.image.load('Assets/morrendo' + Configuration.get_config().player + '.png')

        self.sound_Takeitem = pygame.mixer.Sound('Sounds/Take-item.mp3')
        self.sound_colocarbomb = pygame.mixer.Sound('Sounds/put_bomb.mp3')

        self.invincibility_timer = 0
        self.invincibility_max_timer = 0
        self.is_invincible = False
        self.timer_colete = 0

        self.caveira = {
            'enabled': False,
            'type': '',
        }

    def randon_caveira(self):
        self.caveira['enabled'] = True
        types = [
            'disable_bombs',
            'place_bombs',
            'inverter',
            'speed_up',
            'speed_down'
        ]
        self.caveira['type'] = types[random.randint(0, 4)]

    def disable_caveira(self):
        self.caveira = {
            'enabled': False,
            'type': '',
        }

    @staticmethod
    def check_collision(next_position, board, direction, player):
        matrix_pos = Stage.screen_pos_to_matrix_movimentation(next_position[0], next_position[1], player.position,
                                                              direction)
        if board[int(matrix_pos[0])][int(matrix_pos[1])] == BlockStatus.BOMBA:
            for bomba in player.bombs:
                if bomba.position == Stage.screen_pos_to_matrix(player.position[0], player.position[1]):
                    return True

        return (board[int(matrix_pos[0])][int(matrix_pos[1])] == BlockStatus.CLEAR or
                BlockStatus.POWER_UP <= board[int(matrix_pos[0])][int(matrix_pos[1])] <= BlockStatus.POWER_UP + 9 or
                board[int(matrix_pos[0])][int(matrix_pos[1])] == BlockStatus.CHAVE or
                board[int(matrix_pos[0])][int(matrix_pos[1])] == BlockStatus.PORTAL_ABERTO or
                board[int(matrix_pos[0])][int(matrix_pos[1])] == BlockStatus.PORTAL_FECHADO)

    def move_left(self, frames, board, check_caveira=True):

        if check_caveira and self.caveira['enabled'] and self.caveira['type'] == 'inverter':
            self.move_right(frames, board, check_caveira=False)
            return
        if self.check_collision((self.position[0] - self.speed, self.position[1]), board, (-1, 0), self):
            if self.caveira['enabled'] and self.caveira['type'] == 'speed_up':
                self.position[0] -= 20
            elif self.caveira['enabled'] and self.caveira['type'] == 'speed_down':
                self.position[0] -= 1
            else:
                self.position[0] -= self.speed

        if frames % 12 == 0:
            self.frame_index[0] += 1
            self.frame_index[0] = self.frame_index[0] % 3 + 3

        self.frame_index[1] = 0
        self.last_state = 0

    def move_right(self, frames, board, check_caveira=True):
        if check_caveira and self.caveira['enabled'] and self.caveira['type'] == 'inverter':
            self.move_left(frames, board, check_caveira=False)
            return

        if self.check_collision((self.position[0] + self.speed, self.position[1]), board, (1, 0), self):

            if self.caveira['enabled'] and self.caveira['type'] == 'speed_up':
                self.position[0] += 20
            elif self.caveira['enabled'] and self.caveira['type'] == 'speed_down':
                self.position[0] += 1
            else:
                self.position[0] += self.speed

        if frames % 12 == 0:
            self.frame_index[0] += 1
            self.frame_index[0] = self.frame_index[0] % 3

        self.frame_index[1] = 1
        self.last_state = 1

    def move_up(self, frames, board, check_caveira=True):

        if check_caveira and self.caveira['enabled'] and self.caveira['type'] == 'inverter':
            self.move_down(frames, board, check_caveira=False)
            return

        if self.check_collision((self.position[0], self.position[1] - self.speed), board, (0, -1), self):

            if self.caveira['enabled'] and self.caveira['type'] == 'speed_up':
                self.position[1] -= 20
            elif self.caveira['enabled'] and self.caveira['type'] == 'speed_down':
                self.position[1] -= 1
            else:
                self.position[1] -= self.speed

        if frames % 12 == 0:
            self.frame_index[0] += 1
            self.frame_index[0] = self.frame_index[0] % 3

        self.frame_index[1] = 0
        self.last_state = 2

    def move_down(self, frames, board, check_caveira=True):

        if check_caveira and self.caveira['enabled'] and self.caveira['type'] == 'inverter':
            self.move_up(frames, board, check_caveira=False)
            return

        if self.check_collision((self.position[0], self.position[1] + self.speed), board, (0, 1), self):

            if self.caveira['enabled'] and self.caveira['type'] == 'speed_up':
                self.position[1] += 20
            elif self.caveira['enabled'] and self.caveira['type'] == 'speed_down':
                self.position[1] += 1
            else:
                self.position[1] += self.speed

        if frames % 12 == 0:
            self.frame_index[0] += 1
            self.frame_index[0] = self.frame_index[0] % 3 + 3
        self.frame_index[1] = 1
        self.last_state = 3

    def stop(self):
        if self.last_state == 0:
            self.frame_index[0] = 3
            self.frame_index[1] = 0
        elif self.last_state == 1:
            self.frame_index[0] = 0
            self.frame_index[1] = 1
        elif self.last_state == 2:
            self.frame_index[0] = 1
            self.frame_index[1] = 0
        else:
            self.frame_index[0] = 4
            self.frame_index[1] = 1

    def put_bomb(self):

        if self.caveira['enabled'] and self.caveira['type'] == 'disable_bombs':
            return

        if self.active_bombs < self.max_bombs:
            self.sound_colocarbomb.play()
            self.sound_colocarbomb.set_volume(Configuration.get_config().volume)
            position = Stage.screen_pos_to_matrix(self.position[0], self.position[1])
            if Stage.stage.board[position[0]][position[1]] != BlockStatus.BOMBA and Stage.stage.board[position[0]][
                position[1]] != BlockStatus.PORTAL_ABERTO \
                    and Stage.stage.board[position[0]][position[1]] != BlockStatus.PORTAL_FECHADO and \
                    Stage.stage.board[position[0]][position[1]] != BlockStatus.LUCKY_BLOCK:
                bomb = Bomba(self.bomb_power, position[0], position[1], self.bomb_type)
                self.bombs.append(bomb)
                Stage.stage.bombas.append(bomb)
                self.active_bombs += 1

    def pegar_colete(self):
        self.timer_colete += 15 * Configuration.get_config().game_fps
        self.is_invincible = True
        self.sound_Takeitem.play()
        self.sound_Takeitem.set_volume(Configuration.get_config().volume)

    def morrer(self):
        if not self.is_invincible:
            self.is_morrendo = True
            self.is_invincible = True
            self.sound_morrendo.play()
            self.sound_morrendo.set_volume(Configuration.get_config().volume)

    def update(self, screen, frames):
        if self.isAlive and self.caveira['enabled'] and self.caveira['type'] == 'place_bombs':
            self.put_bomb()

        if self.timer_colete > 0:
            self.timer_colete -= 1
            if self.timer_colete == 0:
                self.is_invincible = False

        # Create a copy of the list to iterate over
        if self.is_morrendo:
            self.is_invincible = False
            if self.vidas == 0:
                self.frames_morrendo += 1
                if self.frames_morrendo >= 10:
                    self.frames_morrendo = 0
                    self.morrendo_index += 1
                    if self.morrendo_index == self.total_morrendo:
                        self.isAlive = False
            else:
                self.invincibility_timer += 1
                self.is_invincible = True
                if self.invincibility_timer > 60:
                    self.invincibility_timer = 0
                    self.vidas -= 1
                    self.is_morrendo = False
                    self.is_invincible = False

        if self.isAlive:
            bombs_copy = self.bombs[:]
            board = Stage.stage.board

            for bomb in bombs_copy:
                bomb.update(screen)
                if bomb.is_exploded:
                    # Remove the bomb from the original list
                    bomb_i = bomb.position[0]
                    bomb_j = bomb.position[1]
                    board[bomb_i][bomb_j] = BlockStatus.CLEAR
                    for i in range(1, bomb.power):
                        if board[bomb_i + i][bomb_j] == BlockStatus.FIRE:
                            board[bomb_i + i][bomb_j] = BlockStatus.CLEAR
                        elif board[bomb_i + i][bomb_j] == BlockStatus.WALL:
                            break

                    for i in range(1, bomb.power):
                        if board[bomb_i - i][bomb_j] == BlockStatus.FIRE:
                            board[bomb_i - i][bomb_j] = BlockStatus.CLEAR
                        elif board[bomb_i - i][bomb_j] == BlockStatus.WALL:
                            break

                    for i in range(1, bomb.power):
                        if board[bomb_i][bomb_j + i] == BlockStatus.FIRE:
                            board[bomb_i][bomb_j + i] = BlockStatus.CLEAR
                        elif board[bomb_i][bomb_j + i] == BlockStatus.WALL:
                            break

                    for i in range(1, bomb.power):
                        if board[bomb_i][bomb_j - i] == BlockStatus.FIRE:
                            board[bomb_i][bomb_j - i] = BlockStatus.CLEAR
                        elif board[bomb_i][bomb_j - i] == BlockStatus.WALL:
                            break

                    Stage.stage.bombas.remove(bomb)
                    self.bombs.remove(bomb)
                    self.active_bombs -= 1

            matrix_pos = Stage.screen_pos_to_matrix(self.position[0], self.position[1])
            if board[matrix_pos[0]][matrix_pos[1]] == BlockStatus.CHAVE:
                for i in range(len(board)):
                    for j in range(len(board[i])):
                        if board[i][j] == BlockStatus.PORTAL_FECHADO:
                            board[i][j] = BlockStatus.PORTAL_ABERTO
                            board[matrix_pos[0]][matrix_pos[1]] = BlockStatus.CLEAR
                            break

            elif 5 <= board[matrix_pos[0]][matrix_pos[1]] <= 14:
                for power in Stage.stage.power_ups:
                    if power.position == matrix_pos:
                        self.power_ups.append(power)
                        power.get_power_up(self)
                        Stage.stage.power_ups.remove(power)
                        board[matrix_pos[0]][matrix_pos[1]] = BlockStatus.CLEAR
                        break
            elif board[matrix_pos[0]][matrix_pos[1]] == BlockStatus.PORTAL_ABERTO:
                return 1

            if board[matrix_pos[0]][matrix_pos[1]] == BlockStatus.FIRE:
                self.morrer()

        if self.isAlive:
            self.draw(screen, frames)
        return 0

    def draw(self, screen, frames):
        if self.is_invincible and frames % 15 > 7:
            return
        if not self.is_morrendo or self.vidas > 0:
            frame = self.sprite.subsurface(
                (self.frame_index[0] * self.frame_width, self.frame_index[1] * self.frame_height,
                 self.frame_width - 1, self.frame_height - 1))
            frame = pygame.transform.scale(frame, Configuration.get_config().cell_size)
        else:
            frame = self.morrendo_sprite.subsurface(
                (self.morrendo_index * self.frame_width, 0,
                 self.frame_width - 1, self.frame_height - 1))
            frame = pygame.transform.scale(frame, Configuration.get_config().cell_size)
        screen.blit(frame, (self.position[0], self.position[1]))
