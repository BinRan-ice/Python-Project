# coding:utf-8
#发送不带参数的get请求
import requests

url="http://www.baidu.com"
resp=requests.get(url)
resp.encoding="utf-8"
cookie=resp.cookies     #获取请求后的cookie信息
headers=resp.headers
print('响应的状态码：',resp.status_code)
print('请求后的cookie',cookie)
print('获取请求的网站：',resp.url)
print("获取响应头：",headers)
print('获取响应的内容：',resp.text)