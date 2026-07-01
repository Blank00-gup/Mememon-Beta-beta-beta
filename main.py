import pygame
import sys

import time
import random
import rpg_arena

from pygame import mixer



mixer.init()





randNum = random.randint(1, 3)


Doge_image = pygame.image.load("images/Buff_doge.png")
Poggers_image = pygame.image.load("images/poggers.png")





pygame.init()




screen_width = 640
screen_height = 480


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("hold this to play music")

player_x = 100
player_y = 250
enemy_x = 500
enemy_y = 110
text = "Doge"
bg_color = (255, 255, 255)
text_color = (0, 0, 0)
ui_color = (255, 255, 255)
font = pygame.font.SysFont("", 30)
text2 = "Poggers"
damage = rpg_arena.Meme_attack2()
Attack_text = (rpg_arena.player2.name + " hits " + rpg_arena.player1.name + " for " + str(damage))
Meme_attack_text = (rpg_arena.player2.name + " memes " + rpg_arena.player1.name + " for " + str(damage))
keys = pygame.key.get_pressed()
happy = False
sad = False

def draw_text(x, y, textIn):
    image = font.render(textIn, True, text_color)
    screen.blit(image, (x, y))

def Enemy_attack():
    randNum = random.randint(1, 3)
    if randNum == 1:
        rpg_arena.Ememe_attack()
    elif randNum == 2:
        rpg_arena.Eattack()










def draw_sprites():
    screen.blit(Doge_image, (player_x, player_y))
    screen.blit(Poggers_image, (enemy_x, enemy_y))
    draw_text(100, 310, text)
    draw_text(500, 170, text2)
    draw_text(520, 190, str(rpg_arena.player2.health))
    draw_text(110, 330, str(rpg_arena.player1.health))

    #("doge"), font, text_color, 10, 10
def draw_meme():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        rpg_arena.Meme_attack2()
        time.sleep(1)
        Enemy_attack()




def draw_attack():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_2]:
        rpg_arena.Attack2()
        time.sleep(1)
        Enemy_attack()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



    screen.fill(bg_color)

    draw_sprites()
    draw_meme()
    draw_attack()

    if sad == True:
        draw_text(100,300, Meme_attack_text)


    pygame.mixer.music.load("music/pokemon.mp3")

    pygame.mixer.music.play()



    pygame.display.flip()



