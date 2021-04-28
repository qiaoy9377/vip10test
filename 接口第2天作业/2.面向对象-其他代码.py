#面向对象的三大特性：封装、继承、多态
#1、体验多态
# #父类，提供公共方法
# class Dog(object):
#     def work(self):
#         print('指哪儿打哪儿.....')
#
# #子类，重写父类方法
# class Amy_dog(Dog):
#     def work(self):
#         print('追击敌人')
#
# class Drug_dog(Dog):
#     def work(self):
#         print('追查毒品')
#
# #创建一个人的类，定义与不同对象的dog工作的方法
# class Person(object):
#     def work_with_dog(self,dog):     #可以在调用方法的时候传入不同的dog对象，从而执行不同的工作
#         dog.work()
#
# #创建实例对象
# xiaoming = Person()
# ad = Amy_dog()
# dd = Drug_dog()
# #对象调用实例方法，传入不同的dog对象
# xiaoming.work_with_dog(ad)
# xiaoming.work_with_dog(dd)

#2、类属性
# class Dog(object):
#     tooth = 10       #记录的某项数据始终保持一致时定义类属性，类属性为全类所共有，仅占用一份内存，节省内存空间
#
# #类对象访问
# print(Dog.tooth)
# #实例对象访问
# wangcai = Dog()
# print(wangcai.tooth)
#
# Dog.tooth = 12         #修改类属性只能通过类对象进行修改
# print(Dog.tooth)
# print(wangcai.tooth)
#
# wangcai.tooth = 14      #实例对象修改类属性表示创建了一个实例属性
# print(Dog.tooth)
# print(wangcai.tooth)

#3、实例属性
# class Dog(object):
#     def __init__(self):
#         self.age = 5
#
#     def info_print(self):
#         print(self.age)
#
# #创建实例对象，访问实例属性
# xiaohei = Dog()
# print(xiaohei.age)
# xiaohei.info_print()
#
# #类对象访问实例属性
# #print(Dog.age)        #类对象无法访问实例属性

#4、类方法
#类方法需要用装饰器@classmethod，第一个参数必须是类对象，一般以cls作为第一个参数
#方法中需要使用类对象，如访问私有属性时，定义类方法，类方法搭配类属性使用
# class Dog(object):
#     __tooth = 10
#
#     @classmethod
#     def get_tooth(cls):
#         return cls.__tooth
#
#
# print(Dog.get_tooth())
# xiaohei = Dog()
# print(xiaohei.get_tooth())

#5、静态方法
#需要装饰器@staticmethod进行修饰，静态方法既不需要传送类对象（cls），也不需要传送实例对象（self）
#静态方法能够通过实例对象和类对象去访问
#取消不需要的参数传递，减少不必要的内存占用和性能消耗
class Dog(object):
    @staticmethod
    def info_print():
        print('这是一个dog类，用于创建dog实例')

#用实例对象访问静态方法
wangcai = Dog()
wangcai.info_print()
#用类对象访问静态方法
Dog.info_print()