import pygame
import math
from pygame.locals import *

width = 1000
height = 1000
screen = pygame.display.set_mode([width, height])
pressed = pygame.key.get_pressed() 
light_Blue = (255, 255, 255)

class MainMenu:

    def __init__(self, gameMode):
        self.gameMode = gameMode


    def startMenu(self, gameMode):
        GameOn = True
        while GameOn == True:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GameOn = False
            screen.fill(light_Blue)

            if (pressed[K_1]):
                gameMode = 1
                pygame.draw.circle(screen, (0, 255, 0), (500, 500), 30)
            if (pressed[K_2]):
                gameMode = 2
                pygame.draw.circle(screen, (0, 0, 255), (500, 500), 30)
            if (pressed[K_3]):
                gameMode = 3
                pygame.draw.circle(screen, (255, 0, 0), (500, 500), 30)
        
            pygame.display.flip()

        