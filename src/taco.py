import pygame
import random

class Taco (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.load_sprite()
        self.x = random.randrange(30, 850)
        self.y = -50
        self.rect = pygame.rect.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())
    def load_sprite(self):
            image = pygame.surface.Surface((1046, 1197))
            image.fill((8, 132, 68))
            image.blit(pygame.image.load('./resources/taco.png'), (0,0), (43, 46, 1046, 1197))
            self.image = image
            self.image = pygame.transform.scale(self.image, (self.image.get_width() / 12, self.image.get_height() / 12))
            self.image.set_colorkey((8, 132, 68))
    def update(self):
        self.v = 0.1
        self.y += self.v
        self.rect = pygame.rect.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())