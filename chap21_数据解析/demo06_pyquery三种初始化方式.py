# coding:utf-8
from pyquery import PyQuery as py

html="""
    <html>
        <head>
            <tittle>PyQuery</tittle>
        </head>
        <body>
            <h1>PyQuery</h1>
        </body>
    </html>
"""
#字符串方式
doc=py(html)    #创建PyQuery对象，实际上就是在进行一个类型转换，将str类型转成PyQuery类型
print(doc)
print(type(doc))
print(type(html))
print(doc('tittle').text())

#url方式
doc=py(url='https://www.baidu.com',encoding="utf-8")
print(doc('span'))

#文件初始化方式
doc=py(filename='xpath.html',encoding="utf-8")
print(doc)
print(doc('h1'))
