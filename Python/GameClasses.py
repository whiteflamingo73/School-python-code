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
    
    def __init__(self, charX, charY, charVel):
        self.charX = charX
        self.charY = charY
        self.charVel = charVel

    
    def platform():
        X = random.randint(20, 100)
        Y = random.randint(30, 100)

        W = random.randint(10, 20)
        H = random.randint(4, 10)

        generatedPlatform = pygame.draw.rect(screen, (50, 220, 12), (X, Y, W, H))