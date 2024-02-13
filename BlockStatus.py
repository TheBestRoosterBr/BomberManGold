from enum import IntEnum


class BlockStatus(IntEnum):
    CLEAR = 0
    WALL = 1
    DESTRUCTIBLE_WALL = 2
    FIRE = 3
    BOMBA = 4
    DESTROY_BLOCK = 0b1000000
    POWER_UP = 5 # Valores entre 5 e 14 são os power UPS todo: tomar vergonha na cara e escrever todos
    CHAVE = 16
    PORTAL_FECHADO = 17
    PORTAL_ABERTO = 18

