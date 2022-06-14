import random
from time import altzone

def main():
    taisyou= AtoZ()
    kaitou(taisyou)

#対象文字のリスト(グローバル変数)

def AtoZ():
    mozi = ["A","B","C","D","E",
    "F","G","H","I","J","K","L",
    "M","N","O","P","Q","R","S",
    "T","U","O","P","Q","R","S",
    "T","U","V","W","X","Y","Z"]
    print("対象文字：")
    #AtoZのリストから10文字出す
    r=random.randint(9)
    print(mozi[r])
    return mozi[r]

#表示文字のリスト()
#対象文字rから-2した文字列
hyouzi=mozi[r-2]
print(hyouzi)


def kaitou(taisyou):
    ans = input("欠損文字はいくつ:")
    if ans in taisyou:
        print("正解")
    else:
        print("間違い")

if __name__=="__main__":
    main()