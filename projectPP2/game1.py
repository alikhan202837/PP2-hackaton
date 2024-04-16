# Задача ловить падающие монеты и когда количсвто очков будет 100 то ты выиграл, но не лови гоблинов
import pygame as py
from random import randrange, choice
py.init()


game_score1 = 0

def game1(display, W, H):

    # initial settings
    py.time.set_timer(py.USEREVENT, 1000)
    clock = py.time.Clock()
    game_surf = py.Surface((W, H))

    # classes
    class Coin(py.sprite.Sprite):
        def __init__(self, image, x, y, speed, group):
            py.sprite.Sprite.__init__(self)
            self.image = image
            self.rect = self.image.get_rect(center = (x,y))
            self.speed = speed
            self.add(group)
        def update(self):
            if self.rect.bottom != H:
                self.rect.bottom += self.speed
            if self.rect.bottom == H:
                self.kill()

    class Enemy(py.sprite.Sprite):
        def __init__(self, image, x, y, speed, group):
            py.sprite.Sprite.__init__(self)
            self.image = image
            self.rect = self.image.get_rect(center = (x,y))
            self.speed = speed
            self.add(group)
        def update(self):
            if self.rect.bottom != H:
                self.rect.bottom += self.speed
            if self.rect.bottom == H:
                self.kill()
        
    background = py.image.load("image/1game/fon_game1.png")

    # telezkha
    telega = py.image.load("image/1game/telega.png")
    telega = py.transform.scale(telega, (150, 155))
    telega_rect = telega.get_rect(center = (W//2, H - 35))
    telega_speed = 10

    # coins
    coin_image = py.image.load("image/1game/coin.png")
    coin_image = py.transform.scale(coin_image, (30,30))
    coins = py.sprite.Group()

    # enemies
    enemy_image = py.image.load("image/1game/goblin.png")
    enemy_image = py.transform.scale(enemy_image, (50,40))
    enemies = py.sprite.Group()

    score_font = py.font.SysFont(None, 50)

    # functions with collisions and creating and sound 
    def catch():
        sound = py.mixer.Sound("sound/catch.mp3")
        sound.play()
    def laugh():
        sound = py.mixer.Sound("sound/laugh.mp3")
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
                game_score1 -= 50
                enemy.kill()
            
    # main loop
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                exit()
            if event.type == py.USEREVENT:
                a = choice([1,2,3,4])
                if a in [1,3,4]:
                    createCoin()
                if a == 2:
                    createEnemy()
        
        # move of the telega
        pressed = py.key.get_pressed()
        if pressed[py.K_LEFT] and telega_rect.left >= 0:
            telega_rect.centerx -= telega_speed
        if pressed[py.K_RIGHT] and telega_rect.right <= W:
            telega_rect.centerx += telega_speed
    
        collideCoin()
        collideEnemy()

        # output
        game_surf.blit(background, (0,0))
        score_text = score_font.render(f"{game_score1}", True, (0,255,0))
        game_surf.blit(score_text, (0,0))
        game_surf.blit(telega,  telega_rect)

        coins.draw(game_surf)
        coins.update()
        enemies.draw(game_surf)
        enemies.update()

        display.blit(game_surf, (0,0))
        py.display.update()
        clock.tick(60)