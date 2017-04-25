# -*- coding: utf-8 -*-

import pygame
import time

screen = pygame.display.set_mode((640, 480))
background = pygame.Surface(screen.get_size())
background.fill((150, 150, 150))
screen.blit(background, (0, 0))
pygame.display.flip()

for point1 in range(0,641,64): # range(start, stop, step)
    for point2 in range(0, 481, 48):
       pygame.draw.line(background, (255, point1%255, point2%255), (320,240), (point1, point2), 1)
       screen.blit(background, (0, 0))
       pygame.display.flip()
#       time.sleep(1)

time.sleep(3)
