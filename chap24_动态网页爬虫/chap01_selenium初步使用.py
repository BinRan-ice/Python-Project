# coding:utf-8
from selenium.webdriver import Chrome

#构造浏览器
chrome=Chrome()

#请求的url
chrome.get("https://www.baidu.com")

#截图操作
chrome.save_screenshot("文件/baidu.jpg")

#获取网页源代码
html=chrome.page_source
print(html)
chrome.quit()