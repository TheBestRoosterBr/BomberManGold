import pygame
from Menu import MenuInicial

from Game import Game
from Configuration import Configuration

class App:
    def __init__(self):
        pygame.init()
        self.isRunning = True
        self.screen = pygame.display.set_mode((Configuration.get_config().screen_width, Configuration.get_config().screen_height))
        self.game = Game(self.screen)

    def run(self):
        menu = MenuInicial(self.screen)
        #menu.main_loop()
        self.game.run()
