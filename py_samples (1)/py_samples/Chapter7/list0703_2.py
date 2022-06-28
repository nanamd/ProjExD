import tkinter
root = tkinter.Tk()
root.title("最初からチェックされた状態にする")
root.geometry("400x200")
cval = tkinter.BooleanVar()
cval.set(True)
cbtn = tkinter.Checkbutton(text="チェックボタン", variable=cval)
cbtn.pack()
root.mainloop()
