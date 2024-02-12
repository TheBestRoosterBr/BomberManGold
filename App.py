import pygame


class App:
    def __init__(self):
        pygame.init()
        self.isRunning = True
        self.screen = pygame.display.set_mode((800,600))

    def run(self):
        while self.isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False
                    pygame.quit()
