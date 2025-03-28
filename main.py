# coding=utf-8
# file: main.py

from config import *
import pygame

pygame.init()

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()
