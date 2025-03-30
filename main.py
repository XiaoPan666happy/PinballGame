# coding=utf-8
# file: main.py

import random
from config import *
import pygame

pygame.init()
pygame.font.init()

font_big = pygame.font.SysFont("microsoftyahei", 128, bold=True)
font_small = pygame.font.SysFont("microsoftyahei", 32, bold=True)
font_little = pygame.font.SysFont("microsoftyahei", 16)
gameover_surface = font_big.render("GAMEOVER", True, (255, 255, 255))
cover_word1_surface = font_big.render("弹球游戏", True, (255, 255, 255))
cover_word2_surface = font_small.render("按下鼠标开始游戏", True, (255, 255, 255))
cover_word3_surface = font_little.render("项目Github仓库:https://github.com/XiaoPan666happy/PinballGame", True, (255, 255, 255))

hud_surface = pygame.surface.Surface((250, 136))
hud_surface.fill((0, 0, 0))
hud_surface.set_alpha(128)

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()
level = 1
count = 0
ball_pos = [SCREEN_W//2, SCREEN_H//2]
ball_move_direction = [random.choice((1,-1)), random.choice((1,-1))]
board_pos = [100, 100]
part = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and part == 0:
            part = 1
    
    screen.fill((0, 0, 0))

    # 封面
    if part == 0:
        screen.blit(cover_word1_surface, (SCREEN_W//2-cover_word1_surface.get_width()//2, 
                                          SCREEN_H//2-cover_word1_surface.get_height()+32))
        screen.blit(cover_word2_surface, (SCREEN_W//2-cover_word2_surface.get_width()//2, 
                                          SCREEN_H//2+32))
        screen.blit(cover_word3_surface, (SCREEN_W//2-cover_word3_surface.get_width()//2, 
                                          SCREEN_H-cover_word3_surface.get_height()))
    # 游戏
    elif part == 1:
        ball_pos[0] += ball_move_direction[0]*level*4
        ball_pos[1] += ball_move_direction[1]*level*4
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
            part = 2
        # 弹板
        if (board_pos[0]-10 < ball_pos[0] < board_pos[0]+10) and (board_pos[1] < ball_pos[1] < board_pos[1]+100):
            ball_move_direction[0] = -ball_move_direction[0]
            if level < 10:
                count += 1
                if count >= (level*8):
                    level += 1
                    count = 0
        
        mouse_pos = pygame.mouse.get_pos()
        board_pos[1] = mouse_pos[1]-50

        fps_text = font_small.render(f"帧数        {round(clock.get_fps(), 2)}", True, (255, 255, 255))
        count_text = font_small.render(f"进度        {count}/{level*8}", True, (255, 255, 255))
        level_text = font_small.render(f"关卡        {level}", True, (255, 255, 255))

        pygame.draw.circle(screen, (255, 255, 255), ball_pos, 10)
        pygame.draw.line(screen, (255, 255, 255), board_pos, (board_pos[0], board_pos[1]+100), 4)
        screen.blit(hud_surface, (0, 0))
        screen.blit(fps_text, (10, 10))
        screen.blit(count_text, (10, 52))
        screen.blit(level_text, (10, 94))

        clock.tick(FPS)
        # print(ball_pos)
    elif part == 2:
        screen.blit(gameover_surface, (SCREEN_W//2-gameover_surface.get_width()//2, 
                                        SCREEN_H//2-gameover_surface.get_height()//2))

    pygame.display.flip()

pygame.font.quit()
pygame.quit()
