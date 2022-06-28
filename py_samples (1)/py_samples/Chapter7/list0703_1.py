import tkinter
root = tkinter.Tk()
root.title("チェックボタンを扱う")
root.geometry("400x200")
cbtn = tkinter.Checkbutton(text="チェックボタン")
cbtn.pack()
root.mainloop()
