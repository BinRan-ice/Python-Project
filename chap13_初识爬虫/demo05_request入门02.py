# coding:utf-8
import requests

url="https://fanyi.baidu.com/sug"
word=input("请输入一个英文单词：")
dat={
    "kw":word
}
#发送post请求
resp=requests.post(url,data=dat)
print(resp.json())  #将服务器返回的内容直接处理成json()-->字典
resp.close()    #关闭resp