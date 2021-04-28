#1、面向对象的继承指的是多个类之间的所属关系，即子类默认继承父类的所有属性和方法
# #父类A
# class A(object):     #在python中，所有类默认继承object类，object类是顶级类或基类；其他子类叫做派生类
#     def __init__(self):
#         self.num = 1
#
#     def info_print(self):
#         print(self.num)
#
# #子类B
# class B(A):
#     pass
#
# b = B()
# b.info_print()

#2、单继承
# #师傅类
# class Master(object):
#     def __init__(self):
#         self.kongfu = '五香味煎饼果子配方'
#
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
#
# #徒弟类
# class Prentice(Master):
#     pass
#
# #创建对象xiaoming
# xiaoming = Prentice()
# #对象访问实例属性
# print(xiaoming.kongfu)
# #对象调用实例方法
# xiaoming.make_cake()

#3、多继承  --一个类同时继承了多个父类
# 师傅类
# class Master(object):
#     def __init__(self):
#         self.kongfu = '五香味煎饼果子配方'
#
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
#
# #学校类
# class School(object):
#     def __init__(self):
#         self.kongfu = '香辣味煎饼果子配方'
#
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
#
# #徒弟类
# class Prentice(School,Master):    #当一个类有多个父类的时候，默认使用第一个父类饭同名属性和方法
#     pass
#
# #创建对象xiaoming
# xiaoming = Prentice()
# #对象访问实例属性
# print(xiaoming.kongfu)
# #对象访问实例方法
# xiaoming.make_cake()

#4、子类重写父类同名方法和属性
# 师傅类
# class Master(object):
#     def __init__(self):
#         self.kongfu = '五香味煎饼果子配方'
#
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
#
# #学校类
# class School(object):
#     def __init__(self):
#         self.kongfu = '香辣味煎饼果子配方'
#
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
#
# class Prentice(Master,School):    #子类和父类具有同名属性和方法，默认使用子类的同名属性和方法
#     def __init__(self):
#         self.kongfu = '独创煎饼果子配方'
#
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
#
# #创建实例对象
# xiaoming = Prentice()
# #对象调用实例属性
# print(xiaoming.kongfu)
# #对象调用实例方法
# xiaoming.make_cake()

#5、子类调用父类的同名属性和方法
# # 师傅类
# class Master(object):
#     def __init__(self):
#         self.kongfu = '五香味煎饼果子配方'
#
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
#
# #学校类
# class School(object):
#     def __init__(self):
#         self.kongfu = '香辣味煎饼果子配方'
#
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
#
# class Prentice(Master,School):    #子类和父类具有同名属性和方法，默认使用子类的同名属性和方法
#     def __init__(self):
#         self.kongfu = '独创煎饼果子配方'
#
#     def make_cake(self):
#         self.__init__()    #如果先调用父类方法，再调用子类方法，属性会被覆盖，所以需要初始化属性
#         print(f'运用{self.kongfu}制作煎饼果子')
#
#     #调用父类的属性和方法
#     def Master_make_cake(self):
#         Master.__init__(self)    #创建对象是初始化属性是徒弟类的属性，调用父类方法前需要先初始化父类属性
#         Master.make_cake(self)
#
#     def School_make_cake(self):
#         School.__init__(self)
#         School.make_cake(self)
#
# #创建实例对象
# xiaoming = Prentice()
# #对象调用实例方法
# xiaoming.Master_make_cake()
# xiaoming.make_cake()
# xiaoming.School_make_cake()
#
# #6、多层继承
# class Tudi(Prentice):
#     pass
#
# #创建徒弟类的实例对象xiaogang
# xiaogang = Tudi()
# #对象访问实例属性
# print(xiaogang.kongfu)
# #对象调用实例方法
# xiaogang.School_make_cake()
# xiaogang.make_cake()
# xiaogang.Master_make_cake()

#7、super()调用父类方法   super可以自动查找父类，调用顺序遵循__mro__类属性的顺序，适合单继承使用
# 师傅类
# class Master(object):
#     def __init__(self):
#         self.kongfu = '五香味煎饼果子配方'
#
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
#
# class School(Master):     #继承Master类
#     def __init__(self):
#         self.kongfu = '香辣味煎饼果子配方'
#
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
#
#         #用super调用父类方法
#         super(School, self).__init__()
#         super(School, self).make_cake()
#
#
# class Prentice(School):
#     def __init__(self):
#         self.kongfu = '独创煎饼果子配方'
#
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
#
#         #用super调用父类方法
#         super().__init__()
#         super().make_cake()
#
# #创建徒弟实例对象xiaoming
# xiaoming = Prentice()
# #对象调用实例方法
# xiaoming.make_cake()

#8、私有属性
#设置私有权限的方法：在属性名和方法名前面加上两个下划线
# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '五香味煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

#学校类
class School(object):
    def __init__(self):
        self.kongfu = '香辣味煎饼果子配方'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

#徒弟类
class Prentice(Master,School):
    def __init__(self):
        self.kongfu = '独创煎饼果子配方'
        #设置私有属性
        self.__money = 2000000

    #获取私有属性
    def get_money(self):
        return self.__money

    #修改私有属性
    def set_money(self,much):
        self.__money = much

    #设置私有方法
    def __print_info(self):
        print(self.__money)

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

        Master.__init__(self)
        Master.make_cake(self)
        School.__init__(self)
        School.make_cake(self)

#徒孙类
class Tusun(Prentice):
    pass

#创建徒孙实例对象xiaogang
xiaogang = Tusun()
#xiaogang.__money    #私有属性无法访问
#xiaogang.__print_info    #私有方法，无法访问
print(xiaogang.get_money())
xiaogang.set_money(150000)
print(xiaogang.get_money())

#创建徒弟实例对象xiaoming
xiaoming = Prentice()
#xiaoming.__money    #私有属性类外无法访问，只能在类内访问
#xiaoming.__print_info()    #私有方法在类外无法访问，只能在类内访问
print(xiaoming.get_money())
xiaoming.set_money(1800005)
print(xiaoming.get_money())