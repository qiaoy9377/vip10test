#父类、基类
class Master(object):
    def __init__(self):
        self.kongfu = '五香味煎饼果子'

    def cook(self):
        print(f'我会制作{self.kongfu}')

#父类2
class School(object):
    def __init__(self):
        self.kongfu = '香辣味煎饼果子'

    def cook(self):
        print(f'我会制作{self.kongfu}')

#子类、派生类
class Prentice(School,Master):
    def __init__(self):
        self.kongfu = '独创煎饼果子'

    def cook(self):
        self.__init__()    #先调用父类，再调用子类时需要初始化
        print(f'我会制作{self.kongfu}')

    def master_cook(self):
        Master.__init__(self)
        Master.cook(self)

    def school_cook(self):
        School.__init__(self)
        School.cook(self)

# class Tusun(Prentice):
#     pass
#
# class Tusun_tusun(Tusun):
#     pass

tudi1 = Prentice()
#print(tudi1.kongfu)
tudi1.cook()
tudi1.master_cook()
tudi1.school_cook()

# print(Prentice.__mro__)

# tusun1 = Tusun()
# print(tusun1.kongfu)
# tusun1.cook()
# tusun1.master_cook()
# tusun1.school_cook()
# print(tusun1.kongfu)
#
# tusun_tusun1 = Tusun_tusun()
# tusun_tusun1.cook()