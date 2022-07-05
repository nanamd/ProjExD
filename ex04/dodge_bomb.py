from re import A
import pygame as pg
import sys
import random

# 「↑,→,↓,←」キーを押されたときの反応を規定した辞書を作成
key_delta = { pg.K_UP    : [0,-1],
              pg.K_DOWN  : [0,+1],
              pg.K_LEFT  : [-1,0],
              pg.K_RIGHT : [+1,0] }


def main():
    pg.display.set_caption("逃げろ！こうかとん")
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

    #　爆弾作成
    bomb = pg.Surface((20,20))                              #爆弾用のsurface
    pg.draw.circle(bomb, (255,0,0),(10,10),10)              #爆弾用surfaceに円を描く。色、中心、半径を指定
    bomb_rect = bomb.get_rect()                             #爆弾用rect
    bomb_rect.centerx = random.randint(0,sc_rect.width)     #爆弾のx座標をランダムに決定
    bomb_rect.centery = random.randint(0,sc_rect.height)    #爆弾のy座標をランダムに決定
                               #爆弾用surfaceを画面用surfaceに貼り付ける
    vx, vy = +1, +1  


    while True:
        screen.blit(bg_img,bg_rect) #スクリーンに背景画像を合成(サイズ通りに)
        screen.blit(tori_img,tori_rect)
        screen.blit(bomb, bomb_rect)
        for event in pg.event.get(): #イベント全てを格納する箱
            #ウィンドウの閉じるボタンを押したとき
            if event.type == pg.QUIT:
                return

        #　こうかとんの移動
        key_states = pg.key.get_pressed()                       #どのキーが押されているか記録した辞書を作成
        for key, delta in key_delta.items():                    #key_deltaから
            if key_states[key] == True:                         #keyが押されていたら
                tori_rect.centerx += delta[0]                   #横方向の変化
                tori_rect.centery += delta[1]                   #縦方向の変化
                if check_bound(sc_rect,tori_rect) != (1,1):     #移動後に画面範囲内か
                    tori_rect.centerx -= delta[0]
                    tori_rect.centery -= delta[1]
        screen.blit(tori_img,tori_rect)

        #　爆弾の移動
        bomb_rect.move_ip(vx,vy)                    #爆弾用のrectを移動する
        screen.blit(bomb, bomb_rect)                #爆弾の画像を貼り付ける
        ret = check_bound(sc_rect, bomb_rect)       #check_bound()関数で画面外にいるかの判定
        vx *= ret[0]                                #横方向に画面外なら、横方向速度の符号反転
        vy *= ret[1]                                #縦方向に画面外なら、縦方向速度の符号反転

        #　爆弾の当たり判定
        if tori_rect.colliderect(bomb_rect) == True: #toriがbombと重なったらTrue
            return #終了(mainから抜ける)

        pg.display.update()
        clock.tick(1000) #1秒に1000画像を表示する(ぬるぬる動く)

def check_bound(sc_r, obj_r):     #引数は、画面用Rect,{こうかとん,爆弾]Rect
    #画面内なら：+1 / 画面外なら：-1を返す
    x, y = +1, +1
    if obj_r.left < sc_r.left or sc_r.right < obj_r.right: x = -1   #画面外に行ったらx=-1
    if obj_r.top < sc_r.top or sc_r.bottom < obj_r.bottom: y = -1   #画面外に行ったらy=-1
    return x, y



if __name__ == "__main__":
    pg.init()        #モジュール初期化
    main()
    pg.quit()        #モジュール初期化解除
    sys.exit()       #プログラム終了(強制終了)