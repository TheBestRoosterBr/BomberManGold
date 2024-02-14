import pygame
import Stage
from BlockStatus import BlockStatus
from Configuration import Configuration


class Bomba:
    def __init__(self, bomb_power, x, y, type):
        self.bomb_types = {
            'espinho': {'sprite': 'BombaEspinho', 'rect': 3, 'enable': self.enable_explosion},
            'relogio': {'sprite': 'BombaRelogio', 'rect': 4, 'explode': False, 'enable': self.enable_explosion_relogio},
            'bombaP': {'sprite': 'BombaP', 'rect': 3, 'enable': self.enable_explosion},
            'normal': {'sprite': 'bomba', 'rect': 3, 'enable': self.enable_explosion}
        }

        self.power = bomb_power
        self.timer = 0
        self.max_timer = Configuration.get_config().game_fps * 3 # 3 Seconds
        self.position = (x, y)

        self.current_type = type
        self.sprite = None
        self.load_sprite(self.current_type)
        self.explosion_sprite = pygame.image.load("Assets/explosao.png")
        self.explosion_index = [0, 0]
        self.explosion_timer = 0
        self.frames = 0
        self.frame_size = 16
        self.frame_index = 0
        self.is_exploded = False

        Stage.stage.board[x][y] = BlockStatus.BOMBA

    def load_sprite(self, bomb_type):
        self.sprite = pygame.image.load("Assets/" + self.bomb_types[bomb_type]['sprite'] + ".png")

    @staticmethod
    def enable_explosion_relogio(bomba):
        bomba.bomb_types['relogio']['explode'] = True

    @staticmethod
    def enable_explosion(bomba):
        bomba.frames = bomba.max_timer + 1

    def update(self, screen):
        self.frames += 1
        if self.current_type == 'relogio' and self.bomb_types[self.current_type]['explode']:
            self.explode(screen)
        elif self.current_type != 'relogio' and self.frames > self.max_timer:
            self.explode(screen)
        else:
            if self.frames % (Configuration.get_config().game_fps / 5) == 0:
                self.frame_index += 1
                if self.frame_index >= self.bomb_types[self.current_type]['rect']:
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
        Stage.stage.board[self.position[0]][self.position[1]] = BlockStatus.FIRE
        # Up
        if self.current_type == 'bombaP':
            power = 17
        else:
            power = self.power

        for i in range(1, power):
            position = self.position[0] - i
            next_block = Stage.stage.board[position][self.position[1]]

            if next_block == BlockStatus.WALL or next_block & 0b1000000 == 0b1000000:
                break
            elif next_block == BlockStatus.BOMBA:
                for bomba in Stage.stage.bombas:
                    if bomba.position == (position, self.position[1]):
                        bomba.bomb_types[bomba.current_type]['enable'](bomba)
            elif next_block == BlockStatus.DESTRUCTIBLE_WALL or next_block == BlockStatus.LUCKY_BLOCK:
                Stage.stage.board[position][self.position[1]] = BlockStatus.DESTROY_BLOCK
                if self.current_type != 'espinho':
                    break
            elif 5 <= next_block <= 14:
                for power_up in Stage.stage.power_ups:
                    if power_up.position == (position, self.position[1]):
                        Stage.stage.board[power_up.position[0]][power_up.position[1]] = BlockStatus.DESTROY_POWER_UP
                        Stage.stage.power_ups.remove(power_up)
                        break
                if self.current_type != 'espinho':
                    break
            elif next_block == BlockStatus.CLEAR or next_block == BlockStatus.FIRE:
                Stage.stage.board[position][self.position[1]] = BlockStatus.FIRE
                index = 2 if i == power - 1 else 1
                spr = self.explosion_sprite.subsurface((index * self.frame_size, self.explosion_index[1] * self.frame_size,
                                                        self.frame_size, self.frame_size))
                rotated_spr = pygame.transform.rotate(spr, 90)
                rotated_spr = pygame.transform.scale(rotated_spr, Configuration.get_config().cell_size)
                screen.blit(rotated_spr, Stage.matrix_to_screen_pos(position, self.position[1]))

        # Down
        for i in range(1, power):
            position = self.position[0] + i
            next_block = Stage.stage.board[position][self.position[1]]

            if next_block == BlockStatus.WALL or next_block & 0b1000000 == 0b1000000:
                break
            elif next_block == BlockStatus.BOMBA:
                for bomba in Stage.stage.bombas:
                    if bomba.position == (position, self.position[1]):
                        bomba.bomb_types[bomba.current_type]['enable'](bomba)
            elif next_block == BlockStatus.DESTRUCTIBLE_WALL or next_block == BlockStatus.LUCKY_BLOCK:
                Stage.stage.board[position][self.position[1]] = BlockStatus.DESTROY_BLOCK
                if self.current_type != 'espinho':
                    break
            elif 5 <= next_block <= 14:
                for power_up in Stage.stage.power_ups:
                    if power_up.position == (position, self.position[1]):
                        Stage.stage.board[power_up.position[0]][power_up.position[1]] = BlockStatus.DESTROY_POWER_UP
                        Stage.stage.power_ups.remove(power_up)
                        break
                if self.current_type != 'espinho':
                    break
            elif next_block == BlockStatus.CLEAR or next_block == BlockStatus.FIRE:
                Stage.stage.board[position][self.position[1]] = BlockStatus.FIRE
                index = 2 if i == power - 1 else 1
                spr = self.explosion_sprite.subsurface((index * self.frame_size, self.explosion_index[1] * self.frame_size,
                                                        self.frame_size, self.frame_size))
                rotated_spr = pygame.transform.rotate(spr, -90)
                rotated_spr = pygame.transform.scale(rotated_spr, Configuration.get_config().cell_size)
                screen.blit(rotated_spr, Stage.matrix_to_screen_pos(position, self.position[1]))

        # Right
        for i in range(1, power):
            position = self.position[1] - i
            next_block = Stage.stage.board[self.position[0]][position]

            if next_block == BlockStatus.WALL or next_block & 0b1000000 == 0b1000000:
                break
            elif next_block == BlockStatus.BOMBA:
                for bomba in Stage.stage.bombas:
                    if bomba.position == (self.position[0], position):
                        bomba.bomb_types[bomba.current_type]['enable'](bomba)
            elif 5 <= next_block <= 14:
                for power_up in Stage.stage.power_ups:
                    if power_up.position == (self.position[0], position):
                        Stage.stage.board[power_up.position[0]][power_up.position[1]] = BlockStatus.DESTROY_POWER_UP
                        Stage.stage.power_ups.remove(power_up)
                        break
                if self.current_type != 'espinho':
                    break
            elif next_block == BlockStatus.DESTRUCTIBLE_WALL or next_block == BlockStatus.LUCKY_BLOCK:
                Stage.stage.board[self.position[0]][position] = BlockStatus.DESTROY_BLOCK
                if self.current_type != 'espinho':
                    break
            elif next_block == BlockStatus.CLEAR or next_block == BlockStatus.FIRE:
                Stage.stage.board[self.position[0]][position] = BlockStatus.FIRE
                position = self.position[1] - i
                index = 2 if i == power - 1 else 1
                spr = self.explosion_sprite.subsurface((index * self.frame_size, self.explosion_index[1] * self.frame_size,
                                                        self.frame_size, self.frame_size))
                if index == 2:
                    spr = pygame.transform.rotate(spr, 180)
                spr = pygame.transform.scale(spr, Configuration.get_config().cell_size)
                screen.blit(spr, Stage.matrix_to_screen_pos(self.position[0], position))

        # Left
        for i in range(1, power):
            position = self.position[1] + i
            next_block = Stage.stage.board[self.position[0]][position]

            if next_block == BlockStatus.WALL or next_block & 0b1000000 == 0b1000000:
                break
            elif next_block == BlockStatus.BOMBA:
                for bomba in Stage.stage.bombas:
                    if bomba.position == (self.position[0], position):
                        bomba.bomb_types[bomba.current_type]['enable'](bomba)
            elif next_block == BlockStatus.DESTRUCTIBLE_WALL or next_block == BlockStatus.LUCKY_BLOCK:
                Stage.stage.board[self.position[0]][position] = BlockStatus.DESTROY_BLOCK

                if self.current_type != 'espinho':
                    break
            elif 5 <= next_block <= 14:
                for power_up in Stage.stage.power_ups:
                    if power_up.position == (self.position[0], position):
                        Stage.stage.board[power_up.position[0]][power_up.position[1]] = BlockStatus.DESTROY_POWER_UP
                        Stage.stage.power_ups.remove(power_up)
                        break
                if self.current_type != 'espinho':
                    break

            elif next_block == BlockStatus.CLEAR or next_block == BlockStatus.FIRE:
                Stage.stage.board[self.position[0]][position] = BlockStatus.FIRE
                position = self.position[1] + i
                index = 2 if i == power - 1 else 1
                spr = self.explosion_sprite.subsurface((index * self.frame_size, self.explosion_index[1] * self.frame_size,
                                                        self.frame_size, self.frame_size))

                if index == 1:
                    spr = pygame.transform.rotate(spr, 180)
                spr = pygame.transform.scale(spr, Configuration.get_config().cell_size)
                screen.blit(spr, Stage.matrix_to_screen_pos(self.position[0], position))

    def draw(self, screen):
        frame = self.sprite.subsurface((self.frame_index * self.frame_size, 0, self.frame_size, self.frame_size))
        frame = pygame.transform.scale(frame, Configuration.get_config().cell_size)
        screen.blit(frame, Stage.matrix_to_screen_pos(self.position[0], self.position[1]))

