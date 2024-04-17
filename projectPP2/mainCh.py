import pygame
import math

class MainCh(pygame.sprite.Sprite):
    
    
    def __init__(self):
        self.playerSpeed = 10
        self.W = 1000
        self.H = 570
        super().__init__()
        self.image = pygame.image.load('image\MainCh.png')
        self.rect = self.image.get_rect()
        
    def move(self):
        pressed  = pygame.key.get_pressed()
        aHeld = pressed[pygame.K_a]
        dHeld = pressed[pygame.K_d]
        sHeld = pressed[pygame.K_s]
        wHeld = pressed[pygame.K_w]
        
        if aHeld and wHeld and self.rect.left>10 and self.rect.top>10:
#             self.image = pygame.image.load('MainChLeftUp.png')
            self.rect.move_ip(-self.playerSpeed*math.sin(math.pi/4), -self.playerSpeed*math.sin(math.pi/4))
        elif aHeld and sHeld and self.rect.left>10 and self.rect.bottom<self.H-10:
#             self.image = pygame.image.load('MainChLeftDown.png')
            self.rect.move_ip(-self.playerSpeed*math.sin(math.pi/4), self.playerSpeed*math.sin(math.pi/4))
        elif dHeld and wHeld and self.rect.right<self.W-10 and self.rect.top>10:
#             self.image = pygame.image.load('MainChRightUp.png')
            self.rect.move_ip(self.playerSpeed*math.sin(math.pi/4), -self.playerSpeed*math.sin(math.pi/4))
        elif dHeld and sHeld and self.rect.right<self.W-10 and self.rect.bottom<self.H-10:
#             self.image = pygame.image.load('MainChRightDown.png')
            self.rect.move_ip(self.playerSpeed*math.sin(math.pi/4), self.playerSpeed*math.sin(math.pi/4))
        elif aHeld and self.rect.left>10:
            self.image = pygame.image.load('image\MainChLeft.png')
            self.rect.move_ip(-self.playerSpeed, 0)
        elif dHeld and self.rect.right<self.W-10:
#             self.image = pygame.image.load('MainChLeft.png')
            self.rect.move_ip(self.playerSpeed, 0)
        elif wHeld and self.rect.top>10:
            self.image = pygame.image.load('image\MainCh.png')
            self.rect.move_ip(0, -self.playerSpeed)
        elif sHeld and self.rect.bottom<self.H-10:
#             self.image = pygame.image.load('MainChLeft.png')
            self.rect.move_ip(0, self.playerSpeed)
        
