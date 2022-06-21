import tkinter

# フォント設定
FONT = ("Times New Roman", 30)

class Calculator():
    def __init__(self, master):
        '''コンストラクタ'''

        # 親ウィジェット
        self.master = master
        # 第１項
        self.item1 = None
        # 次に演算子ボタンが押された時に行う演算
        self.operation = None
        # 直前に演算子ボタンが押されたかどうかのフラグ
        self.op_clicked = False
        # ラベルウィジェット
        self.label = None

        # ウィジェット作成・配置・イベント設定
        self.create_widgets()
    
    def create_widgets(self):
        '''ウィジェットの作成・配置・イベント設定'''

        numbers = ("7","8","9","4","5","6","1","2","3","0")
        operators = ("÷", "×", "-", "+", "=")

        # 計算結果表示用のラベル
        self.label = tkinter.Label(
            self.master,
            text="0", # 表示文字
            font=FONT, # フォント設定
            anchor=tkinter.E, # テキスト右寄せ
            bg="black", # 背景の色
            fg="white" # 文字の色
        )
        self.label.grid(
            column=0,
            row=0,
            columnspan=4,
            sticky=tkinter.NSEW # 左右上下に引き伸ばす
        )

        # ACボタン作成
        self.create_button(text="AC", x=0, y=1, size=3, func=self.AC_click)

        # 数字ボタン作成
        i = 0
        for number in numbers:
            if number == "0":
                # ボタン 0 だけボタン３つ分のサイズで作成
                self.create_button(text=number, x=i%3,y=i//3+2,size=3,func=self.num_click)
            else:
                self.create_button(text=number, x=i%3,y=i//3+2,size=1,func=self.num_click)

            i += 1

        # 演算子ボタン作成
        i = 0
        for operator in operators:
            self.create_button(text=operator, x=3,y=i+1,size=1,func=self.operation_click)
            i += 1

    def create_button(self, text, x, y, size, func):
        '''ボタンウィジェットの作成・配置・イベント設定'''

        button = tkinter.Button(
            self.master,
            text=text, # 表示する文字列
            font=FONT, # FONTサイズ設定
            anchor=tkinter.CENTER, # 中央よせ
        )
        button.grid(
            column=x, # 表示位置（横）
            row=y, # 表示位置（縦）
            columnspan=size, # 表示サイズ（横）
            sticky = tkinter.NSEW # 左右上下に引き伸ばし
        )

        # イベント設定
        button.bind("<ButtonPress>", func)

    def AC_click(self, event):
        '''ACボタンがクリックされたときの処理'''
    
        # ラベルを 0 にセット
        self.label.config(text="0")

        # 初期値に設定
        self.item1 = None
        self.op_clicked = False
        self.operation = None

    def num_click(self, event):
        '''数字ボタンがクリックされたときの処理'''

        # ボタンの数字取得
        num_text = event.widget.cget("text")

        # ラベル表示中の数字取得
        label_text = self.label.cget("text")


        if self.op_clicked or label_text == "0":
            # 演算子ボタンクリック直後 or 表示が 0 の場合は表示中の数字置き換え
            self.label.config(
                text=num_text
            )
        else:
            # それ以外は最後の桁に数字を追加
            self.label.config(
                text=label_text + num_text
            )

        # 直前に押されたのが演算子ボタンでないことを設定
        self.op_clicked = False

    def operation_click(self, event):
        '''演算子ボタンがクリックされたときの処理'''

        # 押されたボタンの演算子を取得
        next_operation = event.widget.cget("text")

        #　表示中の数字を取得
        label_text = self.label.cget("text")

        if self.item1 is None:
            # １つ目の数字入力中にクリックされた場合の処理

            # 表示中の数字を１つ目の数字として登録
            self.item1 = int(label_text)

        elif self.op_clicked:
            # 演算子ボタン入力直後にクリックされた場合の処理

            # ここでは何もしない（最後の演算子の登録のみ行う）
            pass

        else:
            # ２つ目の数字入力中にクリックされた場合の処理

            if self.operation != "=":
                # 表示中の数字を２つ目の数字とする
                item2 = int(label_text)

                # 計算実行
                result_num = self.calc(self.item1, item2, self.operation)

                # 計算結果を表示
                self.label.config(
                    text=str(result_num)
                )

                # 計算結果を１つ目の数字として更新
                self.item1 = result_num


        # 直前に演算子が押されたことを設定
        self.op_clicked = True

        # 次に実行する演算子を設定
        self.operation = next_operation

    def calc(self, item1, item2, operation):
        '''計算を実行する'''

        # 計算を実行
        if operation == "+":
            result_num = item1 + item2
        elif operation == "-":
            result_num = item1 - item2
        elif operation == "÷":
            if item2 == 0:
                result_num = 0
            else:
                result_num = item1 // item2
        elif operation == "×":
            result_num = item1 * item2

        return result_num

app = tkinter.Tk()
app.title("電卓")
calc = Calculator(app)
app.mainloop()