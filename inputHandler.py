import pygame
import sys

class ioHandler:
    def __init__(self, platEngine):

        self.settings = platEngine.settings
        self.playChar = platEngine.playChar


    def eventHandler(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.playChar.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.playChar.moving_left = True
        elif event.key == pygame.K_UP:
            self.playChar.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.playChar.moving_down = True
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.playChar.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.playChar.moving_left = False
        elif event.key == pygame.K_UP:
            self.playChar.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.playChar.moving_down = False
        
