# 第4回
## 逃げろもちさん（ex04/dodge_bomb.py）
### ゲーム概要
- ex04/dodge_bomb.pyを実行すると，1200x650のスクリーンに草原が描画され，もちさんを移動させ飛び回る爆弾から逃げるゲーム
- もちさんが爆弾と接触するとゲームオーバーで終了する
### 操作方法
- 矢印キーでこうかとんを上下左右に移動する
### 追加機能
- 着弾するともちさん画像が切り替わる

- 画像の変更と調整

- 爆弾に当たったら「GAME OVER」を表示させる

- 爆弾の画像を透過させた

- 爆弾を複数個にした
### ToDo（実装しようと思ったけど時間がなかった）
- 時間とともに爆弾が加速するor大きくなる

### メモ
- tori_img=  pg.transform.rotozoom(tori_img, 0, 1) は（画像,回転,大きさ）
- get_rect で画像や作ったものを合成（貼り付ける）
- clock = pg.time.Clock() #表示時間の設定
- if obj_r.left < sc_r.left or sc_r.right < obj_r.right: x = -1   #画面外に行ったらx=-1
- if obj_r.top < sc_r.top or sc_r.bottom < obj_r.bottom: y = -1   #画面外に行ったらy=-1
- これで画面買いに行こうとしたら向きが反転する
