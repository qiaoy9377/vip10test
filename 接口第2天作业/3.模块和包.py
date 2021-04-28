#一、python模块，是一个python文件，以.py结尾，包含了Python对象定义和python语句，模块能定义函数、类和变量，也能包含可执行的代码
# 1、导入模块
# import math
# print(math.sqrt(9))
#
# from math import sqrt
# print(sqrt(9))
#
# from math import *
# print(sqrt(9))
#
# #定义别名
# import time as tt
# tt.sleep(2)
# print('hello')
#
# from time import sleep as sl
# sl(2)
# print('hello')

#2、制作模块
# 模块名必须要符合标识符命名规则
#调用模块
#
# import my_module1
# my_module1.testA(2,3)
#
# #利用from模块导入同名功能，会默认调用最后导入的功能
# from my_module1 import testA
# from my_module2 import testA
#
# testA(2,3)   #调用的是module2的方法

#如果一个模块文件中有__all__变量，当使用from xxx import *导入时，只能导入这个列表中的元素
# from my_module1 import *
# testB()
# #testA(1,2)   #无法调用函数

#二、包
#包内部会自动创建__init__.py文件，这个文件控制着包的导入行为
#导入包
# import test_package.test_module1
# test_package.test_module1.info_print()

#在__init__.py文件中添加__all__ = []，控制允许导入的模块列表
from test_package import *
test_module2.info_print()
#test_module1.info_print()  #__init__.py文件中用__all__ = []控制了包的模块导入