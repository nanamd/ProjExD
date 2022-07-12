import tkinter
import tkinter.messagebox

def click_btn():
    tkinter.messagebox.showinfo("情報", "ボタンを押しました")

root = tkinter.Tk()
root.title("初めてのメッセージボックス")
root.geometry("400x200")
btn = tkinter.Button(text="テスト", command=click_btn)
btn.pack()
root.mainloop()
