#1、求列表最大值，实现get_max函数，函数最终返回列表lst的最大值
def get_max(lst):
    '''
    获取列表最大值的函数
    :return: 最大值列表
    '''
    #定义最大值变量
    lst_max = lst[0]
    #循环遍历列表
    for i in lst:
        #判断i与最大值的大小，大于则替换，小于则保持不变
        if i > lst_max:
            lst_max = i
    return lst_max
lst = [4,2,1,6,7,9]
print(get_max(lst))

#2、求学生最高分数科目和分数
def get_max_score(score_dic):
    '''
    获取学生最高分科目和分数
    :param score_dic: 学生成绩字典
    :return: 返回科目和分数
    '''
    #指定第一门课程为最高分
    max_course = '语文'
    max_score = 90
    #循环遍历成绩字典
    for key,value in score_dic.items():
        if value > max_score:
            max_course = key
            max_score = value
    return max_course,max_score

dict = {
    '语文':90,
    '数学':97,
    '英语':98
}
course,score = get_max_score(dict)
print(course,score)

#3、判断回文
def is_palindrome(string):
    '''
    判断一个字符串是否是回文，正反读都一样
    :param string: 需要判断的字符串
    :return: 返回bool值
    '''
    for i in range(len(string)//2):
        if string[i] != string[len(string)-1-i]:
            print('False')
            break
    else:
        print('True')

is_palindrome('abcddcba')
is_palindrome('pythonohtyp')
is_palindrome('bookkob')

#4、打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}={i * j}',end=' ')
    print()

#5、矩阵对角线元素之和
def result(lst):
    result = 0
    for i in range(len(lst)):
        #主对角线之和
        result += lst[i][i]
        #副对角线之和
        result += lst[i][len(lst)-1-i]
    return result

list1 = [[3,5,6],[4,7,8],[2,4,9]]
print(result(list1))

#水仙花数
def flower_num():
    for num in range(100,1000):
        str_num = str(num)
        num_result = 0
        for i in str_num:
            num_result += int(i)**3
        if num_result == num:
            print(num,end=' ')

flower_num()
print()

#打印10000以内的完全平方数
def perfect_square():
    for num in range(10000):
        for i in range(1,num):
            if num/i == i:
                print(num,end=' ')
                break

perfect_square()

