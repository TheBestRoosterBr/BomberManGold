import pygame
from enum import IntEnum

from pygame import mouse

from Configuration import Configuration


class Controller(IntEnum):
    PERFIL = 0
    AUDIO = 1
    CONTROLES = 2

class ImageButton:
    def __init__(self, x, y, wid, hei, image_path, scale=None):
        self.scale = scale
        self.rect = pygame.Rect(x, y, wid, hei)
        self.image = pygame.transform.scale(pygame.image.load(image_path), (self.rect.width, self.rect.height))
        if self.scale is not None:
            self.rect = pygame.Rect(x, y, self.scale[0], self.scale[1])
            self.image = pygame.transform.scale(self.image, self.scale)

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def is_clicked(self, pos):
        hovered = self.rect.collidepoint(pos)
        if hovered:
            if self.scale is not None:
                self.image = pygame.transform.scale(self.image, (self.scale[0] + 10, self.scale[1] + 10))
            else:
                self.image = pygame.transform.scale(self.image, (self.rect.width + 10, self.rect.height + 10))
        else:
            if self.scale is not None:
                self.image = pygame.transform.scale(self.image, self.scale)
            else:
                self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

        return hovered


class Perfil:
    def __init__(self):
        self.name = "BomberMan"
        self.index_foto = 0
        self.foto = pygame.image.load("Assets/foto.png")
        self.font_path = "./Fonts/nougat.ttf"
        self.font = pygame.font.Font(self.font_path, 40)
        self.foto_pos = [963, 69]
        self.button1 = ImageButton(944, 330, 21, 21, "./assets/arrow_left.png")
        self.button2 = ImageButton(1200, 330, 21, 21, "./assets/arrow_right.png")
        self.Confirmar = ImageButton(944, 540, 64, 16, "Assets/Button.png", (256, 64))
        self.Voltar = ImageButton(404, 540, 64, 16, "Assets/Button.png", (256, 64))
        # Cores padrão
        self.default_color = (255, 255, 255)
        self.hovered_color = (0, 120, 255)
        self.load()

    def draw_text(self, screen, text, rect, color):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x = rect.x + (rect.width / 2) - text_rect.width / 2
        text_rect.y = rect.y + (rect.height / 2) - text_rect.height / 2
        screen.blit(text_surface, text_rect)

    def save(self):
        players = ['', 'Preto', 'Vermelho', 'Azul']
        Configuration.get_config().player = players[self.index_foto]
        Configuration.get_config().save_in_file()


    def load(self):
        players = ['', 'Preto', 'Vermelho', 'Azul']
        self.index_foto = players.index(Configuration.get_config().player)


    def update(self, screen, option):

        pos = mouse.get_pos()

        perfil_clicked = option.perfil_button.is_clicked(pos)
        audio_clicked = option.audio_button.is_clicked(pos)
        controle_clicked = option.control_button.is_clicked(pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.button1.is_clicked(pos):
                    self.index_foto -= 1
                    if self.index_foto < 0:
                        self.index_foto = 3
                elif self.button2.is_clicked(pos):
                    self.index_foto += 1
                    if self.index_foto > 3:
                        self.index_foto = 0
                elif self.Confirmar.is_clicked(pos):
                    self.save()
                    return False
                elif self.Voltar.is_clicked(pos):
                    return False
                elif perfil_clicked:
                    option.controller = Controller.PERFIL
                elif audio_clicked:
                    option.controller = Controller.AUDIO
                elif controle_clicked:
                    option.controller = Controller.CONTROLES

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_LEFT:
                    self.index_foto -= 1
                    if self.index_foto < 0:
                        self.index_foto = 4
                elif event.key == pygame.K_RIGHT:
                    self.index_foto += 1
                    if self.index_foto > 4:
                        self.index_foto = 0

        pos = pygame.mouse.get_pos()
        self.Confirmar.is_clicked(pos)
        self.Voltar.is_clicked(pos)
        self.button1.draw(screen)
        self.button2.draw(screen)
        self.Voltar.draw(screen)
        self.Confirmar.draw(screen)
        self.draw_text(screen, "Confirmar", self.Confirmar.rect, self.default_color)
        self.draw_text(screen, "Voltar", self.Voltar.rect, self.default_color)

        spr_foto = pygame.transform.scale(self.foto.subsurface(self.index_foto * 32, 0, 32, 32), (256, 256))
        screen.blit(spr_foto, self.foto_pos)
        return True


class Controle:
    def __init__(self):

        self.font_path = "./Fonts/nougat.ttf"
        self.font = pygame.font.Font(self.font_path, 40)
        self.foto_pos = [360, 360]

        self.Confirmar = ImageButton(944, 540, 64, 16, "Assets/Button.png", (256, 64))
        self.Voltar = ImageButton(404, 540, 64, 16, "Assets/Button.png", (256, 64))
        # Cores padrão
        self.default_color = (255, 255, 255)
        self.hovered_color = (0, 120, 255)

    def draw_text(self, screen, text, rect, color):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x = rect.x + (rect.width / 2) - text_rect.width / 2
        text_rect.y = rect.y + (rect.height / 2) - text_rect.height / 2
        screen.blit(text_surface, text_rect)

    def update(self, screen, option):
        pos = pygame.mouse.get_pos()

        confirmar = self.Confirmar.is_clicked(pos)
        voltar = self.Voltar.is_clicked(pos)

        perfil_clicked = option.perfil_button.is_clicked(pos)
        audio_clicked = option.audio_button.is_clicked(pos)
        controle_clicked = option.control_button.is_clicked(pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if confirmar:
                    return False
                elif voltar:
                    return False
                elif perfil_clicked:
                    option.controller = Controller.PERFIL
                elif audio_clicked:
                    option.controller = Controller.AUDIO
                elif controle_clicked:
                    option.controller = Controller.CONTROLES

        self.Voltar.draw(screen)
        self.Confirmar.draw(screen)
        self.draw_text(screen, "Confirmar", self.Confirmar.rect, self.default_color)
        self.draw_text(screen, "Voltar", self.Voltar.rect, self.default_color)

        return True


class Audio:
    def __init__(self):
        self.enabled = Configuration.get_config().audio
        self.spr_path = {
            True: 'speaker',
            False: 'mute'
        }
        size = (300, 200)
        pos_x = Configuration.get_config().screen_width / 2 - size[0] / 2 + 140
        pos_y = Configuration.get_config().screen_height / 2 - size[1] / 2
        self.rect = pygame.Rect(pos_x, pos_y, size[0], size[1])

        self.button = ImageButton(pos_x + 20, pos_y + 100 - 20 + 2, 40, 40, 'Assets/' + self.spr_path[self.enabled] + '.png')
        self.font_path = "./Fonts/nougat.ttf"
        self.font = pygame.font.Font(self.font_path, 40)

        self.load_volume()

        self.Confirmar = ImageButton(944, 540, 64, 16, "Assets/Button.png", (256, 64))
        self.Voltar = ImageButton(404, 540, 64, 16, "Assets/Button.png", (256, 64))
        # Cores padrão
        self.default_color = (255, 255, 255)
        self.hovered_color = (0, 120, 255)

    @staticmethod
    def circle_point_collision(cx, cy, r, px, py):
        # Calculate the distance between the circle's center and the point
        distance = ((px - cx) ** 2 + (py - cy) ** 2) ** 0.5

        # Check if the distance is less than or equal to the circle's radius
        return distance <= r


    def save_volume(self, volume):
        Configuration.get_config().volume = volume
        Configuration.get_config().save_in_file()
        self.load_volume()

    def load_volume(self):
        size = (300, 200)
        pos_x = Configuration.get_config().screen_width / 2 - size[0] / 2 + 140
        pos_y = Configuration.get_config().screen_height / 2 - size[1] / 2

        self.bar = pygame.Rect(pos_x + 70, pos_y + 100, 200, 4)
        self.volume_bar = pygame.Rect(pos_x + 70, pos_y + 100, 200 * Configuration.get_config().volume, 4)
        self.radius_bolinha = 8
        self.posicao_bolinha = (self.volume_bar.x + self.volume_bar.width, self.volume_bar.y + self.radius_bolinha - self.volume_bar.height - 2)

        if Configuration.get_config().volume <= 0.05:
            Configuration.get_config().audio = False
        else:
            Configuration.get_config().audio = True

        self.button = ImageButton(pos_x + 20, pos_y + 100 - 20 + 2, 40, 40,
                                  'Assets/' + self.spr_path[Configuration.get_config().audio] + '.png')


    def draw_text(self, screen, text, rect, color):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x = rect.x + (rect.width / 2) - text_rect.width / 2
        text_rect.y = rect.y + (rect.height / 2) - text_rect.height / 2
        screen.blit(text_surface, text_rect)

    def update(self, screen, option):
        pos = pygame.mouse.get_pos()

        confirmar = self.Confirmar.is_clicked(pos)
        voltar = self.Voltar.is_clicked(pos)

        perfil_clicked = option.perfil_button.is_clicked(pos)
        audio_clicked = option.audio_button.is_clicked(pos)
        controle_clicked = option.control_button.is_clicked(pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if confirmar:
                    return False
                elif voltar:
                    return False
                elif perfil_clicked:
                    option.controller = Controller.PERFIL
                elif audio_clicked:
                    option.controller = Controller.AUDIO
                elif controle_clicked:
                    option.controller = Controller.CONTROLES
                elif self.bar.collidepoint(*pos):
                    new_volume = (pos[0] - self.bar.x) / 200
                    self.save_volume(new_volume)
                    pass
        pygame.draw.rect(screen, color=(125, 125, 125), rect=self.rect)
        self.button.draw(screen)
        pygame.draw.rect(screen, color=(100, 100, 100), rect=self.bar)
        pygame.draw.rect(screen, color=(0, 0, 90), rect=self.volume_bar)
        pygame.draw.circle(screen, (0, 0, 90), self.posicao_bolinha, self.radius_bolinha)
        self.Voltar.draw(screen)
        self.Confirmar.draw(screen)

        self.draw_text(screen, "Confirmar", self.Confirmar.rect, self.default_color)
        self.draw_text(screen, "Voltar", self.Voltar.rect, self.default_color)

        return True


class Options:
    def __init__(self):
        self.name = ""
        self.controller = Controller.PERFIL
        self.spr = pygame.image.load("Assets/base.png")
        self.font_path = "./Fonts/nougat.ttf"
        self.font = pygame.font.Font(self.font_path, 40)
        self.is_running = True
        self.perfil = Perfil()
        self.audio = Audio()
        self.controle = Controle()
        self.controller_pos = (41, 26)
        self.rectangle_controller = pygame.Rect(self.controller_pos[0], self.controller_pos[1], 280, 650)
        # Cores padrão
        self.default_color = (255, 255, 255)
        self.hovered_color = (0, 120, 255)
        self.pos_control_but = (72, 72)
        self.space_buttons = 96
        self.perfil_button = ImageButton(self.pos_control_but[0], self.pos_control_but[1], 32, 16,
                                         "Assets/button_small.png", (200, 64))
        self.audio_button = ImageButton(self.pos_control_but[0], self.pos_control_but[1] + self.space_buttons,
                                        32, 16, "Assets/button_small.png", (200, 64))
        self.control_button = ImageButton(self.pos_control_but[0], self.pos_control_but[1] + self.space_buttons * 2,
                                        32, 16, "Assets/button_small.png", (200, 64))

    def draw_text(self, screen, text, rect, color):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x = rect.x + (rect.width / 2) - text_rect.width / 2
        text_rect.y = rect.y + (rect.height / 2) - text_rect.height / 2
        screen.blit(text_surface, text_rect)

    def main_loop(self, screen):

        while self.is_running:
            screen.blit(self.spr, (0, 0))
            pygame.draw.rect(screen, (125, 125, 125), self.rectangle_controller)

            self.perfil_button.draw(screen)
            self.audio_button.draw(screen)
            self.control_button.draw(screen)

            self.draw_text(screen, "Perfil", self.perfil_button.rect, self.hovered_color)
            self.draw_text(screen, "Audio", self.audio_button.rect, self.hovered_color)
            self.draw_text(screen, "Controles", self.control_button.rect, self.hovered_color)

            if self.controller == Controller.PERFIL:
                self.is_running = self.perfil.update(screen, self)
                if not self.is_running:
                    break
            if self.controller == Controller.AUDIO:
                self.is_running = self.audio.update(screen, self)
                if not self.is_running:
                    break
            if self.controller == Controller.CONTROLES:
                self.is_running = self.controle.update(screen, self)
                if not self.is_running:
                    break

            pygame.display.update()

