'''
需求主线：
1. 被烤的时间和对应的地⽠状态：
0-3分钟：⽣的
3-5分钟：半⽣不熟
5-8分钟：熟的
超过8分钟：烤糊了
2. 添加的调料：
⽤户可以按⾃⼰的意愿添加调料

分析：
类：地瓜
    属性：被烤的时间、地瓜状态、调料情况
    方法：烤地瓜、撒调料
'''
#创建地瓜类
class Potato():
    #初始化属性
    def __init__(self):
        self.time = 0
        self.status = '生的'
        self.condiment_list = []

    def baked_potato(self):
        time = int(input('请输入烤地瓜的时间(分钟)：'))
        self.time += time
        if 0 <= self.time <= 3:
            self.status = '生的'
        elif 3 < self.time <= 5:
            self.status = '半生不熟'
        elif 5 < self.time <= 8:
            self.status = '熟的'
        else:
            self.status = '烤糊了'

    def condiment_potato(self):
        condiment = input('请输入您要加的调料：')
        self.condiment_list.append(condiment)

    def __str__(self):
        return f'您的地瓜烤了{self.time}分钟，状态是{self.status},添加的调料有{self.condiment_list}'

potato1 = Potato()
potato1.baked_potato()
potato1.condiment_potato()
print(potato1)
