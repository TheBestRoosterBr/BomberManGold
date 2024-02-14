
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
        self.level = 1
        self.map_size = (936, 648)
        self.foto = 0
        self.volume = 0.2
        self.audio = True
        self.player = ''
        self.load_from_file()

    def load_from_file(self):
        with open('player_data.properties', 'r') as arquivo:
            linha = arquivo.readline()

            while linha != "":

                prop = linha.split('=')
                if len(prop) <= 1:
                    break
                prop[1] = prop[1].replace('\n', '')
                if prop[0] == 'color':
                    self.player = prop[1]
                if prop[0] == 'volume':
                    self.volume = float(prop[1])
                    if self.volume <= 0.05:
                        self.audio = False
                    else:
                        self.audio = True

                linha = arquivo.readline()


    def save_in_file(self):
        with open('player_data.properties', 'w') as f:
            f.write('color=' + self.player + '\n')
            f.write('volume=' + str(self.volume) + '\n')
