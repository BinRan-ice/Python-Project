# coding:utf-8
import requests

query=input("请输入你一喜欢的明星：")
url=f"https://sogou.com/web?query={query}"
dic={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
resp=requests.get(url,headers=dic)  #处理一个小小的反爬
print(resp.text)    #拿到页面源代码
resp.close()    #关闭resp