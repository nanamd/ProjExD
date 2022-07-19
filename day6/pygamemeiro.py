import pygame
import sys
import random

#色指定
WALL_COLOR = (87, 45, 24)
FLOOR_COLOR = (181, 152, 132)

# 床1枚の幅と高さ
FLOOR_W = 48
FLOOR_H = 48
# 迷路の幅と高さ（床の枚数）
MAZE_W = 9
MAZE_H = 9
# リストの宣言と初期化
maze = []
for y in range(MAZE_H):
    maze.append([0] * MAZE_W)

# 迷路の設計情報を自動生成する
def make_maze():
    # 柱から伸ばす壁のに利用する値を定義
    # [上, 右, 下, 左]
    XP = [0, 1, 0, -1]
    YP = [-1, 0, 1, 0]

    # 迷路を囲う壁を作る
    for x in range(MAZE_W):
        maze[0][x] = 1
        maze[MAZE_H - 1][x] = 1
    for y in range(1, MAZE_H - 1):
        maze[y][0] = 1
        maze[y][MAZE_W - 1] = 1
    
    # 中を何もない状態にする
    for y in range(1, MAZE_H - 1):
        for x in range(1, MAZE_W - 1):
            maze[y][x] = 0
    
    # 柱を作る
    for y in range(2, MAZE_H - 2, 2):           # range()は第三引数を2を指定し、ステップ機能で1マス飛ばししている
        for x in range(2, MAZE_W - 2, 2):
            maze[y][x] = 1
    
    # 各柱から壁を伸ばす
    for y in range(2, MAZE_H - 2, 2):
        for x in range(2, MAZE_W - 2, 2):
            while True:
                d = random.randint(0, 3)            # 変数dに柱から伸ばす方向を0~3で指定
                if x > 2:                           # 2列目以降なら0~2（左を示す3を含めない）で左に伸ばさない
                    d = random.randint(0, 2)
                
                if maze[y + YP[d]][x + XP[d]] == 1: # dの値が既に壁が作られた場所であればやり直し
                    continue

                # 柱から伸ばす壁を示す値（変数d）を、定数YP、XPの添字に使い壁を伸ばすマス目を指定
                # そのマス目を表すmaze[]に壁有りを示す1を代入
                maze[y + YP[d]][x + XP[d]] = 1
                break

def main():
    pygame.init()
    pygame.display.set_caption("Pygameで迷路を自動生成する")
    screen = pygame.display.set_mode((FLOOR_W * MAZE_W, FLOOR_H * MAZE_H))
    clock = pygame.time.Clock()

    make_maze()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    make_maze()
        
        # 自動生成した迷路の設計情報を使い実際に描画する
        for y in range(MAZE_H):
            for x in range(MAZE_W):
                W = FLOOR_W
                H = FLOOR_H
                X = x * W
                Y = y * H
                # 通路を描画
                if maze[y][x] == 0:
                    pygame.draw.rect(screen, FLOOR_COLOR, [X, Y, W, H])
                # 壁を描画
                if maze[y][x] == 1:
                    pygame.draw.rect(screen, WALL_COLOR, [X, Y, W, H])
        
        pygame.display.update()
        clock.tick(2)

if __name__ == '__main__':
     main()