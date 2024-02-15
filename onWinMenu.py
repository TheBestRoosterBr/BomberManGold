from Configuration import Configuration
import pygame


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
        self.draw_ex = self.width / 2.5
        self.draw_ey = self.height / 1.5

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
            pygame.display.update()

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
            pygame.display.update()
