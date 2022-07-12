import random
import datetime
ALP = ["A","B","C","D","E","F","G"]
r = random.choice(ALP)
alp = ""
for i in ALP:
    if i != r:
        alp = alp + i
print(alp)
st = datetime.datetime.now()
ans = input("抜けているアルファベットは?")
if ans == r:
    print("正解です")
    et = datetime.datetime.now()
    print((et-st).seconds)
else:
    print("違います")
