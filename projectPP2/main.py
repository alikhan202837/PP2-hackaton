import pygame, sys
from pygame.locals import *
import time
import math
import button
import goblin
from mainCh import MainCh
from random import randrange, choice, randint, shuffle


pygame.init()


fps = 60
clock = pygame.time.Clock()
W, H = 1000, 570
screen = pygame.display.set_mode((W,H))
screen.fill((255,255,255))
pygame.display.set_caption("Game")
barBg = pygame.image.load('image\\bar.png')
mainMenuBg = pygame.image.load('image\\MainMenuBg.png')
mainMenuBg = pygame.transform.scale(mainMenuBg, (1000, 570))
playerSpeed = 10
fontMain = pygame.font.Font('fonts\Minecraft.ttf', 60)
fontMoney = pygame.font.Font('fonts\Minecraft.ttf', 45)
fontIntro = pygame.font.Font('fonts\Minecraft.ttf', 30)

txtWithMoney = open('money.txt', 'r')
money = txtWithMoney.read()
txtWithMoney.close()
isFirstTimeTxt = open('isFirstTime.txt', 'r')
isFirstTime = isFirstTimeTxt.read()
isFirstTimeTxt.close()
introText = fontIntro.render("afssafsgsdglkfjidlvmemrdlfjelkdvdmskjgdlgdjlgkjglsidgh", True, 'white')

moneyText = fontMoney.render(money, True, 'white')
moneyTextRect = moneyText.get_rect()
lostText = fontMain.render('You Lost', True, 'red')
lostTextRect = lostText.get_rect()
lostTextRect.center = (500, 285)
wonText = fontMain.render('You Won', True, 'green')
wonTextRect = wonText.get_rect()
wonTextRect.center = (500, 285)

goblin1 = goblin.Goblin1()
golbins1 = pygame.sprite.Group()
golbins1.add(goblin1)
goblin2 = goblin.Goblin2()
golbins2 = pygame.sprite.Group()
golbins2.add(goblin2)
goblin3 = goblin.Goblin3()
golbins3 = pygame.sprite.Group()
golbins3.add(goblin3)
mainCh = MainCh()


game_score1 = 0
index = -1
indexOfRandomCard = -1
attempts = 3


def totalLoss():
    while True:
        screen.fill('black')
        
        pauseMousePos = pygame.mouse.get_pos()
        
        pauseText = fontMain.render('YOU LOST', True, 'white')
        pauseRect = pauseText.get_rect(center=(500, 100))
        
        mainMenuButton = button.Button(image=pygame.image.load('image\\button.png'), pos=(500, 250),
                                   textInput='MAIN MENU', font=fontMain, baseColor='#d7fcd4', hoveringColor='White')
        quitToMainMenuButton = button.Button(image=pygame.image.load('image\\button.png'), pos=(500, 400),
                                   textInput='QUIT', font=fontMain, baseColor='#d7fcd4', hoveringColor='White')
        
        screen.blit(pauseText, pauseRect)

        mainMenuButton.changeColor(pauseMousePos)
        mainMenuButton.update(screen)
        quitToMainMenuButton.changeColor(pauseMousePos)
        quitToMainMenuButton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                txtWithMoney = open('money.txt', 'w')
                txtWithMoney.write('50')
                txtWithMoney.close()
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mainMenuButton.checkForInput(pauseMousePos):
                    txtWithMoney = open('money.txt', 'w')
                    txtWithMoney.write('50')
                    txtWithMoney.close()
                    mainMenu()
                if quitToMainMenuButton.checkForInput(pauseMousePos):
                    txtWithMoney = open('money.txt', 'w')
                    txtWithMoney.write('50')
                    txtWithMoney.close()
                    pygame.quit()
                    sys.exit()
            
                    
        pygame.display.flip()
        clock.tick(fps)

def mainMenu():
    pygame.display.set_caption('Main Menu')
    mainMusic = pygame.mixer.Sound("sound/MusicBar.mp3")
    mainMusic.play(-1)
    
    
    global money
    while True:
        
        
        screen.fill('black')
        screen.blit(mainMenuBg, (0,0))
        
        menuMousePos = pygame.mouse.get_pos()
        
        menuText = fontMain.render('MAIN MENU', True, 'white')
        menuRect = menuText.get_rect(center=(500, 100))
        
        buttonton = button.Button(image=pygame.image.load('image\\button.png'), pos=(500, 250),
                                   textInput='PLAY', font=fontMain, baseColor='#d7fcd4', hoveringColor='White')
        quitButton = button.Button(image=pygame.image.load('image\\button.png'), pos=(500, 400),
                                   textInput='QUIT', font=fontMain, baseColor='#d7fcd4', hoveringColor='White')
        
        screen.blit(menuText, menuRect)
        
        buttonton.changeColor(menuMousePos)
        buttonton.update(screen)
        quitButton.changeColor(menuMousePos)
        quitButton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                txtWithMoney = open('money.txt', 'w')
                txtWithMoney.write(money)
                txtWithMoney.close()
                pygame.quit()
                sys.exit()
                
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttonton.checkForInput(menuMousePos):
                    mainMusic.stop()
                    play()
                if quitButton.checkForInput(menuMousePos):
                    mainMusic.stop()
                    txtWithMoney = open('money.txt', 'w')
                    txtWithMoney.write(money)
                    txtWithMoney.close()
                    pygame.quit()
                    sys.exit()
                    
                    
        pygame.display.flip()
        clock.tick(fps)
        
def firstEnter():
    global isFirstTime
    global introText
    while True:
        if int(money)<=0:
            totalLoss()
        
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        txtWithMoney = open('isFirstTime.txt', 'w')
                        txtWithMoney.write("False")
                        txtWithMoney.close()
                        print('sadsa')
                        isFirstTime = 'False'
                        play()
                    
        screen.blit(introText, (0,0))


def play():
    global isFirstTime
    moneyText = fontMoney.render(money, True, 'white')
    mainMusic = pygame.mixer.Sound("sound/MusicBar.mp3")
    mainMusic.play(-1)
    
#     if isFirstTime == 'True':
#         firstEnter()
    
    while True:
        screen.fill((255,255,255))
        screen.blit(barBg, (0,0))
        screen.blit(moneyText, (900, 10))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                txtWithMoney = open('money.txt', 'w')
                txtWithMoney.write(money)
                txtWithMoney.close()
                pygame.quit()
                sys.exit
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    txtWithMoney = open('money.txt', 'w')
                    txtWithMoney.write(money)
                    txtWithMoney.close()
                    pygame.quit()
                    sys.exit
                if event.key == pygame.K_ESCAPE:
                    pauseMenu()
                    
                    
                
        screen.blit(mainCh.image, mainCh.rect)
        mainCh.move()
        screen.blit(goblin1.image, goblin1.rect)
        screen.blit(goblin2.image, goblin2.rect)
        screen.blit(goblin3.image, goblin3.rect)
        
        if pygame.sprite.spritecollideany(mainCh, golbins1):
            mainMusic.stop()
            game1(screen, W, H)
            
        if pygame.sprite.spritecollideany(mainCh, golbins2):
            mainMusic.stop()
            game2(screen, W, H)
                
                
        pygame.display.flip()
        clock.tick(fps)
        
        
def pauseMenu():
    pygame.display.set_caption('Pause Menu')
    
    while True:
        screen.fill('black')
        
        pauseMousePos = pygame.mouse.get_pos()
        
        pauseText = fontMain.render('PAUSE MENU', True, 'white')
        pauseRect = pauseText.get_rect(center=(500, 100))
        
        continueButton = button.Button(image=pygame.image.load('image\\button.png'), pos=(500, 250),
                                   textInput='PLAY', font=fontMain, baseColor='#d7fcd4', hoveringColor='White')
        mainMenuButton = button.Button(image=pygame.image.load('image\\button.png'), pos=(500, 350),
                                   textInput='MAIN MENU', font=fontMain, baseColor='#d7fcd4', hoveringColor='White')
        quitToMainMenuButton = button.Button(image=pygame.image.load('image\\button.png'), pos=(500, 450),
                                   textInput='QUIT', font=fontMain, baseColor='#d7fcd4', hoveringColor='White')
        
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
                txtWithMoney.write(money)
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
                    txtWithMoney.write(money)
                    txtWithMoney.close()
                    pygame.quit()
                    sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    play()
                    
        pygame.display.flip()
        clock.tick(fps)
        
def game1(display, W, H):
    game1Music = pygame.mixer.Sound("sound/MusicVagonetka.mp3")
    game1Music.play(-1)
    global game_score1
    game_score1 = 0
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

    score_font = pygame.font.Font('fonts\Minecraft.ttf', 50)

    # functions with collisions and creating and sound 
    def catch():
        sound = pygame.mixer.Sound("sound/catch.mp3")
        sound.play()
    def laugh():
        sound = pygame.mixer.Sound("sound/laugh.mp3")
        sound.play()

    def createCoin():
        x = randrange(20, W-20)
        speed = randrange(7,10)

        return Coin(coin_image, x, 20, speed, coins)
    
    def collideCoin():
        global game_score1
        for coin in coins:
            if telega_rect.collidepoint(coin.rect.centerx, coin.rect.top):
                catch()
                game_score1 += 1
                coin.kill()

    def createEnemy():
        x = randrange(telega_rect.x-20, telega_rect.x+20)
        speed = 10

        return Enemy(enemy_image, x, 20, speed, enemies)
    
    def collideEnemy(game1Music):
        global game_score1
        global money 
        for enemy in enemies:
            if telega_rect.collidepoint(enemy.rect.centerx, enemy.rect.top):
                laugh()
                money = str(int(money)-10)
                if int(money)<=0:
                    mainCh.rect.center = (900, 285)
                    game1Music.stop()
                    totalLoss()
                txtWithMoney = open('money.txt', 'w')
                txtWithMoney.write(money)
                txtWithMoney.close()
                game1Music.stop()
                screen.fill((0,0,0))
                screen.blit(lostText, lostTextRect)
                mainCh.rect.center = (900, 285)
                pygame.display.update()
                time.sleep(1.5)
                play()
                enemy.kill()
            
    # main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.USEREVENT:
                a = choice([1,2,3,4,5,6,7,8,9])
                if a in [1,3,4,5,6,7]:
                    createCoin()
                if a in [2,8,9]:
                    createEnemy()
            
                    
        if game_score1>=15:
            global money 
            money = str(int(money)+10)
            txtWithMoney = open('money.txt', 'w')
            txtWithMoney.write(money)
            txtWithMoney.close()
            game1Music.stop()
            screen.fill((0,0,0))
            screen.blit(wonText, wonTextRect)
            pygame.display.update()
            game_score = 0
            mainCh.rect.center = (900, 285)
            time.sleep(1.5)
            play()
            enemy.kill()
        
        # move of the telega
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and telega_rect.left >= 0:
            telega_rect.centerx -= telega_speed
        if pressed[pygame.K_RIGHT] and telega_rect.right <= W:
            telega_rect.centerx += telega_speed
    
        collideCoin()
        collideEnemy(game1Music)

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
        
def game2(display, W, H):
    game2Music = pygame.mixer.Sound('sound\MusicCards.mp3')
    game2Music.play(-1)
    global index
    global indexOfRandomCard
    index = -1
    indexOfRandomCard = -1
    global money
    global attempts
    
    screen = pygame.display.set_mode((W, H))
    
    # Class Card
    class Card(pygame.sprite.Sprite):
        def __init__(self, image, x, y):
            pygame.sprite.Sprite.__init__(self)

            self.image = image
            self.rect = self.image.get_rect(topleft = (x,y))
        
    # Background
    tableBackGround = pygame.image.load("image/3game/21table.png")
    
    # Cards
    cardBackImage = pygame.image.load("image/3game/cardback.png")
    cardBackImage = pygame.transform.scale(cardBackImage, (50, 80))
    cardsBACK = list()
    temp = 0
    for i in range(8):
        card = Card(cardBackImage, 100 + temp, H//2)
        cardsBACK.append(card)
        temp += 105

    # Open cards - создание 
    cardOpenImages = list()

    indexOfRandomCard = choice([0,1,2,3,4,5,6,7])
    cards = [i for i in range(2, 10	)]
    shuffle(cards)
    for i in cards:
        card = pygame.image.load(f"image/3game/card{i}.png")
        card = pygame.transform.scale(card, (50, 80))
        cardOpenImages.append(card)    
    w = 0
#     while len(cardOpenImages) != 8:
#         q = randint(2,9)
#         if w == 1 and q == indexOfRandomCard:
#             continue
#         if q == indexOfRandomCard and w == 0:
#             w=1
#         
#         iList = list()
#         if q not in iList:
#             iList.append(q)
#             card = pygame.image.load(f"image/3game/card{q}.png")
#             card = pygame.transform.scale(card, (50, 80))
#             cardOpenImages.append(card)
#         else:
#             continue
        
        
    # Open cards rects
    cardsOPEN = list()
    temp = 0
    for i in range(8):
        card = Card(cardOpenImages[i], 100 + temp, H//2)
        cardsOPEN.append(card)
        temp += 105
    

    def collisionWithCards(posMouse):
        global index
        for i in range(8):
            if cardsBACK[i].rect.collidepoint(posMouse):
                index = i
            
    # Random Card
    
    randomCardBack = Card(cardBackImage, W//2 - 25, 70)
    randomCardOpen = Card(cardOpenImages[indexOfRandomCard], W//2 - 25, 70)
    
    

    prev_index = 0

    while True:
        
        posMouse = pygame.mouse.get_pos()
        
        
        attemptsText = fontMoney.render(f'Attempts: {attempts}', True, 'white')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                collisionWithCards(posMouse)
                print(index)
                print(indexOfRandomCard)
                if index!=indexOfRandomCard and index!=-1 and index != prev_index:
                    prev_index = index
                    attempts-=1
                    
        
        # output
        screen.blit(tableBackGround, (0,0))
        screen.blit(randomCardBack.image, randomCardBack.rect)
        for i in range(8):
            screen.blit(cardsBACK[i].image, cardsBACK[i].rect)

        if index != -1:
            screen.blit(cardsOPEN[index].image, cardsOPEN[index].rect)
            screen.blit(randomCardOpen.image, randomCardOpen.rect)
        
            
        
        if attempts == 0: 
            money = str(int(money)-20)
            if int(money)<=0:
                mainCh.rect.center = (900, 285)
                totalLoss()
            txtWithMoney = open('money.txt', 'w')
            txtWithMoney.write(money)
            txtWithMoney.close()
            game2Music.stop()
            attempts = 3
            index = -1
            indexOfRandomCard = -1
            mainCh.rect.center = (900, 285)
            screen.fill((0,0,0))
            screen.blit(lostText, lostTextRect)
            pygame.display.update()
            print('you failed')
            time.sleep(1)
            play()
        elif cardsOPEN[index].image == randomCardOpen.image: 
            money = str(int(money)+20)
            txtWithMoney = open('money.txt', 'w')
            txtWithMoney.write(money)
            txtWithMoney.close()
            game2Music.stop()
            attempts = 3
            index = -1
            indexOfRandomCard = -1
            mainCh.rect.center = (900, 285)
            screen.fill((0,0,0))
            screen.blit(wonText, wonTextRect)
            pygame.display.update()
            print("congrats!!!")
            time.sleep(1)
            play()

        display.blit(screen, (0,0))
        
        screen.blit(attemptsText, (10,10))
        pygame.display.update()
        clock.tick(fps)


mainMenu()
