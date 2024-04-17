import pygame, sys
from pygame.locals import *
import math
import button
from goblin import Goblin
from mainCh import MainCh
from random import randrange, choice

pygame.init()


fps = 60
clock = pygame.time.Clock()
W, H = 1000, 570
screen = pygame.display.set_mode((W,H))
screen.fill((255,255,255))
pygame.display.set_caption("Game")
game_score1 = 0


playerSpeed = 10

# class Goblin(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load('image\goblin.png')
#         self.rect = self.image.get_rect()
#         self.rect.center = (500, 300)
             
# class MainCh(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load('image\MainCh.png')
#         self.rect = self.image.get_rect()
#         
#     def move(self):
#         pressed  = pygame.key.get_pressed()
#         aHeld = pressed[pygame.K_a]
#         dHeld = pressed[pygame.K_d]
#         sHeld = pressed[pygame.K_s]
#         wHeld = pressed[pygame.K_w]
#         
#         if aHeld and wHeld and self.rect.left>10 and self.rect.top>10:
# #             self.image = pygame.image.load('MainChLeftUp.png')
#             self.rect.move_ip(-playerSpeed*math.sin(math.pi/4), -playerSpeed*math.sin(math.pi/4))
#         elif aHeld and sHeld and self.rect.left>10 and self.rect.bottom<H-10:
# #             self.image = pygame.image.load('MainChLeftDown.png')
#             self.rect.move_ip(-playerSpeed*math.sin(math.pi/4), playerSpeed*math.sin(math.pi/4))
#         elif dHeld and wHeld and self.rect.right<W-10 and self.rect.top>10:
# #             self.image = pygame.image.load('MainChRightUp.png')
#             self.rect.move_ip(playerSpeed*math.sin(math.pi/4), -playerSpeed*math.sin(math.pi/4))
#         elif dHeld and sHeld and self.rect.right<W-10 and self.rect.bottom<H-10:
# #             self.image = pygame.image.load('MainChRightDown.png')
#             self.rect.move_ip(playerSpeed*math.sin(math.pi/4), playerSpeed*math.sin(math.pi/4))
#         elif aHeld and self.rect.left>10:
#             self.image = pygame.image.load('image\MainChLeft.png')
#             self.rect.move_ip(-playerSpeed, 0)
#         elif dHeld and self.rect.right<W-10:
# #             self.image = pygame.image.load('MainChLeft.png')
#             self.rect.move_ip(playerSpeed, 0)
#         elif wHeld and self.rect.top>10:
#             self.image = pygame.image.load('image\MainCh.png')
#             self.rect.move_ip(0, -playerSpeed)
#         elif sHeld and self.rect.bottom<H-10:
# #             self.image = pygame.image.load('MainChLeft.png')
#             self.rect.move_ip(0, playerSpeed)
#         

            
def rockPaperScissor(money):
    screen.fill((0,0,0))

isPlaying = True

goblin1 = Goblin()

goblins = pygame.sprite.Group()
goblins.add(goblin1)

mainCh = MainCh()

fontG = pygame.font.SysFont('comicsansm', 72)
txtWithMoney = open('money.txt', 'r')
money = int(txtWithMoney.read())
txtWithMoney.close()


def mainMenu():
    pygame.display.set_caption('Main Menu')
    
    while True:
        screen.fill('black')
        
        menuMousePos = pygame.mouse.get_pos()
        
        menuText = fontG.render('MAIN MENU', True, 'white')
        menuRect = menuText.get_rect(center=(500, 100))
        
        playButton = button.Button(image=pygame.image.load('image\playBut.png'), pos=(500, 250),
                                   textInput='PLAY', font=fontG, baseColor='#d7fcd4', hoveringColor='White')
        quitButton = button.Button(image=pygame.image.load('image\playBut.png'), pos=(500, 400),
                                   textInput='QUIT', font=fontG, baseColor='#d7fcd4', hoveringColor='White')
        
        screen.blit(menuText, menuRect)
        
        playButton.changeColor(menuMousePos)
        playButton.update(screen)
        quitButton.changeColor(menuMousePos)
        quitButton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                txtWithMoney = open('money.txt', 'w')
                txtWithMoney.write(str(money))
                txtWithMoney.close()
                pygame.quit()
                sys.exit()
                
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(menuMousePos):
                    play()
                if quitButton.checkForInput(menuMousePos):
                    txtWithMoney = open('money.txt', 'w')
                    txtWithMoney.write(str(money))
                    txtWithMoney.close()
                    pygame.quit()
                    sys.exit()
                    
                    
        pygame.display.flip()
        clock.tick(fps)


def play():

    while True:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                txtWithMoney = open('money.txt', 'w')
                txtWithMoney.write(str(money))
                txtWithMoney.close()
                pygame.quit()
                sys.exit
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    txtWithMoney = open('money.txt', 'w')
                    txtWithMoney.write(str(money))
                    txtWithMoney.close()
                    pygame.quit()
                    sys.exit
                if event.key == pygame.K_ESCAPE:
                    pauseMenu()
                    
        screen.fill((255,255,255))
                    
                
        screen.blit(mainCh.image, mainCh.rect)
        mainCh.move()
        screen.blit(goblin1.image, goblin1.rect)
        
        if pygame.sprite.spritecollideany(mainCh, goblins):
            game1(screen, W, H)
                
        pygame.display.flip()
        clock.tick(fps)
        
        
def pauseMenu():
    pygame.display.set_caption('Pause Menu')
    
    while True:
        screen.fill('black')
        
        pauseMousePos = pygame.mouse.get_pos()
        
        pauseText = fontG.render('PAUSE MENU', True, 'white')
        pauseRect = pauseText.get_rect(center=(500, 100))
        
        continueButton = button.Button(image=pygame.image.load('image\playBut.png'), pos=(500, 250),
                                   textInput='PLAY', font=fontG, baseColor='#d7fcd4', hoveringColor='White')
        mainMenuButton = button.Button(image=pygame.image.load('image\playBut.png'), pos=(500, 350),
                                   textInput='MAIN MENU', font=fontG, baseColor='#d7fcd4', hoveringColor='White')
        quitToMainMenuButton = button.Button(image=pygame.image.load('image\playBut.png'), pos=(500, 450),
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
                txtWithMoney = open('money.txt', 'w')
                txtWithMoney.write(str(money))
                txtWithMoney.close()
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continueButton.checkForInput(pauseMousePos):
                    play()
                if mainMenuButton.checkForInput(pauseMousePos):
                    mainMenu()
                if quitToMainMenuButton.checkForInput(pauseMousePos):
                    txtWithMoney = open('money.txt', 'w')
                    txtWithMoney.write(str(money))
                    txtWithMoney.close()
                    pygame.quit()
                    sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    play()
                    
        pygame.display.flip()
        clock.tick(fps)
        
def game1(display, W, H):
    

    # initial settings
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    

    # classes
    class Coin(pygame.sprite.Sprite):
        def __init__(self, image, x, y, speed, group):
            pygame.sprite.Sprite.__init__(self)
            self.image = image
            self.rect = self.image.get_rect(center = (x,y))
            self.speed = speed
            self.add(group)
        def update(self):
            if self.rect.bottom != H:
                self.rect.bottom += self.speed
            if self.rect.bottom == H:
                self.kill()

    class Enemy(pygame.sprite.Sprite):
        def __init__(self, image, x, y, speed, group):
            pygame.sprite.Sprite.__init__(self)
            self.image = image
            self.rect = self.image.get_rect(center = (x,y))
            self.speed = speed
            self.add(group)
        def update(self):
            if self.rect.bottom != H:
                self.rect.bottom += self.speed
            if self.rect.bottom == H:
                self.kill()
        
    background = pygame.image.load("image/1game/fon_game1.png")

    # telezkha
    telega = pygame.image.load("image/1game/telega.png")
    telega = pygame.transform.scale(telega, (150, 155))
    telega_rect = telega.get_rect(center = (W//2, H - 35))
    telega_speed = 10

    # coins
    coin_image = pygame.image.load("image/1game/coin.png")
    coin_image = pygame.transform.scale(coin_image, (30,30))
    coins = pygame.sprite.Group()

    # enemies
    enemy_image = pygame.image.load("image/1game/goblin.png")
    enemy_image = pygame.transform.scale(enemy_image, (50,40))
    enemies = pygame.sprite.Group()

    score_font = pygame.font.SysFont(None, 50)

    # functions with collisions and creating and sound 
    def catch():
        sound = pygame.mixer.Sound("sound/catch.mp3")
        sound.play()
    def laugh():
        sound = pygame.mixer.Sound("sound/laugh.mp3")
        sound.play()

    def createCoin():
        x = randrange(20, W-20)
        speed = randrange(3,7)

        return Coin(coin_image, x, 20, speed, coins)
    
    def collideCoin():
        global game_score1
        for coin in coins:
            if telega_rect.collidepoint(coin.rect.centerx, coin.rect.top):
                catch()
                game_score1 += 10
                coin.kill()

    def createEnemy():
        x = randrange(20, W-20)
        speed = 10

        return Enemy(enemy_image, x, 20, speed, enemies)
    
    def collideEnemy():
        global game_score1
        for enemy in enemies:
            if telega_rect.collidepoint(enemy.rect.centerx, enemy.rect.top):
                laugh()
                mainCh.rect.x, mainCh.rect.y = 0,0
                play()
                enemy.kill()
            
    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.USEREVENT:
                a = choice([1,2,3,4])
                if a in [1,3,4]:
                    createCoin()
                if a == 2:
                    createEnemy()
            
                    
                        
        
        # move of the telega
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and telega_rect.left >= 0:
            telega_rect.centerx -= telega_speed
        if pressed[pygame.K_RIGHT] and telega_rect.right <= W:
            telega_rect.centerx += telega_speed
    
        collideCoin()
        collideEnemy()

        # output
        screen.blit(background, (0,0))
        score_text = score_font.render(f"{game_score1}", True, (0,255,0))
        screen.blit(score_text, (0,0))
        screen.blit(telega,  telega_rect)

        coins.draw(screen)
        coins.update()
        enemies.draw(screen)
        enemies.update()

        display.blit(screen, (0,0))
        pygame.display.update()
        clock.tick(fps)


mainMenu()
