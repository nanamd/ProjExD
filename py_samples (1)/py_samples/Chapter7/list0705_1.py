import tkinter

root = tkinter.Tk()
root.title("ネコ度診断アプリ")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="sumire.png")
canvas.create_image(400, 300, image=gazou)
button = tkinter.Button(text="診断する", font=("Times New Roman", 32), bg="lightgreen")
button.place(x=400, y=480)
text = tkinter.Text(width=40, height=5, font=("Times New Roman", 16))
text.place(x=320, y=30)
root.mainloop()
