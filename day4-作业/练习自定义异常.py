'''
需求：密码⻓度不⾜，则报异常（⽤户输⼊密码，如果输⼊的⻓度不⾜3位，则报错，即抛出⾃定义异
常，并捕获该异常）。

分析：
类：异常
    属性：输入密码长度，密码最短长度

函数
    功能：抛出异常
'''
#创建异常类
class Password_length(Exception):
    #定义属性
    def __init__(self,input_password,min_password):
        self.input_password = input_password
        self.min_password = min_password

    #定义对象的返回值
    def __str__(self):
        return f'您输入的密码长度为{len(self.input_password)}小于{self.min_password},请重新输入'


#定义抛出异常的函数
def rasie_error():
    try:
        # 用户输入密码
        input_password = input('请输入您的密码：')
        # 判断输入密码的长度是否大于最小长度
        if len(input_password) < 3:
            # 是，则抛出异常对象
            error1 = Password_length(input_password,3)
            raise error1
    except Exception as msg:
        print(msg)
    else:
        print('密码输入成功')
    finally:
        print('程序结束')

rasie_error()