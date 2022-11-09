# coding:utf-8
import requests
import re
import csv

"""
拿到页面源代码:requests
通过re来提取想要的有效信息:re
"""
url="https://movie.douban.com/top250?start={i*25}&filter="
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
resp=requests.get(url,headers=headers)
page_content=resp.text

#解析数据
obj=re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
               r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">'
               r'(?P<score>.*?)</span>.*?<span>(?P<num>.*?)</span>',re.S)
#开始匹配
result=obj.finditer(page_content)
with open("豆瓣.csv",mode="w",encoding="utf-8",newline="") as f:
    csvwriter=csv.writer(f)
    for it in result:
        dic=it.groupdict()
        dic['year']=dic['year'].strip()
        csvwriter.writerow(dic.values())
resp.close()    #关闭resp
print("over!")