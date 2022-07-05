import tkinter
import random

# キー入力
key = ""
koff = False
def key_down(e):
    global key, koff
    key = e.keysym
    koff = False

def key_up(e):
    global koff # Mac
    koff = True # Mac
#    global key # Win
#    key = ""   # Win


DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3
ANIMATION = [0, 1, 0, 2]

idx = 0
tmr = 0
stage = 1
score = 0
nokori = 3
candy = 0

pen_x = 0
pen_y = 0
pen_d = 0
pen_a = 0

red_x = 0
red_y = 0
red_d = 0
red_a = 0
red_sx = 0
red_sy = 0

map_data = [] # 迷路用のリスト

def set_stage(): # ステージのデータをセットする
    global map_data, candy
    global red_sx, red_sy

    if stage == 1:
        map_data = [
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
        candy = 32
        red_sx = 630
        red_sy = 450

    if stage == 2:
        map_data = [
        [0,1,1,1,1,1,1,1,1,1,1,0],
        [0,2,2,2,3,3,3,3,2,2,2,0],
        [0,3,3,0,2,1,1,2,0,3,3,0],
        [0,3,3,1,3,3,3,3,1,3,3,0],
        [0,2,1,3,3,3,3,3,3,1,2,0],
        [0,3,3,0,3,3,3,3,0,3,3,0],
        [0,3,3,1,2,1,1,2,1,3,3,0],
        [0,2,2,2,3,3,3,3,2,2,2,0],
        [0,0,0,0,0,0,0,0,0,0,0,0]
        ]
        candy = 38
        red_sx = 630
        red_sy = 90

    if stage == 3:
        map_data = [
        [0,1,0,1,0,1,1,1,1,1,1,0],
        [0,2,1,3,1,2,2,3,3,3,3,0],
        [0,2,2,2,2,2,2,3,3,3,3,0],
        [0,2,1,1,1,2,2,1,1,1,1,0],
        [0,2,2,2,2,3,3,2,2,2,2,0],
        [0,1,1,2,0,2,2,0,1,1,2,0],
        [0,3,3,3,1,1,1,0,3,3,3,0],
        [0,3,3,3,2,2,2,0,3,3,3,0],
        [0,0,0,0,0,0,0,0,0,0,0,0]
        ]
        candy = 23
        red_sx = 630
        red_sy = 450


def set_chara_pos(): # キャラのスタート位置
    global pen_x, pen_y, pen_d, pen_a
    global red_x, red_y, red_d, red_a
    pen_x = 90
    pen_y = 90
    pen_d = DIR_DOWN
    pen_a = 3
    red_x = red_sx
    red_y = red_sy
    red_d = DIR_DOWN
    red_a = 3


def draw_txt(txt, x, y, siz, col): # 影付き文字
    fnt = ("Times New Roman", siz, "bold")
    canvas.create_text(x+2, y+2, text=txt, fill="black", font=fnt, tag="SCREEN")
    canvas.create_text(x, y, text=txt, fill=col, font=fnt, tag="SCREEN")


def draw_screen(): # ゲーム画面を描く
    canvas.delete("SCREEN")
    for y in range(9):
        for x in range(12):
            canvas.create_image(x*60+30, y*60+30, image=img_bg[map_data[y][x]], tag="SCREEN")
    canvas.create_image(pen_x, pen_y, image=img_pen[pen_a], tag="SCREEN")
    canvas.create_image(red_x, red_y, image=img_red[red_a], tag="SCREEN")
    draw_txt("SCORE "+str(score), 200, 30, 30, "white")
    draw_txt("STAGE "+str(stage), 520, 30, 30, "lime")
    for i in range(nokori):
        canvas.create_image(60+i*50, 500, image=img_pen[12], tag="SCREEN")


def check_wall(cx, cy, di, dot): # 各方向に壁があるか調べる
    chk = False
    if di == DIR_UP:
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
    global score, candy, pen_x, pen_y, pen_d, pen_a
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
    if map_data[my][mx] == 3: # キャンディに載ったか？
        score = score + 100
        map_data[my][mx] = 2
        candy = candy - 1


def move_enemy(): # レッドを動かす
    global idx, tmr, red_x, red_y, red_d, red_a
    speed = 10
    if red_x%60 == 30 and red_y%60 == 30:
        red_d = random.randint(0, 6)
        if red_d >= 4:
            if pen_y < red_y:
                red_d = DIR_UP
            if pen_y > red_y:
                red_d = DIR_DOWN
            if pen_x < red_x:
                red_d = DIR_LEFT
            if pen_x > red_x:
                red_d = DIR_RIGHT
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
    if abs(red_x-pen_x) <= 40 and abs(red_y-pen_y) <= 40:
        idx = 2
        tmr = 0


def main(): # メインループ
    global key, koff, idx, tmr, stage, score, nokori
    tmr = tmr + 1
    draw_screen()

    if idx == 0: # タイトル画面
        canvas.create_image(360, 200, image=img_title, tag="SCREEN")
        if tmr%10 < 5:
            draw_txt("Press SPACE !", 360, 380, 30, "yellow")
        if key == "space":
            stage = 1
            score = 0
            nokori = 3
            set_stage()
            set_chara_pos()
            idx = 1

    if idx == 1: # ゲームをプレイ
        move_penpen()
        move_enemy()
        if candy == 0:
            idx = 4
            tmr = 0

    if idx == 2: # 敵にやられた
        draw_txt("MISS", 360, 270, 40, "orange")
        if tmr == 1:
            nokori = nokori - 1
        if tmr == 30:
            if nokori == 0:
                idx = 3
                tmr = 0
            else:
                set_chara_pos()
                idx = 1

    if idx == 3: # ゲームオーバー
        draw_txt("GAME OVER", 360, 270, 40, "red")
        if tmr == 50:
            idx = 0

    if idx == 4: # ステージクリア
        if stage < 3:
            draw_txt("STAGE CLEAR", 360, 270, 40, "pink")
        else:
            draw_txt("ALL STAGE CLEAR!", 360, 270, 40, "violet")
        if tmr == 30:
            if stage < 3:
                stage = stage + 1
                set_stage()
                set_chara_pos()
                idx = 1
            else:
                idx = 0

    if koff == True:
        key = ""
        koff = False

    root.after(100, main)


root = tkinter.Tk()

img_bg = [
    tkinter.PhotoImage(file="image_penpen/chip00.png"),
    tkinter.PhotoImage(file="image_penpen/chip01.png"),
    tkinter.PhotoImage(file="image_penpen/chip02.png"),
    tkinter.PhotoImage(file="image_penpen/chip03.png")
]
img_pen = [
    tkinter.PhotoImage(file="image_penpen/pen00.png"),
    tkinter.PhotoImage(file="image_penpen/pen01.png"),
    tkinter.PhotoImage(file="image_penpen/pen02.png"),
    tkinter.PhotoImage(file="image_penpen/pen03.png"),
    tkinter.PhotoImage(file="image_penpen/pen04.png"),
    tkinter.PhotoImage(file="image_penpen/pen05.png"),
    tkinter.PhotoImage(file="image_penpen/pen06.png"),
    tkinter.PhotoImage(file="image_penpen/pen07.png"),
    tkinter.PhotoImage(file="image_penpen/pen08.png"),
    tkinter.PhotoImage(file="image_penpen/pen09.png"),
    tkinter.PhotoImage(file="image_penpen/pen10.png"),
    tkinter.PhotoImage(file="image_penpen/pen11.png"),
    tkinter.PhotoImage(file="image_penpen/pen_face.png")
]
img_red = [
    tkinter.PhotoImage(file="image_penpen/red00.png"),
    tkinter.PhotoImage(file="image_penpen/red01.png"),
    tkinter.PhotoImage(file="image_penpen/red02.png"),
    tkinter.PhotoImage(file="image_penpen/red03.png"),
    tkinter.PhotoImage(file="image_penpen/red04.png"),
    tkinter.PhotoImage(file="image_penpen/red05.png"),
    tkinter.PhotoImage(file="image_penpen/red06.png"),
    tkinter.PhotoImage(file="image_penpen/red07.png"),
    tkinter.PhotoImage(file="image_penpen/red08.png"),
    tkinter.PhotoImage(file="image_penpen/red09.png"),
    tkinter.PhotoImage(file="image_penpen/red10.png"),
    tkinter.PhotoImage(file="image_penpen/red11.png")
]
img_title = tkinter.PhotoImage(file="image_penpen/title.png")

root.title("はらはら ペンギン ラビリンス")
root.resizable(False, False)
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=720, height=540)
canvas.pack()
set_stage()
set_chara_pos()
main()
root.mainloop()
