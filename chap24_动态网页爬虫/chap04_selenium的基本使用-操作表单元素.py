# coding:utf-8
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# 构造浏览器
chrome = Chrome()

# 操作表达元素输入框
# 请求url
# chrome.get("https://www.baidu.com/")
# input_tag=chrome.find_element(By.XPATH,'//*[@id="kw"]')
# time.sleep(1)
# input_tag.send_keys("python",Keys.ENTER)

# 操作复选框和按钮
# chrome.get("https://mail.qq.com/?cancel_login=true")
# checkbox_tag=chrome.find_element(By.XPATH,'//*[@id="QQMailSdkTool_auto_login"]')
# time.sleep(5)
# checkbox_tag.click()

# 操作下拉列表框
chrome.get("https://kyfw.12306.cn/otn/regist/init")
# 获取元素
select = Select(chrome.find_element(By.XPATH, '//*[@id="cardType"]'))
# (1)根据索引获取
# select.select_by_index(0)
# (2)根据value属性
# select.select_by_value("B")
# (3)根据可见文本
select.select_by_visible_text("台湾居民来往大陆通行证")
time.sleep(5)
chrome.quit()
