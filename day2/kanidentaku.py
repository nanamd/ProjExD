
# Libraries Import
import tkinter as tk

# 簡易的な電卓を作ってみた！
class CaluGui(object):
    def __init__(self, app=None):
        # Window Setting
        app.title('簡易的な電卓を作ってみた') # Window のタイトル
        app.geometry('400x600') # Window のサイズ



def main():
    # Window Setting
    app = tk.Tk()
    CaluGui(app)

    # Display
    app.mainloop() # Window をループで回すことで Widgit に対応できるようになる

if __name__ == '__main__':
    main()