# coding:utf-8
from selenium.webdriver import Chrome
import time

#构造浏览器
chrome=Chrome()

#请求的url
chrome.get("https://www.baidu.com")
time.sleep(5)

chrome.close()  #关闭当前页
time.sleep(5)

chrome.quit()   #关闭浏览器窗口

