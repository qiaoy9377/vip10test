#创建一个dog类，类下面直接添加属性，这个属性为所有的实例对象共有
class Dog(object):
    __tooth = 10

#访问私有类属性的时候，需要用到类方法
    @classmethod
    def get_tooth(cls):
        return cls.__tooth

    @classmethod
    def set_tooth(cls,num):
        cls.__tooth = num
#实例化类
wangcai = Dog()
xiaohei = Dog()

print(Dog.get_tooth())
print(wangcai.get_tooth())

Dog.set_tooth(14)
print(Dog.get_tooth())
print(wangcai.get_tooth())

wangcai.set_tooth(20)
print(Dog.get_tooth())
print(wangcai.get_tooth())
print(xiaohei.get_tooth())

# print(wangcai.tooth)
# print(xiaohei.tooth)
# print(Dog.tooth)
#
# #修改类属性，只能通过类对象修改
# Dog.tooth = 12
# print(Dog.tooth)
# print(wangcai.tooth)
# print(xiaohei.tooth)
#
# #类对象修改属性会自动创建实例属性，不会影响类属性
# wangcai.tooth = 15
# print(Dog.tooth)
# print(wangcai.tooth)
# print(xiaohei.tooth)

#__init__方法内的属性为实例属性，实例属性不能被类对象调用

#静态方法
class Dog(object):
    @staticmethod
    def print_info():
        print('这是一个静态方法，创建了一个狗类')

wangcai = Dog()

wangcai.print_info()
Dog.print_info()
