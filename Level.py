from BlockStatus import BlockStatus
from Enemy import *
from Game import Game
from onWinMenu import TelaResultado

class Level:
    def __init__(self, num):
        self.enemies = []
        self.num = num
        self.game_result = 0

    def alter_stage(self):
        pass

    def run(self, screen):
        pass


class Level1World1(Level):
    def __init__(self):
        super().__init__(1)
        self.lucky_block_position = (13, 16)

    def alter_stage(self):
        Stage.stage.sprite_parede = pygame.transform.scale(pygame.image.load("Assets/marioBlock.png"),
                                                           Configuration.get_config().cell_size)
        Stage.stage.sprite_parede_destrutiva = pygame.transform.scale(
            pygame.image.load("Assets/marioBrickBlock.png"), Configuration.get_config().cell_size)

        Stage.stage.board = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 17, 1],
            [1, 0, 2, 0, 2, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 2, 1, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 1],
            [1, 0, 2, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 2, 1, 2, 1],
            [1, 0, 0, 2, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 2, 1, 0, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 2, 1, 1, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 2, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 2, 1, 0, 1, 0, 1, 0, 1, 2, 1, 2, 1, 0, 1],
            [1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 1],
            [1, 0, 1, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 1, 2, 1, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        Stage.stage.board[self.lucky_block_position[0]][self.lucky_block_position[1]] = BlockStatus.LUCKY_BLOCK
        koopa1 = Koopa(1, 16)
        koopa2 = Koopa(3, 13)
        bill_spawner1 = BillSpawner(1, 7, True)
        bill_spawner2 = BillSpawner(1, 12, True)
        bill_spawner3 = BillSpawner(17, 12)
        bill_spawner4 = BillSpawner(17, 12)
        self.enemies.append(koopa1)
        self.enemies.append(koopa2)
        self.enemies.append(bill_spawner1)
        self.enemies.append(bill_spawner2)
        self.enemies.append(bill_spawner3)
        self.enemies.append(bill_spawner4)

    def run(self, screen):
        self.alter_stage()
        game = Game(screen, enemies=self.enemies)
        self.game_result = game.run(self.lucky_block_position)
        resultado = TelaResultado(screen)
        if not self.game_result:
            resultado.screen_derrota()
        elif self.game_result == 0:
            resultado.screen_vitoria()
            exit(1)


class Level2World1(Level):
    def __init__(self):
        super().__init__(1)

    def alter_stage(self):
        Stage.stage.sprite_parede = pygame.transform.scale(pygame.image.load("Assets/marioBlock.png"),
                                                           Configuration.get_config().cell_size)
        Stage.stage.sprite_parede_destrutiva = pygame.transform.scale(
            pygame.image.load("Assets/marioBrickBlock.png"), Configuration.get_config().cell_size)

        Stage.stage.board = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1],
            [1, 3, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 0, 1, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 3, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 3, 1, 0, 1, 1, 0, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 3, 1, 0, 1, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 3, 1, 0, 1, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        Stage.stage.board = Stage.preencher_board(Stage.stage.board)

        koopa1 = Koopa(1, 16)
        koopa2 = Koopa(3, 13)
        self.enemies.append(koopa1)
        self.enemies.append(koopa2)

    def run(self, screen):
        self.alter_stage()
        #Olhe como ta a do level 1 pra deixar parecido
        game = Game(screen, enemies=self.enemies)
        self.game_result = game.run()
        resultado = TelaResultado(screen)
        if self.game_result == 1:
            resultado.screen_derrota()
        elif self.game_result == 0:
            resultado.screen_vitoria()


class Level2World2(Level):
    def __init__(self):
        super().__init__(1)

    def alter_stage(self):
        Stage.stage.sprite_parede = pygame.transform.scale(pygame.image.load("Assets/marioBlock.png"),
                                                           Configuration.get_config().cell_size)
        Stage.stage.sprite_parede_destrutiva = pygame.transform.scale(
            pygame.image.load("Assets/marioBrickBlock.png"), Configuration.get_config().cell_size)

        Stage.stage.board = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1],
            [1, 3, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 0, 1, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 3, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 0, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 3, 1, 0, 1, 1, 0, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 3, 1, 0, 1, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 3, 1, 0, 1, 0, 1, 3, 1, 0, 1, 0, 1, 0, 1, 0, 1, 3, 1],
            [1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        Stage.stage.board = Stage.preencher_board(Stage.stage.board)

        koopa1 = Koopa(1, 16)
        koopa2 = Koopa(3, 13)
        self.enemies.append(koopa1)
        self.enemies.append(koopa2)

    def run(self, screen):
        self.alter_stage()
        game = Game(screen, enemies=self.enemies)
        game.run()