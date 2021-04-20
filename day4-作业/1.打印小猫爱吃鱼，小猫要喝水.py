#打印小猫爱吃鱼，小猫要喝水
'''
类：小猫
    属性：无
    方法：1、爱吃鱼
         2、要喝水
'''

class Cat():
    #方法1：爱吃鱼
    def eat_fish(self):
        print('小猫爱吃鱼')

    #方法2：要喝水
    def drink(self):
        print('小猫要喝水')

cat1 = Cat()
cat1.eat_fish()
cat1.drink()