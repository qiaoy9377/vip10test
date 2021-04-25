#定义父类
class Dog(object):
    def work(self):
        print('指哪儿打哪儿....')
#创建子类，重写父类方法
class Amrydog(Dog):
    def work(self):
        print('追击敌人')
#创建子类，重写父类方法
class Drugdog(Dog):
    def work(self):
        print('追查毒品')
#定义新的类，调用dog类
class Person(object):
    def work_with_dog(self,dog):
        dog.work()

#创建不同的dog对象
ad = Amrydog()
dd = Drugdog()
dog = Dog()
#人和不同的狗在一起进行不同的工作
p1 = Person()
p1.work_with_dog(ad)
p1.work_with_dog(dd)
p1.work_with_dog(dog)