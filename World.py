import pygame.image

import Level
import TheEnd
from Configuration import Configuration


class World1:
    def __init__(self, screen):
        self.levels = []
        self.total_levels = self.load_levels() + 1  # start position
        self.sprite = pygame.image.load('Assets/World1Map.png')
        size = Configuration.get_config().map_size
        self.sprite = pygame.transform.scale(self.sprite, size)
        self.foto_spr = pygame.image.load('Assets/foto.png')
        self.foto_position = [0, 0]
        self.foto_index = Configuration.get_config().foto
        self.cadeado = pygame.image.load('Assets/cadeado.png')
        self.max_level = Configuration.get_config().level + 1
        self.selected_level = 0
        self.last_selected_level = 0
        self.frames = 0
        self.screen = screen
        self.offset_x = Configuration.get_config().screen_width / 2 - self.sprite.get_width() / 2
        self.offset_y = Configuration.get_config().screen_height / 2 - self.sprite.get_height() / 2
        self.is_running = True

    def load_levels(self):
        level1 = Level.Level1World1()
        level2 = Level.Level2World1()
        level3 = Level.Level3World1()
        level4 = Level.Level4World1()
        self.levels.append(level1)
        self.levels.append(level2)
        self.levels.append(level3)
        self.levels.append(level4)
        return len(self.levels)

    def positioned(self, index):
        pos = [0, 0]
        if index == 0:
            pos[0] = 84 + self.offset_x
            pos[1] = 148 + self.offset_y
        elif index == 1:
            pos[0] = 212 + self.offset_x
            pos[1] = 20 + self.offset_y
        elif index == 2:
            pos[0] = 468 + self.offset_x
            pos[1] = 20 + self.offset_y
        elif index == 3:
            pos[0] = 468 + self.offset_x
            pos[1] = 276 + self.offset_y
        elif index == 4:
            pos[0] = 700 + self.offset_x
            pos[1] = 400 + self.offset_y

        return pos

    def level_to_position(self):
        if self.selected_level == 0:
            self.foto_position[0] = 84 + self.offset_x
            self.foto_position[1] = 148 + self.offset_y
        if self.selected_level == 1:
            self.foto_position[0] = 212 + self.offset_x
            self.foto_position[1] = 20 + self.offset_y
        if self.selected_level == 2:
            self.foto_position[0] = 468 + self.offset_x
            self.foto_position[1] = 20 + self.offset_y
        if self.selected_level == 3:
            self.foto_position[0] = 468 + self.offset_x
            self.foto_position[1] = 276 + self.offset_y
        if self.selected_level == 4:
            self.foto_position[0] = 700 + self.offset_x
            self.foto_position[1] = 400 + self.offset_y

    def update(self):
        self.frames += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.is_running = False

                if event.key == pygame.K_d or event.key == pygame.K_RIGHT or event.key == pygame.K_w:
                    if self.selected_level + 1 < self.max_level:
                        self.selected_level += 1

                elif event.key == pygame.K_a or event.key == pygame.K_LEFT or event.key == pygame.K_s:
                    if self.selected_level - 1 >= 0:
                        self.selected_level -= 1

        self.level_to_position()
        self.draw()

    def draw(self):
        self.screen.blit(self.sprite, (self.offset_x, self.offset_y))
        spr = self.foto_spr.subsurface(32 * self.foto_index, 0, 32, 32)
        self.screen.blit(spr, self.foto_position)
        for i in range(self.max_level, self.total_levels):
            spr = pygame.transform.scale(self.cadeado, (64, 64))
            self.screen.blit(spr, self.positioned(i))
        pygame.display.update()

    def run_level(self):
        if self.selected_level == 0:
            self.is_running = True
            self.main_loop()
        result = self.levels[self.selected_level - 1].run(self.screen)
        if result:
            self.selected_level += 1
            if self.selected_level == len(self.levels) + 1:
                cr = TheEnd.Fim()
                cr.display_credits()
                self.selected_level = 0
            else:
                self.run_level()


    def main_loop(self):
        while self.is_running:
            self.update()
            self.draw()
        self.run_level()
