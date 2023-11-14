# coding:utf-8
import requests
from bs4 import BeautifulSoup

"""
用到的技术点：
1.requests发送请求，从服务器获取到数据
2.BeautifulSoup来解析页面的源代码->特简单
"""

#爬取网站的第一件事，发送请求到服务器
resp=requests.get('https://www.umei.cc/meinvtupian/meinvxiezhen/')   #从服务器拿到源码
resp.encoding='utf-8'
#解析html
main_page=BeautifulSoup(resp.text,"html.parser")
#从页面中找到某些东西
#find()找一个 find_all()找所有
aList=main_page.find("div",attrs={"class":"item_list infinite_scroll"}).find_all("a",attrs={"class":""})
url="https://www.umei.cc"
for a in aList:
    #发送请求到子页面，进入到有小姐姐的页面中
    herf=url+a.get("href")  #https://www.umei.cc/meinvtupian/meinvxiezhen/255973.htm
    resp1=requests.get(herf)
    resp1.encoding='utf-8'
    child_page=BeautifulSoup(resp1.text,"html.parser")
    #找到图片的真实路径
    src=child_page.find("div",attrs={"class":"big-pic"}).find("img").get("src")
    #发送请求到服务器，把图片保存到本地
    #创建文件
    data=src.split("/")[-1]
    with open(f"images/{data}",mode="wb") as f:
        resp2=requests.get(src).content #向外拿出图片的数据，不是文本信息
        f.write(resp2)
        print("恭喜你，下载好了一张图片")
resp.close()