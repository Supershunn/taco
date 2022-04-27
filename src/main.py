from os import kill
import pygame, random, time, char, taco, events, burrito
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
pygame.time.set_timer(events.dropburrito,3000)
pygame.time.set_timer(NEW_TACO,3000)
def gameover():
    global running, score, group
    oof = font.render('Game Over!', False, ('YELLOW'))
    tryagain = font.render('Try Again?', False, ('WHITE'))
    gibup = font.render('Exit Game', False, ('WHITE'))
    oof_rect = pygame.Rect(0,0,oof.get_width(),oof.get_height())
    oof_rect.center = (WIDTH / 2, HEIGHT / 2)
    tryagain_rect = pygame.Rect(oof_rect.left,oof_rect.bottom + 10,tryagain.get_width(),tryagain.get_height())
    gibup_rect = pygame.Rect(tryagain_rect.left,tryagain_rect.bottom + 10,gibup.get_width(),gibup.get_height())
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tryagain_rect.collidepoint(event.pos):
                    score = 0
                    group.empty()
                    group.clear(screen,pygame.Surface((WIDTH,HEIGHT)))
                    gaem()
                if gibup_rect.collidepoint(event.pos):
                    pygame.quit()
        screen.fill(GREEN)
        screen.blit(oof, oof_rect)
        screen.blit(tryagain, tryagain_rect)
        screen.blit(gibup, gibup_rect)
        pygame.display.flip()
def collision(player,enemy):
    global score
    if pygame.sprite.collide_rect(player,enemy):
        score += 1
        soundeffect.play()
        return True
    else:
        return False
def gaem():
    while running:
        screen.fill(GREEN)
        for event in pygame.event.get():
            if event.type == NEW_TACO:
                group.add(taco.Taco())
            if event.type == events.dropburrito:
                group.add(burrito.Burrito())
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == events.gameover:
                gameover()
        screen.blit(player.sprite, (player.x,player.y))
        pygame.sprite.spritecollide(player,group,True,collision)
        scorerender = font.render('Score: ' + str(score), False, ('WHITE'))
        screen.blit(scorerender, (700, 500))
        group.draw(screen)
        group.update()
        pygame.display.flip()
        player.moving()
gaem()