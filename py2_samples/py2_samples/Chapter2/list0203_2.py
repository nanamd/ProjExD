import tkinter
import math

def trigo():
    try:
        d = float(entry.get())
        a = math.radians(d)
        s = math.sin(a)
        c = math.cos(a)
        t = math.tan(a)
        label_s["text"] = "sin "+str(s)
        label_c["text"] = "cos "+str(c)
        label_t["text"] = "tan "+str(t)
    except:
        print("角度を度の値で入力してください")

root = tkinter.Tk()
root.geometry("300x200")
root.title("三角関数の値")

entry = tkinter.Entry(width=10)
entry.place(x=20, y=20)
button = tkinter.Button(text="計算", command=trigo)
button.place(x=110, y=20)
label_s = tkinter.Label(text="sin")
label_s.place(x=20, y=60)
label_c = tkinter.Label(text="cos")
label_c.place(x=20, y=100)
label_t = tkinter.Label(text="tan")
label_t.place(x=20, y=140)

root.mainloop()
