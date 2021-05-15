#导入
import requests

# #请求
# login_url = 'https://www.wanandroid.com/user/login'
# login_params = {'username': 'qiaoy','password': '111111'}
# todo_url = 'https://www.wanandroid.com/lg/todo/list/0'
#
# login_r = requests.post(url=login_url,data=login_params)
# cookie = login_r.cookies
# print(cookie)
# #指定cookie
# todo_r = requests.get(url=todo_url,cookies = cookie)
#
# #打印结果
# print(todo_r.text)

#自定义cookie
#请求
# login_url = 'https://www.wanandroid.com/user/login'
# login_params = {'username': 'qiaoy','password': '111111'}
# todo_url = 'https://www.wanandroid.com/lg/todo/list/0'
# login_r = requests.post(url=login_url,data=login_params)
# print(login_r.cookies)
# cookie_value = login_r.cookies['JSESSIONID']
# cookie = {
#     'JSESSIONID':cookie_value
# }
# print(cookie_value)
# todo_r = requests.get(url=todo_url,cookies=cookie)
# print(todo_r.text)

#用header传cookie
login_url = 'https://www.wanandroid.com/user/login'
login_params = {'username': 'qiaoy','password': '111111'}
todo_url = 'https://www.wanandroid.com/lg/todo/list/0'
login_r = requests.post(url=login_url,data=login_params)
cookie_value = login_r.cookies['JSESSIONID']
header = {'cookie':'JSESSIONID='+cookie_value}
todo_r = requests.get(todo_url,headers=header)
print(todo_r.text)

#断言
if todo_r.text.find('已完成清单') != -1:
    print('查询成功')
else:
    print('查询失败')