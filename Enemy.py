import pygame

from BlockStatus import BlockStatus
from Configuration import Configuration
import PathFinder
import Stage
from SangueAnimation import SangueAnimation


class Enemy:
    def __init__(self, health=100, damage=3, speed=1):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.frames = 0
        self.dead = False
        self.is_morrendo = False
        self.death_animation = None

    def update(self, screen, player_board_position):
        pass

    def draw(self, screen):
        pass


class Koopa(Enemy):
    def __init__(self, x, y):
        super().__init__()
        self.sprite = pygame.image.load('Assets\Koopa.png')
        self.index = 0
        self.position = [x, y]
        self.death_animation = None

    def update(self, screen, player_board_position):

        if Stage.stage.board[self.position[0]][self.position[1]] == BlockStatus.FIRE and not self.is_morrendo:
            self.is_morrendo = True
            self.death_animation = SangueAnimation(Stage.matrix_to_screen_pos(self.position[0], self.position[1]))

        if self.is_morrendo:
            if not self.dead:
                self.dead = self.death_animation.update(screen)
        else:
            self.frames += 1
            if self.frames % 100 == 0:
                self.index = 0 if self.index == 1 else 1
                pos = PathFinder.path_finder(player_board_position, self.position)
                self.position[0] += pos[0]
                self.position[1] += pos[1]
            self.draw(screen)

    def draw(self, screen):
        spr = self.sprite.subsurface(self.index * 16, 0, 16, 27)
        spr = pygame.transform.scale(spr, Configuration.get_config().cell_size)
        screen.blit(spr, Stage.matrix_to_screen_pos(self.position[0], self.position[1]))


class BillSpawner(Enemy):
    def __init__(self, x, y, is_left=False):
        super().__init__(health=20, damage=5, speed=1)
        sz = Configuration.get_config().cell_size
        self.sprite = pygame.transform.scale(pygame.image.load("Assets/billSpawner.png"), (sz[0], sz[1] * 2))
        self.pos = (x, y)
        self.is_left = is_left
        self.sprite_bill = pygame.transform.scale(pygame.image.load('Assets/bill.png'), sz)
        if self.is_left:
            self.sprite_bill = pygame.transform.scale(pygame.image.load("Assets/bill_left.png"), sz)
        self.is_atirando = True
        self.bill_init_pos = Stage.matrix_to_screen_pos(self.pos[0], self.pos[1])
        self.bill_pos = [self.bill_init_pos[0], self.bill_init_pos[1]]

    def update(self, screen, player_board_position):
        self.frames += 1
        if self.frames % (Configuration.get_config().game_fps * 5) == 0:
            if self.is_atirando:
                self.is_atirando = False
                self.bill_pos[0] = self.bill_init_pos[0]
                self.bill_pos[1] = self.bill_init_pos[1]
            else:
                self.is_atirando = True
        if self.is_atirando:
            self.bill_pos[0] += 3 if self.is_left else -3
        self.draw(screen)

    def draw(self, screen):
        if self.is_atirando:
            screen.blit(self.sprite_bill, self.bill_pos)
        screen.blit(self.sprite, Stage.matrix_to_screen_pos(self.pos[0], self.pos[1]))


class Fulor(Enemy):
    def __init__(self, x, y):
        super().__init__()
        self.sprite = pygame.image.load('Assets/florzinha.png')
        self.index = 0
        self.position = [x, y]
        self.death_animation = None

    def update(self, screen, player_board_position):

        if Stage.stage.board[self.position[0]][self.position[1]] == BlockStatus.FIRE and not self.is_morrendo:
            self.is_morrendo = True
            self.death_animation = SangueAnimation(Stage.matrix_to_screen_pos(self.position[0], self.position[1]))
        if self.is_morrendo:
            if not self.dead:
                self.dead = self.death_animation.update(screen)
        else:
            self.frames += 1
            if self.frames % 5 == 0:
                self.index += 1
                if self.index > 3:
                    self.index = 0

            self.draw(screen)

    def draw(self, screen):
        spr = self.sprite.subsurface(self.index * 18, 0, 18, 23)
        spr = pygame.transform.scale(spr, Configuration.get_config().cell_size)
        screen.blit(spr, Stage.matrix_to_screen_pos(self.position[0], self.position[1]))


class Muxegu(Enemy):
    def __init__(self, x, y):
        super().__init__()
        self.sprite = pygame.image.load('Assets/Muxegu.png')
        self.size = [31, 34]
        self.index = [0, 0]
        pos = Stage.matrix_to_screen_pos(x, y)
        self.death_animation = SangueAnimation(pos)
        self.position = [pos[0], pos[1]]

    def move_left(self):
        if self.frames % 10 == 0:
            self.index[0] += 1
            if self.index[0] > 3:
                self.index[0] = 0

        self.position[0] -= 1
        self.index[1] = 3

    def move_right(self):
        if self.frames % 10 == 0:
            self.index[0] += 1
            if self.index[0] > 3:
                self.index[0] = 0
        self.position[0] += 1
        self.index[1] = 2

    def move_up(self):
        if self.frames % 10 == 0:
            self.index[0] += 1
            if self.index[0] > 3:
                self.index[0] = 0

        self.position[1] -= 1
        self.index[1] = 1

    def move_down(self):
        if self.frames % 10 == 0:
            self.index[0] += 1
            if self.index[0] > 3:
                self.index[0] = 0

        self.position[1] += 1
        self.index[1] = 0

    def update(self, screen, player_board_position):

        my_pos = Stage.screen_pos_to_matrix(self.position[0], self.position[1])
        pos = PathFinder.path_finder_without_block(player_board_position, my_pos)
        my_pos = Stage.screen_pos_to_matrix_movimentation(self.position[0], self.position[1], None, pos)

        if Stage.stage.board[my_pos[0]][my_pos[1]] == BlockStatus.FIRE and not self.is_morrendo:
            self.is_morrendo = True
            self.death_animation = SangueAnimation((self.position[0], self.position[1]))
        if self.is_morrendo:
            if not self.dead:
                self.dead = self.death_animation.update(screen)

        else:
            self.frames += 1
            if self.frames % 2 == 0:
                if pos == (1, 0):
                    self.move_down()
                elif pos == (-1, 0):
                    self.move_up()
                elif pos == (0, 1):
                    self.move_right()
                elif pos == (0, -1):
                    self.move_left()
            self.draw(screen)

    def draw(self, screen):
        spr = self.sprite.subsurface(self.index[0] * self.size[0], self.index[1] * self.size[1],
                                     self.size[0], self.size[1])
        spr = pygame.transform.scale(spr, Configuration.get_config().cell_size)
        screen.blit(spr, self.position)


class MuxeguSpawner(Enemy):
    def __init__(self, x, y):
        super().__init__()
        self.sprite = pygame.image.load('Assets/muxeguSpawner.png')
        self.index = 0
        self.position = [x, y]
        self.muxegus = []
        self.creating = True
        self.creatingFrames = 0

    def update(self, screen, player_board_position):
        self.frames += 1
        if self.frames % Configuration.get_config().game_fps * 10 == 0:
            self.creating = True

        if self.creating:
            self.creatingFrames += 1
            if self.creatingFrames % Configuration.get_config().game_fps == 0:
                self.muxegus.append(Muxegu(self.position[0], self.position[1]))
            if self.creatingFrames > Configuration.get_config().game_fps * 4:
                self.creating = False

        for i in range(len(self.muxegus)):
            self.muxegus[i].update(screen, player_board_position)
        self.draw(screen)

    def draw(self, screen):

        spr = pygame.transform.scale(self.sprite, Configuration.get_config().cell_size)
        screen.blit(spr, Stage.matrix_to_screen_pos(self.position[0], self.position[1]))


class Ghost(Enemy):
    def __init__(self, x, y):
        super().__init__()
        self.sprite = pygame.image.load('Assets/ghost.png')
        self.size = [16, 16]
        self.index = [0, 0]
        pos = Stage.matrix_to_screen_pos(x, y)

        self.position = [pos[0], pos[1]]

    def move_left(self):
        if self.frames % 10 == 0:
            self.index[0] += 1
            if self.index[0] > 2:
                self.index[0] = 0

        self.position[0] -= 1
        self.index[1] = 0

    def move_right(self):
        if self.frames % 10 == 0:
            self.index[0] += 1
            if self.index[0] > 2:
                self.index[0] = 0
        self.position[0] += 1
        self.index[1] = 1

    def move_up(self):
        if self.frames % 10 == 0:
            self.index[0] += 1
            if self.index[0] > 2:
                self.index[0] = 0

        self.position[1] -= 1
        self.index[1] = 2

    def move_down(self):
        if self.frames % 10 == 0:
            self.index[0] += 1
            if self.index[0] > 2:
                self.index[0] = 0

        self.position[1] += 1
        self.index[1] = 3

    def update(self, screen, player_board_position):

        my_pos = Stage.screen_pos_to_matrix(self.position[0], self.position[1])
        pos = PathFinder.path_finder_without_block(player_board_position, my_pos)
        my_pos = Stage.screen_pos_to_matrix_movimentation(self.position[0], self.position[1], None, pos)

        if Stage.stage.board[my_pos[0]][my_pos[1]] == BlockStatus.FIRE and not self.is_morrendo:
            self.is_morrendo = True
            self.death_animation = SangueAnimation((self.position[0], self.position[1]))


        if self.is_morrendo:
            if not self.dead:
                self.dead = self.death_animation.update(screen)
        else:
            self.frames += 1
            if self.frames % 2 == 0:
                #my_pos = Stage.screen_pos_to_matrix(self.position[0], self.position[1])
                pos = PathFinder.path_finder_without_block(player_board_position, my_pos)
                if pos == (1, 0):
                    self.move_down()
                elif pos == (-1, 0):
                    self.move_up()
                elif pos == (0, 1):
                    self.move_right()
                elif pos == (0, -1):
                    self.move_left()
            self.draw(screen)

    def draw(self, screen):
        spr = self.sprite.subsurface(self.index[0] * self.size[0], self.index[1] * self.size[1],
                                     self.size[0], self.size[1])
        spr = pygame.transform.scale(spr, Configuration.get_config().cell_size)
        screen.blit(spr, self.position)


class GhostSpawner(Enemy):
    def __init__(self, x, y):
        super().__init__()
        self.sprite = pygame.image.load('Assets/ghostSpawner.png')
        self.index = 0
        self.position = [x, y]
        self.ghosts = []
        self.creating = True
        self.creatingFrames = 0

    def update(self, screen, player_board_position):
        self.frames += 1
        if self.frames % Configuration.get_config().game_fps * 10 == 0:
            self.creating = True

        if self.creating:
            self.creatingFrames += 1
            if self.creatingFrames % Configuration.get_config().game_fps == 0:
                self.ghosts.append(Ghost(self.position[0], self.position[1]))
            if self.creatingFrames > Configuration.get_config().game_fps * 4:
                self.creating = False

        for i in range(len(self.ghosts)):
            self.ghosts[i].update(screen, player_board_position)
        self.draw(screen)

    def draw(self, screen):
        spr = pygame.transform.scale(self.sprite, Configuration.get_config().cell_size)
        screen.blit(spr, Stage.matrix_to_screen_pos(self.position[0], self.position[1]))


class Camaleao(Enemy):
    def __init__(self, x, y):
        super().__init__()
        self.sprite = pygame.image.load('Assets/CamaleaoDeFogo.png')
        self.index = 0
        self.size = (16, 56)
        self.position = [x, y]
        self.recharge_time = Configuration.get_config().game_fps * 7
        self.recharge_counter = 0
        self.on_fire = False
        self.death_animation = None

    def update(self, screen, player_board_position):

        if Stage.stage.board[self.position[0] + 3][self.position[1]] == BlockStatus.FIRE and not self.is_morrendo:
            self.is_morrendo = True
            self.death_animation = SangueAnimation(Stage.matrix_to_screen_pos(self.position[0] + 3, self.position[1]))

        if self.is_morrendo:
            if not self.dead:
                self.dead = self.death_animation.update(screen)
        else:
            self.frames += 1
            self.recharge_counter += 1
            if self.recharge_counter >= self.recharge_time:
                self.recharge_counter = 0
                self.on_fire = True

            if self.on_fire:
                if self.frames % 10 == 0:
                    self.index += 1
                    if self.index > 4:
                        self.index = 0

            self.draw(screen)

    def draw(self, screen):
        spr = self.sprite.subsurface(0, self.index * self.size[1], self.size[0], self.size[1])
        sz = Configuration.get_config().cell_size
        scale = self.size[1] / 16
        scale_tupla = (sz[0], sz[1] * scale)
        spr = pygame.transform.scale(spr, scale_tupla)
        screen.blit(spr, Stage.matrix_to_screen_pos(self.position[0], self.position[1]))
