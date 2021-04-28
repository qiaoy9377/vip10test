'''
1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量

分析：
类1：士兵
    属性：姓名
    方法：开火--扣动枪的扳机

类2：枪
    属性：枪名、子弹数量
    方法：枪发射子弹，子弹减少
          枪装填子弹，子弹增加
'''
class Soldier():
    #定义属性方法
    def __init__(self,name):
        self.name = name

    #定义类的说明
    def __str__(self):
        return f'士兵为{self.name}'

    #定义开火方法
    def fire(self,item):
        #判断手枪是否有子弹
        if item.num > 0:
            #有子弹，可以扣动扳机发射，子弹减少1颗--此处可以调用手枪的发射方法
            item.launch()
            print(f'士兵扣动扳机开火，手枪内还剩{item.num}颗子弹')
        else:
            #没有子弹，调用手枪的装填方法
            print('没有子弹，装填子弹')
            num = int(input('请输入您要装填的子弹数量：'))
            item.load(num)

#手枪类
class Gun():
    #定义属性方法
    def __init__(self,name):
        self.name = name
        self.num = 0

    #定义类的说明
    def __str__(self):
        return f'手枪为{self.name}'

    #定义发射方法
    def launch(self):
        self.num -= 1

    #定义装填方法
    def load(self,load_num):
        if load_num <= 20:
            if self.num < 20:
                self.num += load_num
                print(f'子弹已装填，目前手枪内子弹数量为：{self.num}')
            else:
                print('手枪内的子弹已装满20发')
        else:
            print('手枪最多只能装20发子弹')

s1 = Soldier('瑞恩')
print(s1)
gun1 = Gun('AK47')
print(gun1)
gun1.load(20)

s1.fire(gun1)



