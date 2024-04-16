import pygame, sys
from pygame.locals import *
import random, time
import math
import button
from game1 import game1

pygame.init()


fps = 60
clock = pygame.time.Clock()
WIDTH, HEIGHT = 1000, 570
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((255,255,255))
pygame.display.set_caption("Game")



playerSpeed = 10

class Goblin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('goblin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (500, 300)
             
class MainCh(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('MainCh.png')
        self.rect = self.image.get_rect()
        
    def move(self):
        pressed  = pygame.key.get_pressed()
        aHeld = pressed[pygame.K_a]
        dHeld = pressed[pygame.K_d]
        sHeld = pressed[pygame.K_s]
        wHeld = pressed[pygame.K_w]
        
        if aHeld and wHeld and self.rect.left>10 and self.rect.top>10:
#             self.image = pygame.image.load('MainChLeftUp.png')
            self.rect.move_ip(-playerSpeed*math.sin(math.pi/4), -playerSpeed*math.sin(math.pi/4))
        elif aHeld and sHeld and self.rect.left>10 and self.rect.bottom<HEIGHT-10:
#             self.image = pygame.image.load('MainChLeftDown.png')
            self.rect.move_ip(-playerSpeed*math.sin(math.pi/4), playerSpeed*math.sin(math.pi/4))
        elif dHeld and wHeld and self.rect.right<WIDTH-10 and self.rect.top>10:
#             self.image = pygame.image.load('MainChRightUp.png')
            self.rect.move_ip(playerSpeed*math.sin(math.pi/4), -playerSpeed*math.sin(math.pi/4))
        elif dHeld and sHeld and self.rect.right<WIDTH-10 and self.rect.bottom<HEIGHT-10:
#             self.image = pygame.image.load('MainChRightDown.png')
            self.rect.move_ip(playerSpeed*math.sin(math.pi/4), playerSpeed*math.sin(math.pi/4))
        elif aHeld and self.rect.left>10:
            self.image = pygame.image.load('MainChLeft.png')
            self.rect.move_ip(-playerSpeed, 0)
        elif dHeld and self.rect.right<WIDTH-10:
#             self.image = pygame.image.load('MainChLeft.png')
            self.rect.move_ip(playerSpeed, 0)
        elif wHeld and self.rect.top>10:
            self.image = pygame.image.load('MainCh.png')
            self.rect.move_ip(0, -playerSpeed)
        elif sHeld and self.rect.bottom<HEIGHT-10:
#             self.image = pygame.image.load('MainChLeft.png')
            self.rect.move_ip(0, playerSpeed)
        

            
def rockPaperScissor(money):
    screen.fill((0,0,0))

isPlaying = True

goblin1 = Goblin()

goblins = pygame.sprite.Group()
goblins.add(goblin1)

mainCh = MainCh()

fontG = pygame.font.SysFont('comicsansm', 72)

money = 50


def mainMenu():
    pygame.display.set_caption('Main Menu')
    
    while True:
        screen.fill('black')
        
        menuMousePos = pygame.mouse.get_pos()
        
        menuText = fontG.render('MAIN MENU', True, 'white')
        menuRect = menuText.get_rect(center=(500, 100))
        
        playButton = button.Button(image=pygame.image.load('playBut.png'), pos=(500, 250),
                                   textInput='PLAY', font=fontG, baseColor='#d7fcd4', hoveringColor='White')
        quitButton = button.Button(image=pygame.image.load('playBut.png'), pos=(500, 400),
                                   textInput='QUIT', font=fontG, baseColor='#d7fcd4', hoveringColor='White')
        
        screen.blit(menuText, menuRect)
        
        playButton.changeColor(menuMousePos)
        playButton.update(screen)
        quitButton.changeColor(menuMousePos)
        quitButton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(menuMousePos):
                    play()
                if quitButton.checkForInput(menuMousePos):
                    pygame.quit()
                    sys.exit()
                    
                    
        pygame.display.flip()
        clock.tick(fps)


def play():

    while isPlaying:    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit
                if event.key == pygame.K_ESCAPE:
                    pauseMenu()
                    
        screen.fill((255,255,255))
                    
                
        screen.blit(mainCh.image, mainCh.rect)
        mainCh.move()
        screen.blit(goblin1.image, goblin1.rect)
        
        if pygame.sprite.spritecollideany(mainCh, goblins):
            game1(screen, WIDTH, HEIGHT)
                
        pygame.display.flip()
        clock.tick(fps)
        
        
def pauseMenu():
    pygame.display.set_caption('Pause Menu')
    
    while True:
        screen.fill('black')
        
        pauseMousePos = pygame.mouse.get_pos()
        
        pauseText = fontG.render('PAUSE MENU', True, 'white')
        pauseRect = pauseText.get_rect(center=(500, 100))
        
        continueButton = button.Button(image=pygame.image.load('playBut.png'), pos=(500, 250),
                                   textInput='PLAY', font=fontG, baseColor='#d7fcd4', hoveringColor='White')
        mainMenuButton = button.Button(image=pygame.image.load('playBut.png'), pos=(500, 400),
                                   textInput='MAIN MENU', font=fontG, baseColor='#d7fcd4', hoveringColor='White')
        quitToMainMenuButton = button.Button(image=pygame.image.load('playBut.png'), pos=(500, 550),
                                   textInput='QUIT', font=fontG, baseColor='#d7fcd4', hoveringColor='White')
        
        screen.blit(pauseText, pauseRect)

        continueButton.changeColor(pauseMousePos)
        continueButton.update(screen)
        mainMenuButton.changeColor(pauseMousePos)
        mainMenuButton.update(screen)
        quitToMainMenuButton.changeColor(pauseMousePos)
        quitToMainMenuButton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continueButton.checkForInput(pauseMousePos):
                    play()
                if mainMenuButton.checkForInput(pauseMousePos):
                    mainMenu()
                if quitToMainMenuButton.checkForInput(pauseMousePos):
                    pygame.quit()
                    sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    play()
                    
        pygame.display.flip()
        clock.tick(fps)
        



mainMenu()
