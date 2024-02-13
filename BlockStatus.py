from enum import IntEnum


class BlockStatus(IntEnum):
    CLEAR = 0
    WALL = 1
    DESTRUCTIBLE_WALL = 2
    FIRE = 3
    BOMBA = 4
    DESTROY_BLOCK = 0b1000000

