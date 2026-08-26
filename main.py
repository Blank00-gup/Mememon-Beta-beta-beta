import pygame
import sys
import time
import random
import rpg_arena

pygame.init()
pygame.mixer.init()
# OPTIONAL: safer volume control
pygame.mixer.music.set_volume(0.5)
# Load and play music
pygame.mixer.music.load("music/pokemon.mp3")
pygame.mixer.music.play(-1)  # loop forever
randNum = random.randint(1, 3)
Doge_image = pygame.image.load("images/Buff_doge.png")
Poggers_image = pygame.image.load("images/poggers.png")
background_image = pygame.image.load("images/background.png")
bx = 0
by = 0
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mememon-Beta-beta-beta")
player_x = 100
player_y = 250
enemy_x = 500
enemy_y = 250
text = "Doge"
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

def background():
    screen.blit(background_image, (bx, by)) #Initialize background image

def draw_sprites():
    screen.blit(Doge_image, (player_x, player_y))
    screen.blit(Poggers_image, (enemy_x, enemy_y))
    draw_text(100, 310, text)
    draw_text(500, 310, text2)
    draw_text(520, 330, str(rpg_arena.player2.health))
    draw_text(110, 330, str(rpg_arena.player1.health))

    #("doge"), font, text_color, 10, 10
def draw_meme():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1] and rpg_arena.won == "":
        rpg_arena.Meme_attack2()
        time.sleep(1)
        Enemy_attack()
    if rpg_arena.won == rpg_arena.player1.name:
        draw_text(300,240,"Doge Wins!!!")
    if rpg_arena.won == rpg_arena.player2.name:
        draw_text(300, 240, "Poggers Wins!!!")




def draw_attack():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_2] and rpg_arena.won == "":
        rpg_arena.Attack2()
        time.sleep(1)
        Enemy_attack()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    background()
    draw_sprites()
    draw_meme()
    draw_attack()

    if sad == True:
        draw_text(100,300, Meme_attack_text)


    pygame.display.flip()



