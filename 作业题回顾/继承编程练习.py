#师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[五香味煎饼果子配方]'

    def cook(self):
        print(f'我会使用{self.kongfu}制作煎饼果子')

#学校类
# class School(object):
#     def __init__(self):
#         self.kongfu = '[香辣味煎饼果子配方]'
#
#     def cook(self):
#         print(f'我会使用{self.kongfu}制作煎饼果子')

#super()调用父类方法，适用于单继承
class School(Master):
    def __init__(self):
        self.kongfu = '[香辣味煎饼果子配方]'
        #私有属性
        self.__money = 200000

    #获取私有属性
    def get_info(self):
        return self.__money

    #设置私有属性
    def set_info(self):
        self.__money = 210000

    #私有方法--只能在类内调用
    def __printinfo(self):
        print(self.__money)

    def cook(self):
        print(f'我会使用{self.kongfu}制作煎饼果子')
        #super()调用父类方法
        super(School,self).__init__()
        super(School,self).cook()
        # self.__printinfo()   #类内调用
        # print(self.__money)  #类内调用

class Prentice(School):
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'

    def cook(self):
        print(f'我会使用{self.kongfu}制作煎饼果子')
        super().__init__()
        super().cook()

#徒弟类
#单继承-继承师傅类
# class Prentice(Master):
#     pass

#多继承-继承师傅、学校类(与继承的顺序有关，同名属性，同名方法会显示第一个继承的父类的结果)
# class Prentice(School,Master):
#     pass

#子类重写父类同名属性和方法（子类和父类有同名属性和方法，默认使用子类的属性和方法）
# class Prentice(School,Master):
#     def __init__(self):
#         self.kongfu = '[独创煎饼果子配方]'
#
#     def cook(self):
#         self.__init__()    #再初始化一次，如果先调用父类，再调用子类，初始化属性会受父类属性的影响
#         print(f'我会使用{self.kongfu}制作煎饼果子')
#
#     #子类调用父类的同名属性和方法
#     def old_cook(self):
#         Master.__init__(self)   #初始化属性，不然使用的是创建对象时的属性
#         Master.cook(self)
#         School.__init__(self)   #初始化属性，不然使用的是创建对象时的属性
#         School.cook(self)
#
# #多层继承
# class Tusun(Prentice):
#     pass

#实例化师傅类
xiaoming = Master()
#实例化徒弟类
xiaogang = Prentice()
#打印单继承结果
# print(xiaoming.kongfu)
# xiaoming.cook()
# print(xiaogang.kongfu)
# xiaogang.cook()

#打印多继承结果
# print(xiaogang.kongfu)
# xiaogang.cook()

#打印子类重写父类同名属性和方法的结果
# print(xiaogang.kongfu)
# xiaogang.cook()

#打印子类调用父类同名属性和方法的结果
# print(xiaogang.kongfu)
# xiaogang.old_cook()
# xiaogang.cook()

#打印多层继承的结果
# xiaoqiang = Tusun()
# print(xiaoqiang.kongfu)
# xiaoqiang.old_cook()
# xiaoqiang.cook()

#super()调用父类测试结果
# xiaogang.cook()

#私有属性、方法测试结果
# print(xiaogang.__money)   #无法调用
# xiaogang.__printinfo    #无法调用
xiaogang.cook()
print(xiaogang.get_info())
xiaogang.set_info()
print(xiaogang.get_info())