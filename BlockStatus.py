from enum import IntEnum


class BlockStatus(IntEnum):
    CLEAR = 0
    WALL = 1
    DESTRUCTIBLE_WALL = 2
