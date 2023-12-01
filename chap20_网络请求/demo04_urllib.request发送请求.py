# coding:utf-8
import urllib.request

url='https://movie.douban.com/'
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
#构建请求对象
resp=urllib.request.Request(url,headers=headers)
#使用urlopen打开请求
rep=urllib.request.urlopen(resp)
print(rep.read().decode('utf-8'))