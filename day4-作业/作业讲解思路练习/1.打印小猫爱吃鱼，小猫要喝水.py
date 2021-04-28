'''
类：小猫
    属性：无
    方法：爱吃鱼、要喝水
'''
class Cat():
    def eat(self,food):
        print(f'小猫爱吃{food}')

    def drink(self,sopa):
        print(f'小猫要喝{sopa}')

cat1 = Cat()
cat1.eat('鱼')
cat1.drink('水')