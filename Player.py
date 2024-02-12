import pygame
import Stage
from Bomba import Bomba
from BlockStatus import BlockStatus
from Configuration import Configuration


class Player:
    def __init__(self):
        self.score = 0
        self.lives = 1
        self.Name = "BomberManFodase"
        pos = Stage.matrix_to_screen_pos(1, 1)
        self.position = [pos[0], pos[1]]
        self.power_ups = []
        self.sprite = pygame.image.load('Assets/player.png')
        self.frame_width = 16
        self.frame_height = 24
        self.frame_index = [0, 0]
        self.last_state = 0  # 0 for left, 1 for right, 2 for up, and 3 for down
        self.speed = 2
        self.max_bombs = 1
        self.active_bombs = 0
        self.bomb_power = 5
        self.bombs = []

    @staticmethod
    def check_collision(next_position, board, direction):
        matrix_pos = Stage.screen_pos_to_matrix_movimentation(next_position[0], next_position[1], direction)
        return board[int(matrix_pos[0])][int(matrix_pos[1])] == BlockStatus.CLEAR

    def move_left(self, frames, board):
        if self.check_collision((self.position[0] - self.speed, self.position[1]), board, (-1, 0)):
            self.position[0] -= self.speed

        self.frame_index[0] = 4 if frames % 3 == 0 else 5 if frames % 4 == 0 else self.frame_index[0]
        self.frame_index[1] = 0
        self.last_state = 0

    def move_right(self, frames, board):
        if self.check_collision((self.position[0] + self.speed, self.position[1]), board, (1, 0)):
            self.position[0] += self.speed

        self.frame_index[0] = 1 if frames % 3 == 0 else 2 if frames % 4 == 0 else self.frame_index[0]
        self.frame_index[1] = 1
        self.last_state = 1

    def move_up(self, frames, board):
        if self.check_collision((self.position[0], self.position[1] - self.speed), board, (0, -1)):
            self.position[1] -= self.speed

        self.frame_index[0] = 0 if frames % 3 == 0 else 2 if frames % 4 == 0 else self.frame_index[0]
        self.frame_index[1] = 0
        self.last_state = 2

    def move_down(self, frames, board):
        if self.check_collision((self.position[0], self.position[1] + self.speed), board, (0, 1)):
            self.position[1] += self.speed

        self.frame_index[0] = 3 if frames % 3 == 0 else 5 if frames % 4 == 0 else self.frame_index[0]
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
        if self.active_bombs < self.max_bombs:
            position = Stage.screen_pos_to_matrix(self.position[0], self.position[1])
            bomb = Bomba(self.bomb_power, position[0], position[1])
            self.bombs.append(bomb)
            self.active_bombs += 1

    def update(self, screen):
        # Create a copy of the list to iterate over
        bombs_copy = self.bombs[:]

        for bomb in bombs_copy:
            bomb.update(screen)
            if bomb.is_exploded:
                # Remove the bomb from the original list
                self.bombs.remove(bomb)
                self.active_bombs -= 1

        self.draw(screen)

    def draw(self, screen):
        frame = self.sprite.subsurface((self.frame_index[0] * self.frame_width, self.frame_index[1] * self.frame_height,
                                        self.frame_width, self.frame_height))
        frame = pygame.transform.scale(frame, Configuration.get_config().cell_size)
        screen.blit(frame, (self.position[0], self.position[1]))




