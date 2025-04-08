# coding:utf-8
import parsel
import re
import requests

#小数目录页
list_url="https://www.biquqq.com/0_1/"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
resp=requests.get(url=list_url,headers=headers)
resp.encoding="gbk"
obj=re.compile('<dd><a href="(?P<url>.*?)">.*</a></dd>')
tittle=re.findall('<div id="fmimg"><img alt="(.*?)"',resp.text)[0]
urls=obj.findall(resp.text)
for url in urls:
    index_url="https://www.biquqq.com"+url
    # 发送请求
    resp1 = requests.get(index_url, headers=headers)
    # 编码
    resp1.encoding = "gbk"
    # 解析数据
    selector = parsel.Selector(resp1.text)  # 将字符串数据转成可解析的对象
    # h1::text提取h1标签里面的文本内容get()获得获取
    tittle = selector.css(".bookname h1::text").get()
    content = "".join(selector.css("#content::text").getall()).strip()
    # 保存数据
    with open(f"文件/大主宰/{tittle}.txt", mode="w", encoding="utf-8") as f:
        f.write(tittle)
        f.write("\n")
        f.write(content)
    resp1.close()
    print(tittle+"已下载")
resp.close()