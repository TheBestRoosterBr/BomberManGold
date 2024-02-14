import pygame
import sys


class Pause:
    def __init__(self, width, height):
        pygame.init()
        self.opcoes = ["Continuar", "Opções", "Voltar"]
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # Fontes
        self.font_path = "./Fonts/nougat.ttf"
        self.font = pygame.font.Font(self.font_path, 40)

        # Cores padrão
        self.default_color = (255, 255, 255)
        self.hovered_color = (0, 120, 255)

        # Índice da opção atualmente selecionada
        self.selected_option = None

    def draw_rectangle(self, surface, color, rect, radius, opacity, gradient_color, border_color,
                       border_width, image_path, text, text_color, font, font_size):
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

        # Adiciona o texto centralizado
        if text:
            text_font = pygame.font.Font(font, font_size)
            text_surface = text_font.render(text, True, text_color)
            text_rect = text_surface.get_rect(center=(rect.centerx, rect.centery))
            surface.blit(text_surface, text_rect)

    def draw_text_center(self, text, y, color, font_size, font_path):
        font = pygame.font.Font(font_path, font_size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(self.WIDTH // 2, y))
        self.screen.blit(text_surface, text_rect)

    def check_button_hover(self, mouse_pos):
        # Verifica se o mouse está sobre algum botão de opção
        for index, op in enumerate(self.opcoes):
            rect = pygame.Rect((self.WIDTH - 200) / 2, ((self.HEIGHT // 2) - 130) + 90 + (55 * index), 200, 40)
            if rect.collidepoint(mouse_pos):
                self.selected_option = index
                return True
        self.selected_option = None
        return False

    def view_paused(self):
        # Desenhe o background aqui (substitua pelo caminho real do seu arquivo de imagem)
        background_image = pygame.image.load("./Assets/temp.png")
        self.screen.blit(background_image, (0, 0))

        # Configurações do retângulo com texto
        pos_y = (self.HEIGHT // 2) - 130
        self.draw_rectangle(self.screen, (3, 0, 40), (0, 0, 1280, 720), 0, 0.7, None, None, None, None, None, None,
                            None, None)

        self.draw_text_center("Paused", pos_y, (255, 255, 255), 50, self.font_path)
        self.draw_rectangle(self.screen, (255, 255, 255), ((self.WIDTH - 700) / 2, pos_y + 50, 700, 2), 0, 1, None,
                            None, None, None, None, None, None, None)

        # Três opções
        for index, op in enumerate(self.opcoes):
            rect = pygame.Rect((self.WIDTH - 200) / 2, ((self.HEIGHT // 2) - 130) + 90 + (55 * index), 200, 40)

            # Verifica se o mouse está sobre o botão
            if rect.collidepoint(pygame.mouse.get_pos()):
                color = self.hovered_color
                opacidade = 1
            else:
                color = self.default_color
                opacidade = 0.3

            self.draw_rectangle(
                self.screen, color, rect, 3, opacidade, None, None, None, None, op, (255, 255, 255), self.font_path, 25
            )

        pygame.display.flip()

    def quit_game(self):
        pygame.quit()
        sys.exit()


# Crie uma instância da classe Pause
pause = Pause(1280, 720)

# Chame o método view_paused para exibir a tela de pausa


while True:
    pause.view_paused()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pause.quit_game()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pause.selected_option is not None:
                if pause.selected_option == 0:
                    print("botão 1")
                elif pause.selected_option == 1:
                    print("botão 2")
                elif pause.selected_option == 2:
                    pause.quit_game()
    if event.type == pygame.MOUSEMOTION:
        pause.check_button_hover(pygame.mouse.get_pos())
