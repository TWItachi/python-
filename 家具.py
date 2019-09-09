class Huose():
    def __init__(self, name, mianji):

        self.name = name
        self.mianji = mianji
        self.s_mainji = mianji
        self.list1 = []

    def install(self, item):

        if self.s_mainji >= item.mains:
            print("添加成功！")
            self.s_mainji -= item.mains
            self.list1.append(item)
        else:
            print("面积不够")

    def find(self):

        if len(self.list1) == 0:
            print("没有家具")

        else:
            for list_2 in self.list1:
                print("名称是：" + list_2.name + "面积是：" + str(list_2.mains))


class JiaJu:
    def __init__(self, name, mains):

        self.name = name
        self.mains = mains

    def __str__(self):

        return self.name + "||" + str(self.mains)


mens = JiaJu("mens", 10)
daxi = JiaJu("daxi", 100)
dzb = JiaJu("dzb", 20)
bieshu = Huose("bieshu", 70)

bieshu.install(mens)
bieshu.install(dzb)

bieshu.find()

bieshu.install(daxi)
