import random
import pygame
import sys
from background import draw_background
from game_parameters import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('A School of Moving Fish')

running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                print('pressed key up')
            if event.key==pygame.K_DOWN:
                print('pressed key down')
            if event.key==pygame.K_LEFT:
                print('pressed key left')
            if event.key==pygame.K_RIGHT:
                print('pressed key right')
     # draw background
    screen.blit(background, (0, 0))

    pygame.display.flip()

pygame.quit()
sys.exit()