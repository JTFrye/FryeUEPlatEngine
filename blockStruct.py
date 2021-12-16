import pygame
from pygame.sprite import Sprite


class bareBlock(Sprite):
    def __init__(self, platEngine, optVal='0', locVal='0'):
        super().__init__()

        self.screen = platEngine.screen
        self.settings = platEngine.settings
        self.tiles = platEngine.tiles

        self.color1 = (0,0,0)
        self.color2 = (0,255,0)
        self.color3 = (0,0,255)

        self.selfColor = (0,0,0)

        if optVal == '0':
            self.rect = pygame.Rect(locVal * self.settings.tileWidth,400,self.settings.tileWidth,self.settings.tileHeight)
            pygame.draw.rect(self.screen, self.color1, self.rect)
        elif optVal == '1':
            self.rect = pygame.Rect(locVal * self.settings.tileWidth,400,self.settings.tileWidth,self.settings.tileHeight)
            pygame.draw.rect(self.screen, self.color2, self.rect)
            self.selfColor = self.color2
            self.tiles.add(self)
        elif optVal == '2':
            self.rect = pygame.Rect(locVal * self.settings.tileWidth,400,self.settings.tileWidth,self.settings.tileHeight)
            pygame.draw.rect(self.screen, self.color3, self.rect)
            self.selfColor = self.color3
            self.tiles.add(self)


    def renderGround(self):
        pygame.draw.rect(self.screen, self.selfColor, self.rect)
