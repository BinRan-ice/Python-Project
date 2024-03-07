# coding:utf-8
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  # selenium的行为链

# 构造浏览器
driver = Chrome()
driver.get("https://cn.bing.com/")

# 获取文本框
input_tag = driver.find_element(By.XPATH, '//*[@id="sb_form_q"]')

# 创建行为链（更好地去模拟人类的行为）
actions = ActionChains(driver)
# 移动到文本框上，并输入要搜索的关键字
actions.move_to_element(input_tag)
actions.send_keys_to_element(input_tag, "python").send_keys(Keys.ENTER)
# 开始执行行为链
actions.perform()

"""
更多的鼠标操作行为
双击-->double_click(element)
右键点击-->context_click(element)
"""
