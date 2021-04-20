'''
3、摆放家具
需求：
1）.房子有户型，总面积和家具名称列表
   新房子没有任何的家具
2）.家具有名字和占地面积，其中
   床：占4平米
   衣柜：占2平面
   餐桌：占1.5平米
3）.将以上三件家具添加到房子中
4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表

分析：
类：房子
    属性：户型、总面积、家具名称列表、剩余面积
    方法：家具添加到房子中

类：家具
    属性：名字、占地面积
    方法：无
'''
#定义房子类
class House():
    #初始化属性
    def __init__(self,model,area):
        self.model = model
        self.area = area
        self.furniture_list = []
        self.free_area = area

    #定义家具添加到房子中的方法
    def put_furniture(self,furniture):
        #判断房子剩余面积是否大于家具占地面积
        if self.free_area > furniture.area:
            #是，将家具放入房子中，家具列表增加该家具，剩余面积减去该家具占地面积
            self.furniture_list.append(furniture.name)
            self.free_area -= furniture.area
            return f'房子户型为{self.model},总面积为{self.area}平米,剩余面积为{self.free_area}平米,家具列表为{self.furniture_list}。'

#定义家具类
class Furniture():
    #定义家具属性
    def __init__(self,name,area):
        self.name = name
        self.area = area

furniture1 = Furniture('床',4)
furniture2 = Furniture('衣柜',2)
furniture3 = Furniture('餐桌',1.5)
house1 = House('两室一厅',100)
print(house1.put_furniture(furniture1))
print(house1.put_furniture(furniture2))
print(house1.put_furniture(furniture3))