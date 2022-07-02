#pygameモジュールをインストール
import pygame

#sysモジュールをインポート
import sys

WHITE = (255,255,255) #白
BLACK = (0,0,0) #黒

def main(): #メイン処理を行う関数の定義
    pygame.init() #pygameモジュールの初期化
    #タイトル設定
    pygame.display.set_caption("初めてのPygame")
    #スクリーンの初期化
    screen = pygame.display.set_mode((800,600))
    #clockオブジェクトを作成
    clock = pygame.time.Clock()
    #fontオブジェクトを作成
    font = pygame.font.Font(None,80)
    #時間を管理する変数のtmrの宣言
    tmr = 0

    while True:
        tmr = tmr +1 #tmrの値を1増やす
        for event in pygame.event.get():
            #ウィンドウの閉じるボタンを押したとき
            if event.type == pygame.QUIT:
                pygame.quit() #pygameモジュールの初期化を解除
                sys.exit() #プログラムを終了

        #Surfaceに文字列を書く
        txt = font.render(str(tmr),True,WHITE)
        #指定した色でスクリーン全体をクリアする
        screen.fill(BLACK)
        #文字列を書いたSurfaceをスクリーンに転送
        screen.blit(txt,[300,200])
        #画面を更新する
        pygame.display.update()
        #フレームレートを指定
        clock.tick(10)

if __name__ == "__main__":
    main()
