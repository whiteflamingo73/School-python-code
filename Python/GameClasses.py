import pygame
import math
from pygame.locals import *
import random
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
        

        while gameMode == None and GameOn == True:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GameOn = False
            screen.fill(light_Blue)

            myfont = pygame.font.SysFont('None', 50)
            descriptionFont = pygame.font.SysFont('None', 30)
            pressed = pygame.key.get_pressed() 
            
            
            ### BUTTONS ###

            #Gamemode 1 button
            buttontext = myfont.render('Gamemode 1', 50, (255, 255, 255))
            button = pygame.draw.rect(screen, (50, 50, 50), (300, 100, 400, 200))
            if button.collidepoint(pygame.mouse.get_pos()):
                    button = pygame.draw.rect(screen, (150, 0, 50), (300, 100, 400, 200))
                    description1 = descriptionFont.render('Default Game: Nothing Changed', 1, (255, 255, 255))
                    screen.blit(description1, (355, 220))
            screen.blit(buttontext, (395, 180))

            #Gamemode 2 button
            button2text = myfont.render('Gamemode 2', 50, (255, 255, 255))
            button2 = pygame.draw.rect(screen, (50, 50, 50), (300, 350, 400, 200))
            if button2.collidepoint(pygame.mouse.get_pos()):
                    button2 = pygame.draw.rect(screen, (150, 0, 50), (300, 350, 400, 200))
                    description2 = descriptionFont.render('Default Game: Nothing Changed', 1, (255, 255, 255))
                    screen.blit(description2, (355, 470))
            screen.blit(button2text, (395, 430))

            #Gamemode 3 button
            button3text = myfont.render('Gamemode 3', 50, (255, 255, 255))
            button3 = pygame.draw.rect(screen, (50, 50, 50), (300, 600, 400, 200))
            if button3.collidepoint(pygame.mouse.get_pos()):
                    button3 = pygame.draw.rect(screen, (150, 0, 50), (300, 600, 400, 200))
                    description3 = descriptionFont.render('Drawing Mode', 1, (255, 255, 255))
                    screen.blit(description3, (395, 720))
            screen.blit(button3text, (395, 680))
            #Quit Button
            quittext = myfont.render('QUIT', 50, (255, 255, 255))
            QuitButton = pygame.draw.rect(screen, (50, 50, 50), (300, 850, 400, 200))
            if QuitButton.collidepoint(pygame.mouse.get_pos()):
                    QuitButton = pygame.draw.rect(screen, (150, 0, 50), (300, 850, 400, 200))
            screen.blit(quittext, (395, 930))
            
            

            screen.blit(button3text, (395, 680))

            for event in pygame.event.get():
                #Gamemode 1 Button
                if event.type == MOUSEBUTTONDOWN:
                    if button.collidepoint(event.pos):
                        self.gameMode = 1
                        return self.gameMode
                    #Gamemode 2 button
                    if button2.collidepoint(event.pos):
                        self.gameMode = 2
                        return self.gameMode
                    #gamemode 3 button
                    if button3.collidepoint(event.pos):
                        self.gameMode = 3
                        return self.gameMode
                    
                    #Quit Button
                    if QuitButton.collidepoint(event.pos):
                         GameOn = False
                    
            
            
                
        
            pygame.display.flip()
    #def __new__(self):
    #    return gameMode



class Platform:
    
    def __init__(self, charX, charY, charVel, platformX=[], platformY=[], platformW=[], platformH=[]):
        self.charX = charX
        self.charY = charY
        self.charVel = charVel
        self.platformX = platformX
        self.platformY = platformY
        self.platformH = platformH
        self.platformW = platformW

    
    def platform(self):
        X = random.randint(20, 1000)
        self.platformX.append(X)
        Y = random.randint(30, 1000)
        self.platformY.append(Y)
        W = random.randint(100, 300)
        self.platformW.append(W)
        H = random.randint(30, 75)
        self.platformH.append(H)

import spritesheets
sprite_sheet_image = pygame.image.load("/home/abargd/Desktop/Python/UnitPygame/Sprites/doux.png").convert_alpha()
class Player:
    

    

    def __init__(self, x, y):
        self.image = sprite_sheet_image 
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.flip = True

    def playersprite(self, sprite_sheet_image=sprite_sheet_image):
        BLACK = (0, 0, 0)

        
        sprite_sheet = spritesheets.SpriteSheet(sprite_sheet_image)
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
    
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(animation_list[action]):
                frame = 0
                print(frame)
        
        #Animation updates
        pressed = pygame.key.get_pressed()
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


        # if event.type == pygame.KEYUP:
        #     pass
        #     if event.key == K_d or event.key == K_s or event.key == K_a or event.key == K_w or event.key == K_UP or event.key == K_LEFT or event.key == K_DOWN or event.key == K_RIGHT or event.key == K_q:
        #         action = 0
        #         if frame >= 4:
        #             frame = 0
        

       
        self.image = (animation_list[action][frame])
        return self.image
    
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 12, self.rect.y - 5))
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

    

         