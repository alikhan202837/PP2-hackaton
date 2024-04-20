import pygame
import math

class MainCh(pygame.sprite.Sprite):
    
    def __init__(self):
        self.playerSpeed = 5
        self.W = 1000
        self.H = 570
        super().__init__()
        self.lastDirect = 'left'
        
        
        self.leftSprites = []
        self.leftSprites.append(pygame.image.load('image\chLeft1.png'))
        self.leftSprites.append(pygame.image.load('image\chLeft2.png'))
        self.currentLeft = 0
        self.isLeftAnim = False
        
        
        
        self.rightSprites = []
        self.rightSprites.append(pygame.image.load('image\chRight1.png'))
        self.rightSprites.append(pygame.image.load('image\chRight2.png'))
        self.currentRight = 0
        self.isRightAnim = False
        
        self.upSprites = []
        self.upSprites.append(pygame.image.load('image\chUp1.png'))
        self.upSprites.append(pygame.image.load('image\chUp2.png'))
        self.currentUp = 0
        self.isUpAnim = False
        
        self.downSprites = []
        self.downSprites.append(pygame.image.load('image\chDown1.png'))
        self.downSprites.append(pygame.image.load('image\chDown2.png'))
        self.currentDown = 0
        self.isUpAnim = False
        
        self.image = pygame.image.load('image\chLeft.png')
        self.image = pygame.transform.scale(self.image, (53, 83))
        self.rect = self.image.get_rect()
        self.rect.center = (900, 285)
        
    
        
    def move(self):
        
        def updateLeft():
            if self.isLeftAnim == True:
                self.currentLeft+=0.1
                
                if self.currentLeft >= 2:
                    self.currentLeft = 0
                
                self.image = self.leftSprites[int(self.currentLeft)]
                
        def updateRight():
            if self.isRightAnim == True:
                self.currentRight+=0.1
                
                if self.currentRight >= 2:
                    self.currentRight = 0
                
                self.image = self.rightSprites[int(self.currentRight)]
                
        def updateUp():
            if self.isUpAnim == True:
                self.currentUp+=0.1
                
                if self.currentUp >= 2:
                    self.currentUp = 0
                
                self.image = self.upSprites[int(self.currentUp)]
                
        def updateDown():
            if self.isDownAnim == True:
                self.currentDown+=0.1
                
                if self.currentDown >= 2:
                    self.currentDown = 0
                
                self.image = self.downSprites[int(self.currentDown)]
        
        pressed  = pygame.key.get_pressed()
        aHeld = pressed[pygame.K_a]
        dHeld = pressed[pygame.K_d]
        sHeld = pressed[pygame.K_s]
        wHeld = pressed[pygame.K_w]
        
        if not aHeld and not sHeld and not dHeld and not wHeld:
            if self.lastDirect == 'left':
                self.image = pygame.image.load('image\chLeft.png')
                self.image = pygame.transform.scale(self.image, (53, 83))
            elif self.lastDirect == 'right':
                self.image = pygame.image.load('image\chRight.png')
                self.image = pygame.transform.scale(self.image, (53, 83))
            elif self.lastDirect == 'down':
                self.image = pygame.image.load('image\chDown.png')
                self.image = pygame.transform.scale(self.image, (53, 83))
            elif self.lastDirect == 'up':
                self.image = pygame.image.load('image\chUp.png')
                self.image = pygame.transform.scale(self.image, (53, 83))
                
        
        if aHeld and wHeld and self.rect.left>333 and self.rect.top>130:
            self.isLeftAnim = True
            updateLeft()
            self.lastDirect = 'left'
            self.image = pygame.transform.scale(self.image, (53, 83))
            self.rect.move_ip(-self.playerSpeed*math.sin(math.pi/4), -self.playerSpeed*math.sin(math.pi/4))
        elif aHeld and sHeld and self.rect.left>333 and self.rect.bottom<self.H-130:
            self.isLeftAnim = True
            updateLeft()
            self.lastDirect = 'left'
            self.image = pygame.transform.scale(self.image, (53, 83))
            self.rect.move_ip(-self.playerSpeed*math.sin(math.pi/4), self.playerSpeed*math.sin(math.pi/4))
        elif dHeld and wHeld and self.rect.right<self.W-10 and self.rect.top>130:
            self.isRightAnim = True
            updateRight()
            self.lastDirect = 'right'
            self.image = pygame.transform.scale(self.image, (53, 83))
            self.rect.move_ip(self.playerSpeed*math.sin(math.pi/4), -self.playerSpeed*math.sin(math.pi/4))
        elif dHeld and sHeld and self.rect.right<self.W-10 and self.rect.bottom<self.H-130:
            self.isRightAnim = True
            updateRight()
            self.lastDirect = 'right'
            self.image = pygame.transform.scale(self.image, (53, 83))
            self.rect.move_ip(self.playerSpeed*math.sin(math.pi/4), self.playerSpeed*math.sin(math.pi/4))
        elif aHeld and self.rect.left>333:
            self.isLeftAnim = True
            updateLeft()
            self.lastDirect = 'left'
            self.image = pygame.transform.scale(self.image, (53, 83))
            self.rect.move_ip(-self.playerSpeed, 0)
        elif dHeld and self.rect.right<self.W-10:
            self.isRightAnim = True
            updateRight()
            self.lastDirect = 'right'
            self.image = pygame.transform.scale(self.image, (53, 83))
            self.rect.move_ip(self.playerSpeed, 0)
        elif wHeld and self.rect.top>130:
            self.isUpAnim = True
            updateUp()
            self.lastDirect = 'up'
            self.image = pygame.transform.scale(self.image, (53, 83))
            self.rect.move_ip(0, -self.playerSpeed)
        elif sHeld and self.rect.bottom<self.H-130:
            self.isDownAnim = True
            updateDown()
            self.lastDirect = 'down'
            self.image = pygame.transform.scale(self.image, (53, 83))
            self.rect.move_ip(0, self.playerSpeed)
        
