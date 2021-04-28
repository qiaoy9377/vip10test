'''
类：人
    属性：姓名、体重
    方法：爱跑步--体重减0.5公斤
         爱吃东西--体重增加1公斤
'''
class Person():
    #属性
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    #定义对象返回值
    def __str__(self):
        return f'{self.name}的体重是{self.weight}公斤'

    #定义跑步方法
    def run(self):
        self.weight -= 0.5
        print(f'{self.name}爱跑步，体重减0.5公斤，现在是{self.weight}公斤')

    #定义吃东西方法
    def eat(self):
        self.weight += 1
        print(f'{self.name}爱吃东西，体重增加1公斤，现在是{self.weight}公斤')

xiaoming = Person('小明',75.0)
print(xiaoming)
xiaoming.run()
xiaoming.eat()

xiaomei = Person('小美',45.0)
print(xiaomei)