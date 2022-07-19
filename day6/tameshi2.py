import tkinter
import random

# キー入力
key = ""                #キーの値を代入する変数
koff = False            #キーが離された時に使う変数(フラグ)
def key_down(e):        #キーが押された時に使う関数
    global key, koff    #グローバル変数として設定
    key = e.keysym      
    koff = False

def key_up(e):
    global koff # Mac
    koff = True # Mac



DIR_UP = 0      #キャラを上向き
DIR_DOWN = 1    #下向き
DIR_LEFT = 2    #左
DIR_RIGHT = 3   #右
ANIMATION = [0, 1, 0, 2]

tmr = 0     #タイマーの初期値
score = 0   #スコアの初期値

pen_x = 90  #青ペンギンのx座標の初期値
pen_y = 90  #青ペンギンのy座標の初期値
pen_d = 0   #青ペンギンの向きの初期値
pen_a = 0   #青ペンギンの画像番号の初期値

red_x = 630     #赤ペンギンのx座標の初期値
red_y = 450     #赤ペンギンのy座標の初期値
red_d = 0       #赤ペンギンの向きの初期値
red_a = 0        #赤ペンギンの画像番号の初期値

map_data = [    #迷路の生成
    [0,1,1,1,1,0,0,1,1,1,1,0],
    [0,2,3,3,2,1,1,2,3,3,2,0],
    [0,3,0,0,3,3,3,3,0,0,3,0],
    [0,3,1,1,3,0,0,3,1,1,3,0],
    [0,3,2,2,3,0,0,3,2,2,3,0],
    [0,3,0,0,3,1,1,3,0,0,3,0],
    [0,3,1,1,3,3,3,3,1,1,3,0],
    [0,2,3,3,2,0,0,2,3,3,2,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]
]


def draw_txt(txt, x, y, siz, col): # 影付き文字
    fnt = ("Times New Roman", siz, "bold")
    canvas.create_text(x+2, y+2, text=txt, fill="black", font=fnt, tag="SCREEN")
    canvas.create_text(x, y, text=txt, fill=col, font=fnt, tag="SCREEN")


def draw_screen(): # ゲーム画面を描く
    for y in range(9):
        for x in range(12):
            canvas.create_image(x*60+30, y*60+30, image=img_bg[map_data[y][x]], tag="SCREEN")
    canvas.create_image(pen_x, pen_y, image=img_pen[pen_a], tag="SCREEN")
    canvas.create_image(red_x, red_y, image=img_red[red_a], tag="SCREEN")
    draw_txt("SCORE "+str(score), 200, 30, 30, "white")


def check_wall(cx, cy, di, dot): # 各方向に壁があるか調べる
    chk = False
    if di == DIR_UP:    #上向きの時
        mx = int((cx-30)/60)    
        my = int((cy-30-dot)/60)
        if map_data[my][mx] <= 1: # 左上
            chk = True
        mx = int((cx+29)/60)
        if map_data[my][mx] <= 1: # 右上
            chk = True
    if di == DIR_DOWN:
        mx = int((cx-30)/60)
        my = int((cy+29+dot)/60)
        if map_data[my][mx] <= 1: # 左下
            chk = True
        mx = int((cx+29)/60)
        if map_data[my][mx] <= 1: # 右下
            chk = True
    if di == DIR_LEFT:
        mx = int((cx-30-dot)/60)
        my = int((cy-30)/60)
        if map_data[my][mx] <= 1: # 左上
            chk = True
        my = int((cy+29)/60)
        if map_data[my][mx] <= 1: # 左下
            chk = True
    if di == DIR_RIGHT:
        mx = int((cx+29+dot)/60)
        my = int((cy-30)/60)
        if map_data[my][mx] <= 1: # 右上
            chk = True
        my = int((cy+29)/60)
        if map_data[my][mx] <= 1: # 右下
            chk = True
    return chk


def move_penpen(): # ペンペンを動かす
    global score, pen_x, pen_y, pen_d, pen_a
    if key == "Up":
        pen_d = DIR_UP
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_y = pen_y - 20
    if key == "Down":
        pen_d = DIR_DOWN
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_y = pen_y + 20
    if key == "Left":
        pen_d = DIR_LEFT
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_x = pen_x - 20
    if key == "Right":
        pen_d = DIR_RIGHT
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_x = pen_x + 20
    pen_a = pen_d*3 + ANIMATION[tmr%4]
    mx = int(pen_x/60)
    my = int(pen_y/60)
    if map_data[my][mx] == 3: # キャンディ
        score = score + 50
        map_data[my][mx] = 2 #凍った道
    elif map_data[my][mx] ==4: #解けた道
        score = score -20
        map_data[my][mx] = 2 #凍った道
    elif map_data[my][mx] == 5: #解けた道白黒キャン 5
        score = score +5
        map_data[my][mx] = 6 #凍った道白黒キャン 6
    elif map_data[my][mx] ==6:
        score = score -50
        map_data[my][mx] = 7
    elif map_data[my][mx] == 8:
        score = score + 100
        map_data[my][mx] = 2


def move_enemy(): # レッドを動かす
    global red_x, red_y, red_d, red_a
    speed = 10
    if red_x%60 == 30 and red_y%60 == 30:
        red_d = random.randint(0, 3)
    if red_d == DIR_UP:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_y = red_y - speed
    if red_d == DIR_DOWN:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_y = red_y + speed
    if red_d == DIR_LEFT:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_x = red_x - speed
    if red_d == DIR_RIGHT:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_x = red_x + speed
    red_a = red_d*3 + ANIMATION[tmr%4]
    mx = int(red_x/60)
    my = int(red_y/60)
    if map_data[my][mx] == 2: # 凍った道
        map_data[my][mx] = 4#氷が解ける
    elif map_data[my][mx] == 3: #色キャン
        map_data[my][mx] = 5 #解けた道白黒キャン
    elif map_data[my][mx] == 7:#おかしなキャン
        map_data[my][mx] = 8#キラキラキャン
    
'''
 elif map_data[my][mx] == 6:#凍った道白黒キャン
        map_data[my][mx] = 5#解けた道白黒キャン
        '''


def main(): # メインループ
    global key, koff, tmr
    tmr = tmr + 1
    draw_screen()
    move_penpen()
    move_enemy()
    if koff == True:
        key = ""
        koff = False
    root.after(100, main)


root = tkinter.Tk()

img_bg = [  #道の画像
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/chip0.png"),#氷の壁 0
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/chip1.png"),#氷の境目 1
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/chip2.png"),#凍った道 2
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/chip3.png"),#凍った床色キャン 3
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/chip4.png"),#解けた道 4
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/chip5.png"),#解けた道白黒キャン 5
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/chip6.png"),#凍った道白黒キャン 6
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/chip7.png"),#おかしなキャン7
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/chip8.png")#おかしなキャン7

]
#青いペンギンの画像
img_pen = [
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/pen00.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/pen01.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/pen02.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/pen03.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/pen04.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/pen05.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/pen06.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/pen07.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/pen08.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/pen09.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/pen10.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/pen11.png")
]
#赤いペンギンの画像
img_red = [
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/red00.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/red01.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/red02.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/red03.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/red04.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/red05.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/red06.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/red07.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/red08.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/red09.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/red10.png"),
    tkinter.PhotoImage(file="py2_samples/Chapter3/image_penpen/red11.png")
]

root.title("食中毒には気をつけろ！") #タイトル
root.resizable(False, False)        #ウィンドウのサイズを変更不可にする
root.bind("<KeyPress>", key_down)   #
root.bind("<KeyRelease>", key_up)   #
canvas = tkinter.Canvas(width=720, height=540)
canvas.pack()                       #キャンバスの部品を作る
main()
root.mainloop()                     #ウィンドウを表示
