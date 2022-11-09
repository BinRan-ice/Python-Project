# coding:utf-8
import requests
from bs4 import BeautifulSoup

#拿到页面源代码，使用bs4进行解析，拿到数据
url='http://www.xinfadi.com.cn/priceDetail.html'
resp=requests.get(url)

#解析数据
#1.把页面源代码交给BeautifulSoup进行处理，生成bs对象
page=BeautifulSoup(resp.text,"html.parser")#指定html解析器
#2.从bs对象中查找数据
"""
find:找一个（标签，属性=值）
find_all:找所有（标签，属性=值）
"""
#div=page.find("div",class_="tablebox")  #class是python的关键字
div=page.find("div",attrs={
    "class":"tablebox",
})
#拿到所有数据行
trs=div.find_all("tr")[0:1] #取第一个tr标签的内容
for tr in trs:
    tds=tr.find_all("th")   #取tr中所有的th
    name1=tds[0].text   #.text表示拿到被标签标记的内容
    name2=tds[1].text   #.text表示拿到被标签标记的内容
    name3=tds[2].text   #.text表示拿到被标签标记的内容
    name4=tds[3].text   #.text表示拿到被标签标记的内容
    name5=tds[4].text   #.text表示拿到被标签标记的内容
    name6=tds[5].text   #.text表示拿到被标签标记的内容
    name7=tds[6].text   #.text表示拿到被标签标记的内容
    name8=tds[7].text   #.text表示拿到被标签标记的内容
    name9=tds[8].text   #.text表示拿到被标签标记的内容
    name10=tds[9].text   #.text表示拿到被标签标记的内容
    print(name1,name2,name3,name4,name5,name6,name7,name8,name9)
resp.close()


