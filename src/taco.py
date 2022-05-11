import pygame
import random
import events
import sys, os
from tools import running, screen

class Taco (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.load_sprite()
        self.x = random.randrange(30, 850)
        self.y = -50
        self.rect = pygame.rect.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())
        font = pygame.font.Font(self.resource_path("./resources/PUSAB___.otf"),32)
        self.gameover = font.render('Game Over!', False, ('BLUE'))
    def load_sprite(self):
            image = pygame.surface.Surface((1046, 1197))
            image.fill((8, 132, 68))
            image.blit(pygame.image.load(self.resource_path('resources/taco.png')), (0,0), (43, 46, 1046, 1197))
            self.image = image
            self.image = pygame.transform.scale(self.image, (self.image.get_width() / 12, self.image.get_height() / 12))
            self.image.set_colorkey((8, 132, 68))
    def update(self):
        global running
        self.v = 0.1
        self.y += self.v
        if self.y >= 600:
            pygame.event.post(pygame.event.Event(events.gameover))
            self.kill()
        self.rect = pygame.rect.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())
    def resource_path(self,relative_path):
        try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)