import tkinter
import random

# キャンバスのサイズ設定
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400

# 迷路のサイズ設定
WIDTH = 31 # 5以上の奇数
HEIGHT = 21 # 5以上の奇数

# 色設定
PATH_COLOR = "white"
WALL_COLOR = "gray"
GOAL_COLOR = "blue"
START_COLOR = "green"
PASSED_COLOR = "orange"
NOW_COLOR = "red"

# 数値の定義
PATH = 0
WALL = 1
GOAL = 2
START = 3
PASSED = 4
NOW = 5

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


class Maze():
    def __init__(self, master):
        '''迷路ゲームの起動'''

        # ゲームを作成する親ウィジェット
        self.master = master

        # 迷路のサイズ
        self.width = WIDTH
        self.height = HEIGHT

        # 迷路の元になるリスト
        self.maze = None

        # 現在位置
        self.now = None

        # 1つ前の位置
        self.before = None

        # スタートとゴールの位置
        self.start = None
        self.goal = None

        # 解答を既に見つけたかどうかのフラグ
        self.resolved = False

        # 迷路の元になる２次元リストを作成
        self.createMaze()

        # ウィジェットを作成して迷路を表示
        self.createWidgets()

    def createMaze(self):
        '''迷路の元になる２次元リストを作成'''

        # ２次元リストを作成（全て壁）
        self.maze = [[WALL] * self.width for j in range(self.height)]

        # 開始点を決定
        i = 2 * random.randint(0, self.width // 2 - 1) + 1
        j = 2 * random.randint(0, self.height // 2 - 1) + 1

        # (i, j) を通路に設定
        self.maze[j][i] = PATH

        # 穴掘り法でマス(i, j) を起点に穴を掘る
        self.dig(i, j)

        # ここまで穴掘り法

        # スタートを設定
        self.setStart()

        # ゴールを決定
        self.setGoal()

    def setStart(self):
        '''スタートの位置を設定'''

        # 通路の数をカウント
        num_path = 0
        for j in range(self.height):
            for i in range(self.width):
                if self.maze[j][i] == PATH:
                    num_path += 1

        # スタートの位置をランダムに決定
        startPos = random.randint(0, num_path - 1)

        # 左上からstartPos個目の通路のマスをスタートに設定
        count = 0
        for j in range(self.height):
            for i in range(self.width):
                if self.maze[j][i] == PATH:
                    if count == startPos:
                        self.maze[j][i] = START
                        self.start = (i, j)
                        return
                    else:
                        count += 1

    def setGoal(self):
        '''ゴールの位置を設定'''

        # 通路の数をカウント
        num_path = 0
        for j in range(self.height):
            for i in range(self.width):
                if self.maze[j][i] == PATH:
                    num_path += 1

        # ゴールの位置をランダムに決定
        goalPos = random.randint(0, num_path - 1)

        # 左上からgoalPos個目の通路のマスをゴールに設定
        count = 0
        for j in range(self.height):
            for i in range(self.width):
                if self.maze[j][i] == PATH:
                    if count == goalPos:
                        self.maze[j][i] = GOAL
                        self.goal = (i, j)
                        return
                    else:
                        count += 1

    def dig(self, i, j):
        '''(i,j)座標を起点に穴を掘る'''

        # どの方向を掘ろうとしたかを覚えておく変数
        up = True
        down = True
        left = True
        right = True

        # 全方向試すまでループ
        while up or down or left or right:
            # 0 - 3 の乱数を取得
            d = random.randint(0, 3)

            if d == UP:
                # 上方向が掘れるなら掘る
                if j - 2 >= 0 and j - 2 < self.height:
                    if self.maze[j - 2][i] == WALL:
                        self.maze[j - 2][i] = PATH
                        self.maze[j - 1][i] = PATH
                        self.dig(i, j - 2)

                up = False

            elif d == DOWN:
                # 下方向が掘れるなら掘る
                if j + 2 >= 0 and j + 2 < self.height:
                    if self.maze[j + 2][i] == WALL:
                        self.maze[j + 2][i] = PATH
                        self.maze[j + 1][i] = PATH
                        self.dig(i, j + 2)

                down = False

            elif d == LEFT:
                # 左方向が掘れるなら掘る
                if i - 2 >= 0 and i - 2 < self.width:
                    if self.maze[j][i - 2] == WALL:
                        self.maze[j][i - 2] = PATH
                        self.maze[j][i - 1] = PATH
                        self.dig(i - 2, j)

                left = False

            elif d == RIGHT:
                # 右方向が掘れるなら掘る
                if i + 2 >= 0 and i + 2 < self.width:
                    if self.maze[j][i + 2] == WALL:
                        self.maze[j][i + 2] = PATH
                        self.maze[j][i + 1] = PATH
                        self.dig(i + 2, j)

                right = False

    def change_color(self, i, j):
        '''(i,j)座標に対応する長方形の色を変更'''

        # mazeリストの値に応じて色を取得
        if self.maze[j][i] == WALL:
            color = WALL_COLOR
        elif self.maze[j][i] == PATH:
            color = PATH_COLOR
        elif self.maze[j][i] == GOAL:
            color = GOAL_COLOR
        elif self.maze[j][i] == START:
            color = START_COLOR
        elif self.maze[j][i] == PASSED:
            color = PASSED_COLOR
        elif self.maze[j][i] == NOW:
            color = NOW_COLOR
        else:
            print("そんなマスはあり得ません")
            return

        # (i,j)座標の長方形を特定するためにタグを作る
        tag = "rectangle_" + str(i) + "_" + str(j)

        # そのタグがつけられたfill設定を変更
        self.canvas.itemconfig(
            tag,
            fill=color
        )

    def createWidgets(self):
        '''ウィジェットを作成する'''

        # キャンバスウィジェットの作成と配置
        self.canvas = tkinter.Canvas(
            self.master,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
        )
        self.canvas.pack()

        for j in range(self.height):
            for i in range(self.width):

                # 後から操作できるように座標に基づいたタグを付ける
                tag = "rectangle_" + str(i) + "_" + str(j)

                # キャンバスへの長方形の描画（迷路の描画）
                self.canvas.create_rectangle(
                    3 + i * CANVAS_WIDTH / self.width,
                    3 + j * CANVAS_HEIGHT / self.height,
                    3 + (i + 1) * CANVAS_WIDTH / self.width,
                    3 + (j + 1) * CANVAS_HEIGHT / self.height,
                    width=0,  # 枠線なし
                    tag=tag  # タグ
                )

                # 長方形に色をつける
                self.change_color(i, j)

        # ボタンの作成と配置
        self.button = tkinter.Button(
            self.master,
            text="ボタン",
            command=self.show_answer
        )
        self.button.pack()

    def resolve_maze(self, i, j):
        '''(i,j)マスから移動できる方向に１マス進む'''

        # 迷路外 or 壁のマスが指定された場合はエラー
        if i < 0 or i >= self.width or j < 0 or j >= self.height or self.maze[j][i] == WALL:
            return

        # 既に経路表示済みの場合は即終了
        if self.resolved:
            return

        # このマスがゴールなら終了
        if self.maze[j][i] == GOAL:

            # ここまでの経路を表示
            self.print_pass()
            self.resolved = True
            return

        # このマスを通過したことを覚えておく
        if self.maze[j][i] != START:
            self.maze[j][i] = PASSED

        # 上に１マス移動
        ni = i
        nj = j - 1  # 上に移動
        if nj >= 0:
            if self.maze[nj][ni] != WALL:
                if self.maze[nj][ni] != PASSED and self.maze[nj][ni] != START:
                    # 次のマスからゴールまで移動させる
                    self.resolve_maze(ni, nj)

        # 下に１マス移動
        ni = i
        nj = j + 1  # 下に移動
        if nj < self.height:
            if self.maze[nj][ni] != WALL:
                if self.maze[nj][ni] != PASSED and self.maze[nj][ni] != START:
                    # 次のマスからゴールまで移動させる
                    self.resolve_maze(ni, nj)

        # 左に１マス移動
        ni = i - 1  # 左に移動
        nj = j
        if ni >= 0:
            if self.maze[nj][ni] != WALL:
                if self.maze[nj][ni] != PASSED and self.maze[nj][ni] != START:
                    # 次のマスからゴールまで移動させる
                    self.resolve_maze(ni, nj)

        # 右に１マス移動
        ni = i + 1  # 右に移動
        nj = j
        if ni < self.width:
            if self.maze[nj][ni] != WALL:
                if self.maze[nj][ni] != PASSED and self.maze[nj][ni] != START:
                    # 次のマスからゴールまで移動させる
                    self.resolve_maze(ni, nj)

        # このマスを通過したことを忘れる
        if self.maze[j][i] != START:
            self.maze[j][i] = PATH

    def print_pass(self):
        '''答えを表示する'''

        for j in range(self.height):
            for i in range(self.width):
                self.change_color(i, j)


    def show_answer(self):
        '''解答表示する'''

        if self.playing:

            # プレイ中フラグをFalseに設定
            self.playing=False

            # 答えを見つけ出して表示する
            self.resolve_maze(self.start[0], self.start[1])

    def play(self):
        '''ゲームプレイを開始する'''

        # ゲームプレイフラグをTrueにセット
        self.playing = True

        # 現在地をスタート値値に設定
        self.now = self.start

        # 上下左右キーに対してイベント受付設定
        self.master.bind("<KeyPress-Up>", self.up_move)
        self.master.bind("<KeyPress-Down>", self.down_move)
        self.master.bind("<KeyPress-Left>", self.left_move)
        self.master.bind("<KeyPress-Right>", self.right_move)

    def update(self):
        '''移動後の状態に迷路リストを更新'''

        # 移動後の現在地を取得
        i, j = self.now

        # GOALであれば終了処理
        if self.maze[j][i] == GOAL:
            self.game_clear()
            return

        # 現在地を更新
        self.maze[j][i] = NOW

        # 色を更新
        self.change_color(i, j)

        # 移動前の現在地を取得
        i, j = self.before

        # 移動前の位置を更新
        if self.before != self.start:
            self.maze[j][i] = PATH
        else:
            self.maze[j][i] = START

        # 色を更新
        self.change_color(i, j)

    def up_move(self, event):
        ''' 上に１マス移動する'''

        # 現在地を取得
        now = self.now
        i, j = now

        # 上に移動
        j = j - 1

        # 迷路外 or 壁のマスが指定された場合は移動しない
        if i < 0 or i >= self.width or j < 0 or j >= self.height or self.maze[j][i] == WALL:
            return

        self.before = self.now

        # 移動後の座標を現在位置に設定
        self.now = i, j

        self.update()

    def down_move(self, event):
        ''' 下に１マス移動する'''

        # 現在地を取得
        now=self.now
        i, j=now

        # 下に移動
        j=j + 1

        # 迷路外 or 壁のマスが指定された場合は移動しない
        if i < 0 or i >= self.width or j < 0 or j >= self.height or self.maze[j][i] == WALL:
            return

        self.before=self.now

        # 移動後の座標を現在位置に設定
        self.now=i, j

        self.update()

    def left_move(self, event):
        ''' 左に１マス移動する'''

        # 現在地を取得
        now=self.now
        i, j=now

        # 左に移動
        i=i - 1

        # 迷路外 or 壁のマスが指定された場合は移動しない
        if i < 0 or i >= self.width or j < 0 or j >= self.height or self.maze[j][i] == WALL:
            return

        self.before=self.now

        # 移動後の座標を現在位置に設定
        self.now=i, j

        self.update()

    def right_move(self, event):
        ''' 右に１マス移動する'''

        # 現在地を取得
        now=self.now
        i, j=now

        # 右に移動
        i=i + 1

        # 迷路外 or 壁のマスが指定された場合は移動しない
        if i < 0 or i >= self.width or j < 0 or j >= self.height or self.maze[j][i] == WALL:
            return

        self.before=self.now

        # 移動後の座標を現在位置に設定
        self.now=i, j

        # 座標に移動する
        self.update()

    def game_clear(self):
        self.playing=False

        self.canvas.create_text(
            CANVAS_WIDTH // 2,
            CANVAS_HEIGHT // 2,
            font=("", 80),
            text="ゲームクリア！"
        )

        self.master.unbind("<KeyPress-Up>")
        self.master.unbind("<KeyPress-Left>")
        self.master.unbind("<KeyPress-Right>")
        self.master.unbind("<KeyPress-Down>")

app=tkinter.Tk()

maze=Maze(app)

maze.play()

app.mainloop()