# -*- coding: utf-8 -*-

import pygame
import time

pygame.init()

screen = pygame.display.set_mode((640, 480))
background = pygame.Surface(screen.get_size())
background.fill((240, 240, 240))
background = background.convert()
screen.blit(background, (0, 0))
pygame.display.flip()

time.sleep(2)
