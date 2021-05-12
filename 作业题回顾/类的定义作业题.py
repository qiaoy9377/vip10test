#1、打印小猫爱吃鱼，小猫要喝水
'''
类：小猫
    属性：无
    方法：吃鱼、喝水
'''
#创建类
class Cat(object):
    def eat(self,food):
        print(f'小猫爱吃{food}')

    def drink(self,juice):
        print(f'小猫要喝{juice}')

#实例化类，创建实例对象
cat1 = Cat()
cat1.eat('鱼')
cat1.drink('水')

#2、小明爱跑步，爱吃东西
'''
1)小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美体重是45.0公斤
分析：
类：人
    属性：姓名、体重
    方法：跑步，减重0.5公斤
         吃东西，增重1公斤
'''
#创建类
class Person():
    #定义属性
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    #定义类的说明
    def __str__(self):
        return f'{self.name}的体重{self.weight}公斤'

    #定义跑步方法
    def run(self):
        self.weight -= 0.5
        print(f'{self.name}跑步，减肥0.5公斤，现在体重是{self.weight}')

    #定义吃东西方法
    def eat(self):
        self.weight += 1
        print(f'{self.name}吃东西，增重1公斤，现在体重是{self.weight}')

xiaoming = Person('小明',75.0)
print(xiaoming)
xiaoming.run()
xiaoming.eat()
xiaomei = Person('小美',45.0)
print(xiaomei)

#3、摆放家具
'''
需求：
1）.房子有户型，总面积和家具名称列表   新房子没有任何的家具
2）.家具有名字和占地面积，其中   床：占4平米   衣柜：占2平米   餐桌：占1.5平米
3）.将以上三件家具添加到房子中
4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
分析：
类：房子
    属性：户型，总面积，拥有的家具列表，剩余面积
    方法：容纳家具
类：家具
    属性：家具名，占地面积
    方法：无
'''
#创建房子类
class House():
    #定义房子属性
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.funiture_list = []

    #定义类描述，用于打印类的时候显示
    def __str__(self):
        return f'房子为{self.house_type},总面积为{self.area},拥有的家具列表为{self.funiture_list},剩余面积为{self.free_area}'

    #定义放家具的方法
    def put_funiture(self,funiture):
        if funiture.area < self.free_area:
            self.funiture_list.append(funiture.name)
            self.free_area -= funiture.area
        else:
            print('家具太大，无法放入')

class Funiture():
    def __init__(self,name,area):
        self.name = name
        self.area = area

#创建家具的实例对象
bed = Funiture('床',4)
wardrobe = Funiture('衣柜',2)
table = Funiture('餐桌',1.5)

#创建房子的实例对象
house1 = House('三室一厅',100)
print(house1)
house1.put_funiture(bed)
print(house1)
house1.put_funiture(wardrobe)
house1.put_funiture(table)
print(house1)


#4.士兵开枪
'''
需求：
1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量
分析：
类：士兵
    属性：姓名
    方法：开火-扣动抢的扳机
类：枪
    属性：枪名，子弹数量
    方法：发射子弹-士兵开火，子弹数量减1
         装填子弹-子弹数量增加
'''
#创建士兵类
class Soldier():
    #定义属性
    def __init__(self,name):
        self.name = name

    def fire(self,gun):
        if gun.bullet > 0:
            gun.launch()
        else:
            answer = input('枪内目前没有子弹，无法开火，是否需要装填子弹（Y-是，N-否）：')
            if answer == 'Y':
                gun.loading()
                if gun.bullet > 0:
                    choice = input('子弹装填完毕，是否开火（Y-是，N-否）：')
                    if choice == 'Y':
                        gun.launch()
                    else:
                        pass
                else:
                    print('子弹装填失败，请重新装填')
            else:
                pass

#创建枪类
class Gun():
    #定义枪的属性
    def __init__(self,name,bullet):
        self.name = name
        self.bullet = bullet

    def __str__(self):
        return f'该枪名为{self.name}，枪内有{self.bullet}颗子弹'

    #定义发射子弹方法
    def launch(self):
        self.bullet -= 1
        print(f'士兵扣动扳机开火，子弹数量减1，,剩余数量为{self.bullet}')

    def loading(self):
        bullet_num = int(input('请输入您要装填的子弹数量：'))
        if self.bullet+bullet_num < 20:
            self.bullet += bullet_num
        else:
            print(f'{self.name}目前有{self.bullet}颗子弹，最多还能装填{20-self.bullet}颗子弹')

#创建实例化对象
ruien = Soldier('瑞恩')
gun1 = Gun('AK47',0)
print(gun1)

gun1.loading()
ruien.fire(gun1)