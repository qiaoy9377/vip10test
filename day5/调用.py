# # import my_moudle1
# from my_moudle1 import *    #使用__all__  = []限制方法使用
# # import time
#
# print(sum(4,5))
# print(ji(4,5))

# import my_package.my_module1
# my_package.my_module1.print_info()

from my_package import *     #必须在__init__文件中加入__all__  = []

my_module2.print_info()
my_module1.print_info()


