print ('hello python')

try:
    open('test.txt','r')
except:
    open('test.txt','w')

try:
    print(num)
except:
    print('有错误')

try:
    print(num)
except Exception:
    print('名称错误')

try:
    print(num)
except (ImportError,IndexError,NameError) as msg:
    print(msg)

try:
    num = 1
    print(num)
except Exception as msg:
    print(msg)
else:
    print('没有异常执行的代码')
finally:
    print('无论是否有异常都要执行')

try:
    f = open('test.txt','r')
except Exception as result:
    print(result)
else:
    print('文件存在，已打开')
finally:
    print('操作结束')
    try:
        f.close()
    except:
        print('文件不存在')