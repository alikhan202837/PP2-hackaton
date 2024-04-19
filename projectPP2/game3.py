import pygame as py
import time
from random import choice
py.init()

W, H = 1000, 570
screen = py.display.set_mode((W, H))
clock = py.time.Clock()
fps = 60

yourChoice = None
goblinChoice = None
game_score3 = 0
attempts = 5

font = py.font.SysFont(None, 60)
choose_text = font.render("Choose One of them!!!", True, "white")
win_text = font.render("Good job!", True, "light green")
lose_text = font.render("Loser(", True, "red")
win_text_rect = win_text.get_rect(center = (W//2, 80))
lose_text_rect = lose_text.get_rect(center = (W//2, 80))
draw_text = font.render("Draw!", True, "white")
draw_text_rect = draw_text.get_rect(center = (W//2, 80))


def game3(display, W, H):
    global yourChoice, goblinChoice, game_score3, started

    game_surf = py.Surface((W, H))

    # classes
    # 1
    class Paper(py.sprite.Sprite):
        def __init__(self, image, x, y):
            py.sprite.Sprite.__init__(self)
            self.image = image
            self.rect = self.image.get_rect(topleft = (x, y))
    # 2
    class Scissors(py.sprite.Sprite):
        def __init__(self, image, x, y):
            py.sprite.Sprite.__init__(self)
            self.image = image
            self.rect = self.image.get_rect(topleft = (x, y))
    # 3
    class Rock(py.sprite.Sprite):
        def __init__(self, image, x, y):
            py.sprite.Sprite.__init__(self)
            self.image = image
            self.rect = self.image.get_rect(topleft = (x, y))

# Downloading images and setting class objects
    # background
    background = py.image.load("image/2game/stolsulifa.png")

    # images of the Hero
    paperHeroImage = py.image.load("image/2game/PaperHero.png")
    scissorsHeroImage = py.image.load("image/2game/ScissorsHero.png")
    fistHeroImage = py.image.load("image/2game/FistHero.png")

    paperOutput = py.image.load("image/2game/paper.png")
    scissorsOutput = py.image.load("image/2game/scissors.png")
    fistOutput = py.image.load("image/2game/fist.png")

    # images of the Enemy(Goblins)
    paperGoblinImage = py.image.load("image/2game/PaperGoblin.png")
    scissorsGoblinImage = py.image.load("image/2game/ScissorsGoblin.png")
    fistGoblinImage = py.image.load("image/2game/FistGoblin.png")
    
    # images of the Goblin's choice
    paperGoblinImage_1 = py.image.load("image/2game/StolSulifaPaperGoblin.png")
    scissorsGoblinImage_1 = py.image.load("image/2game/StolSulifaScissorsGoblin.png")
    fistGoblinImage_1 = py.image.load("image/2game/StolSulifaFistGoblin.png")

    # creating rects and hands bt using classes
        # for hero
    paperHero = Paper(paperHeroImage, 0, 50)
    scissorsHero = Scissors(scissorsHeroImage, 25, 230)
    fistHero = Rock(fistHeroImage, 0, 400)
    toolSC = py.Surface((165, H))
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
        global game_score3, yourChoice, goblinChoice, attempts, started
        time.sleep(0.5)
        attempts -= 1
        game_surf.blit(draw_text, draw_text_rect)
        started = False

    def win():
        global game_score3, yourChoice, goblinChoice, attempts, started
        time.sleep(0.5)
        game_score3 += 1
        attempts -= 1
        game_surf.blit(win_text, win_text_rect)
        started = False
    def lose():
        global game_score3, yourChoice, goblinChoice, attempts, started
        time.sleep(0.5)
        attempts -= 1
        game_surf.blit(lose_text, lose_text_rect)
        started = False

    while True:
        posMouse = py.mouse.get_pos()
        for event in py.event.get():
            if event.type == py.QUIT or attempts == 0:
                time.sleep(1)
                exit()
            if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                collisionWithHands(posMouse)
        
        score_font = font.render(str(game_score3), True, "green")

        # output

        if yourChoice == None:
            game_surf.blit(background, (0,0))
            game_surf.blit(choose_text, (325, 250))

            toolSC.blit(paperHero.image, paperHero.rect)
            toolSC.blit(scissorsHero.image, scissorsHero.rect)
            toolSC.blit(fistHero.image, fistHero.rect)
            game_surf.blit(toolSC, (0,0))

            game_surf.blit(score_font, (0,0))

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

            print(yourChoice, attempts)

        display.blit(game_surf, (0,0)) 
        py.display.update()
        clock.tick(fps)

game3(screen, W, H)

py.quit()
