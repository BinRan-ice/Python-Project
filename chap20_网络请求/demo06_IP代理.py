# coding:utf-8
from urllib.request import build_opener
from urllib.request import ProxyHandler

"""
免费代理网站：https://www.xicidaili.com/nn/
"""

proxy=ProxyHandler({'https':'https://183.240.203.136:8118'})
opener=build_opener(proxy)
url='https://www.xslou.com'
resp=opener.open(url)
print(resp.read().decode('utf-8'))