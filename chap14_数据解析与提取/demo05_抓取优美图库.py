# coding:utf-8
#1.拿到主页面的源代码，然后提取子页面的链接地址，href
#2.通过href拿到子页面的内容，从子页面中找到图片的下载地址 img->src
#3.下载图片
import requests
from bs4 import BeautifulSoup
import time

url="https://www.umei.cc/bizhitupian/weimeibizhi/"
domain="https://www.umei.cc/"
resp=requests.get(url)
resp.encoding="utf-8"   #处理乱码
#把源代码交给bs
main_page=BeautifulSoup(resp.text,"html.parser")
#把范围第一次缩小
alist=main_page.find("div",attrs={
    "class":"Clbc_r_cont"
}).find_all("a")
for a in alist:
    href=domain+a.get('href')   #直接通过get就可以拿到属性的值
    #拿到子页面的源代码
    child_page_resp=requests.get(href)
    child_page_resp.encoding="utf-8"
    child_page_test=child_page_resp.text
    #从子页面中拿到图片的下载路径
    child_page=BeautifulSoup(child_page_test,"html.parser")
    div=child_page.find("div",attrs={
        "class":"big-pic"
    })
    img=div.find('img')
    src=img.get('src')
    #下载图片
    img_resp=requests.get(src)
    #img_resp.content    #这里拿到的是字节
    img_name=src.split('/')[-1] #拿到url中的最后一个/以后的内容
    with open("images/"+img_name,mode='wb') as f:
        f.write(img_resp.content)   #图片内容写入
    print("over",img_name)
    time.sleep(1)
print("all over!!!")
resp.close()