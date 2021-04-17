#创建类
class Washer():
    def wash(self):
        print('我会洗衣服')

class Washer2(object):
    def wash(self):
        print('我会洗衣服')

class Washer3:
    def wash(self):
        print('我会洗衣服')

#创建对象
haier1 = Washer()
#调用对象的方法
haier1.wash()

#在类外添加属性
haier1.width = 500
haier1.heigth = 800

#在类外获取属性
print(f'haier1的宽度为{haier1.width}')
print(f'haier1的高度为{haier1.heigth}')

#在类内获取对象属性
class Washer1():
    def print_info(self):
        print(f'宽度为{self.width}')
        print(f'高度为{self.heigth}')

haier1 = Washer1()

haier1.width = 400
haier1.heigth = 600

haier1.print_info()

haier2 = Washer1()
haier2.print_info()