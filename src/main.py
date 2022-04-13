from os import kill
import pygame, random, time, char, taco
from tools import font, screen
from taco import running
pygame.init()
score = 0
soundeffect = pygame.mixer.Sound("./resources/tacoget.wav")
player = char.Joe()
group = pygame.sprite.Group()
GREEN = (8, 132, 68)
WIDTH, HEIGHT = 900, 600
pygame.display.set_caption('Raining Tacos')
NEW_TACO = pygame.event.custom_type()
pygame.time.set_timer(NEW_TACO,3000)
def collision(player,enemy):
    global score
    if pygame.sprite.collide_rect(player,enemy):
        score += 1
        soundeffect.play()
        return True
    else:
        return False
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
