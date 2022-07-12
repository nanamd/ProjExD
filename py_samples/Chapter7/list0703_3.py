import tkinter

def check():
    if cval.get() == True:
        print("チェックされています")
    else:
        print("チェックされていません")

root = tkinter.Tk()
root.title("チェックの状態を知る")
root.geometry("400x200")
cval = tkinter.BooleanVar()
cval.set(False)
cbtn = tkinter.Checkbutton(text="チェックボタン", variable=cval, command=check)
cbtn.pack()
root.mainloop()
