# 人物
# 0 名字
# 1.生命之
# 2.有的枪，max1（添加枪）
# 3.移动速度
# 4.子弹数目
# 方法
# 1 跑
# 2 上子弹
# 3 开枪
# 枪
# 1 子弹数
# 2 名字
# 3 开枪的声音


class Human(object):
    def __init__(self, name, life, speed, zidan):

        self.name = name
        self.life = life
        self.speed = speed
        self.zidan = zidan
        self.Human_gun = None

        if life == 0:
            del(Human.name)

    def run(self, time):

        run = time * self.speed
        print(run)

    def add(self, item):
        if self.Human_gun is None:
            self.Human_gun = item

        else:
            print("傻逼吧，没空间了")

    def fire(self, number):
        if self.Human_gun is None:
            print("老弟你要用拳头楞子弹吗")

        else:
            if self.Human_gun.number_gun == 0:
                print("mzd")
            elif number <= self.Human_gun.number_gun:
                print("tu "*number)
                self.Human_gun.number_gun -= number

            elif number > self.Human_gun.number_gun:
                print("tu " * self.Human_gun.number_gun)
                self.Human_gun.number_gun = 0

    def rezidan(self):
        self.zidan -= (5-self.Human_gun.number_gun)
        self.Human_gun.number_gun = 5
        print(self.Human_gun.number_gun)

    def attach(self, number):
        self.life -= number
        print(self.life)
        print(dzb)

class Gun(object):
    def __init__(self, number_gun, name):
        self.name = name
        self.number_gun = number_gun




dzb = Human('DZB', 1000, 50, 500)

AWM = Gun(10, "AWM")

dzb.add(AWM)

dzb.fire(15)

dzb.fire(1)

dzb.rezidan()

dzb.attach(1000)