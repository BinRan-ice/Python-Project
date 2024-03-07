# coding:utf-8
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#构造浏览器
chrome=Chrome()

#请求url
chrome.get("https://cn.bing.com/")
input_tag = chrome.find_element(By.XPATH, '//*[@id="sb_form_q"]')
time.sleep(1)
input_tag.send_keys("python", Keys.ENTER)