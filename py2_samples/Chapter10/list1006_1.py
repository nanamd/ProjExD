import pygame
import sys
import math
from pygame.locals import *

WHITE = (255, 255, 255)
YELLOW= (255, 224,   0)

DATA_LR = [0, 0, 1, 0, 6, -6, -4, -2, 0]
CLEN = len(DATA_LR)

BOARD = 120
CMAX = BOARD*CLEN
curve = [0]*CMAX
updown = [0]*CMAX


def make_course():
    for i in range(CLEN):
        lr1 = DATA_LR[i]
        lr2 = DATA_LR[(i+1)%CLEN]
        for j in range(BOARD):
            pos = j+BOARD*i
            curve[pos] = lr1*(BOARD-j)/BOARD + lr2*j/BOARD


def main(): # メイン処理
    pygame.init()
    pygame.display.set_caption("Python Racer")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    img_bg = pygame.image.load("image_pr/bg.png").convert()

    # 道路の板の基本形状を計算
    BOARD_W = [0]*BOARD
    BOARD_H = [0]*BOARD
    BOARD_UD = [0]*BOARD
    for i in range(BOARD):
        BOARD_W[i] = 10+(BOARD-i)*(BOARD-i)/12
        BOARD_H[i] = 3.4*(BOARD-i)/BOARD
        BOARD_UD[i] = 2*math.sin(math.radians(i*1.5))

    make_course()

    car_y = 0
    vertical = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed()
        if key[K_UP] == 1:
            car_y = (car_y+1)%CMAX

        # 描画用の道路のX座標と路面の高低を計算
        di = 0
        ud = 0
        board_x = [0]*BOARD
        board_ud = [0]*BOARD
        for i in range(BOARD):
            di += curve[(car_y+i)%CMAX]
            ud += updown[(car_y+i)%CMAX]
            board_x[i] = 400 - BOARD_W[i]/2 + di/2
            board_ud[i] = ud/30

        horizon = 400 + int(ud/3) # 地平線の座標の計算
        sy = horizon # 道路を描き始める位置

        vertical = vertical - di*key[K_UP]/30 # 背景の垂直位置
        if vertical < 0:
            vertical += 800
        if vertical >= 800:
            vertical -= 800

        # フィールドの描画
        screen.fill((0, 56, 255)) # 上空の色
        screen.blit(img_bg, [vertical-800, horizon-400])
        screen.blit(img_bg, [vertical, horizon-400])

        # 描画用データをもとに道路を描く
        for i in range(BOARD-1, 0, -1):
            ux = board_x[i]
            uy = sy - BOARD_UD[i]*board_ud[i]
            uw = BOARD_W[i]
            sy = sy + BOARD_H[i]*(600-horizon)/200
            bx = board_x[i-1]
            by = sy - BOARD_UD[i-1]*board_ud[i-1]
            bw = BOARD_W[i-1]
            col = (160,160,160)
            pygame.draw.polygon(screen, col, [[ux, uy], [ux+uw, uy], [bx+bw, by], [bx, by]])

            if int(car_y+i)%10 <= 4: # 左右の黄色線
                pygame.draw.polygon(screen, YELLOW, [[ux, uy], [ux+uw*0.02, uy], [bx+bw*0.02, by], [bx, by]])
                pygame.draw.polygon(screen, YELLOW, [[ux+uw*0.98, uy], [ux+uw, uy], [bx+bw, by], [bx+bw*0.98, by]])
            if int(car_y+i)%20 <= 10: # 白線
                pygame.draw.polygon(screen, WHITE, [[ux+uw*0.24, uy], [ux+uw*0.26, uy], [bx+bw*0.26, by], [bx+bw*0.24, by]])
                pygame.draw.polygon(screen, WHITE, [[ux+uw*0.49, uy], [ux+uw*0.51, uy], [bx+bw*0.51, by], [bx+bw*0.49, by]])
                pygame.draw.polygon(screen, WHITE, [[ux+uw*0.74, uy], [ux+uw*0.76, uy], [bx+bw*0.76, by], [bx+bw*0.74, by]])

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
