import pygame
from Game import Game
from Configuration import Configuration


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
        self.font = pygame.font.Font(None, 45)
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
                            if i == 2:
                                pygame.quit()

            pygame.display.flip()
        if option == 0:
            self.run_game()

    def run_game(self):
        game = Game(self.screen)
        game.run()

    @staticmethod
    def is_hovered(rect):
        mouse_pos = pygame.mouse.get_pos()
        return rect.collidepoint(mouse_pos)

