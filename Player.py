import random
import math

import pygame

import PowerUp
import Stage
from Bomba import Bomba
from BlockStatus import BlockStatus
from Configuration import Configuration


class Player:
    def __init__(self, x, y):
        self.score = 0
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
    def is_tile_passable(board, i, j, player):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        status = board[i][j]
        if status == BlockStatus.CLEAR:
            return True
        if BlockStatus.POWER_UP <= status <= BlockStatus.POWER_UP + 9:
            return True
        if status in (BlockStatus.CHAVE, BlockStatus.PORTAL_ABERTO, BlockStatus.PORTAL_FECHADO, BlockStatus.FIRE):
            return True
        if status == BlockStatus.BOMBA:
            config = Configuration.get_config()
            cell_size = config.cell_size[0]
            tile_rect = pygame.Rect(
                int(j * cell_size + config.offset_x),
                int(i * cell_size + config.offset_y),
                cell_size,
                cell_size
            )
            curr_rect = pygame.Rect(
                int(round(player.position[0])),
                int(round(player.position[1])),
                cell_size,
                cell_size
            )
            return curr_rect.colliderect(tile_rect)
        return False

    @staticmethod
    def can_move_to(pos, board, player):
        config = Configuration.get_config()
        cell_size = config.cell_size[0]
        offset_x = config.offset_x
        offset_y = config.offset_y

        px, py = pos
        px_off = px - offset_x
        py_off = py - offset_y

        min_j = int(math.floor(px_off / cell_size))
        max_j = int(math.floor((px_off + cell_size - 0.001) / cell_size))
        min_i = int(math.floor(py_off / cell_size))
        max_i = int(math.floor((py_off + cell_size - 0.001) / cell_size))

        for i in range(min_i, max_i + 1):
            for j in range(min_j, max_j + 1):
                if not Player.is_tile_passable(board, i, j, player):
                    return False
        return True

    @staticmethod
    def check_collision(next_position, board, direction, player):
        return Player.can_move_to(next_position, board, player)

    def dir_to_state(self, direction):
        x, y = direction
        if x == -1 and y == 0:
            return 0
        elif x == 1 and y == 0:
            return 1
        elif x == 0 and y == -1:
            return 2
        elif x == 0 and y == 1:
            return 3
        else:
            return None

    def move(self, direction, frames, board, check_caveira=True):
        inverted_direction = tuple(-x for x in direction)
        if check_caveira and self.caveira['enabled'] and self.caveira['type'] == 'inverter':
            self.move(inverted_direction, frames, board, check_caveira=False)
            return

        if self.caveira['enabled'] and self.caveira['type'] == 'speed_up':
            effective_speed = 20
        elif self.caveira['enabled'] and self.caveira['type'] == 'speed_down':
            effective_speed = 1
        else:
            effective_speed = self.speed

        dx, dy = direction
        config = Configuration.get_config()
        cell_size = config.cell_size[0]
        offset_x = config.offset_x
        offset_y = config.offset_y

        remaining = effective_speed
        while remaining > 0:
            step = min(remaining, 2)
            new_x = self.position[0] + dx * step
            new_y = self.position[1] + dy * step

            if Player.can_move_to((new_x, new_y), board, self):
                self.position[0] = new_x
                self.position[1] = new_y
                remaining -= step
            else:
                if step > 1 and Player.can_move_to((self.position[0] + dx, self.position[1] + dy), board, self):
                    self.position[0] += dx
                    self.position[1] += dy
                    remaining -= 1
                    continue

                max_slide = cell_size * 0.45
                slide_applied = False
                if dx != 0 and dy == 0:
                    target_row = int(round((self.position[1] - offset_y) / cell_size))
                    target_y = target_row * cell_size + offset_y
                    diff_y = target_y - self.position[1]
                    if 0 < abs(diff_y) <= max_slide:
                        target_col = int(round((self.position[0] - offset_x) / cell_size)) + dx
                        if Player.is_tile_passable(board, target_row, target_col, self):
                            step_y = math.copysign(min(step, abs(diff_y)), diff_y)
                            if Player.can_move_to((new_x, self.position[1] + step_y), board, self):
                                self.position[0] = new_x
                                self.position[1] += step_y
                                slide_applied = True
                                remaining -= step
                            elif Player.can_move_to((self.position[0], self.position[1] + step_y), board, self):
                                self.position[1] += step_y
                                slide_applied = True
                                remaining -= step
                elif dy != 0 and dx == 0:
                    target_col = int(round((self.position[0] - offset_x) / cell_size))
                    target_x = target_col * cell_size + offset_x
                    diff_x = target_x - self.position[0]
                    if 0 < abs(diff_x) <= max_slide:
                        target_row = int(round((self.position[1] - offset_y) / cell_size)) + dy
                        if Player.is_tile_passable(board, target_row, target_col, self):
                            step_x = math.copysign(min(step, abs(diff_x)), diff_x)
                            if Player.can_move_to((self.position[0] + step_x, new_y), board, self):
                                self.position[0] += step_x
                                self.position[1] = new_y
                                slide_applied = True
                                remaining -= step
                            elif Player.can_move_to((self.position[0] + step_x, self.position[1]), board, self):
                                self.position[0] += step_x
                                slide_applied = True
                                remaining -= step

                if not slide_applied:
                    break

        if frames % 12 == 0:
            self.frame_index[0] += 1
            self.frame_index[0] = self.frame_index[0] % 3 + (3 if (direction[0] == -1 or direction[1] == 1) else 0)

        self.frame_index[1] = 1 if (direction[0] + direction[1]) > 0 else 0
        self.last_state = self.dir_to_state(direction)

    def move_left(self, frames, board, check_caveira=True):
        self.move((-1, 0), frames, board, check_caveira)

    def move_right(self, frames, board, check_caveira=True):
        self.move((1, 0), frames, board, check_caveira)

    def move_up(self, frames, board, check_caveira=True):
        self.move((0, -1), frames, board, check_caveira)

    def move_down(self, frames, board, check_caveira=True):
        self.move((0, 1), frames, board, check_caveira)


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

        #pygame.draw.circle(screen, (255, 0, 0), (self.position[0], self.position[1]), 4)

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
