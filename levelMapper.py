import pygame
from pygame.sprite import Sprite
from blockStruct import bareBlock

class levelMaker(Sprite):
    def __init__(self, platEngine):
        super().__init__()

        self.screen = platEngine.screen
        self.settings = platEngine.settings
        self.tiles = platEngine.tiles
        self.playChar = platEngine.playChar
        self.rect = pygame.Rect(100,400,self.settings.tileWidth,self.settings.tileHeight)

        self.dirtmap = ['1','1','1','2','2','2','0','1','2','1','0','1','1','1','2','2','2']        

    def levInit(self):
        for xed in range(len(self.dirtmap)):
            qwikBlock = bareBlock(self, self.dirtmap[xed], xed)
        

    def Update_Render(self):
        for yed in self.tiles.sprites():
            if self.playChar.offset == True:
                yed.rect.x -= self.playChar.xVel #+ self.settings.playChar_Hspeed
            yed.renderGround()
        
