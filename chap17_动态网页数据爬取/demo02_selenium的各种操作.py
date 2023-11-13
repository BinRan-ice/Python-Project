# coding:utf-8
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

web=Chrome()
web.get("http://lagou.com")

#找到某个元素，点击
element=web.find_element(By.XPATH,'//*[@id="changeCityBox"]/p[1]/a')
element.click() #点击事件
time.sleep(1)   #让浏览器缓一会
#找到输入框，输入python，输入回车
web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys("python",Keys.ENTER)

#查找存放数据的位置，进行数据提取
#找到页面中存放数据的所有的div
div_list=web.find_elements(By.XPATH,'//*[@id="jobList"]/div[1]/div')
for div in div_list:
    job_name=div.find_element(By.XPATH,'./div[1]/div[1]/div[1]/a').text
    job_salary=div.find_element(By.XPATH,'./div[1]/div[1]/div[2]/span').text
    print(job_name,job_salary)
    time.sleep(1)