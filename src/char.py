import pygame
class Joe (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load('./resources/character.png')
        self.x = 450
        self.y = 870
        self.rect = pygame.rect.Rect(self.x,self.y,self.sprite.get_width(),self.sprite.get_height())
    def movement(self):
        self.speed = 0.1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed