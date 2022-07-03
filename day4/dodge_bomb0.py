
import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1200,650))
    sc_rect = screen.get_rect()                     #画面用rect
    bg_img = pg.image.load("fig/pg_bg.jpg")         #背景画像用のsurface
    bg_rect = bg_img.get_rect()                     #背景用rect
    screen.blit(bg_img, bg_rect)                    #背景用surfaceを画面用surfaceに貼り付ける    
    pg.display.update()  #画面の更新
    clock = pg.time.Clock() #表示時間の設定
    clock.tick(0.5) #2秒間表示


if __name__ == "__main__":
   pg.init()        #モジュール初期化
   main()
   pg.quit()        #モジュール初期化解除
   sys.exit()       #プログラム終了