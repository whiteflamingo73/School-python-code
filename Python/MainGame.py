# Simple pygame program

# Import and initialize the pygame library
import pygame
import spritesheets
import math
import GameClasses
from GameClasses import Platform
from GameClasses import MainMenu

from pygame.locals import *
pygame.init()

sprite_sheet_image = pygame.image.load("/home/abargd/Desktop/Python/UnitPygame/Sprites/doux.png").convert_alpha()
sprite_sheet = spritesheets.SpriteSheet(sprite_sheet_image)
BG = (50, 50, 50)
BLACK = (0, 0, 0)
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


gravity = 9.8
jumpforce = 18

playerXCoords = []
playerYCoords = []

#Gamemode
GameMode = None
menu = MainMenu(GameMode)

diagonalDirection = None

animation_list = []
animation_steps = [4, 6, 3, 4, 7]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0
step_counter = 0


for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 24, 24, 3, BLACK))
        step_counter += 1
    animation_list.append(temp_img_list)

print(animation_list)


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
        

    #Animation updates
    if (pressed[K_RIGHT] or pressed[K_d]):
        
        action = 1
        if frame >= 4:
            frame = 0
    
    if pressed[K_LEFT] or pressed[K_a]:
        action = 1
        if frame >= 4:
            frame = 0

    if (pressed[K_q]):
        
        action = 2
        if frame >= 3:
            frame = 0
    if (pressed[K_UP] or pressed[K_w]):
        
        action = 1
        if frame >= 4:
            frame = 0
    if (pressed[K_DOWN] or pressed[K_s]):
        action = 1
        if frame >=4:
            frame = 0
    
    if (pressed[K_LCTRL] and pressed[K_w] or pressed[K_LCTRL] and pressed[K_a] or pressed[K_LCTRL] and pressed[K_s] or pressed[K_LCTRL] and pressed[K_d] or pressed[K_LCTRL] and pressed[K_UP] or pressed[K_LCTRL] and pressed[K_LEFT] or pressed[K_LCTRL] and pressed[K_DOWN] or pressed[K_LCTRL] and pressed[K_RIGHT]):
        action = 4
        if frame >= 4:
            frame = 0
        
        velocity = 2
    
    else:
        
        velocity = 1


    if event.type == pygame.KEYUP:
        pass
        if event.key == K_d or event.key == K_s or event.key == K_a or event.key == K_w or event.key == K_UP or event.key == K_LEFT or event.key == K_DOWN or event.key == K_RIGHT or event.key == K_q:
            action = 0
            if frame >= 4:
                frame = 0

    
    print(frame)

    # Fill the background with white
    screen.fill(light_Blue)

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    screen.blit(animation_list[action][frame], (playerX, playerY))

    

    
    if menu.gameMode == 3:
        if (pressed[K_SPACE]):
            playerXCoords.append(int(playerX))
            playerYCoords.append(int(playerY))
          
        
        for i in range(0, len(playerYCoords)):
            pygame.draw.circle(screen, (0, 0, 0), (playerXCoords[i], playerYCoords[i]), 5)

        if (pressed[K_c]):
            playerXCoords.clear()
            playerYCoords.clear()
    

    if menu.gameMode == 2:
        createdplatform = Platform(playerX, playerY, jumpforce)

        for i in range(5):
            createdplatform.platform()

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, red, (playerX, playerY), 15)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
