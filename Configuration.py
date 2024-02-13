
class Configuration:
    __instance = None

    @staticmethod
    def get_config():
        if Configuration.__instance is None:
            Configuration.__instance = Configuration()
        return Configuration.__instance

    def __init__(self):
        self.screen_height = 720
        self.screen_width = 1280
        self.game_fps = 60
        self.cell_size = (16 * 3, 48)
        self.board_size = (19, 15)
        self.offset_x = (self.screen_width - self.cell_size[0] * self.board_size[0]) / 2
        self.offset_y = (self.screen_height - self.cell_size[1] * self.board_size[1]) / 2
        self.actual_world = 0
        self.level = 0
        self.map_size = (936, 648)
