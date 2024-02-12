import pygame
from Menu import MenuInicial

from Game import Game


class App:
    def __init__(self):
        pygame.init()
        self.isRunning = True
        self.screen = pygame.display.set_mode((800, 600))
        self.game = Game(self.screen)

    def run(self):
        menu = MenuInicial(self.screen)
        #menu.main_loop()
        self.game.run()
