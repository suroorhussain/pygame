# -*- coding: utf-8 -*-

import pygame
import time

screen = pygame.display.set_mode((500, 500))
background = pygame.Surface(screen.get_size())
background.fill((200, 200, 200))
screen.blit(background, (0, 0))
pygame.display.flip()
time.sleep(1)
pygame.draw.circle(background, (0, 0, 255), (25, 25), 25)

screen.blit(background, (0, 0))

pygame.display.flip()

time.sleep(1)

pygame.draw.rect(background, (13, 231, 123), (123, 123, 30, 25))

screen.blit(background, (0, 0))

pygame.display.flip()

time.sleep(1)

pygame.draw.polygon(background, (12, 31, 242), ((200, 200), (212, 230), (250, 250), (432, 400), (300, 350)))

screen.blit(background, (0, 0))

pygame.display.flip()

time.sleep(2)
