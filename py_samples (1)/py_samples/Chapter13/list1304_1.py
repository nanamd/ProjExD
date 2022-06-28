class Human:
    def __init__(self, name, life):
        self.name = name
        self.life = life

    def info(self):
        print(self.name)
        print(self.life)


class Soldier(Human):
    def __init__(self, name, life, weapon):
        super().__init__(name, life)
        self.weapon = weapon

    def info(self):
        print("私の名前は"+self.name)
        print("私の体力は{}".format(self.life))

    def talk(self):
        print(self.weapon + "を携え、冒険に出発します")


man = Human("トム(一般人)", 50)
man.info()
print("----------")
prince = Soldier("アレクス(王子)", 200, "光の剣")
prince.info()
prince.talk()
