# Simple pygame program

# Import and initialize the pygame library
import pygame
import math
from GameClasses import MainMenu
from pygame.locals import *
pygame.init()

width = 1000
height = 1000

playerX = int(width/ 2)
playerY = int(height/ 2)
#Screen Colors
light_Blue = (173, 216, 230)

#Player Colors
blue = (0, 0, 255)
red = (255, 0, 20)

velocity = 1
direction = None

playerXCoords = []
playerYCoords = []

#Gamemode
GameMode = None
menu = MainMenu(GameMode)

diagonalDirection = None
# Set up the drawing window
screen = pygame.display.set_mode([width, height], pygame.RESIZABLE)

# Run until the user asks to quit
running = True
while running:

    

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pressed = pygame.key.get_pressed()     
    ###Main Menu###
    def startmenu(GameMode):
        menu.startMenu(GameMode)
        return menu.gameMode
        
    
    
        
    
    if menu.gameMode == None: 
        startmenu(GameMode)





    ###PLAYER ACTIONS###

    #Movements, NESW
    
    if (pressed[K_RIGHT] or pressed[K_d]):
        direction = 'east'
    if (pressed[K_LEFT] or pressed[K_a]):
        direction = 'west'
    if (pressed[K_UP] or pressed[K_w]):
        direction = 'north'
    if (pressed[K_DOWN] or pressed[K_s]):
        direction = 'south'
    
    #Movements, diagonal

    if (pressed[K_RIGHT] and pressed[K_UP]):
        diagonalDirection = 'NorthEast'
    if (pressed[K_LEFT] and pressed[K_UP]):
        diagonalDirection = 'NorthWest'
    if (pressed[K_RIGHT] and pressed[K_DOWN]):
        diagonalDirection = 'SouthEast'
    if (pressed[K_LEFT] and pressed[K_DOWN]):
        diagonalDirection = 'SouthWest'
    

    ############

    ### LOGICAL UPDATES FOR PLAYER
    
    

    #Movement Updates
    if direction == 'east':
        playerX += velocity
        direction = None
    if direction == 'west':
        playerX -= velocity
        direction = None
    if direction == 'north':
        playerY -= velocity
        direction = None
    if direction == 'south':
        playerY += velocity
        direction = None

    if diagonalDirection == 'NorthEast':
        playerX += (velocity)/2
        playerY -= (velocity)/2
        diagonalDirection = None
    if diagonalDirection == 'NorthWest':
        playerX -= (velocity)/2
        playerY -= (velocity)/2
        diagonalDirection = None
    if diagonalDirection == 'SouthEast':
        playerX += (velocity)/2
        playerY += (velocity)/2
        diagonalDirection = None
    if diagonalDirection == 'SouthWest':
        playerX -= (velocity)/2
        playerY += (velocity)/2
        diagonalDirection = None
        

    # Fill the background with white
    screen.fill(light_Blue)

    
    if menu.gameMode == 3:
        if (pressed[K_SPACE]):
            playerXCoords.append(int(playerX))
            playerYCoords.append(int(playerY))
          
        
        for i in range(0, len(playerYCoords)):
            pygame.draw.circle(screen, (0, 0, 0), (playerXCoords[i], playerYCoords[i]), 5)

        if (pressed[K_c]):
            playerXCoords.clear()
            playerYCoords.clear()

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, red, (playerX, playerY), 15)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
