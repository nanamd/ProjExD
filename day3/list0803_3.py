from logging import root
import tkinter

from pip import main

key =""
def key_down(e):
    global key
    key = e.keysym

def key_up(e):
    global key
    key = ""

cx = 400
cy = 300

def main_proc():
    global cx,cy

    if key=="Up":
        cy = cy-20
    if key=="Down":
        cy = cy+20
    if key=="Left":
        cy = cy-20
    if key=="Right":
        cy = cy+20

    canvas.coords("MYCHR",cx,cy)
    root.after(100,main_proc)

root = tkinter.Tk()
root.title("キャラクターの移動")
root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)
canvas = tkinter.Canvas(width=800,height=600,
                        bg="Lightgreen")
canvas.pack()
img = tkinter.PhotoImage(file="mimi.png")
canvas.create_image(cx,cy,image=img, tag="MYCHR")
main_proc()
root.mainloop()