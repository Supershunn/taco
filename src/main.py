from os import kill
import pygame, random, time, char, taco
pygame.init()
score = 0
player = char.Joe()
group = pygame.sprite.Group()
GREEN = (8, 132, 68)
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Raining Tacos')
NEW_TACO = pygame.event.custom_type()
pygame.time.set_timer(NEW_TACO,3000)
running = True
def collision(player,enemy):
    global score
    if pygame.sprite.collide_rect(player,enemy):
        score += 1
        return True
    else:
        return False
font = pygame.font.Font("./resources/PUSAB___.otf",32)
while running:
    screen.fill(GREEN)
    for event in pygame.event.get():
        if event.type == NEW_TACO:
            group.add(taco.Taco())
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(player.sprite, (player.x,player.y))
    pygame.sprite.spritecollide(player,group,True,collision)
    scorerender = font.render('Score: ' + str(score), False, ('WHITE'))
    screen.blit(scorerender, (700, 500))
    group.draw(screen)
    group.update()
    pygame.display.flip()
    player.moving()
pygame.quit()