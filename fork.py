import pygame, random

class Fork(pygame.sprite.Sprite):
    def __init__(self, pos, isTop = False):
        super().__init__()
        self.image = pygame.image.load('fork.png')
        self.image = pygame.transform.smoothscale(self.image, (400, 800))
        if isTop:
            self.image = pygame.transform.rotate(self.image, -180)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(-6, 0)

    def update(self):
        self.rect.move_ip(self.speed)