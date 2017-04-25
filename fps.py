# -*- coding: utf-8 -*-

import pygame
import time

pygame.init()

screen = pygame.display.set_mode((640, 480)) #set windo size
background = pygame.Surface(screen.get_size()) #create a surface
background.fill((240, 240, 240)) #fill a color
background = background.convert() #for faster blitting
screen.blit(background, (0, 0)) # attaxh background to screen

clock = pygame.time.Clock()

mainloop = True

FPS = 30
playtime = 0.0

while mainloop:
    playtime += clock.tick(FPS)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False

    pygame.display.set_caption("FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime))

    pygame.display.flip()

pygame.quit()

print("This game was played for {:.2f} seconds".format(playtime))
