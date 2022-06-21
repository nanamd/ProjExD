# 電卓 Level0

import sys
import tkinter as tk

# メイン関数
def main():
    root = tk.Tk()
    root.title("電卓L0")
    den = Dentaku(root)
    root.mainloop()

# 電卓クラス
class Dentaku():
    # 作成
    def __init__(self, root):
        self.tf = tk.Frame(root)    # トップレベルのフレーム
        self.tf.grid(column = 0, row = 0, padx = 15, pady = 15)

        # ボタンを配置
        ButtonDef = (
        #     行 列 ラベル 関数
            (4, 0, "0", self.numinput),
            (3, 0, "1", self.numinput),
            (3, 1, "2", self.numinput),
            (3, 2, "3", self.numinput),
            (2, 0, "4", self.numinput),
            (2, 1, "5", self.numinput),
            (2, 2, "6", self.numinput),
            (1, 0, "7", self.numinput),
            (1, 1, "8", self.numinput),
            (1, 2, "9", self.numinput),
            (4, 1, "*", self.mul),
            (4, 2, "/", self.div),
            (1, 3, "-", self.sub),
            (2, 3, "+", self.add),
            (3, 3, "=", self.equal),
            (4, 3, "C", self.clear))

        root.option_add('*Button.font', 'ＭＳゴシック 28')
        for r, c, label, func in ButtonDef:
            Button = tk.Button(self.tf, text = label)
            Button.bind("<Button-1>", func)
            Button.grid(column = c, row = r, sticky = tk.N +tk.E + tk.S + tk.W)

        # 数字が表示される「エントリー」
        root.option_add('*Entry.font', 'ＭＳゴシック 32')
        self.NumBox = tk.Entry(self.tf, width = 10, justify = tk.RIGHT)
        self.NumBox.insert(tk.END, "0")
        self.NumBox.grid(column = 0, columnspan = 4, row = 0)

    # ボタン毎の動作を定義（イベントドライバ群）
    def numinput(self, e):            # 数字キー
        pass

    def mul(self, e):                # ×
        pass

    def div(self, e):                # ／
        pass

    def sub(self, e):                # －
        pass

    def add(self, e):                # ＋
        pass

    def equal(self, e):                # ＝
        pass

    def clear(self, e):                # Ｃ
        pass

if __name__ == '__main__':
    main()