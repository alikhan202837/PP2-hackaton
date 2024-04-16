import pygame as py
from game1 import game1
py.init()

# Main display
W, H = 1000, 570
display = py.display.set_mode((W, H))
py.display.set_caption("Clash Royale")
done = False
clock = py.time.Clock()
FPS = 60


while not done:
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True
    
    game1(display, W, H)
    # py.display.update()
    # clock.tick(FPS)