#定义一个老师类，属性：姓名、性别、课程，可以教学，实现：xx老师，性别是xx，教xx课
#分析：
#类：teacher
    #属性：姓名、性别、课程
    #方法：教学-打印话
class Teacher():
    #初始化属性
    def __init__(self,name,gender,course):
        self.name = name
        self.gender = gender
        self.course = course

    #定义方法：打印xx老师，性别是xx，教xx课
    def print_info(self):
        print(f'{self.name}老师，性别是{self.gender},教{self.course}课')

#实例化类
teacher1 = Teacher('张三','女','数学')
#调用类的方法
teacher1.print_info()
