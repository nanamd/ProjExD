print("Hello world")

from cProfile import label
from cgitb import text
import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo("タイトル",f"{txt}が押されました")

root = tk.Tk()
root.title("おためしか")
root.geometry("500x200")

label = tk.Label(root,
                text="ラベルを書いてみた件",
                font=("Ricty Diminished",20)
                )
label.pack()

#ボタン
button=tk.Button(root, text="押すな")
#"<1>"が押されたらbutton_click関数が呼び出される
button.bind("<1>",button_click)
button.pack()

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}]ボタンが押されました")
#エントリーEntryクラス
entry = tk.Entry(width=30)
#insert(位置,文字列(入力したい文字))
#これを入れなければ自分で入力する形になる
entry.insert(tk.END, "fugapiyo")
entry.pack()


#showOOで変わる
tkm.showwarning("警告","ボタン押したらあかんやろ")


root.mainloop()

