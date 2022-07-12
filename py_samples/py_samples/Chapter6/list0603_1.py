import tkinter
root = tkinter.Tk()
root.title("初めてのボタン")
root.geometry("800x600")
button = tkinter.Button(root, text="ボタンの文字列", font=("Times New Roman", 24))
button.place(x=200, y=100)
root.mainloop()
