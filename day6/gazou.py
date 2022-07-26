import tkinter as tk
from PIL import ImageTk

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("画像の表示")       # ウィンドウタイトル
        self.master.geometry("400x300")     # ウィンドウサイズ(幅x高さ)

        # Canvasの作成
        self.canvas = tk.Canvas(self.master)
        # Canvasを配置
        self.canvas.pack(expand = True, fill = tk.BOTH)

        # 画像ファイルを開く（対応しているファイルフォーマットはPGM、PPM、GIF、PNG）
        self.photo_image = ImageTk.PhotoImage(file = "fig/stat.png")

        # キャンバスのサイズを取得
        self.update() # Canvasのサイズを取得するため更新しておく
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # 画像の描画
        self.canvas.create_image(
                canvas_width / 2,       # 画像表示位置(Canvasの中心)
                canvas_height / 2,                   
                image=self.photo_image  # 表示画像データ
                )

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()