# Libraries Import　引っ張ってくる
from logging import RootLogger, root
import tkinter as tk
from tkinter import ttk
 
#ボタンの種類
# Define
BUTTON = [
    ['', 'C', 'AC', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['00', '0', '.', '=']
]
 
SYMBOL = ['+', '-', '*', '/']
 
# 電卓の機能
class Tuika(object):
    def __init__(self, root=None):
        # Define
        self.calc_str = '' # 計算用の文字列
 
 #サイズと余白の設定
        calc_frame = ttk.Frame(root, width=300, height=100) # 計算式と結果用のFrame
        calc_frame.propagate(False) # サイズが固定される
        calc_frame.pack(side=tk.TOP, padx=10, pady=20) # 余白の設定
        button_frame = ttk.Frame(root, width=300, height=400) # 計算ボタン用のFrame
        button_frame.propagate(False) # サイズが固定される
        button_frame.pack(side=tk.BOTTOM) # 余白の設定
 
# 計算結果や計算式の場所の設定
        self.calc_var = tk.StringVar() # 計算式用の動的変数
        self.ans_var = tk.StringVar() # 結果用の動的変数
        #色やフォントの変化　色は緑
        calc_label = tk.Label(calc_frame, textvariable=self.calc_var, 
                            font=("Ink Free",20), bg="green2") 
        #色は水色
        ans_label = tk.Label(calc_frame, textvariable=self.ans_var, 
                            font=("Ink Free",15), bg="turquoise1") 
        calc_label.pack(anchor=tk.E) # 右揃えで配置
        ans_label.pack(anchor=tk.E) # 右揃えで配置
 
 #ボタンの設定
        for y, row in enumerate(BUTTON, 1): # Buttonの配置
            for x, num in enumerate(row):
                #ボタンの色や大きさ等の変更
                button = tk.Button(button_frame, text=num, 
                                    font=('Ink Free', 20), width=6, height=3, 
                                    bg="Sky Blue1",fg="maroon")
                button.grid(row=y, column=x) # 列や行を指定して配置
                button.bind('<Button-1>', self.click_button) # Buttonが押された場合

#ボタンが押された時の設定
    def click_button(self, event):
        check = event.widget['text'] # 押したボタンのCheck

 #四則演算の設定
        if check == '=': # イコールの場合
            if self.calc_str[-1:] in SYMBOL: # 記号の場合、記号よりも前で計算
                self.calc_str = self.calc_str[:-1]
 
            res = '= ' + str(eval(self.calc_str)) # eval関数の利用
            self.ans_var.set(res)
        elif check == 'AC': # クリアの場合
            self.calc_str = ''
            self.ans_var.set('')
        elif check == 'C': # バックの場合
            self.calc_str = self.calc_str[:-1]
        elif check in SYMBOL: # 記号の場合
            if self.calc_str[-1:] not in SYMBOL and self.calc_str[-1:] != '':
                self.calc_str += check
            elif self.calc_str[-1:] in SYMBOL: # 記号の場合、入れ替える
                self.calc_str = self.calc_str[:-1] + check
        else: # 数字などの場合
            self.calc_str += check
 
        self.calc_var.set(self.calc_str)
    
#main 関数
if __name__ == '__main__':
    # Window Setting
    root = tk.Tk()
    # Window size non resizable
    root.resizable(width=False, height=False)
    root.title('三島電卓') # Window のタイトル
    Tuika(root)
    # Display表示させる
    root.mainloop() # Window をループで回すことで Widgit に対応できるようになる