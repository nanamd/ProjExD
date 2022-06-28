from logging import root
import tkinter

key=""
def key_down(e):
    global key
    key=e.keysym

def key_up(e):
    global key
    key = ""

mx = 1
my = 1

def main_proc():
    global mx, my
    if key == "Up" and maze[my-1][mx]==0:
        my = my -1
    if key == "Down" and maze[my+1][mx]==0:
        my = my +1
    if key == "Left" and maze[my][mx-1]==0:
        my = my -1
    if key == "Right" and maze[my][mx+1]==0:
        my = my +1
    canvas.coords("MYCHR",mx*80+40,my*80+40)
    root.after(300,main_proc)

root
    