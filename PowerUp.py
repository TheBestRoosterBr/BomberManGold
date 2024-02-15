from enum import IntEnum
from random import choices
import Stage
from Configuration import Configuration
import pygame


class PowerUpEnum(IntEnum):
    Foguinho = 0
    FoguinhoGold = 1
    Bombinha = 2
    Patins = 3
    Colete = 4
    Vida = 5
    BombaRelogio = 6
    BombaEspinho = 7
    Caveira = 8
    BombaP = 9


class PowerUp:
    def __init__(self, x, y):
        self.num = self.generate_random_powerup()
        sprite = pygame.image.load('Assets/powerups.png')
        size = 16
        sprite = sprite.subsurface(size * self.num, 0, size, size)
        self.sprite = pygame.transform.scale(sprite, Configuration.get_config().cell_size)
        self.border_sprite = pygame.image.load('Assets/borders_power_up.png')
        self.frames = 0
        self.position = (x, y)
        self.sound_Takeitem = pygame.mixer.Sound('Sounds/Take-item.mp3')

    def generate_random_powerup(self):
        # Define the weights for each enum member
        weights = [10, 1, 10, 10, 3, 3, 1, 1, 10, 1]
        powerups = list(PowerUpEnum)

        # Use the choices function to randomly select a powerup based on the weights
        self.num = choices(powerups, weights)[0]
        return self.num

    def draw(self, screen):
        self.frames += 1
        pos = Stage.matrix_to_screen_pos(self.position[0], self.position[1])
        screen.blit(self.sprite, (pos[0], pos[1]))

        index = self.frames % 5
        size = 16
        spr_bord = self.border_sprite.subsurface(index * size, 0, size, size)
        spr_bord = pygame.transform.scale(spr_bord, Configuration.get_config().cell_size)
        screen.blit(spr_bord, (pos[0], pos[1]))

    def get_power_up(self, player):
        self.sound_Takeitem.play()
        self.sound_Takeitem.set_volume(Configuration.get_config().volume)
        player.disable_caveira()
        if self.num == PowerUpEnum.Foguinho:
            player.bomb_power += 1
        elif self.num == PowerUpEnum.FoguinhoGold:
            player.bomb_power += 17
        elif self.num == PowerUpEnum.Bombinha:
            player.max_bombs += 1
        elif self.num == PowerUpEnum.Patins:
            player.speed += 1
        elif self.num == PowerUpEnum.BombaEspinho:
            player.bomb_type = 'espinho'
        elif self.num == PowerUpEnum.BombaP:
            player.bomb_type = 'bombaP'
        elif self.num == PowerUpEnum.BombaRelogio:
            player.bomb_type = 'relogio'
        elif self.num == PowerUpEnum.Vida:
            player.vidas += 1
        elif self.num == PowerUpEnum.Colete:
            player.pegar_colete()
        elif self.num == PowerUpEnum.Caveira:
            player.randon_caveira()


