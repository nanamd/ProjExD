import random

def main():
    seikai= shutudai()
    kaitou(seikai)


def shutudai():
    qas = [{"q":"サザエさんの旦那の名前は？","a":["ますお","マスオ",]},
           {"q":"カツオの妹の名前は？","a":["わかめ","ワカメ"]},
           {"q":"タラオはカツオから見てどんな関係？","a":["甥","おい","甥っ子","おいっこ"]},
         ]
    print("問題：")
    r=random.randint(0,2)
    print(qas[r]["q"])
    return qas[r]["a"]

def kaitou(seikai):
    ans = input("答えて:")
    if ans in seikai:
        print("正解")
    else:
        print("間違い")

if __name__=="__main__":
    main()