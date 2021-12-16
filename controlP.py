from levelMapper import levelMaker
from playerEnt import playerCharacter
from settingsData import settingsWAD
from inputHandler import ioHandler
from pygame.sprite import Sprite
import gc
import sys
import pygame


#settings file

class platformEngine:
    def __init__(self):
        pygame.init()
        self.settings = settingsWAD()
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.Group()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Platformer Engine')

        self.playChar = playerCharacter(self)
        self.player.add(self.playChar)
        self.tileMap = levelMaker(self)
        #self.tiles.add(self.tileMap)
        self.ioSys = ioHandler(self)
        self.tileMap.levInit()

    def qollide(self):
        collider = pygame.sprite.groupcollide(self.tiles, self.player, False, False)

        if collider:
            self.playChar.gravity = False
        else:
            self.playChar.gravity = True
            #print('col det')

        if self.playChar.rect.x >= 600 and self.playChar.moving_right == True:
            self.playChar.offset = True
        else:
            self.playChar.offset = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.tileMap.Update_Render()
        self.playChar.blitMe()

        pygame.display.flip()
        
    def run_game(self):

        while True:
            self.ioSys.eventHandler()
            self.qollide()
            self.playChar.update()

            self._update_screen()

if __name__ == '__main__':
    print('mnr')
    newp = platformEngine()
    newp.run_game()
