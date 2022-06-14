#<問題作り>
#アルファベットのリストを作る
#対象文字10文字をランダムで表示させる
#対象文字から‐2文字させる(これを表示文字にする)
#-2文字側を別の関数に入れる(これを削除された文字の1文字ずつ数える時に使う)
#<回答作り>
#
#

#ランダムを使うのでrandom変数呼び出し
import random
#アルファベットのリスト
mozi = [chr(ord("a")+i)for i in range(26)]
#10文字をランダムで表示させる
r=random.sample(mozi, 10)
print("対象文字:"+r)
#対象文字から‐2文字させる(これを表示文字にする)
taisyou=r-[2]
print("表示文字"+taisyou)


#def taisyou():
  #  mozi = ["A","B","C","D","E",
  #  "F","G","H","I","J","K","L",
  #  "M","N","O","P","Q","R","S",
   # "T","U","O","P","Q","R","S",
   # "T","U","V","W","X","Y","Z"]
  #  r=random.sample(mozi)
   # return 
#print("対象文字："+random.sample(taisyou))
#from time import altzone

#def main():
 #  taisyou= AtoZ()
   #kaitou(taisyou)

#対象文字のリスト(グローバル変数)

    #AtoZのリストから10文字出す

#def main():

#    mozi = ["A","B","C","D","E",
 #   "F","G","H","I","J","K","L",
  #  "M","N","O","P","Q","R","S",
   # "T","U","O","P","Q","R","S",
    #"T","U","V","W","X","Y","Z"]
    #AtoZのリストから10文字出す
   # print("対象文字："random.sample(mozi,9))
    
    

#表示文字のリスト()
#対象文字rから-2した文字列
#hyouzi=mozi[r-2]
#print(hyouzi)


#def kaitou(taisyou):
   # ans = input("欠損文字はいくつ:")
    #if ans in taisyou:
    #    print("正解")
    #else:
     #   print("間違い")

#if __name__=="__main__":
 #   main()