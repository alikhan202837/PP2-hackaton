import pygame as py
py.init()

# Main display
W, H = 1000,500
display = py.display.set_mode((W, H))
py.display.set_caption("Clash Royale")
done = False
clock = py.time.Clock()
FPS = 60


while not done:
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True
    
    
    py.display.update()
    clock.tick(FPS)