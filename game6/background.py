import pygame
from game_parameters import *
import random

def draw_background(surf):
    water=pygame.image.load("../assets/sprites/water.png").convert()
    sand=pygame.image.load("../assets/sprites/sand_top.png").convert()
    seagrass=pygame.image.load("../assets/sprites/seagrass.png").convert()

    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    #fill screen
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            surf.blit(water, (x,y))

    #draw sand
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        surf.blit(sand, (x,SCREEN_HEIGHT-TILE_SIZE))

    #making seagrass
    for _ in range(7):
        x=random.randint(0,SCREEN_WIDTH)
        surf.blit(seagrass, (x, SCREEN_HEIGHT-TILE_SIZE*2))

    #draw text
    # load font into game
    custom_font = pygame.font.Font("../assets/fonts/electrical.ttf", 50)
    text=custom_font.render('Chomp', True, (255,0,0))
    surf.blit(text, (SCREEN_WIDTH/2-text.get_width()/2, SCREEN_HEIGHT-550-text.get_height()/2))