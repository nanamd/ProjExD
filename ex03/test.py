
from logging import root
import tkinter as tk
import tkinter.messagebox as tkm


def count_up():
    global tmr 
    tmr = tmr +1
    label["text"]=tmr
    root.after(1000, count_up)

def count_down(event):
    btn = event.keysym
    txt = btn["text"]
    tkm.showinfo("キー推す", f"[{txt}]ボタンが押されました")



if __name__ == "__main__":
    root = tk.Tk()
    label = tk.Label(root, text="hello",
                    font=("Times New Roman",80)
                    )
    label.pack()
    tmr=0 #グローバル変数
    #root.after(1000, count_up)
    root.bind("<KeyPress>",key_down)
    root.mainloop()