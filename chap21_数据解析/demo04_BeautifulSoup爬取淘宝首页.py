# coding:utf-8
import requests
from bs4 import BeautifulSoup

url="https://www.taobao.com/"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
resp=requests.get(url,headers=headers)
#print(resp.text)
obj=BeautifulSoup(resp.text,"lxml")
a_list=obj.find_all("a")
for a in a_list:
    url=a.get('href')
    if url==None:
        continue
    elif url.startswith('http') or url.startswith('https'):
        print(url)