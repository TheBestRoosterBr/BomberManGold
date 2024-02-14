import pygame.image

import Level
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
        self.selected_level = 0
        self.last_selected_level = 0
        self.is_in_transition = False
        self.frames = 0
        self.transition_frames_counter = 0
        self.screen = screen
        self.offset_x = Configuration.get_config().screen_width/ 2 - self.sprite.get_width() / 2
        self.offset_y = Configuration.get_config().screen_height/ 2 - self.sprite.get_height() / 2
        self.is_running = True

    def load_levels(self):
        level1 = Level.Level1World1()
        level2 = Level.Level2World1()
        level3 = Level.Level3World1()
        self.levels.append(level1)
        self.levels.append(level2)
        self.levels.append(level3)
        return len(self.levels)

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

        if self.is_in_transition:
            if self.transition_frames_counter > Configuration.get_config().game_fps * 3:
                self.is_in_transition = False
            else:
                self.transition_frames_counter += 1

    def update(self):
        self.frames += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.is_running = False

                if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and not self.is_in_transition:
                    if self.selected_level + 1 < self.total_levels:
                        self.last_selected_level = self.selected_level
                        self.selected_level += 1
                        self.is_in_transition = True
                elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and not self.is_in_transition:
                    if self.selected_level - 1 >= 0:
                        self.last_selected_level = self.selected_level
                        self.selected_level -= 1
                        self.is_in_transition = True

        self.level_to_position()
        self.draw()

    def draw(self):

        self.screen.blit(self.sprite, (self.offset_x, self.offset_y))
        spr = self.foto_spr.subsurface(32 * self.foto_index, 0, 32, 32)
        self.screen.blit(spr, self.foto_position)
        pygame.display.update()

    def run_level(self):
        self.levels[self.selected_level - 1].run(self.screen)

    def main_loop(self):
        while self.is_running:
            self.update()
            self.draw()
        self.run_level()
