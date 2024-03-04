# coding:utf-8
import requests
from pyquery import PyQuery

url='https://www.qidian.com/rank/yuepiao/page1/'
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
resp=requests.get(url,headers=headers)
#print(resp.text)
#初始换pyquery对象
doc=PyQuery(resp.text)  #使用字符串初始化方式初始化PyQuery对象
#a_tag=doc("h2 a")
#print(a_tag)
names=[a.text for a in doc("h2 a")]
#print(names)
authors=doc('p.author a')
author_lst=[]
for index in range(len(authors)):
    if index%2==0:
        author_lst.append(authors[index].text)
#print(author_lst)
for name,author in zip(names,author_lst):
    print(name,":",author)