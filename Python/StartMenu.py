import pygame
import math
from pygame.locals import *
pygame.init()

width = 1000
height = 1000
screen = pygame.display.set_mode([width, height])

light_Blue = (173, 216, 230)
# Run until the user asks to quit
running = True
while running:

    

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    ### Game Modes ###

    
    screen.fill(light_Blue)

    pressed = pygame.key.get_pressed()
    if (pressed[K_1]):
        pygame.draw.circle(screen, (0, 255, 0), (500, 500), 30)
    if (pressed[K_2]):
        pygame.draw.circle(screen, (0, 0, 255), (500, 500), 30)
    if (pressed[K_3]):
        pygame.draw.circle(screen, (255, 0, 0), (500, 500), 30)

    pygame.display.flip()