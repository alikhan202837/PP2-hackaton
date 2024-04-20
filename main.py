import pygame, sys
from pygame.locals import *
import time
import math
import button
import goblin
from mainCh import MainCh
from random import randrange, choice, randint, shuffle


pygame.init()

#general settings
fps = 60
clock = pygame.time.Clock()
W, H = 1000, 570
screen = pygame.display.set_mode((W,H))
screen.fill((255,255,255))
pygame.display.set_caption("Loss of Coins")

#menu settings
mainMenuBg = pygame.image.load('image\\MainMenuBg.png')
mainMenuBg = pygame.transform.scale(mainMenuBg, (1000, 570))
fontMain = pygame.font.Font('fonts\Minecraft.ttf', 60)

#bar settings
barBg = pygame.image.load('image\\bar.png')
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
playerSpeed = 10
fontMoney = pygame.font.Font('fonts\Minecraft.ttf', 45)


#getting amount of money from money.txt
txtWithMoney = open('money.txt', 'r')
money = txtWithMoney.read()
txtWithMoney.close()


moneyText = fontMoney.render(money, True, 'white')
moneyTextRect = moneyText.get_rect()
lostText = fontMain.render('You Lost', True, 'red')
lostTextRect = lostText.get_rect()
lostTextRect.center = (500, 285)
wonText = fontMain.render('You Won', True, 'green')
wonTextRect = wonText.get_rect()
wonTextRect.center = (500, 285)



#variables for 1st game
game_score1 = 0
index = -1
indexOfRandomCard = -1
attempts2 = 3

#variables for 3rd game
yourChoice = None
goblinChoice = None
game_score3 = 0
goblin_score3 = 0
attempts3 = 5
fontGame3 = pygame.font.Font('fonts\Minecraft.ttf', 60)
choose_text = fontGame3.render("Choose One of them!!!", True, "white")
win_text = fontGame3.render("Good job!", True, "light green")
lose_text = fontGame3.render("Loser(", True, "red")
win_text_rect = win_text.get_rect(center = (W//2, 80))
lose_text_rect = lose_text.get_rect(center = (W//2, 80))
draw_text = fontGame3.render("Draw!", True, "white")
draw_text_rect = draw_text.get_rect(center = (W//2, 80))


#function for completing or failing game
def total(text):
    while True:
        screen.fill('black')
        
        pauseMousePos = pygame.mouse.get_pos()
        
        pauseText = fontMain.render(text, True, 'white')
        pauseRect = pauseText.get_rect(center=(500, 100))
        
        quitToMainMenuButton = button.Button(image=pygame.image.load('image\\button.png'), pos=(500, 320),
                                   textInput='QUIT', font=fontMain, baseColor='#d7fcd4', hoveringColor='White')
        
        screen.blit(pauseText, pauseRect)

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
                if quitToMainMenuButton.checkForInput(pauseMousePos):
                    txtWithMoney = open('money.txt', 'w')
                    txtWithMoney.write('50')
                    txtWithMoney.close()
                    pygame.quit()
                    sys.exit()
            
                    
        pygame.display.flip()
        clock.tick(fps)

#function for failing game
def totalLoss():
    total("YOU LOST, TRY AGAIN")

#function for competing game
def totalWin():
    total("YOU COMPLETED GAME")


#function for main menu
def mainMenu():
    mainMusic = pygame.mixer.Sound("sound/MusicBar.mp3")
    mainMusic.play(-1)
    
    
    global money
    while True:
        
        
        screen.fill('black')
        screen.blit(mainMenuBg, (0,0))
        
        menuMousePos = pygame.mouse.get_pos()
        
        menuText = fontMain.render('LOSS OF COINS', True, 'white')
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
        
#function for bar (lobby)
def play():
    txtWithMoney = open('money.txt', 'r')
    money = txtWithMoney.read()
    txtWithMoney.close()
    moneyText = fontMoney.render(money, True, 'white')
    mainMusic = pygame.mixer.Sound("sound/MusicBar.mp3")
    mainMusic.play(-1)
    
    
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
                    mainMusic.stop()
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
            
        if pygame.sprite.spritecollideany(mainCh, golbins3):
            mainMusic.stop()
            game3(screen, W, H)
                
                
        pygame.display.flip()
        clock.tick(fps)
        
#function for pause menu
def pauseMenu():

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
    
#function of 1st game
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
        speed = 17

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
            if int(money)>=500:
                    mainCh.rect.center = (900, 285)
                    game1Music.stop()
                    totalWin()
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
    
#function for 2nd game
def game2(display, W, H):
    game2Music = pygame.mixer.Sound('sound\MusicCards.mp3')
    game2Music.play(-1)
    global index
    global indexOfRandomCard
    index = -1
    indexOfRandomCard = -1
    global money
    global attempts2
    
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
        
        
        attempts2Text = fontMoney.render(f'attempts2: {attempts2}', True, 'white')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                collisionWithCards(posMouse)
                print(index)
                print(indexOfRandomCard)
                if index!=indexOfRandomCard and index!=-1 and index != prev_index:
                    prev_index = index
                    attempts2-=1
                    
        
        # output
        screen.blit(tableBackGround, (0,0))
        screen.blit(randomCardBack.image, randomCardBack.rect)
        for i in range(8):
            screen.blit(cardsBACK[i].image, cardsBACK[i].rect)

        if index != -1:
            screen.blit(cardsOPEN[index].image, cardsOPEN[index].rect)
            screen.blit(randomCardOpen.image, randomCardOpen.rect)
        
            
        
        if attempts2 == 0: 
            money = str(int(money)-20)
            if int(money)<=0:
                mainCh.rect.center = (900, 285)
                game2Music.stop()
                totalLoss()
            txtWithMoney = open('money.txt', 'w')
            txtWithMoney.write(money)
            txtWithMoney.close()
            game2Music.stop()
            attempts2 = 3
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
            if int(money)>=500:
                    mainCh.rect.center = (900, 285)
                    game2Music.stop()
                    totalWin()
            txtWithMoney = open('money.txt', 'w')
            txtWithMoney.write(money)
            txtWithMoney.close()
            game2Music.stop()
            attempts2 = 3
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
        
        screen.blit(attempts2Text, (10,10))
        pygame.display.update()
        clock.tick(fps)
      
#function for 3rd game
def game3(display, W, H):
    global yourChoice, goblinChoice, game_score3, started, goblin_score3, money

    game3Music = pygame.mixer.Sound("sound/MusicSuefa.mp3")
    game3Music.play(-1)

    game_surf = pygame.Surface((W, H))

    # classes
    # 1
    class Paper(pygame.sprite.Sprite):
        def __init__(self, image, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = image
            self.rect = self.image.get_rect(topleft = (x, y))
    # 2
    class Scissors(pygame.sprite.Sprite):
        def __init__(self, image, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = image
            self.rect = self.image.get_rect(topleft = (x, y))
    # 3
    class Rock(pygame.sprite.Sprite):
        def __init__(self, image, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = image
            self.rect = self.image.get_rect(topleft = (x, y))

# Downloading images and setting class objects
    # background
    background = pygame.image.load("image/2game/stolsulifa.png")

    # images of the Hero
    paperHeroImage = pygame.image.load("image/2game/PaperHero.png")
    scissorsHeroImage = pygame.image.load("image/2game/ScissorsHero.png")
    fistHeroImage = pygame.image.load("image/2game/FistHero.png")

    paperOutput = pygame.image.load("image/2game/paper.png")
    scissorsOutput = pygame.image.load("image/2game/scissors.png")
    fistOutput = pygame.image.load("image/2game/fist.png")

    # images of the Enemy(Goblins)
    paperGoblinImage = pygame.image.load("image/2game/PaperGoblin.png")
    scissorsGoblinImage = pygame.image.load("image/2game/ScissorsGoblin.png")
    fistGoblinImage = pygame.image.load("image/2game/FistGoblin.png")
    
    # images of the Goblin's choice
    paperGoblinImage_1 = pygame.image.load("image/2game/StolSulifaPaperGoblin.png")
    scissorsGoblinImage_1 = pygame.image.load("image/2game/StolSulifaScissorsGoblin.png")
    fistGoblinImage_1 = pygame.image.load("image/2game/StolSulifaFistGoblin.png")

    # creating rects and hands bt using classes
        # for hero
    paperHero = Paper(paperHeroImage, 0, 50)
    scissorsHero = Scissors(scissorsHeroImage, 25, 230)
    fistHero = Rock(fistHeroImage, 0, 400)
    toolSC = pygame.Surface((165, H))
    toolSC.fill("beige")

    started = False
# Choice of the Hero 
    def collisionWithHands(posMouse):
        global yourChoice, started
        if paperHero.rect.collidepoint(posMouse):
            yourChoice = "paper"
        if scissorsHero.rect.collidepoint(posMouse):
            yourChoice = "scissors"
        if fistHero.rect.collidepoint(posMouse):
            yourChoice = "rock"

        started = True

# Choice of the Goblin
    goblinChoice = choice(["rock", "paper", "scissors"])

    def updateChoice():
        global yourChoice, goblinChoice, started
        yourChoice = None
        goblinChoice = choice(["rock", "paper", "scissors"])
        started = False

    def draw():
        global game_score3, yourChoice, goblinChoice, attempts3, started, goblin_score3
        time.sleep(0.5)
        attempts3 -= 1
        game_surf.blit(draw_text, draw_text_rect)
        started = False

    def win():
        global game_score3, yourChoice, goblinChoice, attempts3, started, goblin_score3
        time.sleep(0.5)
        game_score3 += 1
        attempts3 -= 1
        game_surf.blit(win_text, win_text_rect)
        started = False
    def lose():
        global game_score3, yourChoice, goblinChoice, attempts3, started, goblin_score3
        time.sleep(0.5)
        goblin_score3 += 1
        attempts3 -= 1
        game_surf.blit(lose_text, lose_text_rect)
        started = False

    while True:
        
        if goblin_score3 == 3:
            goblin_score3 = 0
            game_score3 = 0
            money = str(int(money)-30)
            if int(money)<=0:
                mainCh.rect.center = (900, 285)
                game3Music.stop()
                totalLoss()
                
            txtWithMoney = open('money.txt', 'w')
            txtWithMoney.write(money)
            txtWithMoney.close()
            game3Music.stop()
            screen.fill((0,0,0))
            screen.blit(lostText, lostTextRect)
            mainCh.rect.center = (900, 285)
            pygame.display.update()
            time.sleep(1.5)
            play()
            
        if game_score3 == 3:
            goblin_score3 = 0
            game_score3 = 0
            money = str(int(money)+30)
            if int(money)>=500:
                mainCh.rect.center = (900, 285)
                game3Music.stop()
                totalWin()
                
            txtWithMoney = open('money.txt', 'w')
            txtWithMoney.write(money)
            txtWithMoney.close()
            game3Music.stop()
            screen.fill((0,0,0))
            screen.blit(wonText, wonTextRect)
            mainCh.rect.center = (900, 285)
            pygame.display.update()
            time.sleep(1.5)
            play()
        
        
        posMouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                time.sleep(1)
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                collisionWithHands(posMouse)
        
        score_font = fontGame3.render(str(game_score3), True, "green")
        goblin_font = fontGame3.render(str(goblin_score3), True, "green")

        # output

        if yourChoice == None:
            game_surf.blit(background, (0,0))
            game_surf.blit(choose_text, (325, 250))

            toolSC.blit(paperHero.image, paperHero.rect)
            toolSC.blit(scissorsHero.image, scissorsHero.rect)
            toolSC.blit(fistHero.image, fistHero.rect)
            game_surf.blit(toolSC, (0,0))

            game_surf.blit(score_font, (0,0))
            game_surf.blit(goblin_font, (W-30,0))

        elif yourChoice != None:
            if started:
                # hands of goblin
                if goblinChoice == "rock":
                    game_surf.blit(fistGoblinImage_1, (0,0))
                elif goblinChoice == "paper":
                    game_surf.blit(paperGoblinImage_1, (0,0))
                elif goblinChoice == "scissors":
                    game_surf.blit(scissorsGoblinImage_1, (0,0))
                
                # hands of hero
                if yourChoice == "rock":
                    game_surf.blit(fistOutput, (0, 120))
                elif yourChoice == "scissors":
                    game_surf.blit(scissorsOutput, (0,120))
                elif yourChoice == "paper":
                    game_surf.blit(paperOutput, (0,120))

                game_surf.blit(score_font, (0,0))
                game_surf.blit(goblin_font, (W-30,0))


                # check for win or draw or lose
                    # win
                if yourChoice == "rock" and goblinChoice == "scissors":
                    win()
                elif yourChoice == "paper" and goblinChoice == "rock":
                    win()
                elif yourChoice == "scissors" and goblinChoice == "paper":
                    win()

                
                    # draw
                if yourChoice == goblinChoice:
                    draw()

                    # lose
                if yourChoice == "scissors" and goblinChoice == "rock":
                    lose()
                elif yourChoice == "rock" and goblinChoice == "paper":
                    lose()
                elif yourChoice == "paper" and goblinChoice == "scissors":
                    lose()
                
            else:
                updateChoice()
                time.sleep(1)

            print(game_score3, goblin_score3)

        display.blit(game_surf, (0,0)) 
        pygame.display.update()
        clock.tick(fps)

#running main menu function
mainMenu()
