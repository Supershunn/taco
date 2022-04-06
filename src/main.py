import pygame, random, time, char, taco
pygame.init()
player = char.Joe()
group = pygame.sprite.Group()
GREEN = (8, 132, 68)
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Raining Tacos')
NEW_TACO = pygame.event.custom_type()
pygame.time.set_timer(NEW_TACO,3000)
running = True
while running:
    screen.fill(GREEN)
    for event in pygame.event.get():
        if event.type == NEW_TACO:
            group.add(taco.Taco())
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(player.sprite, (player.x,player.y))
    group.draw(screen)
    group.update()
    pygame.display.flip()
    player.moving()
pygame.quit()