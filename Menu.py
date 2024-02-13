import pygame
from Game import Game
from Configuration import Configuration

class ImageButton:
    def __init__(self, x, y, image_path):
        self.rect = pygame.Rect(x, y, 21, 21)
        self.image = pygame.image.load(image_path)

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


class TelaResultado:
    def __init__(self, screen):
        config = Configuration.get_config()
        self.width = config.screen_width
        self.height = config.screen_height

        vitoria_background = pygame.image.load("./Assets/ganhou.jpg")
        self.background_vitoria = pygame.transform.scale(vitoria_background, (self.width, self.height))

        derrota_background = pygame.image.load("./Assets/perdeu.jpg")
        self.background_derrota = pygame.transform.scale(derrota_background, (self.width, self.height))


        # Cores
        self.white = (255, 255, 255)
        self.yellow = (255, 255, 0)
        self.hover_color = self.yellow  # hover amarelo

        # Fontes
        self.font_path = "./Fonts/nougat.ttf"
        self.font = pygame.font.Font(self.font_path, 40)

        # botões
        self.texts_vitoria = ["Tela Inicial", "Próximo nível"]
        self.texts_derrota = ["Tela Inicial", "Jogar novamente"]
        self.screen = screen
        self.is_running = True
        self.draw_ex = self.width / 2
        self.draw_ey = self.height / 2.5

    def is_hovered(self, rect):
        mouse_pos = pygame.mouse.get_pos()
        return rect.collidepoint(mouse_pos)

    def draw_text(self, text, x, y, color):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(bottomleft=(x, y))
        self.screen.blit(text_surface, text_rect)

    def draw_menu_screen(self, options, draw_x, draw_y, op):
        if op:  # Substitua pela sua condição de vitória
            self.screen.blit(self.background_vitoria, (0, 0))
        else:
            self.screen.blit(self.background_derrota, (0, 0))

        rectangles = []

        for i, text in enumerate(options):
            rect = self.font.render(text, True, self.white).get_rect(bottomleft=(draw_x, draw_y + i * 60))
            rectangles.append(rect)
            color = self.hover_color if self.is_hovered(rect) else self.white
            self.draw_text(text, draw_x, draw_y + i * 60, color)

        return rectangles

    def screen_vitoria(self):
        option = 0
        while self.is_running:
            rectangles = self.draw_menu_screen(self.texts_vitoria, self.draw_ex, self.draw_ey, True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for i in range(len(rectangles)):
                        if self.is_hovered(rectangles[i]):
                            if i == 0:
                                option = 0
                                self.is_running = False
                            elif i == 1:
                                # Lógica para "Próximo Nível"
                                pass

    def screen_derrota(self):
        option = 0
        while self.is_running:
            rectangles = self.draw_menu_screen(self.texts_derrota, self.draw_ex, self.draw_ey, False)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for i in range(len(rectangles)):
                        if self.is_hovered(rectangles[i]):
                            if i == 0:
                                option = 0
                                self.is_running = False
                            elif i == 1:
                                # Lógica para "Jogar Novamente"
                                pass



class MenuInicial:
    def __init__(self, screen):
        config = Configuration.get_config()
        self.width = config.screen_width
        self.height = config.screen_height
        original_background = pygame.image.load("Assets/background.jpg")
        self.background_image = pygame.transform.scale(original_background, (self.width, self.height))
        # Cores
        self.white = (255, 255, 255)
        self.yellow = (255, 255, 0)
        self.hover_color = self.yellow  # hover amarelo
        # Fontes
        self.font_path = "./Fonts/nougat.ttf"
        self.font = pygame.font.Font(self.font_path, 40)
        # botões
        self.texts = ["Jogar", "Opções", "Sair", ]
        self.screen = screen
        self.is_running = True
        self.draw_x = self.width/2
        self.draw_y = self.height/2.5

    def draw_text(self, text, x, y, color):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def draw_rounded_rectangle(self, surface, color, rect, radius, opacity, gradient_color, border_color, border_width, image_path):
        rect = pygame.Rect(rect)
        alpha_color = color[:3] + (int(opacity * 255),)

        shape_surf = pygame.Surface(rect.size, pygame.SRCALPHA)

        pygame.draw.rect(shape_surf, alpha_color, shape_surf.get_rect(), border_radius=radius)

        if gradient_color:
            gradient = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
            pygame.draw.rect(gradient, gradient_color[0], gradient.get_rect(), border_radius=radius)
            shape_surf.blit(gradient, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        if border_color and border_width > 0:
            pygame.draw.rect(shape_surf, border_color, shape_surf.get_rect(), border_radius=radius, width=border_width)

        if image_path:
            image = pygame.image.load(image_path)
            shape_surf.blit(image, ((rect.width - image.get_width()) // 2, (rect.height - image.get_height()) // 2))

        surface.blit(shape_surf, rect.topleft)

    def draw_text_second(self, text, position, color, font_size):
        text_surface = self.font_helvetica.render(text, True, color)
        self.screen.blit(text_surface, position)

    def draw_text_center(self, text, y, color, font_size):
        text_surface = self.font_helvetica.render(text, True, color)
        text_rect = text_surface.get_rect(center=(self.WIDTH//2, y))
        self.screen.blit(text_surface, text_rect)

    def rgb(self, hex_color):
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


    def draw_image(self, surface, image_path, max_dimensions, position):
        if image_path:
            image = pygame.image.load(image_path)

            image_width, image_height = image.get_size()

            max_width, max_height = max_dimensions
            aspect_ratio = image_width / image_height

            if image_width > max_width:
                new_width = max_width
                new_height = int(new_width / aspect_ratio)
            elif image_height > max_height:
                new_height = max_height
                new_width = int(new_height * aspect_ratio)
            else:
                new_width, new_height = image_width, image_height

            image = pygame.transform.scale(image, (new_width, new_height))

            x, y = position
            image_position = (x - new_width // 2, y - new_height // 2)

            surface.blit(image, image_position)

    def main_loop(self):
        option = 0
        while self.is_running:
            self.screen.blit(self.background_image, (0, 0))  # background

            rectangles = []
            for i, text in enumerate(self.texts):
                rect = self.font.render(text, True, self.white).get_rect(center=(self.draw_x, self.draw_y + i * 60))
                rectangles.append(rect)
                color = self.hover_color if self.is_hovered(rect) else self.white
                self.draw_text(text, self.draw_x, self.draw_y + i * 60, color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Verifica se algum botão foi clicado
                    pos = pygame.mouse.get_pos()
                    for i in range(len(rectangles)):
                        if self.is_hovered(rectangles[i]):
                            if i == 0:
                                option = 0
                                self.is_running = False
                            elif i == 2:
                                pygame.quit()

            pygame.display.flip()

        if option == 0:
            resultado = TelaResultado(self.screen)
            resultado.screen_derrota()
        elif option == 1:
            resultado = TelaResultado(self.screen)
            resultado.screen_derrota()

    def run_game(self):
        game = Game(self.screen)
        game.run()

    @staticmethod
    def is_hovered(rect):
        mouse_pos = pygame.mouse.get_pos()
        return rect.collidepoint(mouse_pos)

