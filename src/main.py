from os import kill
import pygame, random, time, char, taco, events, burrito, sys, os
from tools import screen
from taco import running
from states import States
pygame.init()
def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
score = 0
font = pygame.font.Font(resource_path("./resources/PUSAB.otf"),32)
soundeffect = pygame.mixer.Sound(resource_path("./resources/tacoget.wav"))
gameovereffect = pygame.mixer.Sound(resource_path("./resources/oof.mp3"))
player = char.Joe()
group = pygame.sprite.Group()
burritogroup = pygame.sprite.Group()
GREEN = (8, 132, 68)
WIDTH, HEIGHT = 900, 600
pygame.display.set_caption('Raining Tacos')
NEW_TACO = pygame.event.custom_type()
pygame.time.set_timer(events.dropburrito,3000)
pygame.time.set_timer(NEW_TACO,3000)
state = States.TITLE
def titlescreen():
    global state, running
    howtoplay = font.render('Catch all the tacos falling while avoiding', False, ('WHITE'))
    howtoplay2 = font.render('the burritos.', False, ('WHITE'))
    titlename = font.render('RAINING TACOS!', False, ('YELLOW'))
    startbutton = font.render('Start!', False, ('WHITE'))
    startbutton_rect = pygame.Rect(0,0,startbutton.get_width(),startbutton.get_height())
    titlename_rect = pygame.Rect(25,25,titlename.get_width(),titlename.get_height())
    howtoplay_rect = pygame.Rect(25,75,howtoplay.get_width(),howtoplay.get_height())
    howtoplay2_rect = pygame.Rect(25,110,howtoplay2.get_width(),howtoplay2.get_height())
    startbutton_rect.center = WIDTH / 2, HEIGHT / 2
    while state == States.TITLE:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                    return
                case pygame.MOUSEBUTTONDOWN:
                    if startbutton_rect.collidepoint(event.pos):
                        state = States.ACTUALGAME
                        return
        screen.fill(GREEN)
        screen.blit(titlename,titlename_rect)
        screen.blit(startbutton,startbutton_rect)
        screen.blit(howtoplay,howtoplay_rect)
        screen.blit(howtoplay2,howtoplay2_rect)
        pygame.display.flip()
def gameover():
    global running, score, group
    gameovereffect.play()
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
                new_taco = taco.Taco()
                group.add(new_taco)
            if event.type == events.dropburrito:
                new_burrito = burrito.Burrito()
                if new_burrito.rect.colliderect(new_taco.rect):
                    if new_burrito.rect.x < new_taco.rect.x:
                        new_burrito.x -= new_taco.rect.width
                        new_burrito.update()
                    if new_burrito.rect.x >= new_taco.rect.x:
                        new_burrito.x += new_taco.rect.width
                        new_burrito.update()
                burritogroup.add(new_burrito)
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == events.gameover:
                gameovereffect.play()
                gameover()
        screen.blit(player.sprite, (player.x,player.y))
        pygame.sprite.spritecollide(player,group,True,collision)
        scorerender = font.render('Score: ' + str(score), False, ('WHITE'))
        screen.blit(scorerender, (700, 500))
        group.draw(screen)
        group.update()
        burritogroup.draw(screen)
        burritogroup.update()
        if pygame.sprite.spritecollide(player, burritogroup,True):
            gameover()
            gameovereffect.play()
        pygame.display.flip()
        player.moving()
while running:
    match state:
        case States.TITLE:
            titlescreen()
            if not running:
                break
        case States.ACTUALGAME:
                    gaem()
                    if not running: break
        case States.GAMEOVER:
            gameover()
            if not running: break
       
pygame.quit()