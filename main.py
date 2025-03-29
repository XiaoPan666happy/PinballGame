# coding=utf-8
# file: main.py

from config import *
import pygame

pygame.init()

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()
ball_pos = [SCREEN_W//2, SCREEN_H//2]
ball_move_direction = [-4, 4]
board_pos = [100, 100]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    ball_pos[0] += ball_move_direction[0]
    ball_pos[1] += ball_move_direction[1]
    # 反弹
    # 下方
    if ball_pos[1]>SCREEN_H:
        ball_move_direction[1] = -ball_move_direction[1]
    # 右侧
    elif ball_pos[0]>SCREEN_W:
        ball_move_direction[0] = -ball_move_direction[0]
    # 上方
    elif ball_pos[1]<0:
        ball_move_direction[1] = -ball_move_direction[1]
    # 左侧
    elif ball_pos[0]<0:
        ball_move_direction[0] = -ball_move_direction[0]
    # 弹板
    if (board_pos[0]-10 < ball_pos[0] < board_pos[0]+10) and (board_pos[1] < ball_pos[1] < board_pos[1]+100):
        ball_move_direction[0] = -ball_move_direction[0]
    
    mouse_pos = pygame.mouse.get_pos()
    board_pos[1] = mouse_pos[1]-50

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), ball_pos, 10)
    pygame.draw.line(screen, (255, 255, 255), board_pos, (board_pos[0], board_pos[1]+100), 4)
    pygame.display.flip()

    clock.tick(FPS)
    # print(ball_pos)

pygame.quit()
