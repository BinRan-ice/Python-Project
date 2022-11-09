# coding:utf-8
import re
import requests

"""
1.定位到2022必看片
2.从2022必看片中提取到子页面的链接地址
3.请求子页面的链接地址，拿到我们想要的下载地址
"""
domin="https://www.dytt89.com/"
obj1 = re.compile(r'2022必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
obj2=re.compile(r"<a href='(?P<href>.*?)'")
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf">'
                  r'<a href="(?P<download>.*?)">', re.S)

resp=requests.get(domin,verify=False) #verify=False去掉安全验证
resp.encoding="gb2312"  #指定字符集
result = obj1.finditer(resp.text)
child_href_list=[]
for it in result:
    ul=it.group('ul')
    #提取子页面链接
    result2=obj2.finditer(ul)
    for itt in result2:
        #拼接子页面url地址
        child_href=domin+itt.group("href").strip('/')
        child_href_list.append(child_href)  #把子页面连接保存起来

#提取子页面内容
for href in child_href_list:
    child_resp=requests.get(href,verify=False)
    child_resp.encoding="gb2312"
    result3=obj3.search(child_resp.text)
    print(result3.group("movie"))
    print(result3.group("download"))

resp.close()



