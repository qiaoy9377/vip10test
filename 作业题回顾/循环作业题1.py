#三角形的不同样子
#1、左对齐三角形
#while 循环
#循环变量
j = 1
#循环判断
while j <= 5:
    #循环体
    #循环变量
    i = 1
    #循环判断
    while i <= j:
        #循环体
        print('*',end='')
        #循环变量发生变化
        i += 1
    print()
    #循环变量发生变化
    j += 1

#for循环
for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()

#2、右对齐三角形
for i in range(5):
    str1 = ''
    for j in range(i+1):
        str1 += '*'
    print(str1.rjust(5))

for i in range(1,6):
    for j in range(5-i):
        print(' ',end='')
    for k in range(5-i,5):
        print('*',end='')
    print()

#3、倒左对齐三角形
for i in range(5,0,-1):
    for j in range(i):
        print('*',end='')
    print()

#4、倒右对齐三角形
for i in range(5,0,-1):
    str2 = ''
    for j in range(i):
        str2 += '*'
    print(str2.rjust(5))

#5、正三角形
for i in range(1,6):
    for j in range(0,5-i):
        print(' ',end='')
    for k in range(5-i,5):
        print('*',end=' ')
    print()

#6、菱形
for i in range(5):
    str3 = ''
    for j in range(i+1):
        str3 += '* '
    print(str3.center(9))
for i in range(4,0,-1):
    str4 = ''
    for j in range(i):
        str4 += '* '
    print(str4.center(9))

#求100以内能被3整除的数
list1 = []
for i in range(100):
    if i % 3 == 0:
        list1.append(i)
print(list1)

#列表[1,2,3,4,3,4,2,5,5,8,9,7]去重
list2 = [1,2,3,4,3,4,2,5,5,8,9,7]
list3 = []
for i in list2:
    if i not in list3:
        list3.append(i)
print(list3)

#求斐波那契数列1 1 2 3 5 8 13.....
list4 = [1,1]
for i in range(10):
    if i == 0 or i == 1:
        pass
    else:
        list4.append(list4[i-2]+list4[i-1])
print(list4)

#求100以内的质数
list5 = []
for i in range(100):
    if i == 0 or i == 1:
        pass
    else:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            list5.append(i)
print(list5)

#有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef
str5 = 'aabbbcddef'
list6 = []
for i in str5:
    if str5.count(i) > 1:
        pass
    else:
        list6.append(i)

print(''.join(list6))

#有一堆字符串，“welocme to super&Test”，打印出superTest，不能查字符的索引
str6 = 'welocme to super&Test'
list7 = str6.split(' ')
for i in list7:
    list8 = i.split('&')
    if len(list8) > 1:
        str7 = ''.join(list8)
print(str7)

#有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ……全部单词原位置反转
list9 = list(str6)
for i in range(len(str6)//2):
    list9[i],list9[len(str6)-1-i] = list9[len(str6)-1-i],list9[i]
print(''.join(list9))

#有一堆字符串，“aabbbcddef”，输出abcdef
str8 = 'aabbbcddef'
str9 = ''
for i in str8:
    if i not in str9:
        str9 += i

print(str9)

#用列表推导式生成能被5整除的数（100以内）
list10 = [i for i in range(100) if i % 5 == 0]
print(list10)

#有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄
name_list = ['tom','lily','rose']
age_list = [20,19,21]
dict1 = {name_list[i]:age_list[i] for i in range(len(name_list))}
print(dict1)

#开发一个注册系统
#学生信息系统
student_info = {'Tom':20,'Lily':19,'张三':18}
def display():
    print('--------------')
    print('*   1-新增用户')
    print('*   2-查询用户')
    print('*   3-删除用户')
    print('--------------')

def add():
    name = input('请输入您要添加的学生姓名：')
    age = input('请输入您要添加的学生年龄：')
    for key,value in student_info.items():
        if key == name:
            print('该学生信息已存在')
            break
    else:
        student_info[name] = age
        print(f'{name}学生已经添加成功')
        print(student_info)


def search():
    name = input('请输入您要查询的学生姓名：')
    for key,value in student_info.items():
        if key == name:
            print(f'该学生信息为：姓名：{key},年龄{value}')
            break
    else:
        print('无该学生信息')


def delete():
    name = input('请输入您要删除的学生姓名：')
    for key,value in student_info.items():
        if key == name:
            del student_info[key]
            print(f'{key}学生信息已删除')
            break
    else:
        print('无该学生信息')



def select():
    num = int(input('请输入您要进行的操作序号：'))
    if num == 1:
        add()
    elif num == 2:
        search()
    elif num == 3:
        delete()
    else:
        print('输入错误')

display()
select()