import pygame
from Menu import MenuInicial


class App:
    def __init__(self):
        pygame.init()
        self.isRunning = True
        self.screen = pygame.display.set_mode((800, 600))

    def run(self):
        menu = MenuInicial(self.screen)
        menu.main_loop()

