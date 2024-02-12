import pygame


class Stage:
    def __init__(self):
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.blockSize = (48, 48)
        self.sprite_parede = pygame.transform.scale(pygame.image.load("Assets/parede.png"), self.blockSize)
        self.sprite_parede_destrutiva = pygame.transform.scale(pygame.image.load("Assets/ParedeDestrutiva.png"), self.blockSize)



    def draw(self, screen):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    pass
                elif self.board[i][j] == 1:
                    screen.blit(self.sprite_parede, self.blockSize[0] * j)

        pass

