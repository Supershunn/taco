import pygame
class Joe (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.load_sprite()
        self.x = 450
        self.y = 400
        self.rect = pygame.rect.Rect(self.x,self.y,self.sprite.get_width(),self.sprite.get_height())
        
    def movement(self):
        self.speed = 0.1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
            
    def load_sprite(self):
        image = pygame.surface.Surface((144, 316))
        image.fill((8, 132, 68))
        image.blit(pygame.image.load('./resources/character.png'), (0,0), (177, 137, 144, 416))
        self.sprite = image
        self.sprite = pygame.transform.scale(self.sprite, (self.sprite.get_width() / 2, self.sprite.get_height() / 2))
    def moving(self):
        self.speed = 0.15
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if self.x > 900 - self.sprite.get_width():
            self.x = 900 - self.sprite.get_width()
        if self.x < 0:
            self.x = 0