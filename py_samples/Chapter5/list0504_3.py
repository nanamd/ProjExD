import random
ALP = ["A","B","C","D","E","F","G"]
r = random.choice(ALP)
alp = ""
for i in ALP:
    if i != r:
        alp = alp + i
print(alp)
ans = input("抜けているアルファベットは?")
if ans == r:
    print("正解です")
else:
    print("違います")
