class Washer():
    #定义初始化属性--固定值，不灵活
    # 对不同的对象设置不同的属性
    def __init__(self,width,heigth,brand):
        self.width = width
        self.heigth = heigth
        self.brand = brand
    #定义方法
    def print_info(self):
        print(f'宽度为{self.width}')
        print(f'高度为{self.heigth}')
        print(f'品牌为{self.brand}')
    #返回对象数据的方法-打印对象时调用
    def __str__(self):
        return f'这是{self.brand}的说明书'

    def __del__(self):
        print(f'{self.brand}被删除了')

haier1 = Washer(200,300,'Haier')  #创建函数的时候默认会调用
haier1.print_info()
print(haier1)

haier2 = Washer(500,800,'西门子')
haier2.print_info()

print(haier2)

del haier1
#haier1.print_info()
haier2.print_info()

