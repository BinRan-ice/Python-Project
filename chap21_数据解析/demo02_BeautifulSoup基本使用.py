# coding:utf-8
from bs4 import BeautifulSoup

html="""
    <html>
        <head>
            <title>标题</title>
        </head>
        <body>
            <h1 class='info bg' float='left'>主体部分</h1>
            <a href="https://www.baidu.com">百度</a>
            <h2><!--注释--></h2>
        </body>
    </html>
"""
bs1=BeautifulSoup(html,'html.parser')
bs2=BeautifulSoup(html,'lxml')
print(bs2.title)    #获取标签
print(bs2.h1.attrs) #获取h1标签的所有属性
#获取单个属性
print(bs2.h1.get('class'))
print(bs2.h1['class'])
print(bs2.a['href'])
#获取文本内容
print(bs2.title.text)
print(bs2.title.string)
#获取内容
print(bs2.h2.string)    #获取到了h2标签中的注释的内容
print(bs2.h2.text)      #不能获取标签中的注释内容