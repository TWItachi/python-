class Turtle:
    def __init__(self, x):
        self.num = x


class Fish:
    def __init__(self, x):
        self.num = x


class Pool:
    def __init__(self, x, y):
        self.turtle = x
        self.fish = y

    def print_num(self):
        print("乌龟%s 小鱼%s" % (self.turtle, self.fish))


turtle_1 = Turtle('10')
fish_1 = Fish('100')

pool_1 = Pool(turtle_1.num, fish_1.num)
pool_1.print_num()