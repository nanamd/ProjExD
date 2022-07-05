import tkinter

root = tkinter.Tk()
root.title("Canvasに画像を描画する")
canvas = tkinter.Canvas(width=480, height=300)
canvas.pack()
img_bg = tkinter.PhotoImage(file="park.png")
canvas.create_image(240, 150, image=img_bg)
root.mainloop()
