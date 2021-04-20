'''
4.士兵开枪
需求：
1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量

分析：
类：士兵
    属性：姓名，有枪
    方法：开火

类：枪
    属性：枪名
    方法：发射子弹、装填子弹
'''
#创建士兵类
class Soldier():
    #定义属性
    def __init__(self,name,gun):
        self.name = name
        self.gun = gun

    #定义开火方法
    def open_fire(self):
        return '士兵扣动扳机开火'

    #定义对象返回值
    def __str__(self):
        return f'士兵{self.name}有一把{self.gun.name}'

#创建枪类
class Gun():
    #定义属性
    def __init__(self,name):
        self.name = name

    #定义发射子弹方法
    def bullet(self):
        return '枪能够把子弹发射出去'

    #定义装填子弹方法
    def reload(self,num):
        return f'枪装填了{num}颗子弹'

#创建对象
gun1 = Gun('AK47')
soldier1 = Soldier('瑞恩',gun1)

#调用方法
print(soldier1)
print(soldier1.open_fire())
print(gun1.bullet())
print(gun1.reload(10))