import pygame
import sys

from Configuration import Configuration


class Fim:
    def __init__(self):
        pygame.init()
        self.WIDTH = Configuration.get_config().screen_width
        self.HEIGHT = Configuration.get_config().screen_height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Créditos")

        # Fonte
        self.font_path = "Fonts/nougat.ttf"
        self.font = pygame.font.Font(self.font_path, 25)

        # Carregar créditos do arquivo
        self.load_credits()

        # Carregar imagem de fundo
        self.background_image = pygame.image.load("./Assets/fim.jpg")

    def load_credits(self):
        with open("./Fonts/agradecimentos.txt", "r", encoding="utf-8") as file:
            self.credits_text = file.readlines()


    def display_credits(self):
        clock = pygame.time.Clock()
        y_position = self.HEIGHT

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    running = False

            self.screen.blit(self.background_image, (0, 0))  # Desenha o fundo
            y_position -= 1  # Ajuste a velocidade de subida alterando este valor

            for i in range(len(self.credits_text)):
                text_surface = self.font.render(self.credits_text[i].strip(), True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(self.WIDTH // 3.2, y_position + i * 24))
                self.screen.blit(text_surface, text_rect)

                if y_position < -len(self.credits_text) * 24:  # Reinicia no topo quando atinge a parte superior
                    y_position = self.HEIGHT

            pygame.display.flip()
            clock.tick(60)  # 60 FPS

