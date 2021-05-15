#导入
import requests

#请求
login_url = 'https://www.wanandroid.com/user/login'
login_params = {'username': 'qiaoy','password': '111111'}
todo_url = 'https://www.wanandroid.com/lg/todo/list/0'
s = requests.Session()
s.post(url=login_url,data=login_params)
r = s.get(url=todo_url)

#打印结果
print(r.text)

#断言
if r.status_code == 200:
    try:
        if r.text.find('已完成清单') != -1:
            print('请求成功')
        else:
            print('请求失败')
    except Exception as msg:    #报错才走这条路径
        print('请求报错，错误原因：', msg)


# #快递实例
# #导入
# import requests
# #请求
# kuaid_url = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-773058962040428-shentong-KUAIDI1621064096122.html'
# s = requests.Session()
# r = s.post(url=kuaid_url)
# #打印结果
# print(r.json())
# #找到data的值
# status_list = r.json()['data']
# #最新一条物流状态下标为0，用字典形式存储time、context内容
# print(status_list[0]['time'])
# print(status_list[0]['context'])