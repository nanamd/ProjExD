import pygame as pg
import sys

def main():
    screen = pg.display.set_mode((1200,650))
    sc_rect = screen.get_rect()                     #画面用rect
    bg_img = pg.image.load("fig/pg_bg.jpg")         #背景画像用のsurface
    bg_rect = bg_img.get_rect()                     #背景用rect    
    clock = pg.time.Clock() #表示時間の設定


    #こうかとん磔
    tori_img = pg.image.load("fig/6.png")                   #こうかとん画像用のsurface
    #rotozoomは画像の拡大縮小回転(画像名,回転,拡縮)
    tori_img=  pg.transform.rotozoom(tori_img, 0, 2.0)      #こうかとん画像の拡大
    tori_rect = tori_img.get_rect()                         #こうかとん画像用のrect
    tori_rect.center =900, 450                              #こうかとんの中心を900,400に指定
    #blit(画像名,サイズ)
    screen.blit(tori_img, tori_rect) 

    while True:
        screen.blit(bg_img,bg_rect) #スクリーンに背景画像を合成(サイズ通りに)
        screen.blit(tori_img,tori_rect)
        for event in pg.event.get(): #イベント全てを格納する箱
            #ウィンドウの閉じるボタンを押したとき
            if event.type == pg.QUIT:
                return
        pg.display.update()
        clock.tick(1000) #1秒に1000画像を表示する(ぬるぬる動く)


if __name__ == "__main__":
    pg.init()        #モジュール初期化
    main()
    pg.quit()        #モジュール初期化解除
    sys.exit()       #プログラム終了