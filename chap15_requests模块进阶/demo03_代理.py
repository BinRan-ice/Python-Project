# coding:utf-8
import requests

"""
原理：通过第三方的一个机器去发送请求
"""

#157.100.53.99:999
proxies={
    "https": "https://47.95.199.44:80"
}
resp = requests.get("https://www.baidu.com",proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)

