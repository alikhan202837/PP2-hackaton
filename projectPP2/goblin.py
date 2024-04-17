import pygame

class Goblin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('image\goblin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (500, 300)