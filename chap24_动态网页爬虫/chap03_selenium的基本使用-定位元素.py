# coding:utf-8
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 构造浏览器
chrome = Chrome()

# 请求url
chrome.get("https://cn.bing.com/")

# 定位元素
# (1)通过ID定位元素
# input_tag = chrome.find_element(By.ID, "sb_form_q")
# (2)通过name属性定位元素
# input_tag=chrome.find_element(By.NAME,"q")
# (3)通过类样式的名称定位元素
# input_tag = chrome.find_element(By.CLASS_NAME, "sb_form_q")
# (4)通过标签名称定位元素
# input_tag=chrome.find_element(By.TAG_NAME,'input')
# (5)通过链接文本定位元素
# a_tag = chrome.find_element(By.LINK_TEXT, '地图')
# print(a_tag)
# (6)通过CSS定位元素
# input_tag=chrome.find_element(By.CSS_SELECTOR,'#sb_form_q')  #id样式
# input_tag=chrome.find_element(By.CSS_SELECTOR,'.sb_form_q')  #class样式
# (7)通过xpath语法获取元素
input_tag = chrome.find_element(By.XPATH, '//*[@id="sb_form_q"]')
time.sleep(1)
input_tag.send_keys("python", Keys.ENTER)
