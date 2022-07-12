QUESTION = [
"サザエさんの旦那さんの名前は？",
"カツオの妹の名前は？",
"タラちゃんはカツオからみてどんな関係？"]
R_ANS = ["マスオ", "ワカメ", "甥"]
for i in range(3):
    print(QUESTION[i])
    ans = input()
    if ans == R_ANS[i]:
        print("正解です")
    else:
        print("不正解です")
