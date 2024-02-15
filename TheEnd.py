import pygame
import sys

class Fim:
    def __init__(self, width, height):
        pygame.init()
        self.WIDTH = width
        self.HEIGHT = height
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
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.background_image, (0, 0))  # Desenha o fundo
            y_position -= 1  # Ajuste a velocidade de subida alterando este valor

            for i in range(len(self.credits_text)):
                text_surface = self.font.render(self.credits_text[i].strip(), True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(self.WIDTH // 2, y_position + i * 20))
                self.screen.blit(text_surface, text_rect)

                if y_position < -len(self.credits_text) * 20:  # Reinicia no topo quando atinge a parte superior
                    y_position = self.HEIGHT

            pygame.display.flip()
            clock.tick(60)  # 60 FPS

        pygame.quit()
        sys.exit()

# Certifique-se de ter instalado o Pygame usando: pip install pygame

# Tente iniciar o Pygame antes de criar a instância da classe Credits
try:
    pygame.init()
except pygame.error:
    print("Erro ao iniciar o Pygame. Verifique a instalação.")
    sys.exit()

# Crie uma instância da classe Credits
credits = Fim(1280, 720)

# Chame o método display_credits para exibir os créditos com animação
credits.display_credits()
