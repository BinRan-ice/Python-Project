# coding:utf-8
import requests
from lxml import etree

"""
1.拿到页面源代码
2.提取和解析
"""
url="https://www.zbj.com/search/service?kw=saas&r=1&nt=3553&fcn=图像识别"
resp=requests.get(url,headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
})
#解析
html=etree.HTML(resp.text)
#拿到每一个服务商
divs=html.xpath("//*[@id='__layout']/div/div[3]/div/div[3]/div[4]/div[1]/div")
for div in divs:
    price=div.xpath("./div/div[3]/div[1]/span/text()")[0].strip("￥")
    tittle="SAAS".join(div.xpath("./div/div[3]/a/text()"))
    com_name=div.xpath("./div/a/div[2]/div[1]/div/text()")[0]
    print(com_name)

resp.close()
