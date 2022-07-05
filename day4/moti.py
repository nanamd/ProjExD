import pygame as pg
import sys
import random

# 「↑,→,↓,←」キーを押されたときの反応を規定した辞書を作成
key_delta = { pg.K_UP    : [0,-1],
              pg.K_DOWN  : [0,+1],
              pg.K_LEFT  : [-1,0],
              pg.K_RIGHT : [+1,0] }

def main():
    #　ウィンドウ作成・背景貼り付け
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ!こうかとん")     #windowの名前
    screen = pg.display.set_mode((1000,650))        #画面用surface
    sc_rect = screen.get_rect()                     #画面用rect
    bg_img = pg.image.load("fig/pg_bg.jpg")         #背景画像用のsurface
    bg_rect = bg_img.get_rect()                     #背景用rect
    screen.blit(bg_img, bg_rect)                    #背景用surfaceを画面用surfaceに貼り付ける    


    #　こうかとん貼り付け
    tori_img = pg.image.load("moti/6.png")                   #こうかとん画像用のsurface
    tori_img=  pg.transform.rotozoom(tori_img, 0, 1)      #こうかとん画像の拡大
    tori_rect = tori_img.get_rect()                         #こうかとん画像用のrect
    tori_rect.center =900, 400                              #こうかとんの中心を900,400に指定
    screen.blit(tori_img, tori_rect)                        #こうかとん画像用surfaceを画面用surfaceに張り付ける


    #　爆弾貼り付け
    bomb = pg.Surface((20,20))                              #爆弾用のsurface
    pg.draw.circle(bomb, (255,0,0),(10,10),10)              #爆弾用surfaceに円を描く。色、中心、半径を指定
    bomb_rect = bomb.get_rect()                             #爆弾用rect
    bomb_rect.centerx = random.randint(0,sc_rect.width)     #爆弾のx座標をランダムに決定
    bomb_rect.centery = random.randint(0,sc_rect.height)    #爆弾のy座標をランダムに決定
    screen.blit(bomb, bomb_rect)                            #爆弾用surfaceを画面用surfaceに貼り付ける
    vx, vy = +1, +1                                         #爆弾の速さ


    while True:
        screen.blit(bg_img, bg_rect)            #背景用surfaceを画面用surfaceに張り付ける
        for event in pg.event.get():
            if event.type == pg.QUIT: return    #✕ボタンを押されたらmain()関数を抜ける

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
        if tori_rect.colliderect(bomb_rect) == True:
            #こうかとんの表情を変える・爆発する
            expl_img = pg.image.load("fig/bakuhatsu.png")           #爆発画像の読み込み
            expl_img = pg.transform.rotozoom(expl_img, 0, 1/3)      #爆発画像のサイズ調整
            screen.blit(bg_img, bg_rect)                            #こうかとんを消すために背景を再描画
            screen.blit(expl_img, tori_rect)                        #爆発画像を貼り付ける
            pg.display.update()                                     #画面更新(爆発)
            clock.tick(1)                                           #1秒停止
            tori_img = pg.image.load("moti/11.png")                   #こうかとん画像用のsurface
            tori_img= pg.transform.rotozoom(tori_img, 0, 1)       #こうかとん画像の拡大
            screen.blit(bg_img, bg_rect)                            #爆発を消すために背景を再描画
            screen.blit(tori_img, tori_rect)                        #新しいこうかとんの画像に置き換える
            pg.display.update()                                     #画面更新(こうかとん泣き顔)
            clock.tick(1)                                           #1秒停止
            return                                                  #こうかとん用のRectが爆弾用のRectと衝突していたらreturn


        pg.display.update()  #画面の更新
        clock.tick(1000)     #1000fpsに設定


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
    sys.exit()       #プログラム終了