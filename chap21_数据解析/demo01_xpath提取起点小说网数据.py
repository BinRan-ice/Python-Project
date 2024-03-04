# coding:utf-8
import requests
from lxml import etree

url='https://www.qidian.com/rank/yuepiao/page1/'
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
#发送请求
resp=requests.get(url,headers=headers)
html=etree.HTML(resp.text)  #类型转换,将str类型转换成etree类型
names=html.xpath('//div[@class="book-mid-info"]/h2/a/text()')
authors=html.xpath('//p[@class="author"]/a[1]/text()')
dic=dict(zip(names,authors))
for key,value in dic.items():
    print(key+"-->"+value)