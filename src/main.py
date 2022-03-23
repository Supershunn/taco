import pygame, random, time, char
pygame.init()
player = char.Joe()
GREEN = (8, 132, 68)
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Raining Tacos')
fps = 60
running = True
while running:
    screen.fill(GREEN)
    screen.blit(player.sprite, (player.x,player.y))
    pygame.display.flip()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
pygame.quit()