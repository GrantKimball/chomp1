import pygame
import random
import sys
from game_parameters import *
from fish import Fish, fishes
from background import draw_background
from player import Player

#init pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding a player fish')

#clock object
clock=pygame.time.Clock()

running = True
background = screen.copy()
draw_background(background)

for _ in range(5):
    fishes.add(Fish(random.randint(SCREEN_WIDTH,SCREEN_WIDTH*2), random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))

#create a player fish
player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
            #control fish with keyboard
        player.stop()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                print('pressed key up')
                player.move_up()
            if event.key==pygame.K_DOWN:
                print('pressed key down')
                player.move_down()
            if event.key==pygame.K_LEFT:
                print('pressed key left')
                player.move_left()
            if event.key==pygame.K_RIGHT:
                print('pressed key right')
                player.move_right()
     # draw background
    screen.blit(background, (0, 0))

    #draw fish
    fishes.update()

    player.update()



    for fish in fishes:
        if fish.rect.x < -fish.rect.width: #or tile_size
            fishes.remove(fish)#remove fish from sprite group
            fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH +50), random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))

    fishes.draw(screen)
    player.draw(screen)

    pygame.display.flip()

    clock.tick(60)
pygame.quit()
sys.exit()