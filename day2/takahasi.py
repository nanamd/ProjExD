import tkinter as tk
import tkinter.messagebox as tkm
from unicodedata import ucnhash_CAPI

def click_equal(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(res))

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    #tkm.showinfo(txt, f"{txt}ボタンクリックされました")
    entry.insert(tk.END,txt)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("tk")
    root.geometry("300x450")
    r, c = 1, 1
    for i, num in enumerate(range(9, -1, -1), 1):
        btn = tk.Button(root,text=num,command=button_click, font=("Times New Roman", 60))
        btn.bind("<1>", button_click)
        btn.grid(row=r, column=c, padx=3, pady=3)
        if i%3 == 0:
            r += 1
            c = 0
        c += 1

    btn = tk.Button(root,text="+", font=("Times New Roman", 60))
    btn.bind("<1>", button_click)
    btn.grid(row=r, column=c, padx=10,pady=10)

    btn = tk.Button(root,text="=", font=("Times New Roman", 60))
    btn.bind("<1>", click_equal)
    btn.grid(row=4, column=3, padx=10,pady=10)

    entry = tk.Entry(root, justify="right", width=10, font=("Times New Roman", 50))
    entry.grid(row=0, column=1, columnspan=4)

    root.mainloop()
