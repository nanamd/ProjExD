"""
迷路生成、迷路解きプログラム
"""
import numpy as np
import random
import cv2
import matplotlib.pyplot as plt
import seaborn as sns
import sys


class MazeCreater():
    """
    迷路を作るクラス
    """
    def __init__(self, size_w=10, size_h=5):
        """
        Parameters
        ----------
        size_w: int
            迷路の横サイズ（分岐できる点の数）
        size_h: int
            迷路の縦サイズ
        """

        self.size_w = size_w
        self.size_h = size_h

        # 道生成クラスのインスタンス生成
        # 引数 max_col は画像出力時の色の数
        self.roadfiller =RoadFiller(
            max_col=size_w,
            )
    
    def generate_maze(self, is_show=True, unit=10, delay=100):
        """
        迷路を生成する
        内部で使用するRoadFillerクラスが、実際に迷路を生成している
        Parameters
        ----------
        unit: int
            画像生成時のセルサイズ
        delay: int
            アニメーション時の遅延(ms)
        Returns
        -------
        field_out: 2d numpuy.array
            生成した迷路
            0が壁
            1が通路
        """

        # field のサイズ
        n_w = 2 * self.size_w + 1
        n_h = 2 * self.size_h + 1

        # field をブランク0で満たす
        field = np.zeros((n_h, n_w), dtype=np.uint8)

        # 道の開始時のid (画面表示の都合上2から開始)
        road_id = 2

        # スタート地点をランダムで決める
        x = 2* np.random.randint(0, self.size_w) + 1
        y = 2* np.random.randint(0, self.size_h) + 1

        # 道の生成
        field = self.roadfiller.fill_with_road(
            field, x, y, id=road_id, mode='create',
            is_show=is_show,
            delay=delay, unit=unit,
            )
        
        # 道のid を全て1に変換して出力
        field_out = field.copy()
        field_out[field > 0] = 1

        return field_out


class MazeSolver:
    """
    迷路を解くクラス
    """
    def __init__(self, field, start, goal):
        self.field = field.copy()
        self.start_xy = start
        self.goal_xy = goal
        self.xy = self.start_xy
        max_col = int(self.field.shape[1] / 2)
        self.roadfiller =RoadFiller(
            max_col=max_col,
            goal_xy=goal,
            start_xy=start,
            )

    def solve_maze(self, is_show=True, unit=10, delay=100):
        """
        通路を0、壁を1とする
        通路に沿って進む、分岐点に来たらゴールが近くなる方を選ぶ
        迷路生成クラスと同じ、RoadFillerクラスを内部で使用
        Parameters
        ----------
        unit: int
            画像生成時のセルサイズ
        delay: int
            アニメーション時の遅延(ms)
        Returns
        -------
        field_out: 2d numpuy.array
            解いた迷路
            0が壁
            1が通路
            2以上が通った軌跡
        """

        field = self.field.copy()
        x, y = self.start_xy

        # 道のidは2から開始
        road_id = 2
        field[y, x] = road_id

        # 道の生成ds
        field_out = self.roadfiller.fill_with_road(
            field, x, y, id=road_id, mode='solve',
            is_show=is_show,
            delay=delay, unit=unit,
            )
        return field_out
   
        
class RoadFiller:
    """
    指定したidの領域を、道を分岐させながら道で満たすクラス
    """
    def __init__(self, max_col=10, mode='create', goal_xy=None, start_xy=None):
        self.render = Render(
            max_col=max_col, mode=mode, 
            goal_xy=goal_xy, start_xy=start_xy,
            )
        self.reach_goal = False
        self.mode = mode
        self.goal_xy = goal_xy
        self.start_xy = start_xy

    def fill_with_road(
        self, field, x, y, id=1, mode='create',
        is_show=True, delay=100, unit=10,
        ):
        """
        0の領域を道で満たす
        迷路を生成する本体
        迷路を解くときにも使用
        Parameters
        ----------
        field: 2d numpy.array
            迷路のフィールド
            0の領域に道が作られる
        x, y: int
            スタート地点
        id: int
            作る道のid 
        mode: str
            'create': 迷路を作る
            'solve': 迷路を解く
        is_show: bool
            True: アニメーションを出す
        
        Returens
        --------
        field: 2d numpy.array
            道が生成されたフィールド
        """

        # ゴールに到達したら終了
        if self.reach_goal is True:
            return field

        self.field = field.copy()
        self.delay = delay
        self.unit = unit
        
        # 開始地点が0なら id とする
        if self.field[y, x] == 0:
            self.field[y, x] = id

        # xy の履歴 (B)で使用
        xy_history = [(x, y)]

        # (A)
        while True:
            # x, y の周囲を調べて、道が伸ばせるならば伸ばす
            res, x, y, fields = self.extend_road(
                self.field, x, y, id, mode=mode,
                )
            self.field = fields[-1]

            if res == 'stretched':
                # 道を伸ばした場合は、xy を記録して繰り返す
                xy_history.append((x, y))

                # 描画
                if is_show is True:
                    if self.delay > 50:
                        for ff in fields:
                            self.render.draw(
                                ff, delay=self.delay, unit=self.unit,
                                )
                    else:
                        self.render.draw(
                            fields[-1], delay=self.delay, unit=self.unit,
                            )

                # ゴール判定
                if mode == 'solve':
                    if x == self.goal_xy[0] and y == self.goal_xy[1]:
                        # ゴールに辿り着いたら終了
                        self.reach_goal = True
                        return self.field

                continue

            # 行き止まりに来たら
            # ループから抜けて(B)へ
            if res == 'deadend':
                break
        
        # (B)
        # 履歴を一つずつもどった地点から、行き止まりまで道を伸ばす
        xy_history.pop(-1)
        xy_history.reverse()
        for xy in xy_history:
            x = xy[0]
            y = xy[1]
            self.fill_with_road(
                self.field, x, y, id=id + 1, mode=mode,
                is_show=is_show,
                delay=self.delay, unit=self.unit,
                )
        
        return self.field

    def extend_road(
        self, field, x, y, id, mode='create',
        ):
        """
        fieldの(x,y)を中心として、
        上下左右の4方向を調べ、
        id_brank があったら道を伸ばす
        'create'のときid_brank = 0
        'solve'のときid_brank = 1
        Parameters
        ----------
        field: 2d numpy.array
            フィールド
        x, y: int
            開始地点
        id: int
            道のid
        mode: str
            'create': 迷路を作る
            'solve': 迷路を解く
        
        Returens
        --------
        res: str
            'stretched': 道を伸ばした
            'deaded': 行き止まりだった
        next_x, next_y: int
            'streatched' で伸ばした先の座標
        fields: list of 2d numpy.array
            段階的に道を伸ばしたときのfieldのリスト
            （アニメーション用）
        """
        if mode == 'create':
            id_brank = 0
        elif mode == 'solve':
            id_brank = 1
        else:
            raise ValueError('modeが違います')

        # 4方向のx, y の増加分
        dd = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        # 変数準備        
        n_h, n_w = field.shape[:2]
        next_field = field.copy()
        pre_field = field.copy()

        # 4方向の状態を調べる
        dd_res = [''] * 4 # 結果の格納変数
        for id_dir in range(4):
            x1 = x + dd[id_dir][0] * 2
            y1 = y + dd[id_dir][1] * 2
            x0 = x + dd[id_dir][0]
            y0 = y + dd[id_dir][1]

            if x1 < 0 or n_w <= x1:
                # 横方向のはみ出し
                dd_res[id_dir] = 'out'
                continue

            if y1 < 0 or n_h <= y1:
                # 縦方向のはみ出し
                dd_res[id_dir] = 'out'
                continue

           
            if (mode == 'create' and field[y1, x1] == id_brank) or \
                (mode == 'solve' and field[y0, x0] == id_brank): 
                # ブランク(道を伸ばせる)
                dd_res[id_dir] = 'brank'
                continue
                

            # 道を伸ばせない
            dd_res[id_dir] = 'no'

        # ブランクあったらそこに道を伸ばす
        ids_dir = [i for i, x in enumerate(dd_res) if x == 'brank']
        if len(ids_dir) > 0:
            res = 'stretched'
            if mode == 'create':
                # ランダムで選ぶ
                id_dir = random.sample(ids_dir, 1)[0]
            elif mode == 'solve':
                # ゴールに近くなる方を選ぶ
                dist = []
                for i, id_dir in enumerate(ids_dir):
                    x0 = x + dd[id_dir][0]
                    y0 = y + dd[id_dir][1]
                    dist.append((x0 - self.goal_xy[0])**2 + (y0 - self.goal_xy[1]) ** 2)
                iid = dist.index(min(dist)) # 最小の要素のindex を返す
                id_dir = ids_dir[iid]
            else:
                raise ValueError('modeが違います')

            x1 = x + dd[id_dir][0] * 2
            y1 = y + dd[id_dir][1] * 2
            x0 = x + dd[id_dir][0]
            y0 = y + dd[id_dir][1]
            pre_field[y0, x0] = id  # アニメーション用の途中状態
            next_field[y1, x1] = id
            next_field[y0, x0] = id # 最終的な状態
            next_x = x1
            next_y = y1
            fields = [pre_field, next_field]

            return res, next_x, next_y, fields

        # 行き止まり
        res = 'deadend'
        next_x = None
        next_y = None
        fields = [pre_field, next_field]
        return res, next_x, next_y, fields


class Render():
    """
    画像生成、表示
    """
    def __init__(
        self, max_col=10, 
        goal_xy=None, start_xy=None, mode='create',
        ):
        self.max_col = max_col # 色の種類の上限
        self.goal_xy=goal_xy
        self.start_xy=start_xy
        self.mode=mode

        self.colorpalette = sns.color_palette(
            "hls", n_colors = self.max_col,
            )

    def draw(
        self,
        field,
        unit=10,
        is_show=True, delay=0,
        unicol=None,
        start_xy=None,
        goal_xy=None,
        ):
        """
        迷路の画像生成
        """

        if start_xy is not None:
            self.start_xy = start_xy
        if goal_xy is not None:
            self.goal_xy = goal_xy
    
        # field をunit分拡大
        val = field
        max_val = np.max(val)
        val = val.astype(dtype=np.uint8)
        val = cv2.resize(
            val,
            dsize=(0, 0),
            fx=unit, fy=unit,
            interpolation=cv2.INTER_NEAREST,
            )
        
        #--- for video fix size
        """
        val_bak = np.ones((440, 840), dtype=np.uint8) * 80
        h, w = val.shape[:2]
        val_bak[:h, :w] = val
        val = val_bak
        """
        # ----

        img_r = val.copy()
        img_g = val.copy()
        img_b = val.copy()

        # 道をid毎に色を付けて描画
        for v in range(max_val + 1):
            if self.mode == 'create':
                if v == 0: # ブランク（道を伸ばす）
                    col = (80, 80, 80)
                elif v == 1: # 壁（道を伸ばす）
                    col = (255, 255, 255)
                else:
                    ic = v % self.max_col
                    col = np.array(self.colorpalette[ic]) * 255
            elif self.mode == 'solve':
                if v == 0: # 壁
                    col = (80, 80, 80)
                elif v == 1: # ブランク
                    col = (255, 255, 255)
                else:
                    ic = v % self.max_col
                    col = np.array(self.colorpalette[ic]) * 255
            else:
                raise ValueError('mode が違います')

            img_r[val == v] = col[0]
            img_g[val == v] = col[1]
            img_b[val == v] = col[2]

        h, w = val.shape
        img = np.zeros((h, w, 3), dtype=np.uint8)
        img[:, :, 0] = img_b
        img[:, :, 1] = img_g
        img[:, :, 2] = img_r

        # スタート地点の目印
        if self.start_xy is not None:
            x = int(self.start_xy[0] * unit + unit / 2)
            y = int(self.start_xy[1] * unit + unit / 2)
            r = int(0.45 * unit)
            col = (100, 100, 200)
            img = cv2.circle(img, (x, y), r, col, -1)

        # ゴール地点の目印
        if self.goal_xy is not None:
            x = int(self.goal_xy[0] * unit + unit / 2)
            y = int(self.goal_xy[1] * unit + unit / 2)
            r = int(0.45 * unit)
            col = (100, 200, 100)
            img = cv2.circle(img, (x, y), r, col, -1)

        # アニメーション表示
        if is_show:
            cv2.imshow('img', img)
            INPUT = cv2.waitKey(delay) & 0xFF
            if INPUT == ord('q'):
                sys.exit()

        return img


if __name__ == '__main__':

        prms = {
            0: (10, 5, 40, 100),
            1: (20, 10, 20, 50),
            2: (40, 20, 10, 1),
        }

        # for video
        """
        cv2.imshow('img', np.ones((440, 840, 3), dtype=np.uint8) * 80)
        cv2.waitKey(0)
        """

        for i in range(100):
            # パラメータの取得
            w, h, u, d = prms[i % len(prms)]

            # 迷路生成クラスのインスタンス生成
            maze = MazeCreater(size_w=w, size_h=h)

            # 迷路をアニメーションさせながら生成
            field = maze.generate_maze(is_show=True, unit=u, delay=d)

            # スタートとゴール地点を作成
            f_h, f_w = field.shape[:2]
            start_xy = (1, 1)
            goal_xy = (f_w - 2, f_h - 2)

            # 完成した迷路を表示
            img = maze.roadfiller.render.draw(
                field, unit=u, delay=1000, unicol=(255, 255, 255),
                start_xy=start_xy, goal_xy=goal_xy,
                )

            # 迷路解きのインスタンス生成
            solver = MazeSolver(
                field, start=start_xy, goal=goal_xy)
            # 迷路をアニメーションさせながら解く
            map = solver.solve_maze(is_show=True, unit=u, delay=d)
            # 解いた迷路を表示
            solver.roadfiller.render.draw(map, unit=u, delay=1000)
