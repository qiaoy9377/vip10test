__all__ = ['testB']
def testA(a,b):
    print(a+b)

def testB():
    print('testB')
#测试模块信息
#添加该条件可以在导入模块的时候不会自动执行测试信息
if __name__ == '__main__':

    testA(1,2)