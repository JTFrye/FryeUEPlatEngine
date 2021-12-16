import pygame
from pygame.sprite import Sprite

class playerCharacter(Sprite):
    def __init__(self, platEngine):
        super().__init__()

        self.screen = platEngine.screen
        self.settings = platEngine.settings

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.offset = False
        self.gravity = True

        self.pcbg_color = (255,255,255)
        self.yVel = .2
        self.xVel = .2

        self.rect = pygame.Rect(0,0, self.settings.playCharH,self.settings.playCharW)
        self.rectY = float(self.rect.y)
        self.rectX = float(self.rect.x)


    def update(self):
        if self.gravity:
            self.yVel += self.settings.playChar_accel
            self.rectY += self.yVel + 0.5 * self.settings.playChar_accel
        else:
            self.yVel = .2
        if self.moving_right:
            self.xVel += self.settings.playChar_Haccel
            self.rectX += self.xVel + 0.5 * self.settings.playChar_Haccel
            if self.rectX >= 600:
                self.rectX = 600
        if self.moving_left:
            self.rectX -= self.settings.playChar_Hspeed
        if self.moving_up:
            self.rectY -= self.settings.playChar_jumpH
        if self.moving_down:
            self.rectY += self.settings.playChar_jumpH
        #if self.offset:
            #self.settings.offsetX = self.settings.playChar_Hspeed 
            #print(self.settings.offsetX)
        self.rect.x = self.rectX
        self.rect.y = self.rectY

    def blitMe(self):
        pygame.draw.rect(self.screen, self.pcbg_color, self.rect)
        
        

