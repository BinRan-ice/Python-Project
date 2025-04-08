# coding:utf-8
import requests
import parsel
#用自定义的变量接收字符串数据内容
url="https://www.biquqq.com/0_1/1.html"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
#发送请求
resp=requests.get(url,headers=headers)
#编码
resp.encoding="gbk"
#解析数据
selector=parsel.Selector(resp.text)     #将字符串数据转成可解析的对象
#h1::text提取h1标签里面的文本内容get()获得获取
tittle=selector.css(".bookname h1::text").get()
content="".join(selector.css("#content::text").getall()).strip()
#保存数据
with open("../文件/demo01_单章小说爬取.txt", mode="w", encoding="utf-8") as f:
    f.write(tittle)
    f.write("\n")
    f.write(content)
resp.close()

