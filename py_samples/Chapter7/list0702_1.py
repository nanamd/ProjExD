import tkinter

def click_btn():
    text.insert(tkinter.END, "モンスターが現れた！")

root = tkinter.Tk()
root.title("複数行のテキスト入力")
root.geometry("400x200")
button = tkinter.Button(text="メッセージ", command=click_btn)
button.pack()
text = tkinter.Text()
text.pack()
root.mainloop()
