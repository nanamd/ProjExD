import tkinter

root = tkinter.Tk()
root.geometry("400x200")
root.title("PythonでGUIを扱う")
label = tkinter.Label(root, text="ゲーム開発の一歩", font=("Times New Roman", 20))
label.place(x=80, y=60)
root.mainloop()
