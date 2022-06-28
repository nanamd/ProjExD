import random
cnt = 0
while True:
    r = random.randint(1, 100)
    print(r)
    cnt = cnt + 1
    if r == 77:
        break
print(str(cnt)+"回目でレアキャラをゲット")
