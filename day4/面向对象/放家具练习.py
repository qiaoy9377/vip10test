'''
房子类
    属性：总面积、家具列表、剩余面积
    方法：放家具
家具类
    属性：家具名称、家具面积
'''
#家具类
class Furniture():
    #定义家具属性
    def __init__(self,furniture_name,furniture_area):
        self.furniture_name = furniture_name
        self.furniture_area = furniture_area

#定义房子类
class House():
    #定义属性
    def __init__(self,house_area):
        self.house_area = house_area
        self.house_furniture = []
        self.house_remain_area = house_area


    #定义方法
    def put_furniture(self,furniture):
        if self.house_remain_area >= furniture.furniture_area:
            self.house_furniture.append(furniture.furniture_name)
            self.house_remain_area -= furniture.furniture_area
            print(f'家里的总面积为{self.house_area},家里的家具为{self.house_furniture}，剩余面积{self.house_remain_area}')
        else:
            print('家具太大，放不下')


furniture1 = Furniture('床',4)
furniture2 = Furniture('沙发',6)
furniture3 = Furniture('沙发',6)
house1 = House(10)
house1.put_furniture(furniture1)
house1.put_furniture(furniture2)
house1.put_furniture(furniture3)