# coding:utf-8
from selenium.webdriver import Chrome

"""
能不能让我的程序连接到浏览器，让浏览器来完成各种复杂的操作，我们只接受最终的结果
selenium：自动化测试工具，可以打开浏览器，然后像人一样去操作浏览器
程序员可以直接从selenium中直接提取网页上的各种信息
环境搭建：pip install selenium       下载浏览器驱动：https://registry.npmmirror.com/binary.html?path=chromedriver
把解压缩的浏览器驱动放在python解释器所在的文件夹
让selenium启动浏览器
"""

#1.创建浏览器对象
web=Chrome()
#2.打开一个网址
web.get("https://www.baidu.com")
print(web.title)