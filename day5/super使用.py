class Master(object):
    def __init__(self):
        self.kongfu = '五香味煎饼果子'

    def cook(self):
        print(f'我会制作{self.kongfu}')

class School(Master):
    def __init__(self):
        self.kongfu = '香辣味煎饼果子'

    def cook(self):
        print(f'我会制作{self.kongfu}')

        super(School,self).__init__()
        super(School,self).cook()

class Prentice(School):
    def __init__(self):
        self.kongfu = '独创煎饼果子'
        #定义私有属性
        self.__money = 200000
    #定义私有方法
    def __print_money(self):
        return self.__money

    #获取私有属性
    def get_money(self):
        return self.__money

    #设置私有属性
    def set_money(self,much):
        if much >= 0:
            self.__money = much
        else:
            print('余额为负，无法使用')

    def cook(self):
        print(f'我会制作{self.kongfu}')
        # print(self.__print_money())
        # print(self.__money)

        super().__init__()
        super().cook()

class Tusun(Prentice):
    pass

p1 = Prentice()
#p1.cook()
#p1.__money
#p1.__print_money()
#print(Prentice.__mro__)
print(p1.get_money())
p1.set_money(500)
p1.set_money(0)
p1.set_money(-10)
print(p1.get_money())

# s1 = School()
# s1.cook()

tusun1 = Tusun()
#tusun1.__money
#print(tusun1.__print_money)
#tusun1.cook()
print(tusun1.get_money())
tusun1.set_money(500)
print(tusun1.get_money())
tusun1.set_money(0)
tusun1.set_money(-5)