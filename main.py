# coding=utf-8
# file: main.py

from config import *
import pygame

pygame.init()

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()
ball_pos = [SCREEN_W//2, SCREEN_H//2]
ball_move_direction = [1, 1]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    ball_pos[0] += ball_move_direction[0]
    ball_pos[1] += ball_move_direction[1]

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), ball_pos, 10)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
