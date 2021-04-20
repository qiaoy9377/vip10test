'''
2、小明爱跑步，爱吃东西。
1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美的体重是45.0公斤

分析：
类：人
    属性：体重
    方法：1、跑步
         2、吃东西
'''

class People():
    #定义属性
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
        print(f'{self.name}的体重{self.weight}公斤')

    #定义跑步方法
    def run(self):
        #减肥0.5公斤
        self.weight -= 0.5
        return f'{self.name}爱跑步,减肥0.5公斤，现在体重是{self.weight}公斤'

    #定义吃东西方法
    def eat(self):
        #体重增加1公斤
        self.weight += 1
        return f'{self.name}爱吃东西，增重1公斤，现在体重{self.weight}公斤'

xiaoming = People('小明',75.0)
print(xiaoming.run())
print(xiaoming.eat())
xiaomei = People('小美',45.0)