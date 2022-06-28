# 第3回
## 迷える（ex02/calc.py）
### 追加機能
- 画像の変更
- サイズの変更(枠ピッタリになるようにした)
- 複数の画像がランダムで選ばれるようにする
- 画像の大きさをこちらで変えられるようにした

### ToDo（実装しようと思ったけど時間がなかった）

- 色の変化を付ける


### メモ
- def img_select():
    global img
    num = random.randint(0,10)
    img = f"fig/{num}.png"
    return img
    で画像を回す
- tori=tori.zoom(3)
    tori= tori.subsample(20)
    でサイズの変更を行う