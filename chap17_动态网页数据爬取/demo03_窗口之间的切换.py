# coding:utf-8
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

web=Chrome()
web.get("http://lagou.com")
web.find_element(By.XPATH,'//*[@id="cboxClose"]').click()
time.sleep(1)
web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys("python",Keys.ENTER)
time.sleep(1)
web.find_element(By.XPATH,'//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()
#如何进入到新窗口中进行提取
#注意，在selenium眼中，新窗口默认是不切换过来的
web.switch_to.window(web.window_handles[-1])
#在新窗口中提取内容
job_detail=web.find_element(By.XPATH,'//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)
web.close()
web.switch_to.window(web.window_handles[0])
print(web.find_element(By.XPATH,'//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').text)

"""
如果页面遇到了iframe怎么处理
web.get("url")
处理iframe的话，必须先拿到iframe，然后切换视角到iframe,然后才能拿到数据
iframe=(web.find_element(By.XPATH,'iframe的XPATH')
web.switch_to.frame(iframe)
拿到iframe的h3内容
tx=web.find_element(By.XPATH,'iframe中的h3的XPATH')
在切换到原页面
web.switch_to.default_content()
"""
