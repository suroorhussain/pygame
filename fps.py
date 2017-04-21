# -*- coding: utf-8 -*-

import pygame
import time

pygame.init()

screen = pygame.display.set_mode((640, 480)) #set windo size
background = pygame.Surface(screen.get_size()) #create a surface
background.fill((240, 240, 240)) #fill a color
background = background.convert() #for faster blitting
screen.blit(background, (0, 0)) # attaxh background to screen
pygame.display.flip() #update display

time.sleep(2)
