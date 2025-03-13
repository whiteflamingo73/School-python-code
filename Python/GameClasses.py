import pygame
import math
from pygame.locals import *

width = 1000
height = 1000
screen = pygame.display.set_mode([width, height], pygame.RESIZABLE)

light_Blue = (255, 255, 255)

class MainMenu:

    def __init__(self, gameMode):
        self.gameMode = gameMode


    def startMenu(self, gameMode):
        GameOn = True
        gameMode = None
        while gameMode == None:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
            screen.fill(light_Blue)

            pressed = pygame.key.get_pressed() 
            if (pressed[K_1]):
                pygame.draw.circle(screen, (0, 255, 0), (500, 500), 30)
                self.gameMode = 1
                return self.gameMode
        
                
            if (pressed[K_2]):
                pygame.draw.circle(screen, (0, 0, 255), (500, 500), 30)
                self.gameMode = 2
                return self.gameMode
            
                
            if (pressed[K_3]):
                pygame.draw.circle(screen, (255, 0, 0), (500, 500), 30)
                self.gameMode = 3
                return self.gameMode
            
            #buttons
            pygame.draw.rect(screen, (50, 50, 50), (300, 100, 400, 200))
            
                
        
            pygame.display.flip()
    #def __new__(self):
    #    return gameMode

        