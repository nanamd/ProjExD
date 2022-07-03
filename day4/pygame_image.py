#pygameモジュールをインストール
import pygame

#sysモジュールをインポート
import sys


def main(): #メイン処理を行う関数の定義
    pygame.init() #pygameモジュールの初期化
    #タイトル設定
    pygame.display.set_caption("初めてのPygame 画像表示")
    #スクリーンの初期化
    screen = pygame.display.set_mode((640,360))
    #clockオブジェクトを作成
    clock = pygame.time.Clock()
    #背景画像の読み込み
    img_bg = pygame.image.load("pg_bg.png")
    #キャラクター画像の読み込み
    img_chara = [
        pygame.image.load("pg_chara0.png"),
        pygame.image.load("pg_chara1.png")
                ]
    #時間を管理する変数のtmrの宣言
    tmr = 0

    while True:
        tmr = tmr +1 #tmrの値を1増やす
        for event in pygame.event.get(): #イベント全てを格納する箱
            #ウィンドウの閉じるボタンを押したとき
            if event.type == pygame.QUIT:
                pygame.quit() #pygameモジュールの初期化を解除
                sys.exit() #プログラムを終了
            #キーを押すイベントが発生した時
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1: #F1
                    #フルスクリーンモードにする
                    screen = pygame.display.set_mode((640,360),pygame.FULLSCREEN)
                    #F2かEscキーなら
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen=pygame.display.set_mode((640,360)) #通常表示に戻す

                    #背景スクロール用の値をtmrから求める
                    x = tmr%160
                    #繰り返しで横に5枚分
                    for i in range(5):
                        #背景画像を描画
                        screen.blit(img_bg,[i*160-x, 0])
                        #キャラクターをアニメーションさせて描画
                        screen.blit(img_chara[tmr%2],[224,160])
                        pygame.display.update()
                        clock.tick(5)

if __name__ == "__main__":
    main()
