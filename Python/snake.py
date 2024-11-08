import pygame, random
from pygame.locals import *

pygame.init()
pygame.font.init()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


SCREEN_WIDTH = 800                # Height of the playing field.
SCREEN_HEIGHT = 800               # Width of the playing field.

# Player Variables
playerX = int(SCREEN_WIDTH / 2)   # This starts the player X at the midway point.
playerY = int(SCREEN_HEIGHT/ 2)   # This starts the player Y at the midway point.
velocity = 1                     # The 'player' starts out moving.
direction = None                  # But has no direction.
playerSize = 20
score = 0      #importaint change
start = 0
menufont = pygame.font.SysFont("None", 50)

#Bad Apple Variables (important change)
appleX = random.randint(10, SCREEN_WIDTH - 10)  
appleY = random.randint(10, SCREEN_HEIGHT - 10)
appleSize = 10                 

#Bad Apple Song background (sound isn't working)
#pygame.mixer.music.load("Bad Apple!!.mp3")
#pygame.mixer.music.set_volume(0.5)
#pygame.mixer.music.play("Bad Apple!!.mp3")

# Now that pygame is imported and initialized
# we need a screen
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

# Run until not true
running = True
while running:

    # did we quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # This part of the loop detects keys pressed.
    pressed = pygame.key.get_pressed()     
    if (pressed[K_RIGHT] or pressed[K_d]):
        direction = 'east'
    if (pressed[K_LEFT] or pressed[K_a]):
        direction = 'west'
    if (pressed[K_UP] or pressed[K_w]):
        direction = 'north'
    if (pressed[K_DOWN] or pressed[K_s]):
        direction = 'south'
    if (pressed[K_SPACE]):
        velocity += 1

    # Do logical updates here
    
    

    
    if direction == 'east':
        playerX += velocity
    if direction == 'west':
        playerX -= velocity
    if direction == 'north':
        playerY -= velocity
    if direction == 'south':
        playerY += velocity
#detects collision between player and apple (important change)
    for i in range(appleX -10, appleX + 10):
        if playerY in range(appleY-20, appleY+20) and playerX in range(appleX-20, appleX+20):
            playerSize += 1
            score += 1
            appleX = random.randint(10, SCREEN_WIDTH -10)
            appleY = random.randint(10, SCREEN_HEIGHT - 10)
    


    

    # Fill the screen with a color
    screen.fill("#236533")

    #displaying the score: (important change)
    scorefont = pygame.font.SysFont("None", 36)
    scoretext = scorefont.render("Score: " + str(score), 1, (255, 255, 255))
    screen.blit(scoretext, (5, 20))


# This is how thw worm kills itself (important change)
    if playerX < 0 or playerX > SCREEN_WIDTH:   
        direction = None
        velocity = 0
        exittext = scorefont.render("You Died, Your Score Was: " + str(score) + "Press Q To Quit", 1, (255, 255, 255))
        screen.blit(exittext, (150, 400))
        if (pressed[K_q]):
            pygame.QUIT()

    if playerY < 0 or playerY > SCREEN_HEIGHT:
        direction = None
        velocity = 0
        exittext = scorefont.render("You Died, Your Score Was: " + str(score) + " Press Q To Quit", 1, (255, 255, 255))
        screen.blit(exittext, 150, 400)
        if (pressed[K_q]):
            pygame.QUIT()


    # draw the apple (important change)
    pygame.draw.circle(screen, (RED), (appleX, appleY), appleSize)

    # draw something, a dot
    pygame.draw.circle(screen, ("#80604D"), (playerX, playerY), playerSize)

    
    # Flip the display
    pygame.display.flip()

# Done! Time to quit
pygame.quit()