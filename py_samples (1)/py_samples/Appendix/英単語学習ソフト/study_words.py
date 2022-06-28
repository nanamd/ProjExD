import tkinter

FNT1 = ("Times New Roman", 12)
FNT2 = ("Times New Roman", 24)

WORDS = [
"apple", "リンゴ",
"book", "本",
"cat", "猫",
"dog", "犬",
"egg", "卵",
"fire", "火",
"gold", "金色",
"head", "頭",
"ice", "氷",
"juice", "ジュース",
"king", "王様",
"lemon", "レモン",
"mother", "お母さん",
"notebook", "ノート",
"orange", "オレンジ",
"pen", "ペン",
"queen", "女王",
"room", "部屋",
"sport", "スポーツ",
"time", "時間",
"user", "ユーザー",
"vet", "獣医",
"window", "窓",
"xanadu", "桃源郷",
"yellow", "黄色",
"zoo", "動物園"
]
MAX = int(len(WORDS)/2)
score = 0
word_num = 0
yourword = ""
koff = False #１文字ずつ入力するためのフラグ

def key_down(e):
    global score, word_num, yourword, koff
    if koff == True:
        koff = False
        kcode = e.keycode
        ksym  = e.keysym
        if 65 <= kcode and kcode <= 90: #大文字
            yourword = yourword + chr(kcode+32)
        if 97 <= kcode and kcode <= 122: #小文字
            yourword = yourword + chr(kcode)
        if ksym == "Delete" or ksym == "BackSpace":
            yourword = yourword[:-1] # この記述でお尻の１文字を削除
        input_label["text"] = yourword
        if ksym == "Return":
            if input_label["text"] == english_label["text"]:
                score = score + 1
                set_label()

def key_up(e):
    global koff
    koff = True

def set_label():
    global word_num, yourword
    score_label["text"] = score
    english_label["text"] = WORDS[word_num*2]
    japanese_label["text"] = WORDS[word_num*2+1]
    input_label["text"] = ""
    word_num = (word_num + 1)%MAX
    yourword = ""

root = tkinter.Tk()
root.title("単語学習アプリ")
root.geometry("400x200")
root.resizable(False, False)
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
root["bg"] = "#DEF"

score_label = tkinter.Label(font=FNT1, bg="#DEF", fg="#4C0")
score_label.pack()
english_label = tkinter.Label(font=FNT2, bg="#DEF")
english_label.pack()
japanese_label = tkinter.Label(font=FNT1, bg="#DEF", fg="#444")
japanese_label.pack()
input_label = tkinter.Label(font=FNT2, bg="#DEF")
input_label.pack()
howto_label = tkinter.Label(text="英単語を入力し[Enter]を押す\n入力し直しは[Delete]か[BS]", font=FNT1, bg="#FFF", fg="#ABC")
howto_label.pack()

set_label()
root.mainloop()
