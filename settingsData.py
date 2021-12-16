

class settingsWAD:
    def __init__(self):

        self.screen_width = 1024
        self.screen_height = 600

        self.bg_color = (0,0,0)

        #Player Height, Width
        self.playCharH = 30
        self.playCharW = 30

        #Player HSpeed and Gravity
        self.playChar_Hspeed = 1.0
        self.playChar_speed = .0002
        self.playChar_accel = .002
        self.playChar_Haccel = .0002
        self.playChar_jumpH = .99

        #Tile System
        self.tileColor = (255,0,0)
        self.tileWidth = 128
        self.tileHeight = 64
        self.flagColor = (0,127,127)
        self.offsetX = 0
