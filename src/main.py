import pygame, random, time, char, taco
pygame.init()
player = char.Joe()
group = pygame.sprite.Group()
GREEN = (8, 132, 68)
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Raining Tacos')
NEW_TACO = pygame.event.custom_type()
pygame.time.set_timer(NEW_TACO,3)
def newtaco():
    group.add(taco.Taco())
    group.draw(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == NEW_TACO:
            newtaco()
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(GREEN)
    screen.blit(player.sprite, (player.x,player.y))
    pygame.display.flip()
    player.moving()
pygame.quit()


