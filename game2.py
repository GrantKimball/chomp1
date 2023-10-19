import pygame
import random
import sys

# initialize pygame
pygame.init()

# screen dimensions
screen_width = 800
screen_height = 600
tile_size=64

#create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('A beautiful beach')

#load font into game
custom_font=pygame.font.Font("assets/fonts/electrical.ttf", 128)

def draw_background(surf):
    water=pygame.image.load("assets/sprites/water.png").convert()
    sand=pygame.image.load("assets/sprites/sand_top.png").convert()
    seagrass=pygame.image.load("assets/sprites/seagrass.png").convert()

    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    #fill screen
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(water, (x,y))

    #draw sand
    for x in range(0, screen_width, tile_size):
        surf.blit(sand, (x,screen_height-tile_size))

    #making seagrass
    for _ in range(7):
        x=random.randint(0,screen_width)
        surf.blit(seagrass, (x, screen_height-tile_size*2))

    #draw text
    text=custom_font.render('Chomp', True, (255,0,0))
    surf.blit(text, (screen_width/2-text.get_width()/2, screen_height-500-text.get_height()/2))

#draw fish
def draw_fishes(surf):
    green_fish=pygame.image.load('assets/sprites/green_fish.png').convert()
    green_fish_flipped=pygame.transform.flip(green_fish, True, False)
    green_fish.set_colorkey((0,0,0)) #set png transparency
    green_fish_flipped.set_colorkey((0, 0, 0))

    puffer_fish=pygame.image.load('assets/sprites/puffer_fish.png').convert()
    puffer_fish_flipped=pygame.transform.flip(puffer_fish, True, False)
    puffer_fish.set_colorkey((0,0,0))
    puffer_fish_flipped.set_colorkey((0,0,0))

    for _ in range(3):
        x = random.randint(0,screen_width-2*tile_size)
        y=random.randint(0,screen_height-2*tile_size)
        surf.blit(green_fish, (x,y))
    for _ in range(2):
        x = random.randint(0, screen_width - 2 * tile_size)
        y = random.randint(0, screen_height - 2 * tile_size)
        surf.blit(green_fish_flipped, (x, y))
    for _ in range(2):
        x = random.randint(0, screen_width - 2*tile_size)
        y = random.randint(0, screen_height - 2*tile_size)
        surf.blit(puffer_fish, (x,y))
    for _ in range(3):
        x = random.randint(0, screen_width - 2 * tile_size)
        y = random.randint(0, screen_height - 2 * tile_size)
        surf.blit(puffer_fish_flipped, (x, y))

#main loop
running = True
background = screen.copy()
draw_background(background)
draw_fishes(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw background
    screen.blit(background, (0,0))

    pygame.display.flip()

pygame.quit()


