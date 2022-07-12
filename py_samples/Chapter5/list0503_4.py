import random
pl_pos = 1
com_pos = 1
def banmen():
    print("・"*(pl_pos-1) + "Ｐ" + "・"*(30-pl_pos))
    print("・"*(com_pos-1) + "Ｃ" + "・"*(30-com_pos))
while True:
    banmen()
    input("Enterを押すとコマが進みます")
    pl_pos = pl_pos + random.randint(1,6)
    com_pos = com_pos + random.randint(1, 6)
