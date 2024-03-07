# coding:utf-8
# coding:utf-8
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# 构造浏览器
driver = Chrome()

# 隐式等待
# driver.get("https://www.baidu.com/")
# driver.implicitly_wait(5)
# driver.find_element(By.ID, "abc")

# 显示等待
driver.get("https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc")
WebDriverWait(driver, 100).until(
    ec.text_to_be_present_in_element_value((By.XPATH, '//*[@id="fromStationText"]'), '长春')
)
WebDriverWait(driver, 100).until(
    ec.text_to_be_present_in_element_value((By.XPATH, '//*[@id="toStationText"]'), '北京')
)
button = driver.find_element(By.XPATH, '//*[@id="query_ticket"]')
button.click()
