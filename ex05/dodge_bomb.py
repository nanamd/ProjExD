from ast import If
from email.mime import image
from re import A, I, S
import re
import pygame as pg
import sys
import random

class Screen:            #スクリーンクラス
    def __init__(self,title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct= self.bgi_sfc.get_rect()  # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self, image:str, size:float, xy): #（:型名）
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc,0,size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen): #型を指定する
        scr.sfc.blit(self.sfc, self.rct)  #==screen_sfc.blit(kkimg_sfc, kkimg_rct)
        
    def update(self, scr:Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]:
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]:
            self.rct.centery += 1
        if key_states[pg.K_LEFT]:
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 1
        # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery += 1
            if key_states[pg.K_DOWN]:
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]:
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 1
        self.blit(scr)

class Bomb:
    def __init__(self, color, size:float, vxy, scr:Screen):
        self.sfc= pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0,0,0)) 
        pg.draw.circle(self.sfc, color, (size,size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6
    
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)  #==screen_sfc.blit(kkimg_sfc, kkimg_rct)

    def update(self,scr:Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        # 練習5
        self.blit(scr)


def main():
    clock = pg.time.Clock()

    # 練習1：スクリーンと背景画像
    
    scr = Screen("逃げろ！こうかとん",(1200,650),"fig/pg_bg.jpg")#コメントアウトの6文が一行に

    # 練習3：こうかとん
    
    kkt = Bird("fig/6.png", 2.0, (900,400))

    # 練習5：爆弾
    # 練習6
    bkb = Bomb((255,0,0),10,(+1,+1),scr)

    while True:
        #screen_sfc.blit(bgimg_sfc, bgimg_rct)
        scr.blit()


        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        # 練習4
        
        # 練習7
        

        kkt.update(scr) #上の長いやつがこれになる

        # 練習6
        #bmimg_rct.move_ip(vx, vy)
        # 練習5
        #screen_sfc.blit(bmimg_sfc, bmimg_rct)
        # 練習7
        #yoko, tate = check_bound(bmimg_rct, screen_rct)
        #vx *= yoko
        #vy *= tate
        bkb.update(scr)


        # 練習8
        #if kkimg_rct.colliderect(bmimg_rct): return 
        if kkt.rct.colliderect(bkb.rct):return

        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()