import pygame

class Goblin1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('image\\1gameGob.png')
        self.image = pygame.transform.scale(self.image, (89, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (310, 360)
        
class Goblin2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('image\\2gameGob.png')
        self.image = pygame.transform.scale(self.image, (76, 98))
        self.rect = self.image.get_rect()
        self.rect.center = (440, 100)
        
class Goblin3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('image\\3gameGob.png')
        self.image = pygame.transform.scale(self.image, (76, 98))
        self.rect = self.image.get_rect()
        self.rect.center = (710, 460)