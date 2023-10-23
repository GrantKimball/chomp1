import pygame
import random
from fish import Fish, fishes
import sys

# initialize pygame
pygame.init()

# screen dimensions
screen_width = 800
screen_height = 600
tile_size=64

#create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('A School of Moving Fish')

#clock object
clock=pygame.time.Clock()

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
    # load font into game
    custom_font = pygame.font.Font("assets/fonts/electrical.ttf", 50)
    text=custom_font.render('Chomp', True, (255,0,0))
    surf.blit(text, (screen_width/2-text.get_width()/2, screen_height-550-text.get_height()/2))

#main loop
running = True
background = screen.copy()
draw_background(background)


#draw fish
for _ in range(5):
    fishes.add(Fish(random.randint(0,screen_width-2*tile_size), random.randint(0,screen_height-2*tile_size)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw background
    screen.blit(background, (0,0))
    #update fish
    fishes.update()
    #check if fish is off screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width: #or tile_size
            fishes.remove(fish)#remove fish from sprite group
            fishes.add(Fish(random.randint(0, screen_width +50), random.randint(0, screen_height - 2 * tile_size)))

    fishes.draw(screen)

    pygame.display.flip()

    #limit frame rate
    clock.tick(60)


pygame.quit()