# coding:utf-8
from bs4 import BeautifulSoup

html="""
    <title>标题</title>
    <div class="info" float="left">欢迎使用</div>
    <div class="info" float="right" id="gb">
        <span>好好学习天天向上</span>
        <a href="https://www.baidu.com">百度</a>
    </div>
    <span>人生苦短，我学python</span>
"""
bs=BeautifulSoup(html,'lxml')
print(bs.title,type(bs.title))
print(bs.find('div',attrs={'class':'info'}),type(bs.find('div',attrs={'class':'info'})))    #获取第一个满足条件的标签
print(bs.find_all('div',class_='info'))     #得到的是一个标签的列表
for item in bs.find_all('div',class_='info'):
    print(item)
print(bs.find_all('div',attrs={'float':'right'}))
print("==================CSS选择器=====================")
print(bs.select("#gb"))
print(bs.select(".info"))
print(bs.select("div>span"))
print(bs.select('div.info>span')[0].text)
for item in bs.select('div.info>span'):
    print(item.text)