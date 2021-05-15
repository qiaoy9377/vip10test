# #导入
# import requests
# #请求
# urlstr = 'http://www.wanandroid.com'
# params_dic = {'k':'Android'}
# # urlstr = 'https://www.baidu.com'
# # params_dic = {'kw':'橙好科技'}
# r = requests.get(url=urlstr,params=params_dic)
# #打印结果
# print(r.text)
# print(r.status_code)
# print(r.content)
# print(r.headers)
# print(r.url)
# print(r.encoding)
# print(r.cookies)
# print(r.raw)
# print(r.raise_for_status())

#post请求
# #导入
# import requests,json
# #请求
# urlstr = 'http://httpbin.org/post'
# payload = {'qq群名':'selenium+jmeter+loadrunner','qq群号':'106014970'}
#
# #方法1：先将数据字典转化为json，然后再data=xxx
# #通过json.dumps（）将字典转换为json类型
# # payload_json = json.dumps(payload)
# #发送
# # r = requests.post(url=urlstr,data=payload_json)
#
# #方法2，直接json=xx
# r = requests.post(url=urlstr,json=payload)
#
# #打印结果
# print(r.text)   #json格式的结果
# print(r.json())  #将json结果转换为python识别的字典格式
# print(r.json()['data'])

#玩安卓登录接口
#导入
import requests

wanandroid_url = 'https://www.wanandroid.com/user/login'
wanandroid_payload = {'username': 'qiaoy','password': '1111111'}
wanandroid_header = {'User-Agent': 'Mozilla/5.0'}

wanandroid_r = requests.post(url=wanandroid_url,data=wanandroid_payload,headers = wanandroid_header)

print(wanandroid_r.text)   #返回的时json格式的数据
# print(wanandroid_r.headers)
# print(wanandroid_r.json()['data']['username'])
# #将返回的json转换为字典
# dict1 = wanandroid_r.json()
# #取字典里的username
# print(dict1['data']['username'])

#断言
if wanandroid_r.status_code == 200:
    #用errorcode断言
    if wanandroid_r.json()['errorCode'] == 0:
        print('通过errorCode断言结果登录成功')
    else:
        print('通过errorCode断言结果登录失败')

    #用errorMsg断言
    if wanandroid_r.json()['errorMsg'] == '':
        print('通过errorMsg断言结果登录成功')
    else:
        print('通过errorMsg断言结果登录失败，详细信息：',wanandroid_r.json()['errorMsg'])

    #用关键字-username断言，会出现登录失败取不到用户名直接报异常的情况，这时需要用try捕获异常
    try:
        if wanandroid_r.json()['data']['username'] == wanandroid_payload['username']:
            print('登录成功')
    except Exception as msg:
        print('登录失败，失败原因：',msg)
