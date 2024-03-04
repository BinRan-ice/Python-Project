# coding:utf-8
from pyquery import PyQuery as py

html="""
    <html>
        <head>
            <tittle>PyQuery</tittle>
        </head>
        <body>
            <div id="main">
                <a href="https://www.baidu.com">百度</a>
                <h1>欢迎来到百度</h1>
                我是文本
            </div>
            <h2>Python学习</h2>
        </body>
    </html>
"""
doc=py(html)
#获取当前结点
print(doc("#main"))
#获取父节点，子节点，兄弟节点
print("-----------父节点-------------")
print(doc("#main").parent())
print("-----------子节点-------------")
print(doc("#main").children())
print("-----------兄弟节点-------------")
print(doc("#main").siblings())
print("------------获取属性--------------")
print(doc('a').attr('href'))
print("------------获取标签的内容--------------")
print(doc("#main").html())
print(doc("#main").text())