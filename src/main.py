import pygame, random, time, char, taco
pygame.init()
player = char.Joe()
group = pygame.sprite.Group()
GREEN = (8, 132, 68)
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Raining Tacos') 
fps = 60
running = True
while running:
    screen.fill(GREEN)
    screen.blit(player.sprite, (player.x,player.y))
    group.add(taco.Taco())
    group.draw(screen)
    pygame.display.flip()
    player.moving()
pygame.quit()