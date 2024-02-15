import Stage
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
        self.enemies.clear()
        self.alter_stage()
        game = Game(screen, enemies=self.enemies)
        self.game_result = game.run(self.lucky_block_position)
        resultado = TelaResultado(screen)
        if self.game_result == 1:
            result = resultado.screen_derrota()
            if result:
                self.run(screen)
                return
            else:
                return False
        elif self.game_result == 0:
            resultado.screen_vitoria()
            Configuration.get_config().level = self.num + 1
            Configuration.get_config().save_in_file()
            return True
        elif self.game_result == 3:
            pass
        return False


class Level1World1(Level):
    def __init__(self):
        super().__init__(1)
        self.lucky_block_position = (13, 16)

    def alter_stage(self):
        Stage.stage = Stage.Stage()
        Stage.stage.sprite_parede = pygame.transform.scale(pygame.image.load("Assets/marioBlock.png"),
                                                           Configuration.get_config().cell_size)
        Stage.stage.sprite_parede_destrutiva = pygame.transform.scale(
            pygame.image.load("Assets/marioBrickBlock.png"), Configuration.get_config().cell_size)

        Stage.stage.board = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 17, 1],
            [1, 0, 2, 0, 2, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 2, 1, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 1],
            [1, 0, 2, 0, 1, 0, 1, 2, 1, 2, 0, 0, 1, 0, 1, 2, 1, 2, 1],
            [1, 0, 0, 2, 0, 0, 2, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 2, 1, 0, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 2, 1, 1, 2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 2, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 2, 1, 0, 1, 0, 1, 0, 1, 2, 1, 2, 1, 0, 1],
            [1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 1],
            [1, 0, 1, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 1, 2, 1, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        Stage.stage.board[self.lucky_block_position[0]][self.lucky_block_position[1]] = BlockStatus.LUCKY_BLOCK
        koopa1 = Koopa(1, 16)
        koopa2 = Koopa(3, 13)
        bill_spawner1 = BillSpawner(5, 1, True)
        bill_spawner2 = BillSpawner(12, 1, True)
        bill_spawner3 = BillSpawner(7, 12)
        flor1 = Fulor(9, 9)
        flor2 = Fulor(7, 14)
        flor3 = Fulor(3, 11)
        flor4 = Fulor(11, 6)
        self.enemies.append(koopa1)
        self.enemies.append(koopa2)
        self.enemies.append(bill_spawner1)
        self.enemies.append(bill_spawner2)
        self.enemies.append(bill_spawner3)
        self.enemies.append(flor1)
        self.enemies.append(flor2)
        self.enemies.append(flor3)
        self.enemies.append(flor4)
        pygame.mixer.music.load("Sounds/LevelOne.mp3")
        pygame.mixer.music.set_volume(Configuration.get_config().volume)
        pygame.mixer.music.play(-1)


class Level2World1(Level):
    def __init__(self):
        super().__init__(2)
        self.lucky_block_position = (13, 8)

    def alter_stage(self):
        Stage.stage = Stage.Stage()
        Stage.stage.sprite_parede = pygame.transform.scale(pygame.image.load("Assets/block_level_2.png"),
                                                           Configuration.get_config().cell_size)
        Stage.stage.sprite_parede_destrutiva = pygame.transform.scale(
            pygame.image.load("Assets/caixote_level_2.png"), Configuration.get_config().cell_size)

        Stage.stage.spr_lucky_block = pygame.transform.scale(
            pygame.image.load("Assets/lucky_block2.png"), Configuration.get_config().cell_size)

        Stage.stage.board = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 0, 0, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1],
            [1, 2, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 0, 1, 0, 1, 1, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1],
            [1, 3, 1, 0, 1, 1, 0, 2, 17, 2, 1, 0, 1, 0, 1, 0, 1, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 1, 0, 1, 0, 1, 2, 1, 2, 1, 0, 1, 0, 1, 0, 1, 2, 1],
            [1, 2, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1],
            [1, 0, 0, 2, 1, 2, 2, 1, 0, 1, 2, 1, 2, 1, 2, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        Stage.stage.board[self.lucky_block_position[0]][self.lucky_block_position[1]] = BlockStatus.LUCKY_BLOCK
        Stage.stage.background_color = (136, 113, 145)

        harem = MuxeguSpawner(12, 12)
        self.enemies.append(harem)
        pygame.mixer.music.load("Sounds/LevelTwon.mp3")
        pygame.mixer.music.set_volume(Configuration.get_config().volume)
        pygame.mixer.music.play(-1)


class Level3World1(Level):
    def __init__(self):
        super().__init__(3)
        self.lucky_block_position = (13, 1)

    def alter_stage(self):
        Stage.stage = Stage.Stage()
        Stage.stage.sprite_parede = pygame.transform.scale(pygame.image.load("Assets/block_level_3.png"),
                                                           Configuration.get_config().cell_size)
        Stage.stage.sprite_parede_destrutiva = pygame.transform.scale(
            pygame.image.load("Assets/caixote_level_3.png"), Configuration.get_config().cell_size)

        Stage.stage.board = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 17, 1],
            [1, 0, 1, 2, 2, 1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 2, 0, 1],
            [1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 0, 1],
            [1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1],
            [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 2, 0, 1],
            [1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 0, 1],
            [1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1],
            [1, 2, 1, 2, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1],
            [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 2, 1, 2, 1, 0, 1],
            [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        Stage.stage.board[self.lucky_block_position[0]][self.lucky_block_position[1]] = BlockStatus.LUCKY_BLOCK
        Stage.stage.background_color = (212, 69, 0)

        bill_spawner1 = BillSpawner(5, 1, True)
        bill_spawner2 = BillSpawner(8, 12)
        harem = MuxeguSpawner(12, 12)
        fanta = GhostSpawner(1, 13)
        camaleao1 = Camaleao(9, 5)
        camaleao2 = Camaleao(9, 9)

        self.enemies.append(bill_spawner1)
        self.enemies.append(bill_spawner2)
        self.enemies.append(fanta)
        self.enemies.append(camaleao1)
        self.enemies.append(camaleao2)
        self.enemies.append(harem)
        pygame.mixer.music.load("Sounds/LevelTree.mp3")
        pygame.mixer.music.set_volume(Configuration.get_config().volume)
        pygame.mixer.music.play(-1)



class Level4World1(Level):
    def __init__(self):
        super().__init__(4)
        self.lucky_block_position = (13, 16)

    def alter_stage(self):
        Stage.stage.sprite_parede = pygame.transform.scale(pygame.image.load("Assets/block_level_4.png"),
                                                           Configuration.get_config().cell_size)
        Stage.stage.sprite_parede_destrutiva = pygame.transform.scale(
            pygame.image.load("Assets/caixote_level_4.png"), Configuration.get_config().cell_size)

        Stage.stage.board = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        Stage.stage.board[self.lucky_block_position[0]][self.lucky_block_position[1]] = BlockStatus.LUCKY_BLOCK
        pygame.mixer.music.load("Sounds/Level4.mp3")
        pygame.mixer.music.set_volume(Configuration.get_config().volume)
        pygame.mixer.music.play(-1)

        herobrine = Herobrine()
        self.enemies.append(herobrine)

