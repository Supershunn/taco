import pygame
import random
import events
from tools import font, running, screen
class Burrito (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.load_sprite()
        self.x = random.randrange(30, 850)
        self.y = -50
        self.rect = pygame.rect.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())
    def load_sprite(self):
            image = pygame.surface.Surface((1506, 1048))
            image.fill((8, 132, 68))
            image.blit(pygame.image.load('./resources/burrito.png'), (0,0), (35, 5, 1541 - 35, 1053 - 5))
            self.image = image
            self.image = pygame.transform.scale(self.image, (self.image.get_width() / 12, self.image.get_height() / 12))
            self.image.set_colorkey((8, 132, 68))
    def update(self):
        global running
        self.v = 0.1
        self.y += self.v
        if self.y >= 600:
            self.kill()
        self.rect = pygame.rect.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())